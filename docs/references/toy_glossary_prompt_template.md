# Toy Glossary — Generator Prompt Template

Use this file to write a generation prompt for any new unit. It captures the structural rules and naming principles without assuming any specific toys or animations.

For a complete worked example, see `docs/u1_toy_glossary.md`.

---

## Key Concepts

**Toy** — a visual, interactive object placed on screen. Toys have state (mode, values, orientation) and are added, updated, animated, or removed across scenes. The specific instance of a toy in a script is its **tangible ID** (e.g. `picture_graph_books`, `row_builder`).

**Mode** — how the toy is currently configured. `"reading"` means it's pre-built and the student reads or identifies things on it. `"building"` means the student constructs it. Mode determines which tools apply.

**Tool** — the interaction mechanism a student uses on a toy. It describes *how* the student acts, not *what* they act on. Tools only appear in `prompt` beats and always have a **validator** — a JSON condition that defines what a correct response looks like. Some tools are **cross-toy**: they work on any toy and belong in their own section.

**Animation event** — something the guide fires on a toy: highlighting, counting, demonstrating, transforming. Animation events are scene beats, not student actions. They are **atomic** — each is one self-contained visual moment. Two atomics can fire simultaneously. When a multi-step effect is needed, it is a **compound sequence**: a named event that lists its constituent atomics as numbered steps in order.

**Sequential variant** — some atomic animations can run either all-at-once or one-item-at-a-time. The one-at-a-time version is the sequential variant. Note it inline under the core event — not as a separate entry.

---

## Document Structure

**Toy section** (`## toy_name`) — describes what the toy is: its purpose, behavioral modes, visual variants, tangible IDs seen in scripts, and which modules it appears in.

**Student Interactions** (`### Student Interactions`) — one entry per tool. Each entry gives the canonical tool name (and any aliases seen in scripts), one sentence on what the student does and why, the validator shape, and example prompts drawn from real scripts.

**Guide Animations** (`### Guide Animations`) — one entry per animation event. Opens with a callout: *"animations are atomic and can fire simultaneously; compound effects are two events fired at the same time rather than one compound name."* Atomic entries describe the visual and give an example of when and how the event fires (including any common pairings). Compound entries list their steps as a numbered sequence.

**Cross-toy Interactions** (`## Cross-toy Interactions`) — tools not bound to one toy. Same entry format as toy-specific tools.

**Tool Taxonomy** (`## Tool Taxonomy (quick reference)`) — flat table at the end: every tool in the document, one row each, with a one-line description and validator shape.

---

## Naming Principles

**Same action, different cardinality — same verb, singular vs plural.**
When two tools perform the same student action but differ in how many correct answers exist, keep the verb identical and distinguish by pluralizing the noun. Example: `select_category` (one correct answer) vs `select_categories` (all that apply). Do not use different verbs to signal this distinction — different verbs imply fundamentally different actions.

**Ordering** — list cardinality variants adjacent to each other in the document.

**Canonical names** — scripts often contain older or implementation-specific names. As you read the scripts, build a normalization table: whenever you see the same interaction under two different names, pick the clearest canonical form and note the alias under "Tool field aliases seen" in that entry. The canonical name should describe the student action, not the implementation detail.

---

## How to Write the Prompt

1. **List the toys** — skim the scripts and collect every distinct toy type that appears. These become your top-level sections.

2. **Collect tools and validators** — for each toy, find every `prompt` beat and note the tool name and validator. Group by toy. Note any name variations as aliases.

3. **Collect animation events** — for each toy, find every guide animation beat. Note whether each is atomic (single visual moment) or compound (multi-step sequence). Note any sequential variants.

4. **Identify cross-toy tools** — tools that appear across multiple different toy types with the same validator shape belong in Cross-toy Interactions.

5. **Apply naming principles** — normalize aliases, apply same-verb/singular-plural for cardinality pairs.

---

## Example Prompt

```
You are writing a Toy Glossary — Design Requirements document for [unit name].

A Toy Glossary catalogs every toy (interactive UI component), student interaction, and guide animation across the unit. It is organized by toy type. Each toy section covers: what the toy is and how it behaves, how students interact with it (tools and validators), and what the guide can animate on it (atomic events and compound sequences).

Key concepts:
- Toys have modes: "reading" (pre-built, student reads/identifies) or "building" (student constructs)
- Tools are student actions in prompt beats. Each has a validator — a JSON condition defining a correct response
- Animation events are guide actions. They are atomic by design: each is one visual moment that can fire simultaneously with others. Compound sequences are named events that list their constituent atomics as numbered steps
- Sequential variants (one-at-a-time vs all-at-once) are noted inline under the core event, not as separate entries
- Cross-toy tools go in their own section at the end

Naming principles:
- Canonical tool names describe the student action, not the implementation. Note any aliases under "Tool field aliases seen"
- When two tools are the same action but differ in cardinality (one correct answer vs all that apply), use the same verb and distinguish via singular/plural. Do not use different verbs to signal this distinction

Only document what appears in the scripts — do not invent entries.

For a worked example of a complete glossary, see docs/u1_toy_glossary.md.

Here are the scripts:
[paste scripts]
```
