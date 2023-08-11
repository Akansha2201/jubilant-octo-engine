# -*- coding: utf-8 -*-
"""Chipotle__Sales_Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YXXvxKP-s-RHCZ6pdk3lxlnp5kKTpueo

Objective: Use the pandas library to perform basic data analysis over Chipotle sales data. This workout will provide you practice in introductory exploratory data analysis to understand your data.

Link to dataset: https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv

1. Which was the most-ordered item?
2. For the most-ordered item, how many items were ordered?
3. What was the most ordered item in the choice_description column?
4. How many items were ordered in total?
5. Convert the item price into a float.
6. How much was the revenue for the period in the dataset?
7. How many orders were made in the period?
8. What is the average revenue amount per order?
9. How many different items are sold?

# Importing Packages
"""

import pandas as pd

"""# Read tsv file as csv"""

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
chipotle_data = pd.read_csv(url, sep = '\t')

chipotle_data.head

"""# Which was the most ordered item?"""

chipotle_most_ordered = chipotle_data.groupby('item_name') ['quantity'].sum().idxmax()
print ("Most ordered item:", chipotle_most_ordered)

"""# For the most-ordered item, how many items were ordered?"""

num_chipotle_most_ordered = chipotle_data.groupby('item_name') ['quantity'].sum().max()
print ("Number of items ordered:", num_chipotle_most_ordered)

"""# What was the most ordered item in the choice_description column?"""

chipotle_most_ordered_choice = chipotle_data.groupby('choice_description') ['quantity'].sum().idxmax()
print ("Most ordered choice:", chipotle_most_ordered_choice)

"""# How many items were ordered in total?"""

chipotle_total_orders = chipotle_data['quantity'].sum()
print ("Total items ordered:",  chipotle_total_orders)

"""# Convert the item price into a float."""

chipotle_data['item_price'].dtype
chipotle_data['item_price'] = chipotle_data['item_price'].astype(str)
chipotle_data['item_price'] = chipotle_data['item_price'].apply (lambda x: float ( x[1:]))
print("the item price column is of data type:", chipotle_data['item_price'].dtype)

"""# How much was the revenue for the period in the dataset?"""

revenue = (chipotle_data['quantity'] * chipotle_data['item_price']).sum()
print("Revenue for the period: $" , round(revenue,2))

"""# How many orders were made in the period?"""

total_orders = chipotle_data['order_id'].nunique()
print("total no. of orders:", total_orders)

"""# What is the average revenue amount per order?"""

average_revenue_per_order = revenue / total_orders
print("average revenue amount per order: $", round(average_revenue_per_order,2))

"""# How many different items are sold?"""

total_items_sold = chipotle_data['item_name'].nunique(0)
print("Total items sold: ", total_items_sold)