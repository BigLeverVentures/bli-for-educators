# Ex08 — Email Template Library

[Curriculum](../curriculum.md) · Alpha release · [Evidence and limits](../educators/evaluation.md)

<div><p>Big Lever Institute · Prompt Library</p>
<p>Turn recurring emails into better drafts, using templates you can adapt and improve.</p>
<div><span>Step 1</span>
</div>
<h2>Pick an email you write again and again</h2>
<p>Do you often follow up after meetings, request information, arrange appointments, or send project updates? Instead of starting from scratch each time, make a template: a reusable email with spaces for the details that change.</p>
<p>For help supplying your writing example as text or a permitted file, see <a href="../basics/basics-06.md">Give AI Text or a File to Work From</a>. Keep the “voice only” label described below.</p>
<p>Choose one recurring situation to start. You can add more as you find them useful. Think about who receives the email, what they need to know, and what you want them to do.</p>
<div><div>A simple example</div>
<p>For a follow-up after a meeting, the structure might stay the same: a short recap, agreed actions, and the next step. The recipient, meeting topic, actions, and dates change. A template marks those fields, such as <strong>[AGREED ACTION]</strong>, so you can fill them in each time.</p>
</div>
<p>If you have an email that already works well, paste it below the Build prompt in the same message, labeled “Writing example — voice only.” Remove private details you do not need for this exercise. You can ask your assistant for help choosing a situation or adding a file.</p>

<div><span>Step 2</span>
</div>
<h2>Make your first template</h2>
<p>Use a writing example for style, not for its names, dates or commitments. Explain which sections apply only sometimes. With no agreed action, omit the recap; with no proposed date, ask for availability. Missing facts may prevent a send-ready message, but they do not prevent a useful template.</p>
<p>Copy the prompt below into the chat. Replace the bracketed instructions with your own information, then send it. Answer any questions the assistant asks.</p>
<div><div>Prompt — build reusable email templates</div>
<p>New to using or adapting a prompt? <a href="../basics/basics-04.md">Ask for What You Want</a> shows how.</p>
<p><strong>Copy this prompt</strong></p>
<blockquote><p>Help me make reusable email templates for situations I encounter regularly.</p>
<p>My role and who I usually write to:</p>
<p>[DESCRIBE YOUR ROLE AND RECIPIENTS]</p>
<p>The recurring situation or situations, and what I want the recipient to do:</p>
<p>[DESCRIBE ONE TO THREE SITUATIONS AND THE DESIRED NEXT ACTION FOR EACH]</p>
<p>How I want to sound:</p>
<p>[FOR EXAMPLE: DIRECT AND FRIENDLY, BRIEF AND PROFESSIONAL]</p>
<p>Use any writing example I supplied as a guide to my voice. If something essential is unclear, ask me a focused question; otherwise make a useful first draft.</p>
<p>For each chosen situation, give me one compact, flexible template: a descriptive name, subject line, concise body, and only the fields needed. Make conditional sections easy to omit. A writing example supplies voice, not current facts. Do not add deadline fields unless my task needs a deadline.</p>
<p>Mark changing details with clear placeholders such as [RECIPIENT NAME] or [REQUESTED INFORMATION]. Make the recipient&#x27;s next action clear.</p>
<p>Do not invent facts, commitments, deadlines, previous conversations, or approvals. If those details matter, leave a placeholder or ask me. Keep the wording natural and specific to the situation, without unnecessary filler. Draft the templates only; do not send anything.</p>
</blockquote>
</div>
<p>Read the draft as yourself. If it is too formal, too long, or does not sound like you, say what you would change. A template should make a familiar task easier, not turn every email into the same generic message.</p>

