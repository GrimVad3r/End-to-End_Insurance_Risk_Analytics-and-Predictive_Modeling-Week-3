# Pre_Processor.py

A foundational data cleaning and feature identification script for the KIAM8 Insurance Risk Analytics Project. This script prepares the raw insurance claims data for Exploratory Data Analysis (EDA) and subsequent machine learning model training.

## 📝 Script Overview

The Pre_Processor.py script contains a single function, cleaner, which performs essential data quality checks, data type conversions, and classification of columns (numerical, categorical, and date/time).

## 🚀 Key Features

Data Integrity: Removes duplicate rows to ensure a clean dataset.

Data Type Conversion: Safely converts specified columns into proper datetime objects, critical for time-series analysis (e.g., TransactionMonth).

Column Classification: Automatically identifies and separates columns into Numerical, Categorical, and Date/Time types, which is essential for feature selection and subsequent encoding steps in the machine learning pipeline.

Safety: Operates on a copy of the input DataFrame to prevent side-effects on the original data.

## 🛠️ Requirements

The script relies only on the pandas library for data manipulation.

Bash

pip install pandas

## ⚙️ Usage

The main functionality is encapsulated in the cleaner function, which accepts a DataFrame and a list of columns to be converted to date/time format.

Function Signature
Python

def cleaner(df: pd.DataFrame, date_columns: list) -> tuple:
    """
    Cleans the raw dataframe, converts date/time columns, and identifies column types.

    Args:
        df (pd.DataFrame): The raw input DataFrame.
        date_columns (list): A list of column names (strings) that should be 
                             converted to datetime objects.

    Returns:
        tuple: A tuple containing:
            - temp_df (pd.DataFrame): The cleaned and processed DataFrame.
            - numerical_cols (list): List of numerical column names.
            - categorical_cols (list): List of categorical column names.
            - converted_date_cols (list): List of successfully converted date column names.
    """
Example
To use the script, you would typically:

Import the function.

Load your raw data.

Specify date columns.

Call the cleaner function.

Python

import pandas as pd
from Pre_Processor import cleaner

# 1. Load your raw data
raw_data_path = 'data/raw_insurance_data.csv' 
df_raw = pd.read_csv(raw_data_path)

# 2. Specify columns that need to be date/time objects
date_cols_to_convert = ['TransactionMonth', 'VehicleIntroDate']

# 3. Call the cleaning function
df_cleaned, num_cols, cat_cols, date_cols = cleaner(df_raw, date_cols_to_convert)

print("\n--- Summary ---")
print(f"Cleaned Data Shape: {df_cleaned.shape}")
print(f"Example Numerical Column: {num_cols[0]}")
print(f"Example Categorical Column: {cat_cols[0]}")

# You can now proceed to use df_cleaned for EDA or feature engineering
# e.g., df_cleaned.to_csv('data/pre_processed_data.csv', index=False)
⏭️ Next Steps
The output of Pre_Processor.py is intended to be the input for the next stage of the Data Version Control (DVC) pipeline, followed by specific feature engineering steps (like calculating LossRatio and VehicleAge as performed in task-1.ipynb) and ultimately, model training.