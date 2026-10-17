#!/usr/bin/env python3
"""Read-only inventory, disclosure, prompt and local-link checks. Python standard library."""
import hashlib
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
from urllib.parse import unquote,urlsplit

ROOT=Path(__file__).resolve().parents[1]

class Page(HTMLParser):
    def __init__(self):
        super().__init__();self.links=[];self.ids=set();self.depth=0;self.parts=[];self.prompts=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag in {'script','link'} and ('src' in a or 'href' in a):self.links.append(a.get('src',a.get('href')))
        if tag=='a' and 'href' in a:self.links.append(a['href'])
        if 'id' in a:self.ids.add(a['id'])
        if tag=='blockquote':
            if not self.depth:self.parts=[]
            self.depth+=1
        elif self.depth and tag in {'p','br','li'}:self.parts.append(' ')
    def handle_endtag(self,tag):
        if tag=='blockquote':
            self.depth-=1
            if self.depth==0:self.prompts.append(hashlib.sha256(' '.join(''.join(self.parts).split()).encode()).hexdigest())
        elif self.depth and tag in {'p','li'}:self.parts.append(' ')
    def handle_data(self,data):
        if self.depth:self.parts.append(data)


def main():
    m=json.loads((ROOT/'release-manifest.json').read_text())
    actual={str(p.relative_to(ROOT)) for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.relative_to(ROOT).parts}
    expected=set(m['files'])|{'release-manifest.json'}
    assert actual==expected,f'File boundary mismatch: extra={actual-expected}, missing={expected-actual}'
    patterns=[r'/Users/',r'/private/(?:tmp|var)/',r'BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY',r'gh[pousr]_[A-Za-z0-9]{20,}',r'sk-[A-Za-z0-9_-]{25,}',r'AKIA[0-9A-Z]{16}',r'BigLeverVentures/big-lever-institute(?:[\s/\"\)])']
    for pattern in patterns:assert not re.search(pattern,(ROOT/'release-manifest.json').read_text()), 'Unexpected disclosure in manifest'
    parsed={}
    for name,sha in m['files'].items():
        p=ROOT/name;assert not p.is_symlink(),f'Symlink: {name}'
        assert hashlib.sha256(p.read_bytes()).hexdigest()==sha,f'Changed file: {name}'
        text=p.read_text()
        scan_text = '\n'.join(line for line in text.splitlines() if not (name == 'tools/verify_release.py' and line.strip().startswith('patterns=[')))
        for pattern in patterns:assert not re.search(pattern,scan_text),f'Unexpected disclosure pattern in {name}'
        if p.suffix in {'.md','.html'}:
            page=Page();page.feed(text);assert page.depth==0,f'Unbalanced prompt: {name}'
            if p.suffix=='.md':
                page.links.extend(re.findall(r'(?<!!)\[[^\]\n]+\]\(([^\s)]+)\)',text))
            parsed[name]=page
    local_links=0
    for name,page in parsed.items():
        for link in page.links:
            u=urlsplit(link)
            if u.scheme or u.netloc:continue
            dest=(ROOT/name).parent/unquote(u.path) if u.path else ROOT/name
            dest=dest.resolve();assert dest.is_relative_to(ROOT),f'Escaping link: {name} {link}'
            assert dest.is_file(),f'Missing target: {name} -> {link}'
            if u.fragment and str(dest.relative_to(ROOT)) in parsed and dest.suffix=='.html':
                assert unquote(u.fragment) in parsed[str(dest.relative_to(ROOT))].ids,f'Missing anchor: {name} {link}'
            local_links+=1
    assert len(m['pages'])==m['lesson_count']==65
    for page in m['pages']:
        for k in ['path','browser_path']:
            assert parsed[page[k]].prompts==page['prompt_sha256'],f'Prompt mismatch: {page[k]}'
    assert sum(p['group']=='Exercises' for p in m['pages'])==27
    assert sum(p['group']=='AI Basics' for p in m['pages'])==9
    assert sum(p['path'].startswith('paths/') for p in m['pages'])==28
    print(json.dumps({'files':len(actual),'lessons':len(m['pages']),'prompt_blocks':sum(len(p['prompt_sha256']) for p in m['pages']),'local_links':local_links,'inventory_and_disclosure_checks':'passed'}))

if __name__=='__main__':main()
