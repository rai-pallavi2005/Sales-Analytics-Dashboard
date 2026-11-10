# Step 1: Import libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from pathlib import Path

print("Libraries imported successfully!")


# Step 2: Find project folder

BASE_DIR = Path(__file__).resolve().parent.parent

# Step 3: Load dataset

file_path = BASE_DIR / "data" / "superstore_sales.csv"

df = pd.read_csv(file_path)

print("Dataset loaded successfully!")


# Step 4: Display first five rows

print(df.head())

 # Step 5 : Display dataset information 
print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

# Step 5: Check duplicate records

duplicates = df.duplicated().sum()

print("\nTotal Duplicate Records:", duplicates)



# STEP 6: Convert mixed date formats into datetime

df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    format="mixed",
    errors="coerce"
)

print("\nUpdated Data Type:")
print(df["Order Date"].dtype)

print("\nDate Range:")
print("First Date:", df["Order Date"].min())
print("Last Date:", df["Order Date"].max())

print("\nInvalid Dates:", df["Order Date"].isnull().sum())

# Step 7: Check loss-making records

loss_records = df[df["Profit"] < 0]

print("\nTotal Loss-Making Records:", len(loss_records))

print("\nLoss-Making Records:")
print(loss_records.head(10))

# Step 8: Save cleaned dataset

df.to_csv("data/cleaned_superstore_sales.csv", index=False)

print("\nCleaned dataset saved successfully!")

# STEP 9: BASIC SALES ANALYSIS

print("\n========== SALES ANALYSIS ==========")

# Total Sales
total_sales = df["Sales"].sum()
print("Total Sales:", round(total_sales, 2))

# Total Profit
total_profit = df["Profit"].sum()
print("Total Profit:", round(total_profit, 2))

# Total Records
total_records = len(df)
print("Total Records:", total_records)

# Total Quantity Sold
total_quantity = df["Quantity"].sum()
print("Total Quantity Sold:", total_quantity)

# Average Sales
average_sales = df["Sales"].mean()
print("Average Sales:", round(average_sales, 2))

# Profit Margin
profit_margin = (total_profit / total_sales) * 100
print("Profit Margin:", round(profit_margin, 2), "%")

# STEP 8: Inspect duplicate records

duplicate_rows = df[df.duplicated(keep=False)]

print("\nDuplicate Records:")
print(duplicate_rows)

print("\nTotal Duplicate Rows:", len(duplicate_rows))

# STEP 9: Remove duplicate records

print("\nRows Before Cleaning:", len(df))

df = df.drop_duplicates()

print("Rows After Cleaning:", len(df))

print("Duplicates Remaining:", df.duplicated().sum())

# STEP 10: Save cleaned dataset

df.to_csv(
    "data/cleaned_superstore_sales.csv",
    index=False
)

print("\nFinal cleaned dataset saved successfully!")

# STEP 10: Final Sales Analysis

print("\n========== CLEANED SALES ANALYSIS ==========")

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()

average_sales = df["Sales"].mean()

profit_margin = (total_profit / total_sales) * 100

print("Total Sales:", round(total_sales, 2))
print("Total Profit:", round(total_profit, 2))
print("Total Records:", len(df))
print("Total Quantity:", total_quantity)
print("Average Sales:", round(average_sales, 2))
print("Profit Margin:", round(profit_margin, 2), "%")

# STEP 11: Regional Sales Analysis

region_sales = df.groupby("Region")["Sales"].sum()

print("\n========== SALES BY REGION ==========")
print(region_sales.sort_values(ascending=False))

# STEP 12: Visualize Regional Sales

region_sales = region_sales.sort_values(ascending=False)

plt.figure(figsize=(9, 5))

region_sales.plot(
    kind="bar",
    color="skyblue",
    edgecolor="black"
)

plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("regional_sales.png", dpi=300)

plt.show()

# STEP 13: Sales Analysis by Category

category_sales = df.groupby("Category")["Sales"].sum()

print("\n========== SALES BY CATEGORY ==========")
print(category_sales.sort_values(ascending=False))

# STEP 14: Visualize Sales by Category

category_sales = category_sales.sort_values(ascending=False)

plt.figure(figsize=(9, 5))

category_sales.plot(
    kind="bar",
    color="lightgreen",
    edgecolor="black"
)

