# Vaults & Guardians

How the ShadowFront map works — what we're fighting over, and what happens after a capture.

See also: [Fight in the Circle](fight-on-the-point.md) · [Bonus Points](bonus-points.md)

---

## Map Layout

ShadowFront has **10 vaults** on the battlefield:

| Type | Count | Placement |
|------|-------|-----------|
| **Small vaults** | 8 | **2 per quadrant** — spread across all four map quadrants |
| **Large vaults** | 2 | Major objectives (higher value — see scoring below) |

```
        [Q1: 2 small]     |     [Q2: 2 small]
    ──────────────────────┼──────────────────────
              [ LARGE ]   |   [ LARGE ]
    ──────────────────────┼──────────────────────
        [Q3: 2 small]     |     [Q4: 2 small]
```

**Coordinator tip:** Name vaults by quadrant + size in comms (e.g. *"Stack Q1 small north"*, *"Rotate to large east"*) until the guild settles on fixed callouts.

---

## Capture Cycle

Each vault follows the same loop:

```
1. CONTESTED  →  fight in capture circle (most numbers wins)
        ↓
2. CAPTURED   →  one team completes the countdown
        ↓
3. GUARDED    →  a Vault Guardian spawns for the capturing team
        ↓
4. LOCKED     →  capture is DISABLED until the guardian is killed
        ↓
5. CONTESTED  →  guardian dead → circle opens again
```

### Vault Guardian

After a **successful capture**, a **Vault Guardian** appears for the team that took the vault.

- The guardian **belongs to the holding team** — it defends their capture
- **Capture cannot resume** until the guardian is **killed**
- To flip a vault, enemies must: **kill guardian → win number fight in circle → complete new capture**

This is why we don't only fight players — see guardian / tower priority in [Fight in the Circle](fight-on-the-point.md).

| Phase | Our goal if we **hold** | Our goal if we **attack** |
|-------|-------------------------|---------------------------|
| Guardian up | Protect it; farm hold points | Kill guardian first, then contest circle |
| Guardian down | Re-capture before they flip | Win numbers in circle, finish capture |

**Call:** **"Guardian [vault]"** or **"Tower [vault]"** — kill or defend the guardian (same objective).

---

## Hold Points (Scoring)

Points tick while your guild **holds** a captured vault (guardian alive, your team in control). **Large vaults pay more per hold time than small vaults** — prioritize them when coordinating stacks and rotations.

> **Point values — verify in-game.** Exact hold-time rates are not published in community guides we checked. Fill the table below from the **event UI** during your next match (tap vault → hold rate / points per interval).

| Vault type | Count | Points per hold (TBD) | Notes |
|------------|-------|------------------------|-------|
| **Small vault** | 8 | _record from UI_ | 2 per quadrant; good for footholds and bonus windows |
| **Large vault** | 2 | _record from UI_ | Higher payout — usually worth heavier stacks |

### How to record values (one match)

1. Open ShadowFront scoring / vault detail in the event UI
2. Note **points per tick** (or per minute) for one **small** and one **large** vault
3. Update this table — coordinator uses it for late-game priority calls

**Until filled in:** assume **large > small** for rotation priority; confirm numbers after first documented match.

---

## Strategic Implications

### Small vaults (8)
- Fast to contest; good for **early footholds** and **bonus point** windows
- Spread across quadrants — don't try to hold all 8; pick home + attack targets
- Easier to rotate between two in the same quadrant

### Large vaults (2)
- **Higher hold value** — often the late-game win condition
- Expect heavier enemy stacks; commit numbers, not solo whales
- Guardian kills here are high-impact — flip or deny can swing the leaderboard

### Guardian + circle together
- **Can't capture with guardian up** — killing it is step one for any flip
- Don't burn guardian while **outnumbered in circle** — they'll recapture when it falls ([Fight in the Circle](fight-on-the-point.md))
- **Exception:** big incoming on guardian → **"Guardian first"** / **"Tower first"**

---

## Coordinator Priority (Quick)

```
Early   → 1 small vault foothold per squad (numbers in circle)
Mid     → Bonus windows on best-value vault we can win
Late    → Large vault hold OR deny enemy large + protect ours
Flip    → Kill guardian → win circle count → finish capture
Deny    → Break bonus when we can't win full flip ([Bonus Points](bonus-points.md))
```

---

## Related Callouts

| Call | Meaning |
|------|---------|
| **"Guardian [vault]"** | Focus the vault guardian |
| **"Guardian first [vault]"** | Kill guardian before circle fight |
| **"Guardian down [vault]"** | Capture open — stack circle now |
| **"Hold large"** | Priority on large vault hold points |

Full list: [Communication](communication.md)

---

*Last updated: May 2026 — scoring table pending in-game verification.*
