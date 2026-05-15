import numpy as np
import pandas as pd
from pathlib import Path

OUTPUT_PATH = Path(__file__).resolve().parent / "retail_sales.csv"

np.random.seed(42)

dates = pd.date_range(start="2024-01-01", periods=180, freq="D")
stores = ["Store_A", "Store_B", "Store_C"]
categories = ["Electronics", "Groceries", "Clothing", "Home", "Beauty"]
promotions = ["None", "Discount", "Bundle", "Loyalty"]

rows = []
for date in dates:
    weekday = date.weekday()
    is_weekend = weekday >= 5
    season = (
        "Winter" if date.month in [12, 1, 2]
        else "Spring" if date.month in [3, 4, 5]
        else "Summer" if date.month in [6, 7, 8]
        else "Fall"
    )
    for store in stores:
        base_traffic = 80 + (10 if store == "Store_A" else 0) + (5 if store == "Store_C" else 0)
        traffic = base_traffic + np.random.randint(-20, 21)
        for category in categories:
            price = float(
                np.clip(
                    {
                        "Electronics": np.random.normal(250, 40),
                        "Groceries": np.random.normal(12, 3),
                        "Clothing": np.random.normal(45, 15),
                        "Home": np.random.normal(70, 20),
                        "Beauty": np.random.normal(28, 7),
                    }[category],
                    5,
                    500,
                )
            )
            promotion = np.random.choice(promotions, p=[0.55, 0.25, 0.15, 0.05])
            discount = 0.0 if promotion == "None" else np.random.choice([0.05, 0.10, 0.15, 0.20])
            if promotion == "Bundle":
                discount *= 1.2
            if promotion == "Loyalty":
                discount *= 1.3
            seasonal_factor = 1.0 + (0.25 if category == "Clothing" and season == "Fall" else 0)
            seasonal_factor += 0.15 if category == "Electronics" and season == "Winter" else 0
            seasonal_factor += 0.20 if category == "Groceries" and is_weekend else 0
            units_mean = (
                max(1, int(traffic * seasonal_factor * {
                    "Electronics": 0.08,
                    "Groceries": 0.35,
                    "Clothing": 0.14,
                    "Home": 0.12,
                    "Beauty": 0.10,
                }[category]))
            )
            units_sold = max(0, int(np.random.normal(units_mean, units_mean * 0.18)))
            revenue = round(units_sold * price * (1.0 - discount), 2)
            rows.append(
                {
                    "date": date,
                    "store_id": store,
                    "product_category": category,
                    "price": round(price, 2),
                    "promotion_type": promotion,
                    "promo_discount": round(discount, 2),
                    "units_sold": units_sold,
                    "revenue": revenue,
                    "weekday": weekday,
                    "is_weekend": int(is_weekend),
                    "season": season,
                }
            )

print(f"Generating {len(rows)} rows into {OUTPUT_PATH}")

pd.DataFrame(rows).to_csv(OUTPUT_PATH, index=False)
print("Done.")
