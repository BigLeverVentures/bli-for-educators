# Ex20 — Build a Personal Tool

[Curriculum](../curriculum.md) · [Teaching-use license; no resale](../LICENSE.md) · Alpha release · [Evidence and limits](../educators/evaluation.md)

<p>Solve one small repeated task with software you can run and understand.</p>
<h2>Start with your task</h2>
<p>Choose a reversible local task such as converting a personal checklist into a formatted summary. Begin with redacted or fictional data. Avoid payments, accounts, and external integrations for this first tool.</p>
<p>You need: One concrete task, sample input/output, an editor and a way to execute the chosen language or browser file. A text-only assistant can supply code but cannot prove it runs.</p>
<h2>Build</h2>
<p>Tell the assistant your experience level. You can finish with a plain saved copy of a local tool; Git and pull requests are optional version/review workflows, not prerequisites. A runtime is what runs your code; a boundary check tries an edge of the allowed input. Ask for literal file, folder, plain-text save and run instructions if these are new to you.</p>
<p>Copy this into your assistant, replace the bracketed inputs, and provide the relevant material. Approve the approach before acting.</p>
<p>New to using or adapting a prompt? <a href="../basics/basics-04.md">Ask for What You Want</a> shows how.</p>
<p><strong>Copy this prompt</strong></p>
<blockquote><p>Help me build a small personal tool for [repeated task]. My experience with code and running commands is [DESCRIBE WHAT I KNOW OR SAY I AM NEW]. My environment is [operating system, editor, languages/runtime available], typical input is [sample], and useful output is [example]. First check whether a simpler non-code method meets the need.</p>
<p>If code earns its place, propose the smallest local design, explain how data moves, and ask me to approve it before building. Include one normal case, an empty/malformed case, and a boundary case; state expected results before execution. Avoid credentials, network services, new dependencies, and file overwrites unless we explicitly choose them.</p>
<p>Give literal instructions for creating the folder, saving plain-text code without altered quotes or extensions, locating the input, and running the command. Explain unfamiliar terms and how I check the output and unchanged input. Use separate disposable test inputs; never ask me to empty my valuable original file for a test.</p>
<p>Specify plain-language errors for likely missing or malformed input instead of silent wrong results or unexplained tracebacks. Agree exact expected output and empty/error messages before checking. For a local-only task, keep Git out unless I ask; help me save a clear working copy. Use an existing repository when my chosen workflow needs it.</p>
<p>Keep the first version small but useful for my stated task; group related checks and ask only choices that could change the result. Do not estimate setup or completion time unless I ask. Run or guide me through checks. Report actual commands, outputs, failures and unrun checks. Do not claim an interface click or code execution that did not occur.</p>
<p>If execution is unavailable, mark the code untested and help me obtain runtime evidence before relying on it. Before I approve the approach, challenge it briefly: does code earn its place, is execution available, could input be lost, and would the planned cases detect incorrect output? Let me choose corrections before building.</p>
<p>If I intend to continue to a pull request, inspect the approved base and clean status and establish a separate tool branch before implementation; protect unrelated changes rather than discarding them.</p>
</blockquote>
<h2>Check the result</h2>
<p>Paste this review prompt into the same chat with the actual result and evidence. In a new chat, include your task, source material, result and observed checks. Choose the corrections before requesting a replacement artifact.</p>
<p>Use the evidence from your work with this review prompt.</p>
<p><strong>Copy this prompt</strong></p>
<blockquote><p>Review the tool for my stated task using [code, run instructions, actual test inputs/outputs and errors]. Does it produce the useful output on normal, malformed, and boundary inputs? Look for silent data loss, accidental overwrites, privacy exposure, hidden dependency assumptions, and errors the user cannot understand.</p>
<p>Check whether the tests distinguish a wrong result from a successful run. Name the highest-impact supported fixes and any evidence still needed. Let me choose a fix, then rerun the affected cases and a normal case after the change. Keep untested behavior explicit. Do not rewrite, supply replacement code or artifacts, or apply changes yet.</p>
<p>Explain the supported corrections and wait for my choice. Distinguish demonstrated failures from inferred causes; do not invent test history.</p>
</blockquote>
<h2>Choose, revise, and use</h2>
<p>Run the tool yourself on the sample and a second case before using important material. Inspect the output, not just the absence of an error. Keep the tested version and a short README with input format, run command and limits.</p>
<h2>Carry it forward</h2>
<p>Try one modest improvement driven by actual use. Define the expected result before editing and keep a working version to compare against.</p>
<hr><p>This is alpha material. Report unclear instructions or errors through <a href="https://github.com/BigLeverVentures/bli-for-educators/issues">a public issue</a> or email help@bigleverinstitute.org. Share only redacted or fictional material.</p>
