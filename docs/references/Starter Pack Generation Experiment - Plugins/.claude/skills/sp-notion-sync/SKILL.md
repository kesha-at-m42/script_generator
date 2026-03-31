# SP Notion Sync — Bidirectional Sync with 📖 Level Curriculum Documents

You bridge the Notion database with the local evaluation pipeline. **Notion is the source of truth.** The primary flow is: pull → evaluate → fix → push back to Notion. Local files are working copies, not deliverables.

---

## DATABASE REFERENCE

- **Database ID**: `3185917eac5280abb772efe0552c88ae`
- **Data Source ID**: `3185917e-ac52-80c0-a46b-000be3c6a416`
- **Schema**: Name (title), Module Number (number), Status (status), Unit (select), Assigned (person), IM/OUR Lessons (multi_select), Primary Toys (relation), Secondary Toys (relation), Script (text)

### Known Module Pages (Unit 2)

| Module | Page ID | Status |
|--------|---------|--------|
| M1 | 3225917eac5280639a2ed86044be1dbe | SME Review |
| M2 | 3225917eac528061bdb8c392f0bca2d2 | SME Review |
| M3 | 3255917eac5280d9ab27f9e77cfbbc49 | SME Review |
| M4 | 32c5917eac5280cbb216e3b456a4c8ac | SME Review |
| M5 | 32d5917eac528049a1a4c42d056221c3 | SME Review |
| M6 | 32d5917eac5280f2a153d5c4da5bb504 | Initial Draft |
| M7 | 32e5917eac52815b8945f14cc69d476f | Initial Draft |

---

## OPERATION 1: LIST MODULES

```
notion-query-data-sources:
  data_source_urls: ["collection://3185917e-ac52-80c0-a46b-000be3c6a416"]
  query: SELECT url, "Name", "Module Number", "Status", "Unit"
         FROM "collection://3185917e-ac52-80c0-a46b-000be3c6a416"
         WHERE "Unit" = 'Unit 2' ORDER BY "Module Number"
```

---

## OPERATION 2: PULL (Notion → Local)

Use when you need a local working copy for evaluation or batch processing.

### Steps

