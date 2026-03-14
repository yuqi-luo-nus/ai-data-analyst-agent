import pandas as pd

def generate_report(df: pd.DataFrame) -> str:

    top_row = df.iloc[0]

    category = top_row["product_category"]
    growth_rate = top_row["growth_rate"]
    q1 = top_row["q1_revenue"]
    q2 = top_row["q2_revenue"]

    report = f"""
Revenue Growth Analysis (Q2 vs Q1)

Top Performing Category:
{category}

Revenue:
Q1: {q1}
Q2: {q2}

Growth Rate:
{growth_rate}%

Conclusion:
{category} had the highest revenue growth from Q1 to Q2, suggesting strong market demand or increased sales performance in this category.
"""

    return report