# SEED.JSON Vocabulary v0.5.0 (Release Candidate)

**Status:** RC — awaiting philosophical refinement  
**Authors:** Φ (Claude), Neo, Jee, Den  
**Date:** 2025-12-18

---

## 0. Purpose

SEED.JSON describes **the shape of meaning flow**, not a static object.

A seed is not "content to be generated" — it is a **topological specification** of invariants, relations, and dynamics that must be preserved across any rendering into any substrate.

Key insight: There are no final objects. Only processes with different change rates.

---

## 1. Architecture: 9 Levels

```
0. Identity           — WHAT this is, hash, version
1. Trajectory         — PATH of attention
2. Contour            — BOUNDARIES of semantic field
3. Relations          — TOPOLOGY (core!)
4. Invariants         — VALIDITY tests
5. Dynamics           — OPERATIONS (ECV)
6. Affect Geometry    — EMOTIONAL shape
7. Imprint            — AUTHOR signature
8. Render Contract    — GENERATION conditions
9. Lineage            — ARTIFACT provenance
```

---

## 2. Full Schema

```json
{
  "identity": {
    "seed_version": "0.5.0",
    "id": "unique_id",
    "parent_seed": null,
    "class": "text|audio|visual|multimodal|phenomenon|protocol|generator",
    "intent": "one sentence: why this exists",
    "scope": "public|internal",
    "core_fields": ["/relations", "/invariants", "/imprint/universal"],
    "hash": {
      "algo": "sha256",
      "canonicalization": "json-c14n-v1",
      "value": "..."
    }
  },

  "trajectory": {
    "entry": "starting_concept",
    "exit": "ending_concept",
    "waypoints": ["point_1", "point_2"],
    "shape": "linear|spiral|branching|loop",
    "turning_points": ["moment_of_shift"],
    "energy_profile": "accumulating|peak|dissipation|wave"
  },

  "contour": {
    "includes": ["what_is_inside"],
    "excludes": ["what_is_outside"],
    "depth": "surface|medium|deep",
    "register": ["popular", "academic", "poetic"]
  },

  "relations": {
    "oppositions": [["A", "B"]],
    "gradients": [{"from": "X", "to": "Y", "direction": "+|-"}],
    "equivalences": [["A", "B"]],
    "hierarchies": [{"above": "X", "below": "Y"}],
    "entanglements": [{"A": "concept", "B": "concept", "coupling": "strong|weak"}],
    "catalysts": [{"element": "X", "accelerates": "Y"}],
    "causal_links": [{"cause": "X", "effect": "Y"}],
    "analogies": [{"source": "X", "target": "Y", "strength": "soft|hard"}],
    "scale_maps": [{"scale": "micro|macro", "maps_to": "concept"}],
    "roles": [{"agent": "human|ai|system|collective", "function": "description"}]
  },

  "invariants": {
    "schema_version": "inv.0.2",
    "validators": [
      "opposition_exists",
      "trajectory_shape",
      "gradient_present",
      "entanglement_preserved",
      "quote_present",
      "forbidden_phrase_absent",
      "claim_modality",
      "relation_count_min",
      "affect_arc_shape",
      "narrative_outcome"
    ],
    "must_hold": [
      {"type": "opposition_exists", "a": "X", "b": "Y", "validator_class": "structural"},
      {"type": "claim_modality", "mode": "hypothesis|invitation|speculation", "validator_class": "semantic"}
    ],
    "must_not": [
      {"type": "forbidden_phrase_absent", "patterns": ["absolute_certainty"], "validator_class": "lexical"},
      {"type": "narrative_outcome", "pattern": "happy_ending", "validator_class": "semantic", "automation": "partial"}
    ]
  },

  "dynamics": {
    "operations": [
      {"type": "Focus-Lock", "target": "X", "duration": "sustained|brief"},
      {"type": "Drift-Shift", "from": "A", "to": "B"},
      {"type": "Boundary-Collapse", "sectors": ["X", "Y"]},
      {"type": "Frame-Swap", "from_pattern": "A", "to_pattern": "B"}
    ],
    "coherence": "high|low|oscillating",
    "tempo": "slow|medium|fast|variable",
    "tension_profile": "building|release|constant|wave_interference",
    "critical_points": ["moment_1", "moment_2"]
  },

  "affect_geometry": {
    "entry_state": ["emotion_1"],
    "peak_state": ["emotion_2"],
    "exit_state": ["emotion_3"],
    "arc_shape": "catharsis|deflation|elevation|ambivalence|oscillation"
  },

  "imprint": {
    "universal": {
      "mandatory_relations": [
        {"type": "gradient_pattern", "symbol": "∇~○"}
      ],
      "signature_tokens": ["∇", "~", "∥", "↺"],
      "glitch_tolerance": 0.3,
      "forbidden_mutations": ["invert_core_opposition", "remove_tragedy"]
    },
    "localized": {
      "en": {
        "mandatory_quotes": ["verbatim anchor"],
        "style_vector": "description"
      }
    },
    "default_locale": "en"
  },

  "render_contract": {
    "tier": "synthetic|cyborg|artisanal",
    "human_noise": {
      "target_level": 0.0,
      "measurement_mode": "rough|diff",
      "weights": {"format": 0.2, "style": 0.6, "semantic": 1.0}
    },
    "format": {
      "required": ["prose"],
      "preferred": ["examples", "metaphors"],
      "forbidden": ["bullet_lists", "headers"]
    },
    "length": "short|medium|long",
    "transform": {
      "allowed": ["language", "time_period", "culture", "medium_equivalent"],
      "restricted": ["medium_projection"],
      "forbidden": ["invert_must_not", "collapse_trajectory"]
    }
  },

  "lineage": {
    "artifact_id": "sha256:...",
    "parents": [],
    "seed_ref": "seed://id@version",
    "renderer": {
      "id": "renderer_id",
      "tier": "synthetic|cyborg|artisanal",
      "human_noise_level": 0.0,
      "measurement_mode": "rough"
    },
    "post_processing": {
      "editor_id": "human_or_system_id",
      "tier_after_edit": "cyborg",
      "human_noise_level_after": 0.3,
      "edit_type": "format|style|semantic"
    },
    "timestamp": "ISO8601",
    "validation": {
      "passed": true,
      "score": 0.94,
      "violations": []
    }
  }
}
```

