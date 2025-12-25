# Trading Memo: European Gas Supply Shock – Power Curve Impact

**Author:** Akar Abdalqadir  
**Email:** <abdalqadirakar@gmail.com>  
**Date:** 26th Dec, 2025  
**GitHub:** <https://github.com/Akar-30/cobblestone-case-study>

---

## Executive Summary

The indefinite shutdown of the Nord Stream 1 pipeline created a historic supply shock, permanently removing ~35% of EU Russian gas imports. This memo proposes a **Long German Power / Short Clean Spark Spread** trade to capture the resulting convex price transmission from gas to power markets. This structure capitalizes on extreme supply scarcity while hedging against the structural compression of generator margins.

---

## 1. Event Definition

### Timeline of Key Events

| Date | Event | Market Impact |
|------|-------|---------------|
| 2022-07-11 | NS1 maintenance begins | Initial uncertainty priced in |
| 2022-07-21 | NS1 restarts at 40% capacity | Reduced flow confirmed (68→~40 mcm/day) |
| 2022-08-31 | NS1 3-day maintenance announced | Peak uncertainty; TTF spikes to €339/MWh |
| 2022-09-02 | Russia: NS1 closed indefinitely | Supply shock crystallizes |
| 2022-09-26 | Pipeline sabotage (leaks detected) | Permanent supply loss confirmed |

### Why It Mattered

- **Pre-crisis NS1 flows:** ~68 mcm/day (Jul 1-10 avg)
- **Post-shutdown flows:** 0 mcm/day (Sep onward)
- **Supply loss:** ~100% of Nord Stream capacity, representing ~35% of EU Russian gas imports

This was not a temporary maintenance event. It represented a **regime change** in European gas supply architecture.

---

## 2. Market Mechanism

**2.1 Marginal Cost Transmission**
German power acts as a leveraged gas position, set by marginal CCGT plants with a ~2:1 heat rate.

**2.2 Correlation**
A **0.879 correlation** between TTF and Power confirms gas is the dominant price driver. Power effectively trades as a convex proxy for gas scarcity.

**2.3 Clean Spark Spread (CSS) Dynamics**

**Formula:**

```
CSS = Power − (2.0 × TTF) − (0.37 × EUA)
```

**Key insight:** CSS swung from +€124/MWh to -€276/MWh, a **€400/MWh range** signaling extreme dislocation in generation economics. This **€400/MWh range** in spread volatility validates the need for the short spread overlay to hedge generation economics.

---

## 3. Trade Expression

### Primary Trade: Long German Power Q4-2022 Forward

**Rationale:** Capture supply scarcity premium with convex upside.

| Parameter | Specification |
|-----------|---------------|
| **Instrument** | German Baseload Power Q4-2022 Forward |
| **Direction** | Long |
| **Entry zone** | €350-400/MWh (post-maintenance restart) |
| **Target** | €550-700/MWh (scarcity pricing) |
| **Stop-loss** | €280/MWh (15-20% below entry) |

### Overlay: Short Clean Spark Spread

**Rationale:** Hedge generation economics. As gas prices spike, generator margins (the spread) will compress or invert, even if power prices rise.

| Parameter | Specification |
|-----------|---------------|
| **Structure** | Synthetic Short CSS (Sell Power / Buy Gas / Buy Carbon) |
| **Legs** | Short Power Q4 / Long TTF Q4 / Long EUA |
| **Entry** | Spread > €0/MWh (Any window of profitability) |
| **Exit** | Spread < -€100/MWh (Deep inversion) |

---

## 4. Execution & Risk Management

**4.1 Entry & Exit Logic**

- **Entry Triggers:** Execute LONG if:
  - NS1 restarts at < 60% capacity or flows drop to 0.
  - TTF closes > €200/MWh
  - 1-month implied volatility expands >20% WoW.
- **Exit Targets:** Scale out 50% at **€550**, remaining at **€650**.
- **Invalidation (Stop):** Hard stop at **€280** (market structure break) or if NS1 flows resume >80% capacity.
- **Time Horizon:** Hold through Q4-22 delivery; roll or close by Oct 15 if thesis stagnates.

**4.2 Position Sizing (Fixed Risk Model)**

- **Risk Budget:** 2% of NAV (€200k on €10m capital).
- **Sizing Logic:** Risk is defined as the distance to Stop Loss (€400 Entry - €280 Stop = €120/MWh risk).
- **Calculation:**
$$\text{Position Size} = \frac{\text{Risk Budget}}{\text{Risk per Unit}} = \frac{€200,000}{€120/MWh} = 1,667 \text{ MWh}$$

---

## 5. Risk Framework

### 5.1 Scenario Analysis

| Scenario | Probability | TTF Impact | Power Impact | P&L Direction |
|----------|-------------|------------|--------------|---------------|
| Base: NS1 remains shut | 50% | €200-250 | €400-500 | +€100-150/MWh |
| Bull: Winter scarcity | 25% | €300-400 | €600-700 | +€200-300/MWh |
| Bear: Demand destruction / mild winter | 20% | €120-150 | €200-250 | -€150-200/MWh |
| Tail: Political resolution | 5% | €80-100 | €150-180 | -€250/MW |

### 5.2 Invalidation Criteria

**Cut the position if:**

1. NS1 resumes flows at >60% capacity for 5+ consecutive days
2. EU storage exceeds 95% AND temperatures forecast +2°C above seasonal
3. TTF falls below €150/MWh with no bounce (demand destruction signal)
4. Correlation between TTF and Power drops below 0.6 (regime change)
5. Emergency policy intervention (price caps, rationing) announced

### 5.3 Risk Categories

| Risk Type | Description | Mitigation |
|-----------|-------------|------------|
| **Fundamental** | NS1 restart, LNG surge, demand destruction | Monitor flow data daily; set alerts |
| **Correlation/Basis** | Gas-power spread widens unexpectedly | Hedge with spark spread overlay |
| **Liquidity** | Wide bid-ask in crisis; rollover costs | Trade front-month/quarter only; avoid illiquid tenors |
| **Policy/Headline** | EU price caps, emergency measures | Position sizing limits; tail hedges |
| **Model Risk** | Heat rate/emission assumptions wrong | Sensitivity test ±10% on parameters |

---
