# Sky Hack 2.0 - United Airlines Hackathon

## Project Overview

This project is developed for the Sky Hack 2.0, a hackathon organized by United Airlines. The primary objective of this project is to optimize call center performance metrics, specifically focusing on Average Handle Time (AHT) and Average Speed to Answer (AST). By leveraging data analysis techniques, we aim to provide insights and predictions that can enhance customer service efficiency.

## Repository Contents

This repository contains the following files:

- **SQL Analysis File**: A detailed SQL script for data analysis on call center metrics.
  
- **Python Scripts**:
  - **Data Cleaning**:
    - `clean_calls.py`: Python script to clean the calls CSV file.
    - `clean_customers.py`: Python script to clean the customers CSV file.
  - **Insights Generation**: `generate_insights.py`: Python script to derive insights from the cleaned data.
  - **Prediction**: `predict_calls.py`: Python script to generate predictions for the test CSV file based on historical data.

- **Test Data**: 
  - `test.csv`: The test CSV file used for making predictions.
  
- **Original Data Files**: Four original data files that contain raw data for analysis.

## Getting Started

### Prerequisites

To run the scripts in this repository, you will need the following:

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SQLAlchemy (if working with SQL)
- Any other libraries specified in the scripts

You can install the required libraries using pip:

```bash
pip install pandas numpy matplotlib seaborn sqlalchemy
```

### Running the Scripts

1. **Data Cleaning**: Start by running the data cleaning scripts to preprocess the raw CSV files:

   ```bash
   python clean_calls.py
   python clean_customers.py
   ```

2. **Generate Insights**: After cleaning the data, generate insights by running:

   ```bash
   python generate_insights.py
   ```

3. **Predictions**: Use the `predict_calls.py` script to make predictions based on the test CSV file:

   ```bash
   python predict_calls.py
   ```

4. **View Results**: The results of the predictions will be saved in a CSV file named `test_<your_name>.csv`, which includes the `call_id` and the predicted `primary_call_reason`.

## Data Sources

The data used for analysis includes call center records, customer sentiments, and primary call reasons. The original files provide a comprehensive view of historical interactions.

