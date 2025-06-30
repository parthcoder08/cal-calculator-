 # Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Load CSV File
# NOTE: Replace 'sales.csv' with your file path or upload to Colab
df = pd.read_csv('sales.csv')

# Step 3: Basic Overview
print("🔍 First 5 rows:\n", df.head())
print("\n🧾 Info:\n")
df.info()

# Step 4: Add Total column
df['Total'] = df['Quantity'] * df['Price']

# Step 5: Group by Region
sales_by_region = df.groupby('Region')['Total'].sum()
print("\n📊 Total Sales by Region:\n", sales_by_region)

# Step 6: Plot by Region
sales_by_region.plot(kind='bar', title="Total Sales by Region", xlabel="Region", ylabel="Total Sales", color='skyblue')
plt.tight_layout()
plt.show()

# Step 7: Group by Product
sales_by_product = df.groupby('Product')['Total'].sum()
print("\n📦 Total Sales by Product:\n", sales_by_product)

# Step 8: Plot by Product
sales_by_product.plot(kind='pie', autopct='%1.1f%%', title="Sales Distribution by Product")
plt.ylabel("")
plt.tight_layout()
plt.show()