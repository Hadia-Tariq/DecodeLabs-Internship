import pandas as pd

file_path = r"C:\Users\anees\OneDrive\Desktop\Dataset for Data Analytics.xlsx"

df = pd.read_excel(file_path)

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print("Duplicate rows:", df.duplicated().sum())
print("Duplicate OrderIDs:", df["OrderID"].duplicated().sum())
print("\nMissing values:")
print(df.isnull().sum())
print("\nPayment Methods:")
print(df["PaymentMethod"].value_counts())

print("\nOrder Status:")
print(df["OrderStatus"].value_counts())

print("\nCoupon Codes:")
print(df["CouponCode"].value_counts(dropna=False))

print("\nReferral Sources:")
print(df["ReferralSource"].value_counts())
print("\nNumerical Summary:")
print(df[["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]].describe())
print("\nInvalid or suspicious values:")

print("Quantity <= 0:", (df["Quantity"] <= 0).sum())
print("UnitPrice <= 0:", (df["UnitPrice"] <= 0).sum())
print("ItemsInCart <= 0:", (df["ItemsInCart"] <= 0).sum())
print("TotalPrice <= 0:", (df["TotalPrice"] <= 0).sum())
df["CalculatedTotal"] = df["Quantity"] * df["UnitPrice"]

df["PriceDifference"] = (
    df["TotalPrice"] - df["CalculatedTotal"]
).round(2)

print("\nPrice calculation check:")
print("Mismatched totals:", (df["PriceDifference"] != 0).sum())

df.drop(columns=["CalculatedTotal", "PriceDifference"], inplace=True)
print("\n===== SALES OVERVIEW =====")

total_revenue = df["TotalPrice"].sum()
average_order_value = df["TotalPrice"].mean()
total_quantity = df["Quantity"].sum()
total_orders = df["OrderID"].nunique()

print("Total Orders:", total_orders)
print("Total Revenue:", round(total_revenue, 2))
print("Average Order Value:", round(average_order_value, 2))
print("Total Quantity Sold:", total_quantity)

print("\n===== PRODUCT PERFORMANCE =====")

product_performance = df.groupby("Product").agg(
    Orders=("OrderID", "count"),
    QuantitySold=("Quantity", "sum"),
    Revenue=("TotalPrice", "sum")
)

product_performance = product_performance.sort_values(
    "Revenue", ascending=False
)

print(product_performance)

import matplotlib.pyplot as plt

product_performance["Revenue"].plot(kind="bar")

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\n===== ORDER STATUS ANALYSIS =====")

status_analysis = df["OrderStatus"].value_counts()

print(status_analysis)

print("\n===== DUPLICATE ID CHECK =====")
print("Duplicate Order IDs:", df["OrderID"].duplicated().sum())

print("\n===== DATE FORMAT CHECK =====")
print("Invalid Dates:", pd.to_datetime(df["Date"], errors="coerce").isna().sum())

df['Date'] = pd.to_datetime(df['Date'])


print("\n===== MISSING VALUES CHECK =====")
print(df.isnull().sum())
print("\n===== HANDLING MISSING VALUES =====")
df["CouponCode"] = df["CouponCode"].fillna("No Coupon")

print("Remaining missing values:", df.isnull().sum().sum())

print("\n===== FINAL VALIDATION =====")
print("Duplicate Order IDs:", df["OrderID"].duplicated().sum())
print("Missing Values:", df.isnull().sum().sum())
print("Invalid Dates:", pd.to_datetime(df["Date"], errors="coerce").isna().sum())

df.to_excel("decodelab_project1_cleaned.xlsx", index=False)
print("Cleaned dataset saved successfully!")

import os
print(os.path.abspath("decodelab_project1_cleaned.xlsx"))

