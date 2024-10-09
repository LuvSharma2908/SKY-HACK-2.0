import pandas as pd

# Load the CSV file
df = pd.read_csv(r'C:\Users\luv\Downloads\customers2afd6ea.csv')

# 1. Fill missing values in 'elite_level_code' with 'NA'
df['elite_level_code'].fillna('NA', inplace=True)

# 2. Remove duplicates if there are any
df.drop_duplicates(inplace=True)

# 3. Strip spaces from 'customer_name' (optional cleaning)
df['customer_name'] = df['customer_name'].str.strip()

# Save the cleaned file
df.to_csv('cleaned_customers.csv', index=False)

print("Cleaning complete and saved as 'cleaned_customers.csv'")
