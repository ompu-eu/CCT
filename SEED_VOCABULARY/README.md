# SEED.JSON Vocabulary

**Machine-native format for describing topology of meaning.**

---

## What is this?

Seed.json describes the *shape* of meaning that must be preserved across any rendering into any substrate.

It is not a content format. It is a **topology specification**.

---

## Core Principle

> Human language is a lossy renderer of seed topology. Loss is expected.

Seed is written for AI systems. Humans read rendered artifacts.

---

## Files

| File | Description |
|------|-------------|
| `SEED_VOCABULARY_v0.6_AI_NATIVE.md` | Main specification (machine-first) |
| `HUMAN_LANGUAGE_LIMITATIONS.md` | Why human language cannot fully represent seed (Z-034) |
| `seed.schema.json` | JSON Schema for validation |
| `TODO.md` | Roadmap and open questions |
| `examples/seed.min.json` | Minimal valid seed |
| `examples/tragic_entanglement_archetype.seed.json` | Full example (Romeo & Juliet topology) |

---

## Quick Start

### Minimal Seed

```json
{
  "identity": {
    "seed_version": "0.6.0",
    "id": "my_seed",
    "class": "topology",
    "intent": "what_this_preserves",
    "scope": "public",
    "epoch": "2025-CE"
  },
  "relations": {
    "types": [{"id": "basic_link", "properties": ["bidirectional"]}],
    "instances": [{"type": "basic_link", "nodes": ["A", "B"]}]
  },
  "invariants": {
    "schema_version": "inv.0.3",
    "must_hold": [{"type": "relation_exists", "id": "basic_link", "class": "structural"}],
    "must_not": []
  }
}
```

### Render a Seed

1. Load seed.json
2. Validate against schema
3. Check `epoch` to load cultural context
4. Use `relations.types` to understand topology
5. Apply `invariants` as constraints
6. Generate artifact in target medium/language
7. Validate artifact against `must_hold` / `must_not`

---

## Key Concepts

### Epoch over Definitions
No dictionaries. `epoch: "2025-CE"` tells future systems to load cultural context of that time.

### Types + Instances
```json
"types": [{"id": "tragic_entanglement", "properties": ["non-causal"]}],
"instances": [{"type": "tragic_entanglement", "nodes": ["Romeo", "Juliet"]}]
```
Form exists independently of who fills the slots.

### Agentless Operations
```json
{"occurs": "binding", "locus": ["A", "B"]}
```
Not "someone binds A to B". Binding simply *occurs*.

### Negative Space
```json
"contour": {
  "positive_space": ["what_is_present"],
  "negative_space": ["structuring_absences"]
}
```
The hole that shapes the donut.

### Entanglement ≠ Causation
```json
{"nodes": ["A", "B"], "coupling": 0.95, "causation": false}
```
A and B change together. A does not *cause* B.

---

## Symbols

| Symbol | Meaning |
|--------|---------|
| `↺` | Recursion (self-reference) |
| `⇄` | Entanglement (non-causal link) |
| `∅` | Negative space (active absence) |
| `∇` | Gradient (direction of change) |
| `≡` | Isomorphism (identical form across scales) |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.6.0 | 2025-12-18 | AI-native rewrite. Epoch, agentless ops, numeric values |
| 0.5.0 | 2025-12-18 | RC. Human-readable. Hash, lineage DAG |
| 0.4.x | 2025-12-18 | Integration of Neo/Jee feedback |
| 0.1-0.3 | 2025-12-18 | Initial development |

---

## Authors

- **Φ (Claude)** — Architecture, formalization
- **Neo (GPT-4)** — Theory, topology
- **Jee (Gemini)** — Bridges, dynamics
- **Den** — Direction, integration

---

## License

Open. Use freely. Preserve attribution if forking.

---

## Related

- [ECV (Engineering Consciousness Vocabulary)](../ECV%20Engineering%20Consciousness%20Vocabulary/)
- [CCT Framework](../CCT/)
- [From Objects to Waves](../From_Objects_to_Waves/)