<div><span>Step 3</span>
</div>
<h2>Use the critique to improve the template</h2>
<p>Use the same chat that contains your situation and template. If you start a new chat, paste the situation and template first. Then copy and send this prompt. It will look for problems in the message and in the parts you plan to reuse.</p>
<div><div>Prompt — check how the email will land</div>
<p><strong>Copy this prompt</strong></p>
<blockquote><p>Review this email template or filled-in draft from the recipient&#x27;s point of view and against the situation I described.</p>
<p>Is the reason for writing clear? Would the recipient know what to do next? Is necessary context missing? Does the tone fit our relationship? Look for wording that assumes an agreement, makes an unsupported promise, creates pressure I did not intend, or would be awkward when reused. For a template, check that changing facts have clear placeholders.</p>
<p>For a filled-in draft, check for leftover placeholders or details carried over from another message.</p>
<p>Identify the material issues, explain why each matters, and suggest a specific improvement or question for me. If there is no material issue, say so. Do not rewrite yet or invent flaws just to find something wrong.</p>
</blockquote>
</div>
<p>Read the critique and choose which suggestions help. Tell the assistant: “Revise the template using these changes: …” Add the changes you want; explain what you want to keep. If a suggestion does not fit your recipient or your voice, say so.</p>
<p>Read the revised template. After a substantial change, run the critique again on the revised version. When the important concerns are resolved, tell the assistant which version you want to use. That improved template is what you carry forward.</p>

<div><span>Step 4</span>
</div>
<h2>Put the template to work</h2>
<p>Choose an email you need to write. If you want the assistant to place a draft in your email app, ask: “Can you connect to my email app and create an unsent draft? Walk me through the setup if that is supported.” Reading your inbox and creating drafts are different capabilities; check that draft creation is available.</p>
<p>For the distinction between a draft and an actual saved action, see <a href="../basics/basics-09.md">Check Your Work and Choose What Comes Next</a>. Inspect the saved draft before sending it yourself.</p>
<p>Then copy the prompt below, replace the bracketed instructions with this email’s details, and send it. If draft creation is unavailable, the assistant can still write the email here for you to copy into your email app.</p>
<div><div>Prompt — write this email and create an unsent draft</div>
<p><strong>Copy this prompt</strong></p>
<blockquote><p>Use the revised template I approved to draft this email.</p>
<p>Recipient and email address, if I want an email-app draft:</p>
<p>[NAME AND ADDRESS]</p>
<p>Situation, facts to include, and what I want the recipient to do:</p>
<p>[PROVIDE THE CURRENT DETAILS]</p>
<p>Use the tone and structure I approved. Ask for missing details needed for a usable draft; do not invent facts, commitments, or deadlines. Remove inapplicable template wording and fill the placeholders from the details I provided.</p>
<p>If a connected email app supports creating drafts, create this as an unsent draft there. If the connection requires a confirmation, show the proposed draft and ask for that confirmation. Do not send the email. Report a saved draft only when the tool confirms it, and tell me where to find it.</p>
<p>If creating a draft in my email app is unavailable, give me the subject and body here so I can copy them into an email draft. Do not claim to have saved it in my email app.</p>
</blockquote>
</div>
<p>Open the draft and read it as a complete message. Check the recipient, subject, names, dates, facts, commitments, and requested action. For a fuller check, run the critique prompt from Step 3 on the filled-in draft. Choose the changes you want, then ask the assistant to update the draft if it can, or edit it yourself. You decide when to send it.</p>

<div><span>Step 5</span>
</div>
<h2>Use the better template next time</h2>
<p>Keep working in this chat when you need another email of the same kind. Say which approved template to use and provide the new recipient, facts, and desired action. The value of the critique is now built into the template; you do not need a separate learning note.</p>
<p>If several templates justify continuing work, <a href="../basics/basics-08.md">Set Up a Project for Continuing Work</a> offers saved-workspace and own-note alternatives. One reusable template does not require a Project.</p>
<p>Keep a copy of the approved template in a note or document you control, so you can paste it later if the chat is unavailable. Name the chat so you can find it, such as <strong>Meeting follow-ups</strong>. If your assistant cannot access the earlier template, paste the approved version into the chat. When a recurring improvement helps, ask it to update the template, then check the change.</p>
<p>If you use several templates often, a Project can keep them and your writing examples together. Ask your assistant how to set it up.</p>

<div><h3>The habit to carry forward</h3>
<p>Reuse the structure that works. Supply the current facts, adapt to the recipient, and read the finished message before sending.</p>
</div>
</div>
<hr><p>This is alpha material. Report unclear instructions or errors through <a href="https://github.com/BigLeverVentures/bli-for-educators/issues">a public issue</a> or email help@bigleverinstitute.org. Share only redacted or fictional material.</p>
