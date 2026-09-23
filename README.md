# MessMind — Intelligent Food Waste & Demand Analytics System

## 1. Project Overview

**MessMind** is a data-driven food waste intelligence system designed for PGs, hostels, and college messes.

Instead of only showing how much food was wasted, the system analyzes historical meal data to answer practical management questions:

- Which meals and food items create the most waste?
- How efficiently is prepared food being consumed?
- How much money is being lost because of food waste?
- Which meals have a high waste risk?
- How much food should potentially be prepared based on historical consumption?
- Which days or meals require attention?
- What actions could reduce unnecessary preparation?

The project starts as a Python/Pandas analytics system and is designed to evolve later into an ML-powered prediction and optimization platform.

---

## 2. Project Name

### MessMind
**Intelligent Food Waste & Demand Analytics System**

---

## 3. Problem Statement

College messes and PG kitchens often prepare food based on rough estimates rather than data.

This can result in:

- over-preparation
- unnecessary food waste
- financial loss
- inefficient use of ingredients
- inconsistent meal planning

MessMind uses historical preparation, consumption, and people-count data to identify waste patterns and generate actionable insights.

---

## 4. Main Objective

The objective is to transform raw mess records into an intelligent decision-support system.

### Basic flow

Raw Data  
↓  
Data Cleaning  
↓  
Data Validation  
↓  
Waste Analytics  
↓  
Cost Analysis  
↓  
Waste Risk Detection  
↓  
Demand Estimation  
↓  
Recommendations

---

# 5. Core Features

## 5.1 Waste Percentage

For every meal:

```text
Waste Percentage =
(Waste Quantity / Prepared Quantity) × 100
```

Example:

```text
Prepared = 15 kg
Waste = 4 kg

Waste % = (4 / 15) × 100
         = 26.67%
```

This makes different meals comparable.

---

## 5.2 Waste Per Person

```text
Waste Per Person =
Waste Quantity / Number of People
```

This helps distinguish between:

- a large waste amount caused by many people
- unusually high waste relative to the number of people served

---

## 5.3 Meal-Wise Waste Intelligence

The system calculates average waste for:

- Breakfast
- Lunch
- Dinner

Example:

```text
Lunch      → 2.8 kg
Breakfast  → 2.1 kg
Dinner     → 3.7 kg
```

---

## 5.4 Food-Wise Waste Analysis

The system identifies food items with consistently high waste.

Example:

```text
Rice       → 3.4 kg average waste
Roti       → 2.9 kg average waste
Poha       → 1.7 kg average waste
```

---

# 6. Waste Risk Score

MessMind can classify meals according to their historical waste behaviour.

Example:

```text
Waste Percentage

< 15%       → LOW RISK
15–25%      → MEDIUM RISK
> 25%       → HIGH RISK
```

Example output:

```text
MEAL WASTE RISK
────────────────────────

Monday Lunch       Rice       HIGH
Tuesday Dinner     Roti       MEDIUM
Wednesday Breakfast Poha      LOW
```

The thresholds can later be made data-driven instead of manually defined.

---

# 7. Financial Waste Analysis

The project can associate an estimated cost with each food item.

Example:

```text
Rice       ₹45/kg
Roti       ₹40/kg
Poha       ₹50/kg
Upma       ₹55/kg
```

Formula:

```text
Financial Loss =
Waste Quantity × Cost per kg
```

Example:

```text
Rice Waste = 4 kg
Cost       = ₹45/kg

Loss = 4 × 45
     = ₹180
```

The system can report:

```text
TOTAL FOOD WASTE      : 38.2 kg
ESTIMATED MONEY LOSS  : ₹1,742
```

---

# 8. Environmental Impact

Food waste can also be represented using an estimated environmental-impact factor.

Conceptually:

```text
Food Waste
     ↓
Waste Quantity
     ↓
Environmental Factor
     ↓
Estimated CO₂-equivalent Impact
```

The conversion factor should be clearly documented and treated as an estimate, not a directly measured value.

---

# 9. Meal Efficiency Score

A useful custom metric:

```text
Meal Efficiency =
Consumed Quantity / Prepared Quantity × 100
```

Example:

```text
Lunch       → 82%
Breakfast   → 76%
Dinner      → 68%
```

