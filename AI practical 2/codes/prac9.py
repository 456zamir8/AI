'''implement the Association rule mining algorithm to find the frequent dataset. 
Generate association rules from the frequent item set and calculate their support.'''

import pandas as pd
import numpy as np
import plotly.graph_objects as go
from apyori import apriori

# Load the groceries dataset
df = pd.read_csv('AI practical 2/datasets/groceries_dataset.csv')

# Get the unique products
all_products = df['item_Description'].unique()
print("Total products: {}".format(len(all_products)))

# Prepare data for plotting: counting occurrences of each product
product_counts = df['item_Description'].value_counts().reset_index()
product_counts.columns = ['Product', 'Count']

# Select top 10 products for visualization
top_10_products = product_counts.head(10)

# Implementing the plot using Plotly
fig = go.Figure([go.Bar(x=top_10_products['Product'], y=top_10_products['Count'])])
fig.update_layout(
    title="Top 10 Most Sold Products", 
    xaxis_title="Product", 
    yaxis_title="Number of Sales"
)

# Show the figure
# fig.show()

# One-hot encoding for product purchases
one_hot = pd.get_dummies(df['item_Description'])
df.drop('item_Description', inplace=True, axis=1)
df = df.join(one_hot)
print(df.head().to_string())

# Handling multiple transactions as one
records = df.groupby(['Member_number', 'Date'])[one_hot.columns].sum().reset_index()

# Replacing non-zero values with product names
def get_pnames(x):
    for product in one_hot.columns:
        if x[product] > 0:
            x[product] = product  # Replace count with product name
    return x

# Apply the function to each row
records = records.apply(get_pnames, axis=1)

print("\n", records.head().to_string())
print("Total transactions: {}".format(len(records)))

# Removing zeros from the transactions
transactions = records[one_hot.columns].apply(lambda row: row[row != 0].tolist(), axis=1)

# Convert the transactions into a list of lists
transactions = transactions.tolist()

# Display the first 10 transactions
print(transactions[0:10])

rules = apriori(transactions, min_support = 0.00030, min_confidance = 0.05, min_lift = 3, min_length = 2, target = 'rules')
association_results = list(rules)

for item in association_results:
    # Extract the base and add items from the rule
    pair = item.items
    items = [x for x in pair]  # Convert the frozen set to a list for better readability
    
    # Print the rule
    if len(items) >= 2:  # To avoid errors in case there's only one item in the rule
        print(f"Rule: {items[0]} -> {items[1]}")
    else:
        print(f"Item: {items[0]}")  # For rules with only one item
    
    # Print the support
    print(f"Support: {item.support}")
    
    # Print the confidence and lift (checking the first ordered statistic if present)
    if len(item.ordered_statistics) > 0:
        print(f"Confidence: {item.ordered_statistics[0].confidence}")
        print(f"Lift: {item.ordered_statistics[0].lift}")
    
    print("============================================")
