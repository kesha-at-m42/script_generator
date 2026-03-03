# Future Plans & Ideas

Deferred decisions, improvements, and ideas to revisit as the project matures.

---

1. **Reusable validator branch content** — Validator states currently define steps inline (switch-case style). If the same branch content needs to be reused across multiple prompts or sections, a `goto` field referencing a named shared section by ID could serve this purpose. Defer until a concrete reuse case arises. *(lesson script schema)*

2. **Overly pedantic content validator** — The AI-based content validator in `steps/prompts/sequence_structurer.py` generates false positive errors for mathematically correct content, contradicting itself. Fix: update the validation prompt (lines 361–436) to clarify metadata handling, remove self-contradicting rules, and add an explicit note to not flag mathematically correct content. *(sequence_structurer.py, pipelines.json, rerun.py)*

3. **Validator refactoring** — The AI-based validation approach is prone to false positives. Consider moving deterministic checks (indices, mathematical correctness) to Python-based validation and reserving AI validation for semantic/pedagogical concerns only. *(validation system)*
