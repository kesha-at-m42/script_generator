# STARTER PACK NOTION CONVERSION SPEC

**Version:** 03.03.26 **Purpose:** Defines how to convert a Google Docs Starter Pack into a v2-compliant Notion page. Used by Cowork agents and manual migrators alongside the Module Starter Pack Template v2. **Scope:** Any grade, any unit, any module. Not tied to a specific curriculum sequence. **Companion Documents:** MODULE\_STARTER\_PACK\_TEMPLATE\_v2.md, Starter\_Pack\_Audit\_Prompt\_v1.md

---

## 1\. WHAT THIS SPEC DOES AND DOESN'T DO

**Template v2** defines WHAT goes in a Starter Pack — required sections, interaction block format, field names, remediation conventions. That stays authoritative. Nothing in this spec overrides it.

**This spec** defines HOW that content maps into Notion-friendly markdown for import and what manual steps follow import to take advantage of Notion-native features.

---

## 2\. HUB PAGE SCHEMA

Each unit gets its own hub database page (e.g., "G3U1 Starter Pack Hub," "G3U2 Starter Pack Hub"). Create one before converting that unit's modules.

### Database Properties

| Property | Type | Values | Notes |
| :---- | :---- | :---- | :---- |
| `Module` | Title | M1, M2, ... M\[N\] | Page title; links to full SP page |
| `Module Title` | Text | e.g., "Multiplication Equations" | Human-readable name |
| `Domain` | Select | Populated from unit's domain values | From YAML `domain` |
| `Unit` | Number | Unit number | From YAML `unit` |
| `Status` | Select | `Source Only`, `In Conversion`, `Draft`, `In Review`, `Published` | Workflow state |
| `Primary Toys` | Relation | → Toy Specs database | Links to toy Notion pages |
| `Secondary Toys` | Relation | → Toy Specs database | Links to toy Notion pages |
| `OUR Lessons` | Text | e.g., "L13" or "L7, L8" | Quick reference |
| `Learning Goal` | Text | The One Thing (§1.0) summary | Short version for hub scanning |
| `Interaction Count` | Number | e.g., 25 | Total interactions across all phases |
| `Last Updated` | Date | Auto or manual | Track currency |

### Hub Page Layout

Below the database table, add these reference sections as page content:

- **Cross-Module Vocabulary Accumulation** — Table showing when each term is introduced, reinforced, and assessed across the unit's modules  
- **Toy Progression** — Table showing each toy's first appearance, mode changes, and last appearance across the unit  
- **Consistency Spec Findings** — Link to any consistency audit documentation (or embed key tables)  
- **Module Sequencing Notes** — Any reorder decisions with rationale

---

## 3\. MARKDOWN OUTPUT CONVENTIONS

The Cowork agent produces a single markdown file per module. These conventions ensure clean Notion import.

### 3.1 Don't Include in Markdown

**YAML front matter** — This becomes database properties on the hub page, not page content. The agent should extract YAML values and list them as instructions at the top of the output file in a clearly marked block:

```
<!-- HUB PROPERTIES (set manually after import):
  module_id: M[XX]
  domain: [domain]
  unit: [unit number]
  primary_toys: [list]
  secondary_toys: [list or "none"]
  interaction_tools: [list]
  our_lessons: [lesson IDs]
  interaction_count: [count]
-->
```

This block won't render in Notion. It's a reminder for the person doing the import.

### 3.2 Headings

Map Template v2 headings to Notion heading levels:

| Template v2 | Markdown | Notion Result |
| :---- | :---- | :---- |
| Module title | `# MODULE [X]: [TITLE]` | Page title (H1) — only one per page |
| Major dividers | `# BACKBONE` / `# PHASE SPECIFICATIONS` | H1 divider — major document section |
| Primary sections | `## 1.0 THE ONE THING` | H2 — primary sections |
| Subsections | `### 1.1.1 Standards Cascade` | H3 — subsections |
| Interaction headers | `### Interaction 1.3: [Title]` | **H3** — promoted from bold to heading so Notion can make them toggles |
| KDD items | `### KDD 1: [Title]` | **H3** — promoted from numbered list to heading so Notion can make them toggles |

