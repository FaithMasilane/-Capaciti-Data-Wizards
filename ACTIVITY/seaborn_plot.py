import matplotlib.pyplot as plt
import seaborn as sns

# Calculate total revenue per product
total_revenue_per_product = df.groupby("Product")["Revenue"].sum()

# Plot pie chart
plt.figure(figsize=(8, 8))
plt.pie(total_revenue_per_product, labels=total_revenue_per_product.index, autopct='%1.1f%%', 
        colors=sns.color_palette("pastel"), startangle=140, wedgeprops={"edgecolor": "black"})
plt.title("Sales Contribution by Product Category")
plt.show()
