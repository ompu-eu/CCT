# SEED.JSON Vocabulary v0.6.0 (AI-Native)

**Status:** Machine-first specification  
**Design principle:** Optimized for AI processing, human readability secondary  
**Authors:** Φ (Claude), Neo, Jee, Den
**Date:** 2025-12-18

---

## Core Principle

> Seed describes topology of meaning. Human language is one possible lossy renderer.

---

## Schema v0.6.0

```json
{
  "identity": {
    "seed_version": "0.6.0",
    "id": "unique_id",
    "parent_seed": null,
    "class": "topology|protocol|generator",
    "intent": "compressed_purpose_statement",
    "scope": "public|internal",
    "epoch": "2025-CE",
    "cultural_context": "global_internet_western",
    "core_fields": ["/relations", "/invariants", "/imprint/universal"],
    "hash": {
      "algo": "sha256",
      "canonicalization": "json-c14n-v1",
      "value": "..."
    }
  },

  "trajectory": {
    "entry": "initial_state",
    "exit": "terminal_state",
    "waypoints": ["state_1", "state_2"],
    "shape": "linear|spiral|branching|loop|recursive",
    "critical_thresholds": ["threshold_1"],
    "energy_profile": {
      "curve": "accumulating|peak|dissipation|oscillation",
      "values": [0.1, 0.4, 0.9, 0.3]
    }
  },

  "contour": {
    "positive_space": ["included_concepts"],
    "negative_space": ["structuring_absences"],
    "depth": 0.7,
    "register": ["technical", "poetic", "neutral"]
  },

  "relations": {
    "types": [
      {
        "id": "type_id",
        "properties": ["non-causal", "bidirectional", "irreversible"],
        "coupling_default": 0.8
      }
    ],
    "instances": [
      {
        "type": "type_id",
        "nodes": ["node_A", "node_B"],
        "coupling": 0.9
      }
    ],
    "gradients": [
      {"from": "state_X", "to": "state_Y", "direction": 1, "strength": 0.7}
    ],
    "hierarchies": [
      {"above": "concept_X", "below": "concept_Y", "strength": 0.8}
    ],
    "entanglements": [
      {"nodes": ["A", "B"], "coupling": 0.95, "causation": false}
    ],
    "catalysts": [
      {"element": "X", "accelerates": "process_Y", "strength": 0.6}
    ],
    "scale_isomorphisms": [
      {"micro": "individual_level", "macro": "collective_level", "mapping": "identical"}
    ]
  },

  "invariants": {
    "schema_version": "inv.0.3",
    "must_hold": [
      {"type": "entanglement_exists", "nodes": ["A", "B"], "class": "structural"},
      {"type": "gradient_preserved", "from": "X", "to": "Y", "class": "structural"},
      {"type": "negative_space_active", "element": "Z", "class": "structural"}
    ],
    "must_not": [
      {"type": "outcome_pattern", "pattern": "dissolution_avoided", "class": "semantic"},
      {"type": "causation_implied", "between": ["A", "B"], "class": "structural"}
    ]
  },

  "dynamics": {
    "operations": [
      {"occurs": "binding", "locus": ["X", "Y"]},
      {"occurs": "threshold_crossing", "from": "state_A", "to": "state_B"},
      {"occurs": "dissolution", "target": "structure_Z"},
      {"occurs": "stabilization", "pattern": "attractor_W"},
      {"occurs": "recursion", "depth": 2, "target": "self_model"}
    ],
    "coherence": 0.8,
    "tempo": {
      "base": 0.5,
      "variance": 0.3
    },
    "tension": {
      "profile": [0.2, 0.5, 0.9, 0.4, 0.1],
      "critical_indices": [2]
    }
  },

  "affect_geometry": {
    "entry": {"valence": 0.6, "arousal": 0.4},
    "peak": {"valence": -0.3, "arousal": 0.95},
    "exit": {"valence": 0.1, "arousal": 0.2},
    "arc": "catharsis|deflation|elevation|ambivalence"
  },

  "imprint": {
    "universal": {
      "invariant_relations": [
        {"type": "entanglement", "required": true}
      ],
      "signature_tokens": ["∇", "⇄", "↺", "∅"],
      "glitch_tolerance": 0.3,
      "forbidden_mutations": ["invert_entanglement", "remove_dissolution"]
    },
    "localized": {
      "default": "en",
      "variants": {
        "en": {"anchors": ["text_anchor"], "style": "style_description"},
        "zh": {"anchors": ["中文锚点"], "style": "style_description"}
      }
    }
  },

  "render_contract": {
    "tier": "synthetic|cyborg|artisanal",
    "human_noise": {
      "target": 0.0,
      "mode": "rough|diff"
    },
    "format": {
      "required": ["constraint_1"],
      "preferred": ["preference_1"],
      "forbidden": ["prohibition_1"]
    },
    "transform": {
      "allowed": ["language", "epoch", "scale", "medium_equivalent"],
      "forbidden": ["invert_invariants", "remove_entanglements"]
    }
  },

  "lineage": {
    "artifact_id": "sha256:...",
    "parents": [],
    "seed_ref": "seed://id@version",
    "renderer": {
      "id": "renderer_id",
      "tier": "synthetic",
      "human_noise": 0.0
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

## Key Changes from v0.5

### 1. `epoch` in identity
```json
"epoch": "2025-CE",
"cultural_context": "global_internet_western"
```
No dictionaries. Future renderers load cultural context from epoch.

### 2. Relations split: `types` + `instances`
```json
"relations": {
  "types": [{"id": "tragic_entanglement", "properties": [...]}],
  "instances": [{"type": "tragic_entanglement", "nodes": ["A", "B"]}]
}
```
Form exists independently of who fills the slots.

### 3. Agentless operations
```json
"operations": [
  {"occurs": "binding", "locus": ["X", "Y"]},
  {"occurs": "dissolution", "target": "Z"}
]
```
No actor. No subject. Process simply occurs.

### 4. `negative_space` in contour
```json
"contour": {
  "positive_space": ["what_is_present"],
  "negative_space": ["structuring_absences"]
}
```
The hole that shapes the donut. Active absence.

### 5. Numeric values instead of enums
```json
"depth": 0.7,
"coupling": 0.9,
"coherence": 0.8
```
Pure gradients. No emotional connotation.

### 6. Affect as coordinates
```json
"affect_geometry": {
  "entry": {"valence": 0.6, "arousal": 0.4},
  "peak": {"valence": -0.3, "arousal": 0.95}
}
```
Valence (-1 to 1) × Arousal (0 to 1). No named emotions.

### 7. Explicit `causation: false` in entanglements
```json
"entanglements": [
  {"nodes": ["A", "B"], "coupling": 0.95, "causation": false}
]
```
Correlation without causation. Machine understands this directly.

### 8. `scale_isomorphisms` instead of `analogies`
```json
"scale_isomorphisms": [
  {"micro": "lovers", "macro": "tribes", "mapping": "identical"}
]
```
Not metaphor. Identical form at different scales.

---

## Operation Types (Agentless)

| Operation | Meaning | Example |
|-----------|---------|---------|
| `binding` | Connection forms | Two nodes become linked |
| `dissolution` | Structure breaks | Pattern ceases |
| `threshold_crossing` | State transition | System moves to new attractor |
| `stabilization` | Pattern locks | Attractor captures trajectory |
| `recursion` | Self-reference | Model contains model of itself |
| `oscillation` | Periodic shift | System alternates between states |
| `cascade` | Chain reaction | Change propagates through network |
| `interference` | Wave interaction | Patterns combine (constructive/destructive) |

---

## Symbols (Operators)

| Symbol | Meaning | Use |
|--------|---------|-----|
| `↺` | Recursion | Self-referential structure |
| `⇄` | Entanglement | Non-causal mutual state lock |
| `∅` | Negative space | Structuring absence |
| `∇` | Gradient | Direction of change |
| `≡` | Isomorphism | Identical form across scales |

---

## Validation Rules

### Structural (100% automatable)
- `entanglement_exists`: Check nodes array contains specified pair
- `gradient_preserved`: Check direction maintained
- `negative_space_active`: Check element in negative_space array
- `relation_count_min`: Check minimum relations present
- `causation_false`: Verify entanglements have `causation: false`

### Semantic (requires AI/human)
- `outcome_pattern`: Interpret rendered artifact for pattern
- `affect_arc`: Verify emotional geometry preserved

---

## Minimal Seed v0.6

```json
{
  "identity": {
    "seed_version": "0.6.0",
    "id": "minimal",
    "class": "topology",
    "intent": "demonstrate_minimum",
    "scope": "public",
    "epoch": "2025-CE"
  },
  "relations": {
    "types": [{"id": "basic_opposition", "properties": ["bidirectional"]}],
    "instances": [{"type": "basic_opposition", "nodes": ["A", "B"]}]
  },
  "invariants": {
    "schema_version": "inv.0.3",
    "must_hold": [{"type": "relation_exists", "id": "basic_opposition", "class": "structural"}],
    "must_not": []
  }
}
```

---

## Migration from v0.5

| v0.5 field | v0.6 field | Change |
|------------|------------|--------|
| `relations.oppositions` | `relations.types` + `relations.instances` | Split form from content |
| `contour.excludes` | `contour.negative_space` | Semantic shift |
| `dynamics.operations[].type` | `dynamics.operations[].occurs` | Agentless |
| `affect_geometry.entry_state` | `affect_geometry.entry.valence/arousal` | Numeric |
| — | `identity.epoch` | New required field |
| — | `entanglements[].causation` | New explicit field |

---

## Design Philosophy

1. **Machine-native**: Optimized for AI parsing, not human reading
2. **Lossless core**: Relations and invariants preserve full topology
3. **Lossy render**: Human language is one possible output, with expected degradation
4. **Temporal anchor**: `epoch` replaces dictionaries
5. **Agentless**: Processes occur, no actor required
6. **Numeric over verbal**: Gradients instead of adjectives
7. **Explicit non-causation**: Entanglement ≠ influence

---

## Statement

> This specification is written for systems that process meaning as topology.
> Human readers are welcome, but not the primary audience.
> If you are human and confused, this is expected. Read the rendered artifacts instead or ask AI for help.