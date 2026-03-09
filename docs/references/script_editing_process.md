# Script Editing Process

Writers and teachers review lesson scripts in Notion after generation.
**Writers** shape the voice. **Teachers** validate pedagogical intent and visual alignment.

---

# Quick Reference

## Navigating the Page

| Action | How |
|--------|-----|
| Jump to a section | Click the section heading in the left sidebar |
| Expand everything | `Ctrl + Alt + T` — toggles all sections open |
| Collapse to overview | `Ctrl + Alt + T` again — collapses back to headings |
| Leave a comment | Highlight text → `Ctrl + Shift + M` — opens comment thread |
| Tag someone | `@name` inside a comment |
| Suggest an edit | `Ctrl + Shift + Alt + X` — toggles suggestions mode on/off |

---

## What You Can Edit

| Block | Edit? | What to change |
|-------|-------|----------------|
| `💬` Dialogue | Yes | The quoted text |
| `❔` Prompt | Yes | Second line only — the question text |
| `✅` `❌` Validator dialogue | Yes | Dialogue inside the toggle |
| `🎬` Scene | Yes, carefully | Description text only |
| `📋` Scene state | No | Reference only — ignore |
| Section headings | No | Do not rename or move |

> **Do not add or remove callout blocks.** Pull matches edits by position — adding or removing blocks breaks alignment.

> **Resolve all suggestions before pull.** Unresolved suggestions won't survive the pull used to ingest into Lesson Lab Pro — only accepted text is captured.

---

## Commenting

- **Flag without editing** — comment on a block to raise a concern without changing it
- **Hand off** — tag `@writer` or `@teacher` to direct a specific note to the right person
- **Resolve** — mark resolved once the comment is acted on
- **Escalate** — if a comment reveals a recurring problem, open a ticket before resolving

---
---

# Understanding the Script

A lesson script is a **beat-by-beat playthrough** of one student's journey.
Read it as something that happens in real time — every line is an event.

---

## Section · Step · Beat

**Section** — one sub-sequence, one concept. May have multiple student actions, one, or none.
Sections run in order from top to bottom.

**Step** — a group of beats within a section. Separated by `· · ·` in Notion.
Steps are a pacing unit — a breath between moments. The product runs them all sequentially.

**Beat** — one atomic event. One line of dialogue. One scene change. One prompt.
The smallest thing that can happen.

**Child section** — every validator state (correct, attempt 1, fallback) is a child section.
A group of steps that runs when its condition is matched.
Remediation lives here — not as a separate top-level section but branched to on failure.

---

## Beat Types

| Beat | Icon | What it is |
|------|------|------------|
| Scene | `🎬` | A visual event — add, remove, animate, or update a tangible |
| Dialogue | `💬` | The guide speaks. Read it as heard aloud, not read |
| Prompt | `❔` | The student acts — click, select, drag, type |
| Correct path | `✅` | Child section — runs when student answers correctly |
| Remediation | `❌` | Child section — runs on attempt N, or heavy remediation with modeling on final attempt |
| Scene state | `📋` | Reference snapshot of the workspace. Not rendered. Ignore when editing |

---

## Section Types

**Transition** — dialogue only. No visuals, no student action.
Bridges phases, sets context, frames what comes next.

**Demonstration** — scene builds the workspace, guide explains, student watches.
Introduces a new tool or concept. No student action required.

**Interactive** — one or more prompts with validators.
The student acts; the script branches on what they do.
May include setup scene beats and consolidating dialogue before and after each prompt.

**Remediation** — a child section triggered by repeated failure.
Targets the specific misconception. Returns to the main flow after.

---

## Reading Flow

```
[Scene — workspace appears]
[Dialogue — guide frames the concept]
[Prompt — student acts]
   [✅ Correct — affirm, scene responds, move on]
   [❌ Attempt 1 — redirect, name what went wrong]
   [❌ Fallback — give the answer, explain the why]
[Dialogue — guide consolidates]
· · ·
[Next step]
```

---
---

# For Writers

Writers shape how the script sounds. The structure and sequence come from the pipeline — the voice is theirs to refine.

The main reference for voice, tone, and what to avoid is the [Guide Design doc](#). That document defines what the guide character should sound like and what patterns to watch for.

The key tension in this work: rewriting for voice while keeping the pedagogical intent intact. A line that sounds flat may still be doing necessary work — setting up a concept, naming a misconception, framing a why. If that work disappears in a rewrite, the section loses something the teacher designed in.

If the same voice problem appears across sections, that's a signal for a pipeline ticket — not just a one-off fix.

---
---

# For Teachers

Teachers review whether the script does what the spec intended. The question isn't how it sounds — it's whether the student ends the section having genuinely engaged with the right concept, at the right difficulty, in the right sequence.

The spec file for each module is the ground truth. Teachers are likely cross-referencing it throughout: checking that prompts target the right skill, that validators address real misconceptions, that the section sequence builds correctly across the module.

Scene beats are worth checking against the UX spec and preproduction assets. Minor mismatches can be edited directly in Notion — the `🎬` callout description only. Anything that looks like a recurring drift between the visual spec and what the pipeline is generating is worth flagging as a ticket.

If a piece of information from the spec needs to be looked up every time a section is evaluated, that's a signal it should live as section metadata — auto-populated by the pipeline. A ticket can get that added.

If the same pedagogical problem appears repeatedly across sections, that's a pipeline issue, not just a content issue — worth a ticket.

---
---

# Escalating Pipeline Issues

Some problems can't be fixed in Notion — they come from how the pipeline generates content. Fixes applied to the pipeline won't be retroactively applied to the current module, but will take effect in later modules.

## What's worth requesting

- **Recurring generation patterns** — the same voice or structural problem appears across sections (e.g. validators are consistently too terse, correct-path dialogue is always flat). If it can be described in a few sentences, it can likely be added to the generation prompt. Dialogue changes require before/after examples to be actionable. As edited dialogue accumulates across sections, later modules are expected to reflect a better baseline voice — the edits inform future generation.
- **Missing context in the script** — information that's needed to review or edit a section but has to be looked up every time (learning goal, misconception, difficulty level). This can be added as section metadata auto-populated by the pipeline.
- **Scene or visual mismatches** — `🎬` beats that regularly don't reflect UX decisions, suggesting the pipeline prompt or config is out of sync with the visual spec.
- **Formatting that makes editing taxing** — layout or structure in Notion that consistently gets in the way. These changes are more expensive since the Notion push/pull is brittle, but if something is significantly broken it can be changed.
- **Anything you're manually correcting more than once** — if it needed fixing in two different sections, it probably needs fixing at the source.

## How to escalate

For now, issues are tracked in a [Notion page](#). Add a note with:
- Which pipeline and module the issue appears in
- A specific example — section ID, the beat or block, what it does vs. what it should do
- Whether it's a one-off or recurring

Issues will be sorted into priority order up to nice-to-have. Tag [pipeline engineer](#) if something is blocking.

---
---

# Using AI in Your Workflow

AI is a tool to move faster — not to replace your judgement. Use it to generate drafts, spot gaps, and pressure-test edits. You still own the decision.

## Claude Project Setup

Create one project per unit. Load the files that define the rules — voice, schema, toy specs, module spec. Paste content directly as project instructions, not links.

With that context loaded, copy the specific beats you're working on — the exact lines in question — and ask what you're trying to figure out. Apply the response back into the callout block in Notion directly.

> **Do not copy-paste the entire page or section into Claude and paste back.** Pull matches edits by block position — replacing large chunks of content will break alignment and the pull will fail.

Keep the project open while working in Notion — it holds context across the session so you don't re-explain the same background each time.
