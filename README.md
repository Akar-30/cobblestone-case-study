# Nord Stream Crisis Trading Analysis

Analysis of the 2022 Nord Stream pipeline crisis and its impact on European energy markets.

---

## 📂 Files in This Directory

```
📁 Data Files:
├── ttf_prices.csv                          # TTF gas prices
├── german_power_da.csv.csv                 # German power prices  
├── Carbon Emissions Futures Historical Data.csv
├── daily_data_2025-12-18.csv              # Pipeline flows
├── StorageData_GIE_2022-07-01_2022-10-31.csv
└── StorageData_GIE_2017-07-01_2022-10-31.csv

📁 Analysis:
├── analysis.ipynb                          # Main analysis (RUN THIS!)
├── Trading Memo.md                         # Trading recommendations
├── ai_trading_copilot.py                  # AI decision support tool
└── combined_analysis_data.csv              # Generated dataset

📁 Charts (in /charts):
└── 8 PNG charts showing crisis impact
```

---

## 🚀 How to Run

### 1. Run Analysis Notebook

```bash
jupyter notebook analysis.ipynb
```

**Generates:** 8 charts + combined data + key statistics

**Expected output:**

- TTF Peak: €339/MWh, Power Peak: €699/MWh
- TTF-Power correlation: 0.879
- Charts saved to `/charts` folder

---

### 2. Run AI Trading Copilot

```bash
python ai_trading_copilot.py
```

**Generates:** 6-section decision workflow with guardrails

**Sections:**

1. Event Summary (facts only)
2. What Matters / What to Watch
3. Scenario Table (4 scenarios)
4. Pre-Trade Checklist + Risk Flags
5. Source Citations
6. Human Sign-Off

**Runtime:** <1 second

---

## 📊 Data Sources

| Data | Source | Download Link |
|------|--------|---------------|
| TTF Gas | Investing.com | [Link](https://www.investing.com/commodities/dutch-ttf-gas-c1-futures-historical-data) |
| German Power | SMARD (Official) | [Link](https://www.smard.de/en) |
| Carbon (EUA) | Investing.com | [Link](https://www.investing.com/commodities/carbon-emissions-historical-data) |
| Pipeline Flows | Bruegel | [Link](https://www.bruegel.org/dataset/european-natural-gas-imports) |
| Storage | GIE AGSI+ (Official) | [Link](https://agsi.gie.eu/) |

**Date range for all:** July 1 - October 31, 2022

---

## 🔧 Requirements

```bash
pip install pandas matplotlib jupyter
```

---

## 📈 Key Results

**Price Impact:**

- TTF: +102% (€168 → €339/MWh)
- Power: +131% (€303 → €699/MWh)
- Clean Spark Spread: -€276 to +€124/MWh range

**Correlation:** 0.879 (gas drives power prices)

**Storage:** 58.5% → 94.8% (EU met 90% target)

---

**Last Updated:** December 26, 2025