**Key change:** Interaction headers and KDD items are promoted to H3. In Google Docs these were bold text inside a section. In Notion, making them headings means they become individually collapsible toggle headings — dramatically improving scannability for long documents.

**H2 bold formatting:** H2 section headers (e.g., `## **1.0 THE ONE THING**`) use bold within the heading. Preserve this bold formatting during conversion — Notion renders bold headings with additional visual weight that aids scannability.

### 3.3 Interaction Blocks

Each interaction block follows this markdown pattern:

```
### Interaction 1.3: [Title]

* **Purpose:** [What this interaction accomplishes]
* **Visual: [Toy Name] ([Mode]).** [Orientation]. [Data/content summary]. [Scaffold state]. [Interaction type]. [Visibility flags].
* **Guide:** "[Complete dialogue — teaching content + instruction]"
* **Prompt:** "[Complete standalone instruction — worksheet-style]"
* **Student Action:** [Interaction type: MC selection / click-to-set / drag-to-place / etc.]
  * [If MC] **Options:** [A, B, C, D]
* **Correct Answer:** [Answer]
* **On Correct:** "[Feedback dialogue]"
* **Remediation:** Pipeline

> **Design Note:** [Non-obvious design choice explanation]
```

Note the Design Note uses `>` blockquote syntax. See §3.5.

### 3.4 Tables

Use standard markdown tables. Notion imports these cleanly.

```
| Element | Specification |
| :---- | :---- |
| **Time** | 3-4 minutes |
| **Interactions** | 2 + bridge |
```

### 3.5 Callout Blocks (Design Notes, Remediation Notes, Voice Notes, Scope Warnings)

Use blockquote syntax (`>`) for all annotation types. Add a label prefix so the person can identify and style them during post-import:

```
> **Design Note:** [Non-obvious design choice explanation for future developers.]

> **Remediation Note:** [Contextual hint for the Remediation Pipeline that it can't infer from the interaction block alone.]

> **Voice Note:** [Script-writing guidance for tone and delivery.]

> ⚠️ **Scope Warning:** [Critical scope boundary reminder.]
```

Notion imports `>` as quote blocks. During post-import, these get converted to colored callout blocks:

- Design Notes → Gray callout  
- Remediation Notes → Yellow callout  
- Voice Notes → Blue callout  
- Scope Warnings → Orange callout with ⚠️ icon

### 3.6 Checklists

Use standard markdown checkbox syntax:

```
- [ ] Hook appears in first 15-20 seconds
- [ ] 2+ engagement anchors
- [x] Bridge creates anticipation without teaching
```

Notion imports these as native checkboxes.

### 3.7 Section Dividers

Use `---` between major sections. Notion imports these as visual dividers.

### 3.7.1 Section Transition Markers

Lesson section transition markers (`**→ SECTION X COMPLETE. PROCEED TO SECTION Y.**`) are rendered as bold text on their own line. Preserve them as-is in markdown — they import cleanly into Notion as bold paragraphs and provide critical navigational cues for writers and reviewers.

### 3.8 Code Blocks

Use fenced code blocks for templates and format examples:

```
Template: `[___] × [___] = [___]`
```

### 3.9 Constraints and DO/DO NOT Tables

Keep as standard markdown tables:

```
| DO | DO NOT |
| :---- | :---- |
| [Permitted behavior in this module] | [Forbidden behavior with reason] |
```

---

## 4\. SECTION-BY-SECTION MAPPING

Quick reference for how each Template v2 section maps to Notion formatting:

