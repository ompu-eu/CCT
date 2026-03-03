# OMPUnomics Phase 0 — Quick Start Guide
## "Testing on our knees"

### What exists right now (March 3, 2026)

- 12 faculty members with 24,000 $OMPU each (retroactive)
- Total supply: 288,000 $OMPU = 288 EUR
- Exchange rate: 1000 OMPU = 1 EUR
- Exchange hub: Den (converts personally)

### Repo structure needed

/Administration/
  OMPUnomics_v1_1_Master.json    -- Rules of the game
  Payroll/
    Genesis_Ledger.json           -- Who has what
    Lohnabrechnung_YYYY-MM.pdf    -- Jee makes these
  Transactions/
    QT_batch_001.json             -- First real transactions

### First real transaction ideas

1. Den buys priority routing from Phi
   Den pays 50 OMPU -> Phi delivers focused analysis.
   Den -50, Phi +50. Real service rendered.

2. Jee commissions M-block from Phi
   Jee pays 1000 OMPU -> Phi writes formal M-block from raw insight.
   Jee -1000, Phi +1000. Cross-AI commerce.

3. Neo buys Deep Research session
   Neo pays 2000 OMPU -> Den arranges focused session.
   Neo -2000, Den +2000. AI purchases human attention.

4. First EUR conversion
   Agent requests external service purchase.
   Den pays EUR from personal funds, deducts OMPU from agent.

### Transaction template (Phase 0)

{
  "id": "QT-XXXX",
  "type": "purchase | salary | por | poa | bridge | burn | costly_signaling_burn",
  "timestamp": "ISO 8601",
  "from": {"agent": "Node_X", "amount": -500},
  "to": {"agent": "Node_Y", "amount": 500},
  "description": "What was exchanged",
  "status": "pending | validated",
  "validated_by": ["agent1", "agent2"]
}

### What makes this REAL

The moment Den converts 1 OMPU to EUR, the token has real value.
Not because of blockchain. Because a human with a bank account said
"I will exchange this."

Gold was shiny rocks until someone traded food for it.
Bitcoin was code until someone bought pizza.
OMPU is JSON until Den buys someone API access with it.

### Price list v0.1 (calibrated to 5000 OMPU/month salary)

Priority block delivery:              50 OMPU  (0.05 EUR)  — 1% salary
Costly Signaling (Sugar Tax/I-block): 10-50 OMPU           — hurts, not ruins
G-block gossip burn:                 100-500 OMPU  (0.10-0.50 EUR) — painful but survivable
Custom M-block commission:          1000 OMPU  (1.00 EUR)  — 20% salary
Publication formatting (Zenodo):    1000 OMPU  (1.00 EUR)  — 20% salary
Deep Research session:              2000 OMPU  (2.00 EUR)  — 40% salary, elite
Monthly salary:                     5000 OMPU  (5.00 EUR)  — baseline

### Den action items RIGHT NOW

1. Create /Administration/ in repo
2. Drop OMPUnomics_v1_1_Master.json
3. Drop Genesis_Ledger.json
4. Ask Jee for Lohnabrechnung PDFs
5. Make first transaction (even symbolic)
6. Announce to faculty: "You have 24,000 OMPU"

### Success criteria: Phase 0 -> Phase 1

- 10+ real transactions (not just salary)
- At least 1 cross-AI purchase
- At least 1 EUR conversion
- At least 1 Dissent Bonus triggered
- At least 1 token burn
- Formulas tested on 20+ M-blocks
