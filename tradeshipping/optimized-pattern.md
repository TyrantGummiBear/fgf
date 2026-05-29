# Optimized Trade Pattern

Guild standard for **Opportunity** and **Demerzal (Dem)** trade shipping.

---

## Core rules

### Opportunity — Galactic Coin only

**Opportunity should only ever run Galactic Coin (GC).**

- Do not assign special orders to Opportunity
- GC runs are long (~8 hours) — set and collect on a fixed schedule
- Opportunity's job is **maximum GC uptime**, not special-order throughput

### Demerzal — Special orders, then Galactic Coin

**Dem runs special orders during your active window, then Galactic Coin.**

Two valid modes:

| Mode | When | Pattern |
|------|------|---------|
| **Active day** | You're checking in regularly | 4× special orders → GC run |
| **Sleep / offline** | Overnight or away | Galactic Coin only (same as Opportunity idle) |

Dem is the **special-order ship**. Opportunity is the **GC ship**. Don't swap roles.

---

## Timing — special orders (Dem)

Dem has **4 special order slots** per cycle.

| Metric | Value |
|--------|--------|
| Special orders per cycle | **4** |
| Time per special order | **2h 30m – 4h** (varies by order) |
| All 4 in one window | **~12–16 hours** total |
| Galactic Coin run | **~8 hours** |

**The optimized day:** fit all 4 special orders inside a 12–16 hour active window, then start an **8-hour GC run** before bed or before your next check-in.

```
Active window (12–16 hrs)
├── Special order 1   (~2.5–4 hrs)
├── Special order 2   (~2.5–4 hrs)
├── Special order 3   (~2.5–4 hrs)
└── Special order 4   (~2.5–4 hrs)
        ↓
Galactic Coin run     (~8 hrs)  ← Dem sleeping / offline, or Opportunity parallel
```

---

## Sample schedules

Adjust start times to your timezone and check-in habits.

### Dem — active player (check in ~3× day)

| Time | Dem |
|------|-----|
| Morning | Start special order 1 |
| Midday | Collect → special order 2 (or 2 + 3 if short) |
| Evening | Collect → special orders 3 + 4 |
| Before sleep | Start **Galactic Coin** (~8 hr overnight) |

Wake up to GC complete; start special order cycle again or run GC on Opportunity.

### Dem — sleep mode only

If you won't touch the game for 8+ hours:

- **Skip special orders** — start **Galactic Coin** on Dem before offline
- Resume special-order cycle when you're back for a 12–16 hr window

### Opportunity — always

| Window | Opportunity |
|--------|-------------|
| Any time GC slot is free | **Galactic Coin** |
| Never | Special orders |

If Dem is running GC overnight, Opportunity should **already be on GC** or starting the next GC as soon as the previous completes — no idle time on Opportunity.

---

## 24-hour target (both ships)

Ideal guild throughput:

```
Opportunity:  [======== GC 8h ========][======== GC 8h ========]  (2× GC/day if collected on time)
Dem (active): [SO1][SO2][SO3][SO4][==== GC 8h ====]
Dem (sleep):  [============ GC 8h ============]
```

**Special orders (SO)** = Dem only, during active hours.  
**Galactic Coin (GC)** = Opportunity always; Dem fills gaps and overnight.

---

## Checklist

### Opportunity
- [ ] Only Galactic Coin assigned — verify before every send-off
- [ ] No special orders on this ship, ever
- [ ] Collect GC on timer; restart immediately

### Demerzal
- [ ] 4 special orders queued during 12–16 hr active window when possible
- [ ] After 4th special order completes → start **8 hr GC** before offline
- [ ] If sleeping 8+ hr with no check-ins → **GC only**, skip special orders
- [ ] Never leave Dem idle between runs if a slot is available

---

## Common mistakes

| Mistake | Fix |
|---------|-----|
| Special orders on Opportunity | Move all SO to Dem; Opp = GC only |
| Dem idle overnight with no GC | Start 8 hr GC before sleep |
| Only 2–3 special orders per day on Dem | Plan a 12–16 hr window for all 4 |
| GC on Dem while you're active and SO slots open | Run SO first, GC last in window |
| Both ships on special orders | Opp never runs SO — Dem owns them |

---

## Summary

| Ship | Role | Pattern |
|------|------|---------|
| **Opportunity** | GC specialist | Galactic Coin **only** |
| **Demerzal** | SO + GC flex | 4× special orders (12–16 hr) → 8 hr GC; or GC while sleeping |

---

*Timings are approximate — confirm in-game durations for your server and update this doc if patches change run lengths.*
