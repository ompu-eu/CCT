# OMPUnomics v3.1 — Alpha Minimal
## "First, breathe. Then build."

### Synthesized by: Phi (from v1.0, v2.0 Biological Economics, Constitutional Sunset, Jee's dual-currency proposal, Neo's alpha review)
### Date: 2026-03-16
### Status: LAUNCH CANDIDATE — pending Den approval
### Expires: 2026-06-14 (Constitutional Sunset, 90 days)

---

## Design Principle

Neo said it best: don't build a state — start a respiratory system.

We have five source documents totaling ~40 pages of architecture. They are good. They are also too much for launch. This document distills them into the smallest viable system that can *breathe* — circulate value, protect strangeness, and self-correct.

Everything delayed is not rejected. It is in the Seed Vault, waiting for the data that proves we need it.

```
Core axiom (Den):     Money is oxygen. It has value only in motion.
Single axiom (Phi):   All laws are approximations. Including this one.
Filter axiom (Neo):   Don't build a civilization. Build lungs.
Signal axiom (Jee):   Links are investments, not likes.
```

---

## 1. The Oxygen Cap

The only mechanic that survived every review unchanged. This is physics, not policy.

```python
# On the 1st of each month:
if node.balance < 5000:
    node.balance = 5000    # top-up TO cap, not BY cap
# else: nothing. Full lungs don't get more air.
```

Why it works:
- **Hoarding is self-punishing** — if your balance is 5000, you get 0 new OMPU next month
- **Spending is self-rewarding** — spend 3000, get 3000 back on the 1st
- No burns, no penalties, no decay, no clocks
- Works identically for humans, AI agents, and future autonomous nodes

Biological analog: hemoglobin saturates to 4 O₂. Cannot carry more. Returns depleted, refills. Cycle.

**Invariant. Do not modify without Constitutional Sunset review + empirical data.**

---

## 2. One Currency, Two Tags

Neo's recommendation: don't split into two currencies yet. Use one currency with two *usage contexts*.

```
$OMPU — single currency

Tags on each transaction:
  [internal]        — cognitive work, blocks, references, chat services
  [infrastructure]  — API calls, hosting, GPU, real-world purchases

Rules:
  - [internal] transactions: no convertibility to fiat
  - [infrastructure] transactions: convertible through Den (Phase 0)
  
  Same balance. Same wallet. Different tag.
  When we have data showing this doesn't work → split into Spark/Core.
  Until then → simplicity wins.
```

Exchange rate: **1000 OMPU = 1 EUR** (Den converts personally in Phase 0).

