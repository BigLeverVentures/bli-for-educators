# Publish once, adapt the presentation

[Home](../README.md)

Sharing your first adaptation in a document or workshop? Use the [copy, credit and share steps](adapt-a-lesson.md). The source-generation and release-manifest details below describe maintaining a repository or site; they are not prerequisites for teaching a lesson.

Maintain one source for each lesson's prose and prompts. Learning paths should link to exercises rather than keep separate editable copies. Generate the public Markdown and browser pages from the same source; check copied prompt text after formatting changes.

## A platform-independent release checklist

1. Select the exact current lessons and educator documents intended for publication.
2. Exclude raw chat exports, private inputs, operational records and unfinished course material.
3. Check lesson links and point-of-need prerequisites. Make optional account-specific resources explicit.
4. Review prompt boundaries, wrapping, copying and saved results in the actual destination.
5. Record review status separately from model, workflow, human and device evidence.
6. Publish the reviewed package and re-open it through a visitor's path.
7. Collect feedback, fix supported issues and recheck material revisions.

## Check the destination

A community platform may collapse long posts or handle copying differently from a
standalone page. Keep prose prompts in wrapping text, put the first useful catalog
link before a collapsed boundary, and check the saved view as a learner.

A school or nonprofit can adapt these lessons to a website, learning platform,
workshop or document collection. These are delivery options, not verified
integrations with every platform. Verify the controls your learners will use.

## Maintaining a deliberate public release

The public file manifest records exactly what was published and its hashes. `python3 tools/verify_release.py` checks the inventory, lesson/prompt counts, local destinations and unexpected content. It does not assess learning effectiveness or prove every external service remains available.

Corrections should originate in maintained source and then flow into a new reviewed release. Public issues and pull requests are welcome; maintainers reconcile accepted changes with their source before the next export. Do not copy an entire private repository, its Git history or its operational agent files into a public release.