A lower efficiency indicates that a larger fraction of prepared food remained unused.

---

# 10. Preparation Recommendation

This is one of the main features that differentiates MessMind from a simple visualization project.

Instead of only reporting:

> Dinner wasted 4 kg.

The system can eventually generate:

> Historical consumption indicates that approximately 12.4 kg may be sufficient for this meal under similar conditions.

The recommendation should be based on historical observations and clearly labelled as an estimate.

---

# 11. Recommendation Engine

MessMind can generate actionable messages.

Example:

```text
RECOMMENDATION
────────────────────────────

Dinner waste is significantly above
the recent average.

Food item:
Roti

Suggested action:
Review preparation quantity for
similar dinner conditions.

Reason:
High historical waste percentage.
```

Later, recommendations can incorporate:

- day of week
- meal type
- food item
- number of people
- historical consumption
- recent trends

---

# 12. Project Architecture

```text
                 RAW MESS DATA
                       │
                       ▼
                    CSV FILE
                       │
                       ▼
                DATA INGESTION
                       │
                       ▼
              DATA UNDERSTANDING
                       │
                       ▼
              CLEANING & VALIDATION
                       │
                       ▼
              FEATURE ENGINEERING
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
   WASTE METRICS   COST METRICS   PEOPLE METRICS
        │              │              │
        └──────────────┼──────────────┘
                       ▼
                WASTE RISK ENGINE
                       │
                       ▼
              DEMAND ESTIMATION
                       │
                       ▼
             RECOMMENDATION ENGINE
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
   VISUALIZATION    REPORTING      INSIGHTS
                       │
                       ▼
                MESS MANAGEMENT
```

---

# 13. Current Dataset

The current demonstration dataset contains:

- 18 records
- 8 original columns
- 6 dates

Columns:

| Column | Meaning |
|---|---|
| Date | Date of meal |
| Day | Day of week |
| Meal | Breakfast/Lunch/Dinner |
| Food_Item | Food prepared |
| Prepared_Qty_kg | Quantity prepared |
| Consumed_Qty_kg | Quantity consumed |
| Waste_Qty_kg | Quantity wasted |
| People | Number of people served |

---

# 14. Technology Stack

### Current

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- CSV

### Planned upgrades

- Statistical analysis
- Scikit-learn
- Demand prediction
- Interactive dashboard
- Streamlit
- Database integration
- Deployment

---

# 15. Current Python Workflow

```text
CSV
 ↓
pd.read_csv()
 ↓
DataFrame
 ↓
head()
shape
info()
isnull()
duplicated()
dtypes
 ↓
Date conversion
 ↓
Data validation
 ↓
Feature engineering
 ↓
GroupBy analysis
 ↓
Visualization
 ↓
Insights
```

---

# 16. Important Metrics

### Total Waste

```python
df["Waste_Qty_kg"].sum()
```

### Average Waste

```python
df["Waste_Qty_kg"].mean()
```

### Waste Percentage

```python
df["Waste_Percentage"] = (
    df["Waste_Qty_kg"] /
    df["Prepared_Qty_kg"]
) * 100
```

### Waste Per Person

```python
df["Waste_Per_Person"] = (
    df["Waste_Qty_kg"] /
    df["People"]
)
```

### Meal-Wise Analysis

```python
df.groupby("Meal")["Waste_Qty_kg"].mean()
```

### Food-Wise Analysis

```python
df.groupby("Food_Item")["Waste_Qty_kg"].mean()
```

---

# 17. Data Validation

MessMind checks whether:

```text
Prepared Quantity - Consumed Quantity
```

matches:

```text
Recorded Waste Quantity
```

Formula:

```python
Calculated_Waste = (
    df["Prepared_Qty_kg"] -
    df["Consumed_Qty_kg"]
)
```

This is important because analytics are only useful when the source data is internally consistent.

---

# 18. Visualizations

The current project includes:

### 1. Average Waste by Meal

Bar chart showing average waste for breakfast, lunch, and dinner.

### 2. Daily Waste Trend

Line chart showing total waste for each date.

### 3. Food Waste Percentage

Seaborn chart comparing waste percentages across food items.

### 4. Prepared vs Consumed vs Waste

Comparison chart showing the total quantities.

---

# 19. Example Final Insight

Instead of simply displaying charts, the final system should summarize findings.

