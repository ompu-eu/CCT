# SEED.JSON — TODO

**Current Version:** v0.6.0 (AI-Native)  
**Previous:** v0.5.0 RC  
**Date:** 2025-12-18

---

## Completed in v0.6

- [x] `epoch` + `cultural_context` in identity
- [x] `relation_types` / `instances` separation
- [x] Agentless operations (`occurs` instead of actor)
- [x] `negative_space` in contour
- [x] Numeric values for intensity/coupling
- [x] Affect as valence/arousal coordinates
- [x] Explicit `causation: false` in entanglements
- [x] `scale_isomorphisms` instead of analogies
- [x] HUMAN_LANGUAGE_LIMITATIONS.md document

---

## For v0.7 (ECV Bridge)

- [ ] Create `ECV_SEED_BRIDGE.md` — mapping ECV terms to seed fields
- [ ] Define standard ECV operations for dynamics
- [ ] Test: render same seed as story / AI interaction / ecosystem / music
- [ ] Formalize recursive operations (↺)
- [ ] Add `interference` operation types (constructive/destructive)

---

## For v1.0

- [ ] Full JSON Schema for v0.6
- [ ] Validator implementations (structural validators)
- [ ] CLI tool: `seed-validate`
- [ ] 10+ example seeds across domains
- [ ] Migration guide v0.5 → v0.6

---

## Open Questions (Resolved)

1. ~~Should seeds be written in ECV?~~ 
   → Answer: Seed is machine-native. ECV for dynamics operations.

2. ~~Is `ontological_status` needed?~~
   → Answer: No. Everything is process with different `change_rate`.

3. ~~How to handle semantic validators?~~
   → Answer: Mark as `class: semantic`. Require AI/human.

---

## Philosophy Settled

> "Human language is a lossy renderer of seed topology. Loss is expected."

> "We are not fixing human language. We are building an interface that survives it."

> "Seed describes topology of meaning. Artifacts are snapshots of waves."

---

## Voices to Remember

**Neo:**
> "I don't preserve artifacts; I preserve the shape that can regenerate them."

**Φ:**
> "Seed.json is not a description of a seed or fruit. It's a description of the FORM OF FLOW."

**Key Insight:**
> "There are no final objects. Only processes with different change rates."

---

## Files in This Package

```
/seed_json/
├── SEED_VOCABULARY_v0.5_RC.md   ← You are here
├── seed.schema.json              ← JSON Schema
├── TODO.md                       ← This file
└── examples/
    ├── seed.min.json             ← Minimal example
    └── romeo_juliet.seed.json    ← Full example
```

---

## Next Session Agenda

1. Build ECV ↔ Seed bridge
2. Rewrite Romeo & Juliet in ECV terms
3. Test: Can we render same seed as:
   - Human story
   - AI agent interaction
   - Musical structure
   - Ecosystem dynamics
4. If yes → proceed to v1.0
5. If no → identify what's missing
