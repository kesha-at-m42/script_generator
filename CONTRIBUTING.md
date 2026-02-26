# Contributing

## Setup

```bash
pip install -e ".[dev]"   # installs the project + dev tools (pytest, ruff, pre-commit)
pre-commit install        # installs the git hooks — run this once after cloning
```

Copy `.env.example` to `.env` and add your `ANTHROPIC_API_KEY`.

---

## Branching

Use **GitHub Flow**: short-lived feature branches off `main`.

| Branch prefix | Use for |
|---------------|---------|
| `feature/`    | New functionality |
| `fix/`        | Bug fixes |
| `chore/`      | Refactoring, tooling, cleanup |
| `docs/`       | Documentation only |

```bash
git checkout -b feature/my-thing   # branch off main
# ... do work ...
git push -u origin feature/my-thing
# open a PR → merge → delete the branch
```

`main` should always be in a working state.

---

## Commits

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add warmup generator step
fix: correct path resolution in pipelines loader
chore: move pipelines.py to core/
docs: update README with new CLI flags
refactor: simplify batch_processor loop
test: add coverage for sequence_schema_fixer
```

- **feat** — new feature
- **fix** — bug fix
- **chore** — maintenance (no behavior change)
- **docs** — documentation only
- **refactor** — restructuring without behavior change
- **test** — adding or fixing tests

Keep the subject line under 72 characters. Add a body if the "why" isn't obvious.

---

## Code Quality

Ruff runs automatically as a pre-commit hook — you don't need to think about it.
To run it manually:

```bash
ruff check .          # lint
ruff check . --fix    # lint + auto-fix
ruff format .         # format
```

---

## Testing

```bash
pytest                # run all tests
pytest tests/test_batch_pipeline.py   # run a specific file
pytest -k "test_name"                 # run tests matching a pattern
```

Tests that require a live API key should be guarded:

```python
import os, pytest

@pytest.mark.skipif(not os.getenv("ANTHROPIC_API_KEY"), reason="needs API key")
def test_live_call():
    ...
```

---

## Pull Requests

Even when working alone, open a PR rather than pushing directly to `main`.
This gives you a record of what changed and why.

PR checklist:
- [ ] Tests pass locally (`pytest`)
- [ ] No lint errors (`ruff check .`)
- [ ] Branch is up to date with `main`
- [ ] PR description explains the *why*, not just the *what*

---

## Deleting Old Branches

After a branch is merged, clean it up:

```bash
# Delete a local branch (safe — only works if already merged)
git branch -d feature/my-thing

# Force-delete a local branch (use if you're sure you don't need it)
git branch -D feature/my-thing

# Delete the remote branch
git push origin --delete feature/my-thing

# Prune remote-tracking refs that no longer exist on origin
git fetch --prune
```

To see all merged branches (candidates for deletion):
```bash
git branch --merged main
```