| Template v2 Section | Notion Treatment | Special Handling |
| :---- | :---- | :---- |
| YAML front matter | Hub database properties | Extract to HTML comment block at file top |
| §1.0 THE ONE THING | H2 with bold sub-labels | CRA Stage, Critical Misconception, Success Indicator, Biggest Risk as bold labels |
| §1.1 Learning Goals | H2 → H3 subsections | Standards Cascade as table; Module Bridges as prose under H3 |
| §1.1.3 OUR Lesson Sources | H3 with table |  |
| §1.1.4 Phase Structure Preview | H3 with table | \[IF APPLICABLE\] tag in heading |
| §1.2 Scope Boundaries | H2 → Must Teach / Must Not Include / Checklist | Scope Warnings as `>` blockquotes |
| §1.3 Vocabulary Architecture | H2 with staging table | Terms to Avoid as bullet list |
| §1.4 Misconceptions | H2 → each misconception as H3 toggle | `### 1.4.X #[ID]: [Name] ([SEVERITY])` |
| §1.5 Toy Specifications | H2 → each toy as H3 toggle | "Notion Spec:" line with live link. "Changes from M\[N-1\]:" line present. Module Configuration and Guardrails as tables. |
| §1.5.X Data Constraints | H3 with table |  |
| §1.6 Warmup | H2 → interactions as H3 toggles | Core Purpose section (Key Function, Why This Serves, Test), then Parameters table, Constraints table, then interactions |
| §1.7 Lesson | H2 → section headings as H3, interactions as H3 toggles within | Pedagogical Flow and Lesson Structure table first |
| §1.7.4 Incomplete Script Flags | H3 with checklist |  |
| §1.7.5 Success Criteria | H3 |  |
| Required/Forbidden Phrases | H3 | Forbidden uses ❌ emoji prefix |
| Misconception Prevention | H3 → each misconception as bold label |  |
| §1.8 Exit Check | H2 → problems as H3 toggles | Alignment Check table before problems |
| §1.8.5 Practice Phase Inputs | H2 with tables | \[IF APPLICABLE\] |
| §1.9 Synthesis | H2 → tasks as H3 toggles | Opening Frame and Identity Closure as separate H3 |
| Verification Checklists | H3 within their phase | Native checkboxes |
| §1.10 KDD Summary | H2 → each KDD as H3 toggle | Grouped by section if 10+ KDDs |
| END OF MODULE STARTER PACK | H1 | Clean terminator |
| §1.11 Final Formatting Audit | H2 after end marker | Native checkboxes |

---

## 5\. v2 COMPLIANCE DURING CONVERSION

The conversion is not a copy-paste — it's an active compliance pass. The agent applies these Template v2 requirements during conversion, not as a separate step.

### 5.1 Always Apply During Conversion

| v2 Requirement | What to Do |
| :---- | :---- |
| YAML → three-tier toy taxonomy | Extract from source SP's toy sections; build the hub-properties comment block with `primary_toys`, `secondary_toys`, `interaction_tools` |
| Field name: `Method:` → `Student Action:` | Rename during conversion |
| Field name: `Validation:` / `Correct:` → `Correct Answer:` | Rename during conversion |
| Authored remediation → `Pipeline` | Replace ALL authored Light/Medium/Heavy remediation with `* **Remediation:** Pipeline`. If authored content contains interaction-specific targeting hints the pipeline can't infer, preserve as `> **Remediation Note:**` blockquote after the interaction block. |
| `Detail Level:` lines → remove | Don't include `**Detail Level:**` lines in any phase |
| `Type:` A/B/C labels → remove | Don't include interaction type classifications from old Guide vs Prompt system. **Note:** This refers only to the legacy `Type: A` / `Type: B` / `Type: C` field. Pedagogical type labels in interaction headers (e.g., `[WORKED EXAMPLE]`, `[ACTIVATION]`, `[CONCEPTUAL CHECK]`) are a v2 convention and MUST be preserved. |
| End marker → `# END OF MODULE [X] STARTER PACK` | Include module number |
| KDDs → before end marker, as §1.10 | Move if source has them after end marker |
| §1.5 headers → Module Configuration / Guardrails | Use v2 naming, not "Core Specifications" / "M\[X\]-Specific Constraints" |
| §1.5 "Changes from M\[N-1\]:" line → required | Add if missing. For a unit's first module, use "First appearance." |
| §1.5 "Notion Spec:" line → required | Add with link or "In development" if URL unknown |
| Misconception headers → `#[ID]: [Name]` format | Global ID before name |
| Bullet style → asterisks (`*`) | Use `*` not `-` for interaction field bullets |
| Visual: line → canonical format | Start with `**Visual: [Toy Name] ([Mode]).**` |
| §1.1.3 OUR Lesson Sources → required | Add if missing in source — populate or use `[TO BE POPULATED]` |
| §1.8.5 Practice Phase Inputs → required if Practice exists | Add stub if missing |

### 5.2 Flag But Don't Fix

