import os
import matplotlib.pyplot as plt
import pandas as pd

def plot_growth(df: pd.DataFrame, output_path: str = "outputs/charts/growth.png"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    plt.figure(figsize=(8, 5))
    plt.bar(df["product_category"], df["growth_rate"])
    plt.xlabel("Product Category")
    plt.ylabel("Growth Rate (%)")
    plt.title("Revenue Growth by Product Category (Q2 vs Q1)")
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

    return output_path