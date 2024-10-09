import pandas as pd

# Load the CSV file
calls_df = pd.read_csv(r'C:\Users\luv\Downloads\callsf0d4f5a.csv')

# Handling missing values: Drop rows with nulls in 'agent_assigned_datetime' or 'call_end_datetime'
calls_df.dropna(subset=['agent_assigned_datetime', 'call_end_datetime'], inplace=True)

# Fill missing 'call_transcript' with 'Unknown'
calls_df['call_transcript'] = calls_df['call_transcript'].fillna('Unknown')

# Convert 'call_start_datetime', 'agent_assigned_datetime', and 'call_end_datetime' to datetime format
calls_df['call_start_datetime'] = pd.to_datetime(calls_df['call_start_datetime'], format='%m/%d/%Y %H:%M')
calls_df['agent_assigned_datetime'] = pd.to_datetime(calls_df['agent_assigned_datetime'], format='%m/%d/%Y %H:%M')
calls_df['call_end_datetime'] = pd.to_datetime(calls_df['call_end_datetime'], format='%m/%d/%Y %H:%M')

# Verify the changes
print(calls_df.info())

# Save the cleaned data back to a CSV file
calls_df.to_csv(r'C:\Users\luv\Downloads\cleaned_calls.csv', index=False)