1. **Fetch** the page via `notion-fetch` with the page ID
2. **Convert** using the pull converter script:
   ```bash
   python <workspace>/.claude/scripts/sp_notion_pull.py <notion_json_file> --module N --output <path>
   ```
   This adds the local-only elements (# MODULE H1, Hub Properties block, Version line) that the evaluation checkers expect.
3. **Save** to `<workspace>/G3U2M{N}_Notion_Ready.md`

### Format Differences: Notion vs Local

| Element | Notion Page | Local File |
|---------|-------------|------------|
| Module title | Page title (property) | `# MODULE N: Title` (H1) |
| Properties | Database columns | `<!-- HUB PROPERTIES -->` block |
| Version | Not stored | `**Version:** MM.DD.YY` line |
| Content start | `# BACKBONE` | After H1 + Hub block |
| Markup | May include `<mention>`, `<span>`, `<bookmark>` | Clean markdown |

---

## OPERATION 3: PUSH (Local → Notion)

**This is the primary output path.** After evaluating and fixing an SP locally, push it back to Notion.

### For EXISTING pages (update)

1. **Convert** the local file to Notion format:
   ```bash
   python <workspace>/.claude/scripts/sp_notion_push.py <local_sp.md> --json
   ```
   Returns `{ "content": "...", "properties": {...}, "module_num": N, "title": "..." }`

2. **Look up the page ID** from the Known Module Pages table above, or query the database.

3. **Replace content** via `notion-update-page`:
   ```
   notion-update-page:
     page_id: <page_id>
     command: replace_content
     new_str: <the content field from step 1>
   ```

4. **Update properties** if changed:
   ```
   notion-update-page:
     page_id: <page_id>
     command: update_properties
     properties: { "Status": "SME Review", ... }
   ```

### For NEW pages (create)

1. **Convert** the local file using `sp_notion_push.py --json`
2. **Create** via `notion-create-pages`:
   ```
   notion-create-pages:
     parent:
       data_source_id: "3185917e-ac52-80c0-a46b-000be3c6a416"
     pages:
       - properties:
           Name: "Module N: Title"
           Module Number: N
           Unit: "Unit 2"
           Status: "Initial Draft"
         content: <the content field>
   ```

### Content Format Rules for Push

The `sp_notion_push.py` script handles stripping local artifacts, but when pushing manually, remember:
- **Do NOT include** the `# MODULE N:` H1 — Notion uses the page title
- **Do NOT include** the `<!-- HUB PROPERTIES -->` block — use DB columns
- **Do NOT include** the `**Version:**` line — not a Notion concept
- Content should start with `# BACKBONE` or the first `---` divider
- Standard markdown works — Notion will render it

---

## OPERATION 4: TARGETED FIX (Edit in Place on Notion)

For small, specific fixes, use `update_content` to search-and-replace directly on the Notion page without pulling/pushing the whole file.

### Steps

1. **Fetch** the current page to get exact text to match:
   ```
   notion-fetch: { id: <page_id> }
   ```

2. **Build content updates** — each is an old_str → new_str pair:
   ```
   notion-update-page:
     page_id: <page_id>
     command: update_content
     content_updates:
       - old_str: "# PHASE SPECIFICATIONS"
         new_str: "## PHASE SPECIFICATIONS"
       - old_str: "#### Module Configuration"
         new_str: "### Module Configuration"
   ```

### Best for:
- Heading level fixes (H4→H3, extra H1→H2)
- Field name renames (Method→Student Action)
- Small text corrections
- Adding missing markers

### Not suitable for:
- Section reordering (use full replace_content instead)
- Large structural changes
- Anything that changes >10 locations (use full push)

---

## OPERATION 5: EVALUATE AND COMMENT

Run evaluation, then post findings as a Notion comment for team visibility.

1. **Pull** the SP (Operation 2)
2. **Run** `sp-quick-check` or `sp-gate-eval`
3. **Post** findings via `notion-create-comment`:
   ```
   notion-create-comment:
     page_id: <page_id>
     content: |
       🔍 **SP Evaluation — Gate N — YYYY-MM-DD**

       **VERDICT**: 0 CRITICAL, 4 MAJOR, 12 MINOR

       **Top findings:**
       • [ST11] MAJOR: §1.7 ordering — Required/Forbidden Phrases after Purpose Frame
       • [MM2] MAJOR: Missing vocab term "square unit" from §1.3
       • [VO3] MINOR: 8 exclamation marks in Lesson phase (max 6)
       • [NC8] MAJOR: 4 H1 headings (expected 3)
   ```

---

## OPERATION 6: DIFF (Local vs Notion)

Compare a local working copy against the live Notion version:

1. **Pull** the current Notion version to a temp file
2. **Diff** using bash:
   ```bash
   diff <local_file> <notion_pulled_file> | head -100
   ```
3. Present summary: sections added/removed/changed, property differences

---

## PIPELINE: EVALUATE → FIX → PUSH

The full closed-loop workflow:

1. `sp-notion-sync` → Pull from Notion (Operation 2)
2. `sp-quick-check` → Run Layer 1 checkers
3. `sp-fix` → Apply Category A auto-fixes locally
4. `sp-quick-check` → Verify fixes resolved
5. `sp-notion-sync` → Push fixed content back (Operation 3)
6. `sp-notion-sync` → Post evaluation comment (Operation 5)

---

## NOTES

- **Notion is the source of truth.** Local files are ephemeral working copies.
- The Notion MCP can be slow for large pages (SPs are 1000+ lines). Be patient.
- `notion-fetch` returns enhanced markdown with Notion-specific tags. The `sp_notion_pull.py` script cleans these automatically.
- Primary/Secondary Toys are relation fields. To resolve names, fetch the related pages from `collection://f6c8ab4c-cd67-4cbe-9a43-6604ae1680fa`.
- Check `Status` before evaluating — "Initial Draft" modules may be too incomplete for meaningful eval.
- When using `replace_content`, Notion will warn if child pages would be deleted. Always check the error and preserve child content.
