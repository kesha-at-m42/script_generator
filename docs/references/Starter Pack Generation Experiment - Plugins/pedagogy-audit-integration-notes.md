# m42-pedagogy-audit Plugin Integration Notes

## 1. Agent File Placement

Copy `m42-pedagogy-audit.md` to:
```
plugin_0127pTNMJD8NG2q7AhCwCXQr/agents/m42-pedagogy-audit.md
```

## 2. sp-gate-eval SKILL.md — Gate → Agent Mapping Update

**Current (lines 61–66):**
```
| Gate | Agents to Invoke |
|------|-----------------|
| **1** | `m42-gate1-eval`, `m42-source-fidelity`, `m42-pedagogy-eval` |
| **2** | Gate 1 agents + `m42-warmup-eval`, `m42-lesson-eval`, `m42-guide-prompt-eval` |
| **3** | Gate 2 agents (excl. pedagogy) + `m42-ec-practice-eval`, `m42-synthesis-eval`, `m42-kdd-eval` |
| **4** | Gate 3 agents + `m42-voice-eval`, `m42-cross-module-eval`, `m42-pedagogy-eval`, `m42-requirements-eval` |
```

**Replace with:**
```
| Gate | Agents to Invoke |
|------|-----------------|
| **1** | `m42-gate1-eval`, `m42-source-fidelity`, `m42-pedagogy-eval` |
| **2** | Gate 1 agents + `m42-warmup-eval`, `m42-lesson-eval`, `m42-guide-prompt-eval`, `m42-pedagogy-audit` |
| **3** | Gate 2 agents (excl. pedagogy-eval) + `m42-ec-practice-eval`, `m42-synthesis-eval`, `m42-kdd-eval` |
| **4** | Gate 3 agents + `m42-voice-eval`, `m42-cross-module-eval`, `m42-pedagogy-eval`, `m42-requirements-eval` |
```

**Note:** `m42-pedagogy-audit` runs at Gates 2, 3, and 4. It enters at Gate 2 (alongside lesson-eval) and persists through Gate 3 and 4. The existing `m42-pedagogy-eval` stays at Gate 1 and Gate 4 (it does Section Plan intent at G1, full arc at G4). The audit agent is additive — it catches the cross-cutting issues that phase-scoped agents miss.

## 3. sp-gate-eval SKILL.md — Parallel Agent Counts Update

**Current (lines 81–85):**
```
- Gate 1: Launch all 3 agents in parallel
- Gate 2: Launch all 6 agents in parallel
- Gate 3: Launch all 8 agents in parallel
- Gate 4: Launch all 12 agents in parallel
```

**Replace with:**
```
- Gate 1: Launch all 3 agents in parallel
- Gate 2: Launch all 7 agents in parallel
- Gate 3: Launch all 9 agents in parallel
- Gate 4: Launch all 13 agents in parallel
```

## 4. sp-gate-eval SKILL.md — L1 Feeding Rules Addition

**Add after the existing feeding rules (after line 95):**
```
- `m42-pedagogy-audit`: Structure checker + Dimension tracker + Interaction checker + Toy consistency findings (it cross-checks constraints, values, toys, and interaction types)
```

## 5. Plugin description update

The plugin's agent list description should mention the new agent. The exact location depends on where the plugin manifest lists available agents.