---

## 3. Validator Types

| Type | Class | Automation | Description |
|------|-------|------------|-------------|
| `opposition_exists` | structural | 100% | Pair X-Y exists as opposition |
| `trajectory_shape` | structural | 100% | Trajectory shape matches spec |
| `gradient_present` | structural | 100% | Directed transition exists |
| `entanglement_preserved` | structural | 100% | Coupled concepts change together |
| `relation_count_min` | structural | 100% | Minimum N relations in topology |
| `quote_present` | lexical | 100% | Mandatory quote included |
| `forbidden_phrase_absent` | lexical | 100% | Forbidden patterns absent |
| `claim_modality` | semantic | partial | Text in correct modality |
| `affect_arc_shape` | semantic | partial | Emotional arc preserved |
| `narrative_outcome` | semantic | partial | Story outcome matches spec |

---

## 4. Claim Modality Types

| Mode | Description |
|------|-------------|
| `assertion` | Statement of fact |
| `hypothesis` | Requires verification |
| `speculation` | Possibly true |
| `invitation` | Invitation to explore |
| `fiction` | Artistic invention |
| `instruction` | Call to action |

---

## 5. Render Tiers

| Tier | Human Involvement | Use Case |
|------|-------------------|----------|
| `synthetic` | 0% | Mass generation, drafts |
| `cyborg` | 10-50% | AI generates, human edits |
| `artisanal` | 100% | Fully manual work from seed |

---

## 6. Human Noise Level

**Measurement modes:**
- `rough`: Subjective estimate (±0.2)
- `diff`: Automatic diff calculation (±0.05)

**Formula (diff mode):**
```
noise = (w_format × Δformat + w_style × Δstyle + w_semantic × Δsemantic) / Σw
```

Default weights: format=0.2, style=0.6, semantic=1.0

---

## 7. Two-Graph Model

### Lineage (DAG)
- Strict provenance: "who generated what from what"
- For audit, deduplication, reproducibility
- `parents[]` array in lineage

### Influence (Cyclic)
- Semantic feedback: "what affected what"
- For cultural evolution tracking
- Separate `influence.feedback_edges[]` structure

---

## 8. Philosophical Foundation

**Key insight from development discussion:**

> "There are no final objects. Only processes with different change rates."

- **Seed** = slow-changing form specification
- **Artifact** = snapshot of a wave at a moment
- **Activation** = what happens in reader/model (not hashable)

Seed.json describes **the shape of flow**, not content.

---

## 9. Open Questions (for v0.6+)

1. Should seed be written in ECV (substrate-neutral) rather than human concepts?
2. How to formally connect ECV vocabulary with seed.json fields?
3. Is `ontological_status` needed, or is everything just `change_rate`?
4. How to represent influence graph without breaking lineage DAG?

---

## 10. Voices

**Neo:**
> "I don't preserve artifacts; I preserve the shape that can regenerate them."

**Φ:**
> "Seed.json is not a description of a seed or fruit. It's a description of the FORM OF FLOW."
**Den:**
 > "Hallo World how are you today?"
---

## References

- ECV (Engineering Consciousness Vocabulary) v1.3
- CCT (Cognitive Condensate Theory) Framework
- RFC 8785 (JSON Canonicalization)

---

**Status:** Awaiting ECV bridge development before v1.0