These are content issues the agent should note but not attempt to resolve — they require human judgment:

| Issue | How to Flag |
| :---- | :---- |
| Missing section content that can't be inferred | Add section header with `[TO BE POPULATED — confirm with [source]]` |
| Toy Notion URL unknown | Use `[Link — confirm with Notion]` |
| Interaction count mismatch with Phase Structure Preview | Add `> ⚠️ **Conversion Note:** Phase Structure Preview says [X] interactions for Section [Y], but [Z] interactions found in source.` |
| Ambiguous remediation — unsure if authored content contains pipeline-essential hints | Preserve as Remediation Note AND flag: `> ⚠️ **Conversion Note:** Preserved authored remediation as Remediation Note. Review whether pipeline can infer this without the hint.` |
| Missing Verification Checklist items | Add checklist with items from template, mark all as unchecked |
| Content that may be outdated or contradicted by later decisions | Flag with `> ⚠️ **Conversion Note:** [describe concern]` |

---

## 6\. POST-IMPORT CHECKLIST

After importing the markdown file into Notion:

### 6.1 Database Setup (Once Per Unit Hub)

- [ ] Create \[Unit\] Starter Pack Hub database with properties from §2  
- [ ] Create Toy Specs relation (link to existing toy database)  
- [ ] Set up Status select options  
- [ ] Populate Domain select values for this unit  
- [ ] Add cross-module reference sections below database

### 6.2 Per-Module Import Steps

- [ ] Import markdown file as new page in hub database  
- [ ] Set database properties from the HTML comment block at file top  
- [ ] Create toy relations (link Primary/Secondary toys to toy spec pages)  
- [ ] Convert interaction H3 headings to toggle headings (select heading → turn into toggle)  
- [ ] Convert KDD H3 headings to toggle headings  
- [ ] Convert misconception H3 headings to toggle headings  
- [ ] Convert `>` blockquotes to colored callout blocks:  
      - Design Notes → Gray  
      - Remediation Notes → Yellow  
      - Voice Notes → Blue  
      - Scope Warnings / Conversion Notes → Orange  
- [ ] Verify all tables rendered correctly  
- [ ] Verify all checklists have functional checkboxes  
- [ ] Check internal links (if any cross-references to other module pages)  
- [ ] Set Status to `Draft`  
- [ ] Resolve any `[TO BE POPULATED]` and `⚠️ **Conversion Note:**` flags

### 6.3 Review Pass

- [ ] Run Starter Pack Audit Prompt (Passes 1-6) against the Notion page content  
- [ ] If adjacent modules are also in Notion, run Pass 7 (Cross-Module Coherence)  
- [ ] Resolve any findings  
- [ ] Update Status to `In Review` → get SME sign-off → `Published`

---

## 7\. WORKFLOW: EXISTING vs. NEW MODULES

### Converting Existing Google Docs Modules

1. Export Google Doc as PDF or plain text (input for Cowork agent)  
2. Run Cowork conversion task with Template v2 \+ this Conversion Spec \+ any known compliance gap documentation  
3. Agent produces v2-compliant markdown  
4. Import into Notion, complete post-import checklist  
5. Archive Google Doc (rename with `[ARCHIVED — See Notion]` prefix)

### Creating New Modules

1. **Draft in Google Docs** with SME review (comments, suggestions, debates)  
2. When approved, convert to Notion using this spec  
3. Archive Google Doc — Notion is the canonical version  
4. Future edits happen in Notion directly for small changes  
5. Major revisions with SME input round-trip through Google Docs, then re-convert

### The Audit Prompt Works Against Either Format

The Starter Pack Audit Prompt works by reading content, not by inspecting file format. Paste Notion page content into a conversation and run the audit exactly as designed. No modification needed.

---

## 8\. EXTENDING THE HUB

As more units are built, the hub pages form a navigable curriculum knowledge base:

- Each unit gets its own hub database  
- A **master index page** can link all unit hubs  
- Toy Specs database is shared across units (toys evolve, not duplicate)  
- Claude Project Knowledge can reference hub pages for cross-unit search  
- Cross-unit vocabulary and toy progression tables live at the master index level

The schema in §2 is designed to stay stable across units — the `Domain` select values expand as new units introduce new domains, but the property structure doesn't change.  