Example:

```text
FINAL INSIGHTS
────────────────────────────

Highest-waste meal:
Dinner

Highest-waste food:
Rice

Highest-waste day:
Friday

Total waste:
38.2 kg

Average waste per entry:
2.12 kg
```

The upgraded system will additionally generate:

```text
Waste risk
Estimated financial loss
Meal efficiency
Preparation guidance
Actionable recommendations
```

---

# 20. Development Roadmap

## Phase 1 — Foundation

- Create dataset
- Load CSV
- Understand data
- Check missing values
- Check duplicates
- Validate data types
- Convert dates

## Phase 2 — Analytics

- Waste percentage
- Total waste
- Average waste
- Meal-wise waste
- Food-wise waste
- Day-wise waste
- Waste per person

## Phase 3 — Intelligence

- Waste risk score
- Cost analysis
- Financial loss
- Meal efficiency score
- Recommendation rules
- Preparation quantity estimation

## Phase 4 — Advanced Analytics

- Statistical analysis
- Correlation analysis
- Outlier detection
- Historical pattern analysis

## Phase 5 — Machine Learning

Potential future models:

- meal consumption prediction
- food demand prediction
- waste prediction
- quantity recommendation

Possible technology:

```text
Scikit-learn
Regression
Random Forest
Gradient Boosting
Time-series approaches
```

The exact model should be selected only after enough quality historical data is collected.

## Phase 6 — Application

Build an interactive dashboard:

```text
MessMind Dashboard
────────────────────────────

Today's People       52
Prepared Food        14.2 kg
Consumed Food        10.8 kg
Waste                 3.4 kg

Waste Risk            HIGH

Estimated Loss       ₹153

Top Waste Item       Rice

Recommendation:
Review preparation quantity
for the next similar meal.
```

Possible technology:

- Streamlit
- Plotly
- PostgreSQL/SQLite

## Phase 7 — Deployment

Possible final architecture:

```text
Mess Data
    ↓
Database
    ↓
Python Analytics
    ↓
ML Prediction
    ↓
Recommendation Engine
    ↓
Streamlit Dashboard
    ↓
Mess Manager
```

---

# 21. Suggested Project Structure

```text
MessMind/
│
├── data/
│   └── DATA.CSV
│
├── src/
│   ├── data_loader.py
│   ├── data_cleaning.py
│   ├── analytics.py
│   ├── risk_engine.py
│   └── recommendations.py
│
├── visualizations/
│
├── main.py
│
├── README.md
│
├── requirements.txt
│
└── .gitignore
```

The current beginner version can remain simpler:

```text
MessMind/
│
├── DATA.CSV
├── main.py
└── README.md
```

The code can be reorganized into modules after the core concepts are understood.

---

# 22. Why This Project Is Different

A basic project answers:

> "What happened?"

MessMind is designed to progress toward:

> "Why did it happen?"

and eventually:

> "What should we do next?"

That progression is the main purpose of the project.

```text
DESCRIPTIVE
What happened?
       ↓
DIAGNOSTIC
Where/when is waste happening?
       ↓
PREDICTIVE
What could happen next?
       ↓
PRESCRIPTIVE
What action could reduce it?
```

---

# 23. Important Limitation

The current dataset contains only a small number of records.

Therefore, the project should NOT claim that its recommendations are universally accurate.

For meaningful prediction:

- collect data over many weeks/months
- record consistent measurements
- include food costs
- record number of people accurately
- handle special events/holidays
- evaluate prediction accuracy

This limitation should be explicitly mentioned in the final project documentation.

---

# 24. Future Vision

MessMind can eventually become a complete food-demand optimization platform:

```text
Historical Mess Data
        ↓
Data Analytics
        ↓
Waste Pattern Detection
        ↓
Demand Prediction
        ↓
Optimal Preparation Estimate
        ↓
Cost Saving Estimate
        ↓
Waste Reduction Recommendation
        ↓
Dashboard
```

The long-term goal is not simply to visualize food waste.

It is to use data to help a mess make **better preparation decisions and reduce avoidable waste**.

---

## Author

**Sanskar Sonawane**

Sinhgad Institute of Technology, Lonavala

---

## License

This project is intended for educational, academic, portfolio, and experimentation purposes.