plt.title("Total Sales by Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("category_sales.png", dpi=300)
plt.show()

# STEP 15: Profit Analysis by Category

category_profit = df.groupby("Category")["Profit"].sum()

print("\n========== PROFIT BY CATEGORY ==========")
print(category_profit.sort_values(ascending=False))

# STEP 16: Visualize Profit by Category

category_profit = category_profit.sort_values(ascending=False)

plt.figure(figsize=(9, 5))

category_profit.plot(
    kind="bar",
    color="orange",
    edgecolor="black"
)

plt.title("Total Profit by Category")
plt.xlabel("Product Category")
plt.ylabel("Total Profit")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("category_profit.png", dpi=300)
plt.show()

# STEP 17: Monthly Sales Trend Analysis

# Extract Year and Month from Order Date
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month

# Group sales by Year and Month
monthly_sales = df.groupby(
    ["Year", "Month"]
)["Sales"].sum()

print("\n========== MONTHLY SALES TREND ==========")
print(monthly_sales)

# STEP 18: Monthly Sales Trend Visualization

monthly_sales = monthly_sales.reset_index()

monthly_sales["Year-Month"] = (
    monthly_sales["Year"].astype(str)
    + "-"
    + monthly_sales["Month"].astype(str).str.zfill(2)
)

plt.figure(figsize=(14, 6))

plt.plot(
    monthly_sales["Year-Month"],
    monthly_sales["Sales"],
    marker="o",
    linewidth=2
)

plt.title("Monthly Sales Trend (2014-2017)")
plt.xlabel("Year-Month")
plt.ylabel("Total Sales")

plt.xticks(rotation=90)
plt.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("monthly_sales_trend.png", dpi=300)
plt.show()

# STEP 19: Customer Segment Sales Analysis

segment_sales = df.groupby("Segment")["Sales"].sum()

print("\n========== SALES BY CUSTOMER SEGMENT ==========")
print(segment_sales.sort_values(ascending=False))

# STEP 20: Visualize Sales by Customer Segment

segment_sales = segment_sales.sort_values(ascending=False)

plt.figure(figsize=(9, 5))

segment_sales.plot(
    kind="bar",
    color="mediumpurple",
    edgecolor="black"
)

plt.title("Total Sales by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("segment_sales.png", dpi=300)
plt.show()

# STEP 21: Top 10 States by Sales

state_sales = df.groupby("State")["Sales"].sum()

top_10_states = state_sales.sort_values(
    ascending=False
).head(10)

print("\n========== TOP 10 STATES BY SALES ==========")
print(top_10_states)

# STEP 22: Visualize Top 10 States by Sales

plt.figure(figsize=(10, 6))

top_10_states.sort_values().plot(
    kind="barh",
    color="cornflowerblue",
    edgecolor="black"
)

plt.title("Top 10 States by Sales")
plt.xlabel("Total Sales")
plt.ylabel("State")

plt.tight_layout()
plt.savefig("top_10_states.png", dpi=300)
plt.show()

# STEP 23: Sales Analysis by Sub-Category

subcategory_sales = df.groupby(
    "Sub-Category"
)["Sales"].sum()

top_subcategories = subcategory_sales.sort_values(
    ascending=False
).head(10)

print("\n========== TOP 10 SUB-CATEGORIES BY SALES ==========")
print(top_subcategories.to_string())

# STEP 24: Visualize Top 10 Sub-Categories by Sales

plt.figure(figsize=(10, 6))

top_subcategories.sort_values().plot(
    kind="barh",
    color="teal",
    edgecolor="black"
)

plt.title("Top 10 Sub-Categories by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Sub-Category")

plt.tight_layout()
plt.savefig("top_10_subcategories.png", dpi=300)
plt.show()

# STEP 25: Top 10 Sub-Categories by Profit

subcategory_profit = df.groupby(
    "Sub-Category"
)["Profit"].sum()

top_10_profit = subcategory_profit.sort_values(
    ascending=False
).head(10)

print("\n========== TOP 10 SUB-CATEGORIES BY PROFIT ==========")
print(top_10_profit.to_string())

# STEP 26: Visualize Top 10 Sub-Categories by Profit

plt.figure(figsize=(10, 6))

top_10_profit.sort_values().plot(
    kind="barh",
    color="mediumseagreen",
    edgecolor="black"
)

plt.title("Top 10 Sub-Categories by Profit")
plt.xlabel("Total Profit")
plt.ylabel("Sub-Category")

plt.tight_layout()
plt.savefig("top_10_subcategories_profit.png", dpi=300)
plt.show()

# STEP 27: Identify Loss-Making Sub-Categories

loss_categories = subcategory_profit[subcategory_profit < 0]

loss_categories = loss_categories.sort_values()

print("\n========== LOSS-MAKING SUB-CATEGORIES ==========")
print(loss_categories)

# STEP 28: Visualize Loss-Making Sub-Categories

plt.figure(figsize=(9, 5))

loss_categories.plot(
    kind="bar",
    color="salmon",
    edgecolor="black"
)

plt.title("Loss-Making Sub-Categories")
plt.xlabel("Sub-Category")
plt.ylabel("Total Loss")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("loss_making_categories.png", dpi=300)
plt.show()

# STEP 29: Final Business Insights

print("\n========== FINAL BUSINESS INSIGHTS ==========")

print("1. West region generated the highest sales.")

print("2. Technology is the highest sales-generating category.")

print("3. Technology generated the highest category profit.")

print("4. Consumer segment contributed approximately 50.6% of total sales.")

print("5. November 2017 recorded the highest monthly sales.")

print("6. California is the highest sales-generating state.")

print("7. Phones is the top sales-generating sub-category.")

print("8. Tables recorded the highest loss among sub-categories.")