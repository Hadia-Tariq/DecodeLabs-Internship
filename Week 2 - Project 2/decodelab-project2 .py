
import pandas as pd

df = pd.read_excel("decodelab_project1_cleaned.xlsx")

print("Dataset loaded successfully!")
print(df.head())
print(df.shape)

print("\n===== COLUMN NAMES =====")
print(df.columns)
print("\n===== BASIC DATASET INFORMATION =====")
print(df.info())
print("\n===== STATISTICAL SUMMARY =====")
print(df.describe())
print("\n===== DUPLICATE CHECK =====")
print("Number of duplicate rows:", df.duplicated().sum())
print("\n===== MISSING VALUES CHECK =====")
print(df.isnull().sum())
print("\n===== PRODUCT PERFORMANCE =====")

product_performance = df.groupby("Product").agg(
    Orders=("OrderID", "count"),
    QuantitySold=("Quantity", "sum"),
    Revenue=("TotalPrice", "sum")
)

print(product_performance.sort_values("Revenue", ascending=False))
print("\n===== ORDER STATUS ANALYSIS =====")

order_status = df["OrderStatus"].value_counts()

print(order_status)
print("\n===== PAYMENT METHOD ANALYSIS =====")

payment_methods = df["PaymentMethod"].value_counts()

print(payment_methods)
print("\n===== REFERRAL SOURCE ANALYSIS =====")

referral_sources = df["ReferralSource"].value_counts()

print(referral_sources)

print("\n===== REVENUE ANALYSIS =====")

total_revenue = df["TotalPrice"].sum()
average_order_value = df["TotalPrice"].mean()
highest_order_value = df["TotalPrice"].max()
lowest_order_value = df["TotalPrice"].min()

print("Total Revenue:", round(total_revenue, 2))
print("Average Order Value:", round(average_order_value, 2))
print("Highest Order Value:", round(highest_order_value, 2))
print("Lowest Order Value:", round(lowest_order_value, 2))

import matplotlib.pyplot as plt

print("\n===== REVENUE BY PRODUCT CHART =====")

product_performance["Revenue"].sort_values(ascending=False).plot(
    kind="bar",
    title="Revenue by Product"
)

plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

print("\n===== ORDER STATUS CHART =====")

order_status.plot(
    kind="bar",
    title="Orders by Status"
)

plt.xlabel("Order Status")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.show()


print("\n===== REVENUE BY PAYMENT METHOD =====")

payment_revenue = df.groupby("PaymentMethod")["TotalPrice"].sum()

print(payment_revenue.sort_values(ascending=False))

print("\n===== REVENUE BY PAYMENT METHOD CHART =====")

payment_revenue.sort_values(ascending=False).plot(
    kind="bar",
    title="Revenue by Payment Method"
)

plt.xlabel("Payment Method")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

print("\n===== REVENUE BY REFERRAL SOURCE =====")

referral_revenue = df.groupby("ReferralSource")["TotalPrice"].sum()

print(referral_revenue.sort_values(ascending=False))

print("\n===== REVENUE BY REFERRAL SOURCE CHART =====")

referral_revenue.sort_values(ascending=False).plot(
    kind="bar",
    title="Revenue by Referral Source"
)

plt.xlabel("Referral Source")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

print("\n===== MONTHLY REVENUE ANALYSIS =====")

df["Month"] = df["Date"].dt.to_period("M").astype(str)

monthly_revenue = df.groupby("Month")["TotalPrice"].sum()

print(monthly_revenue)

print("\n===== MONTHLY REVENUE CHART =====")

monthly_revenue.plot(
    kind="line",
    title="Monthly Revenue Trend",
    marker="o"
)

plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\n===== QUANTITY SOLD BY PRODUCT =====")

quantity_by_product = df.groupby("Product")["Quantity"].sum()

print(quantity_by_product.sort_values(ascending=False))

print("\n===== QUANTITY SOLD BY PRODUCT CHART =====")

quantity_by_product.sort_values(ascending=False).plot(
    kind="bar",
    title="Quantity Sold by Product"
)

plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.tight_layout()
plt.show()

print("\n===== REVENUE BY ORDER STATUS =====")

status_revenue = df.groupby("OrderStatus")["TotalPrice"].sum()

print(status_revenue.sort_values(ascending=False))

print("\n===== REVENUE BY ORDER STATUS CHART =====")

status_revenue.sort_values(ascending=False).plot(
    kind="bar",
    title="Revenue by Order Status"
)

plt.xlabel("Order Status")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

print("\n===== COUPON CODE ANALYSIS =====")

coupon_analysis = df.groupby("CouponCode").agg(
    Orders=("OrderID", "count"),
    Revenue=("TotalPrice", "sum")
)

print(coupon_analysis.sort_values("Revenue", ascending=False))

print("\n===== REVENUE BY COUPON CODE CHART =====")

coupon_analysis["Revenue"].sort_values(ascending=False).plot(
    kind="bar",
    title="Revenue by Coupon Code"
)

plt.xlabel("Coupon Code")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\n===== TOP AND LOWEST PERFORMING PRODUCTS =====")

top_product = product_performance["Revenue"].idxmax()
lowest_product = product_performance["Revenue"].idxmin()

print("Top Revenue Product:", top_product)
print("Lowest Revenue Product:", lowest_product)

top_quantity_product = quantity_by_product.idxmax()
lowest_quantity_product = quantity_by_product.idxmin()

print("Top Selling Product by Quantity:", top_quantity_product)
print("Lowest Selling Product by Quantity:", lowest_quantity_product)


