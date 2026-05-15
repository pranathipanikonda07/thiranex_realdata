# thiranex_realdata

## Retail Sales Data Science Project

This repository contains a domain-specific retail sales analysis workflow designed for applied learning.

### Project contents
- `data/generate_retail_data.py`: synthetic retail dataset generator for sales, promotions, stores, and revenue.
- `data/retail_sales.csv`: generated retail transaction dataset.
- `notebooks/retail_sales_analysis.ipynb`: end-to-end exploratory analysis, visualization, and a sales prediction model.
- `requirements.txt`: Python dependencies for analysis.

### Goals
- Perform exploratory data analysis on retail sales data.
- Visualize sales patterns by store, category, seasonal trend, and promotion.
- Build a prediction model for units sold based on store, category, price, promotions, and calendar features.
- Summarize findings and business insights.

### Run it
1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Generate the dataset:

```bash
python data/generate_retail_data.py
```

3. Open the notebook:

```bash
jupyter notebook notebooks/retail_sales_analysis.ipynb
```

### Notes
This project is intentionally self-contained and uses a realistic synthetic dataset for retail analysis.
