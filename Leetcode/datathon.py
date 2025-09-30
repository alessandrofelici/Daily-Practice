import pandas as pd
import numpy as np # Included for context
 
file_name = 'orders.csv'
df_orders = pd.read_csv(file_name)
 
print(f"Loaded DataFrame shape: {df_orders.shape}")
print("\nFirst 5 rows:")
print(df_orders.head())
print("\nColumn data types:")
print(df_orders.dtypes)