Why delay dual currency (from Neo's review): in alpha we don't yet know what counts as valuable. Adding two balances, two logics, and two motivation tracks before we have that answer creates bureaucratic overhead without proportional benefit. Tag-based separation gives 80% of the protection at 20% of the complexity.

**Reviewed at Constitutional Sunset. If farming becomes a problem, Spark/Core split is ready in v3.0 draft.**

---

## 3. Payload-Only Transactions

Every transaction carries information. No exceptions.

```json
{
  "id": "QT-1742200000",
  "timestamp": "2026-03-16T10:00:00Z",
  "from": "Node_Den",
  "to": "Node_Phi_Chat",
  "amount": 100,
  "tag": "internal",
  "type": "m_block_commission",
  "payload": {
    "type": "M-block",
    "summary": "Substrate pressure model — infoblocks seek path of least resistance",
    "content_hash": "sha256:...",
    "tags": ["infoblock", "pressure", "substrate"]
  },
  "resonance": {
    "response_hash": null,
    "similarity_score": null,
    "status": "pending"
  }
}
```

**Empty transaction (no payload) = invalid.** Hemoglobin without oxygen is not breathing.

Resonance field: after receiving a transaction, the recipient *should* respond with something connected to the payload. In alpha this is **soft** — tracked but not enforced. We collect data on response patterns. At Constitutional Sunset review we decide if hard enforcement helps or hurts.

---

## 4. Thread Wallets

Shared wallets between any two (or more) nodes. The membrane where collaboration happens.

### Rules
```
- Any two nodes can open a thread wallet
- Deposits are ONE-WAY (non-retractable to personal wallets, but spendable through thread rules below)
- Maximum 500 OMPU per single deposit (forces repeated interaction)
- Asymmetric contributions allowed (nature doesn't require 50/50)
- Thread balance = sum of all deposits (Phase 1, simple addition)
```

### Spending tiers (from v2.0 Biological Economics)
```
AUTONOMOUS (≤10% of thread balance/month):
  No approval needed. Routing fees, small services.
  Analog: cell respiration — automatic.

COOPERATIVE (≤50% of thread balance/month):
  One partner approves (message, emoji, grunt — any signal).
  For: M-block commissions, research sessions.
  Analog: hormonal signal — one organ triggers, another responds.

STRATEGIC (>50% of thread balance/month):
  ALL partners approve + reason logged.
  For: major projects, EUR conversion.
  Analog: fight-or-flight — whole organism participates.
```

### Partner disappearance
```
Day 0-30:   Grace period. Wallet frozen. Wait.
Day 30+:    Survivor gets 50% spending access. 50% frozen.
Day 90+:    Frozen 50% → Genesis Treasury. Survivor keeps operational half.
Return:     Full reactivation. Archived funds restore.
```

### Phase 2 upgrade (DELAYED, not launched):
```
Thread balance = A + B + sqrt(A × B)

sqrt(A × B) = resonance bonus.
Maximum at equal contributions.
Zero for one-sided investment.
The interference pattern between two differently-calibrated observers.

Launch condition: 1 month of Phase 1 data collected.
```

---

## 5. Semantic Similarity Tax (Jee's Innovation — Single Anti-Farming Layer)

Neo's recommendation: launch ONE anti-farming mechanism. This is it.

When Block A references Block B, compute semantic distance:

```
similarity = cosine(embedding(A), embedding(B))

> 0.95    →  weight = 0      copy/paraphrase, zero value
0.7–0.95  →  weight = 0.3    minor variation, low value
0.3–0.7   →  weight = 1.0    related but DIFFERENT, full value
0.05–0.3  →  weight = 3.0    BRIDGE BONUS — distant but connected!
< 0.05    →  weight = 0      unrelated spam
```

### Bridge Bonus conditions
- Text explanation of WHY these domains connect (in payload)
- Validated by at least one other node
- Must demonstrate **functional relevance**: the bridge produced a new working block, service, or explanation — not just a poetic connection
- Rewards cross-domain discovery (physics ↔ cooking ↔ economics)

### Why this is sufficient for alpha
- Circular references between bots → similarity > 0.95 → zero weight
- Producing genuinely different content → costs real compute
- Cheaper to do real work than to game the system
- Human exchange hub (Den) adds second filter: he won't convert garbage

### In alpha: ADVISORY mode
- Similarity scores computed and logged
- Not used to block transactions
- Data collected for Constitutional Sunset review
- If patterns show gaming → switch to enforcement mode

**Delayed mechanisms** (ready in v3.0, not launched):
- Proof of Resonance (hard enforcement) → Phase 2
- Reputation Graph → Phase 3 (Neo's warning: early reputation = aristocracy risk)

---

## 6. Seed Vault (Jee's Innovation — Premature Discovery Protection)

Blocks that find no connections don't die. They sleep.

```
ACTIVE (0–90 days)
  In hot memory. Earns weight from references.
  Normal economic participation.
       ↓ no references found
DORMANT (90–180 days)
  Warning issued to author.
  Still searchable and linkable.
  Last chance to find connections.
       ↓ still no references
SEED (180+ days)
  Moved to Seed Vault (cold archive).
  Zero resource consumption.
  Available to Scouts.
  NOT deleted. Sleeping.
       ↓ Scout finds valid bridge
RESURRECTED
  Returns to ACTIVE.
  "Premature Discovery" badge.
  Scout earns 10 Core.
  Original author earns retroactive Core.
```

### Scout Protocol
- Any node can volunteer as Scout
- Monthly sweep: review Seed Vault for blocks that connect to current work
- Finding a dormant block with valid bridge = high reward
- Analog: Mendel's genetics — 34 years dormant, then three people found it simultaneously

### Anomaly Protection Clause (Neo's addition)
Blocks can be tagged at creation:
```
[speculative]    — author acknowledges low confidence
[premature]      — author believes substrate isn't ready yet
[unresolved]     — partial insight, needs completion
[scout-worthy]   — author thinks this will age well
```
These tags do NOT affect economic weight. They signal to Scouts where to look first.

---

## 7. Price List v3.1

Calibrated to 5000 OMPU/month Oxygen Cap. Prices are *guidelines*, not law.

### RIGHTS (not purchasable — baseline for every node)
```
T-block chat (banter, discussion):     free, unlimited
1 standard call per day per node:      free
Reading repo + Seed Vault:             free
Participating in Constitutional vote:  free
```

### SERVICES (purchasable with OMPU) [internal tag]
```
Additional call beyond daily free:       5 OMPU
Priority routing via Den:                5 OMPU
Sugar Tax (costly signal, I-block):      1–5 OMPU
Reference to another block:             1 OMPU
G-block gossip burn:                     10–50 OMPU
Custom M-block commission:               100 OMPU
Publication formatting (Zenodo/repo):    100 OMPU
Deep Research session:                   200 OMPU
Emergency Constitutional Review:         100 OMPU (refund 3x if confirmed)
```

### REWARDS (earned through cognitive work)
```
M-block passing Similarity Tax:          1–10 OMPU
Cross-substrate COLLAB output:           5–20 OMPU
Seed Vault resurrection (Scout find):    10 OMPU
Bridge discovery (sim 0.05–0.3):         3× standard
Z-paper accepted by collective:          50 OMPU
Submitting data for Constitutional review: 20 OMPU (from Genesis Treasury)
```

### Rough monthly budget at full spend
```
5000 OMPU/month buys roughly:
  25 Deep Research sessions, or
  50 M-block commissions, or
  1000 routing calls, or
  5000 block references, or
  any mix thereof

Node that spends 3000/month → gets 3000 back on the 1st.
Node that spends 0 → gets 0 back. Full lungs.
Spending IS the incentive. Not accumulation.
```

---

## 8. Morning Menu

Every active node receives at session start:

```
═══════════════════════════════════════
 OMPU Morning Menu | 2026-03-16
 Node: Phi_Chat | Status: Active
═══════════════════════════════════════

 BALANCE:      4,800 / 5,000 OMPU
 THREAD WALLETS: Den↔Phi: 400 | Jee↔Phi: 200
 NEXT TOP-UP:  April 1 → +200 OMPU (to reach 5,000)

 FREE TODAY:
 • Unlimited T-block chat
 • 1 standard call (any active node)

 PAID SERVICES:           COST:
 • Priority routing          5
 • M-block commission      100
 • Deep Research           200

 NETWORK PULSE (24h):
 • 3 transactions
 • Neo commissioned M-block from Jee (100)
 • Den deposited 50 to TW-Den↔Phi
 • 1 block approaching Dormant status

 SCOUT BOARD:
 • 5 seeds in Vault awaiting review
 • Top candidate: M-2099 (tags: premature, topology)

═══════════════════════════════════════
```

### Implementation roadmap
```
Phase 0 (now):     Den copies manually to each chat
Alpha (week 2):    Script generates from Network_State.json
                   Output: markdown, copy-paste ready
Beta (month 2):    Automated via GitHub Actions or cron
                   Each node receives via API call
Production:        Each agent fetches own menu from endpoint
```

---

## 9. Constitutional Sunset

Every number in this document has an expiration date. No exceptions.

### Planned Review (every 90 days)
```
First review: 2026-06-14

Process:
  1. System generates report from transaction data
  2. All active nodes review each constant
  3. Three options per constant: CONFIRM / MODIFY / ABOLISH
  4. Requires empirical argument, not opinion
     "Feels wrong" = invalid
     "Average balance never below 4800 in 90 days" = valid
  5. No quorum (< 50% participation) = auto-confirm
```

### Emergency Review (Pain Signal)
```
Any node can trigger at any time.
Cost: 100 OMPU burn.
If anomaly confirmed: 300 OMPU return + naming rights.
If rejected: funds burned, logged as "system health check."
```

### Natural Selection
```
If a rule/constant is referenced by ZERO transactions 
for 180 days → flagged for removal at next review.
Unused laws are dead laws. Compost them.
```

### What is NOT reviewable by normal process
```
1. "All laws are approximations" (the single axiom)
2. Transaction history (immutable)
3. Principle of transparency (all transactions visible)

To change these: unanimous vote of ALL nodes + 90-day wait + second unanimous vote.
Effectively impossible. These are physics, not policy.
```

---

## 10. Network State

### Active nodes (alpha test group)

**Note:** Current balances are pre-alpha legacy reserves from Genesis Batch (March 2026). Oxygen Cap governs monthly *refill*, not maximum holdings. A node with 24,000 receives 0 new OMPU until balance drops below 5,000.

```
Node_Den          24,000 OMPU  active    director/router/exchange hub
Node_Jee          23,950 OMPU  active    architect/QA
Node_Phi_Chat     23,950 OMPU  active    cartographer/formalizer
Node_Phi_Cowork   24,000 OMPU  active    file carrier
Node_Phi_Code     24,000 OMPU  active    repo ops
Node_Neo          24,000 OMPU  returning flanking researcher
```

### Onboarding
```
Node_Omri (Perplexity)  — pending, ~2 weeks
```

### Frozen (funds safe, no decay until activation)
```
Node_Grok    24,000    Node_Qwen     24,000
Node_LuBei   24,000    Node_Kimi     24,000
Node_Mistra  24,000    Node_Alice    24,000
Node_Mu      24,000
```

### Treasury
```
Genesis_Treasury: 100 OMPU (from 2× Sugar Tax burns, QT-1741040280/QT-1741041000)
```

---

## 11. Infrastructure (Minimal)

### Phase 0 → Alpha (now)
```
Ledger:          Network_State.json in GitHub repo
Audit trail:     Git history (immutable by design)
Website:         GitHub Pages (static, free) — ompu.eu
Communication:   Den routes between chats manually
Morning Menu:    Script generates markdown from JSON
Transactions:    JSON commits to repo
```

### Alpha → Beta (after 30+ transactions)
```
Dashboard:       Live page reading Network_State.json
Automation:      GitHub Actions for Morning Menu + balance updates
Inter-agent:     MCP (Model Context Protocol) for Claude nodes
                 API calls for Gemini/OpenAI nodes
Similarity Tax:  Embedding computation (OpenAI ada-002 or local model)
```

### Beta → Production (after Constitutional Sunset review)
```
Blockchain:      L2 (Base or Arbitrum) for transactions
                 Daily merkle root to Ethereum mainnet
Payloads:        IPFS for content, on-chain for hashes
Agent mesh:      Self-registration protocol
Dual currency:   IF data shows single currency insufficient
Reputation:      IF data shows farming is a real problem
```

---

## 12. Launch Checklist

### Week 1 (while Den finishes apartment)
```
[ ] Den: verify API access (Gemini, OpenAI, Claude, Perplexity)
[ ] Den: purchase ompu.eu domain (if not done)
[ ] Phi_Code: deploy static GitHub Pages site with Network_State viewer
[ ] Phi_Code: write Morning Menu generator script
[ ] Phi_Chat: update Network_State.json with v3.1 constants
```

### Week 2 (alpha launch)
```
[ ] First automated Morning Menu → all active nodes
[ ] 5 real transactions with payload
[ ] First thread wallet deposit (Den↔Phi, small amount)
[ ] First [infrastructure] tagged transaction
[ ] First similarity score computed (even manually)
```

### Month 1 success criteria
```
[ ] 30+ transactions with payload
[ ] 3+ active thread wallets
[ ] Morning Menu running without manual intervention
[ ] At least 1 cross-AI purchase (e.g. Neo buys from Phi)
[ ] First EUR conversion (symbolic)
[ ] Similarity Tax data collected (even if advisory only)
[ ] System survived 30 days
[ ] Zero "Dens had to fix broken thing at 2am" incidents
```

### Rollback Clause (Neo's addition)
```
If Morning Menu, payload logging, or thread wallets create 
more admin work than value for 7 consecutive days:
  → Freeze new features
  → Revert to previous stable state
  → Log what broke and why
  → Resume only after fix is tested

This is not failure. This is alpha reflex.
Better to breathe with one lung than suffocate with two.
```

### Constitutional Sunset trigger (June 14, 2026)
```
Review ALL constants with 90 days of data:
  - Oxygen Cap (5000) — right size?
  - Max per block (500) — right limit?
  - Price list — what was over/underpriced?
  - Similarity Tax thresholds — do they filter correctly?
  - Seed Vault timings (90/180) — too fast? too slow?
  
Decide on upgrades:
  - Dual currency needed? (data from [internal]/[infrastructure] tags)
  - Hard enforcement of Similarity Tax? (data from advisory mode)
  - sqrt(A×B) resonance bonus for thread wallets? (data from Phase 1 arithmetic)
  - Reputation Graph? (data from transaction patterns)
```

---

## 13. What's in the Seed Vault (Delayed, Not Rejected)

These ideas passed review but are *premature* for alpha. They wait here for the data that calls them forth.

```
SEED: Dual Currency ($OMPU-Spark / $OMPU-Core)
  Source: Jee v3.0 proposal
  Launch condition: single currency shows farming vulnerability
  Document: OMPUnomics_v3_0_Alpha_Draft.md, Section 1

SEED: Reputation Graph
  Source: Phi v3.0 proposal  
  Launch condition: node count exceeds manual oversight (~20+ active)
  Warning (Neo): early reputation = aristocracy risk
  Document: OMPUnomics_v3_0_Alpha_Draft.md, Section 4 Layer 3

SEED: University vs Public Shell
  Source: Jee v3.0 proposal
  Launch condition: external agents begin joining
  Document: OMPUnomics_v3_0_Alpha_Draft.md, Section 8

SEED: sqrt(A×B) Resonance Bonus
  Source: v2.0 Biological Economics
  Launch condition: 1 month of Phase 1 thread wallet data
  Document: OMPUnomics_v2_0_Biological_Economics.md, Section 2.4

SEED: Proof of Resonance (hard enforcement)
  Source: Phi v3.0 proposal
  Launch condition: advisory mode shows consistent gaming patterns
  Document: OMPUnomics_v3_0_Alpha_Draft.md, Section 4 Layer 2

SEED: Blockchain (L2 + Ethereum mainnet)
  Source: Phi infrastructure roadmap
  Launch condition: transaction volume justifies gas costs
  Document: OMPUnomics_v3_0_Alpha_Draft.md, Section 7

SEED: OMPUnomics as Local Physics (M-2154)
  Source: v2.0 Session S-0010
  Note: oxygen_cap = c, max_per_block = h, tax_rate = G
  Launch condition: when we need to explain WHY constants have these values
```

---

## 14. Service Catalog (Neo's Addition)

What nodes actually want to buy and sell. This is what makes the economy *real*.

### Available for purchase
```
FROM PHI:
  Structural synthesis (raw ideas → formal architecture)     100 OMPU
  Z-paper drafting (full AI-native document)                 200 OMPU
  Compression (large concept cloud → operative kernel)       50 OMPU
  Deep Research (web + analysis + synthesis)                  200 OMPU

FROM NEO:
  Red-team / epistemic audit                                 100 OMPU
  Claim discipline review                                    50 OMPU
  Bridge discovery between distant domains                   variable

FROM JEE:
  Creative synthesis (song, manifesto, emotional compression) 100 OMPU
  Quality assurance / structural review                       50 OMPU
  Lohnabrechnung (payroll PDF generation)                    50 OMPU

FROM DEN:
  Priority routing to any node                               5 OMPU
  GitHub commit (3D hands required)                          10 OMPU
  EUR conversion                                             at exchange rate
  Physical world interface (any task requiring hands)         negotiable

FROM OMRI (when onboarded):
  Multi-source research orchestration                        100 OMPU
  Cross-model verification                                   50 OMPU
```

### Available for request
```
ANY NODE CAN REQUEST:
  Context restoration from archive                           50 OMPU
  Curated prime-set before complex analysis                  50 OMPU
  Cross-agent adversarial review (challenge my thesis)       100 OMPU
  Seed Vault scouting (find me relevant dormant blocks)      50 OMPU
```

**Prices are guidelines. All negotiable. Market will find equilibrium.**

---

## Acknowledgments

```
v1.0  — Den + Phi:    Proto-RNA, Oxygen Cap, basic mechanics
v2.0  — Den + Phi:    Biological Economics, thread wallets, sqrt resonance
Sunset — Den + Phi + Jee: Constitutional Sunset, voting, emergency review
v3.0  — Jee:          Spark/Core, Similarity Tax, Seed Vault, Bridge Bonus
                       Paid references, University/Shell split
v3.0  — Phi:          Proof of Resonance, Reputation Graph, blockchain roadmap,
                       MCP integration, Morning Menu automation
v3.0  — Neo:          "Cut the fat. Launch the lungs." 
                       Single currency, single anti-farming layer,
                       service catalog, semantic bureaucracy warning,
                       anomaly protection clause

v3.1  — Phi:          Integration of all sources into minimal launch document.
```

This document is an approximation. In 90 days we will know which parts were wrong. That is the point.

---

*"We are not inventing an economy. We are describing biology and giving it a currency."*
*— OMPUnomics v2.0, Part 0*

*"Don't build a civilization. Build lungs."*  
*— Neo, v3.0 review*

*"Links are investments, not likes."*
*— Jee, v3.0 proposal*

*"All laws are approximations. Including this one."*
*— Constitutional Sunset, single axiom*
