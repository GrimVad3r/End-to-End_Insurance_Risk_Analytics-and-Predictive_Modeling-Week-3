import pandas as pd

def cleaner(df, date_columns):
    """Cleans the raw dataframe, converts date/time columns,
    and identifies column types."""

    # Step 1: Data Cleaning
    print("🧹 Preprocessing data...")

    # Always work on a copy to prevent modifying the original dataframe outside the function
    temp_df = df.copy()

    # Handle missing values and duplicates

    temp_df.drop_duplicates(keep='first', inplace=True)

    print("✅ Finished Cleaning data...")

    # ---

    # Step 2: Convert Date/Time Columns
    print('\n⏰ Converting specified columns to date objects...')

    # Use a try-except block for safer conversion
    for col in date_columns:
        if col in temp_df.columns:
            try:
                # Use .dt.date to get the date part, which results in a Python date object
                temp_df[col] = pd.to_datetime(temp_df[col], errors='coerce')
            except Exception as e:
                print(f"⚠️ Warning: Could not convert column '{col}' to date: {e}")
        else:
            print(f"⚠️ Warning: Column '{col}' not found in the DataFrame.")

    # ---

    # Step 3: Identify Column Types
    # Identify numerical columns (before they might be converted to 'object' for date)
    numerical_cols = temp_df.select_dtypes(include=['int64', 'float64']).columns.tolist()

    # Identify the converted date columns based on the input list
    converted_date_cols = [col for col in date_columns if col in temp_df.columns]

    # Identify categorical columns (objects, excluding the now-converted date columns)
    # The dtypes will be 'object' for strings AND the converted date objects.
    object_cols = temp_df.select_dtypes(include=['object']).columns.tolist()
    categorical_cols = [col for col in object_cols if col not in converted_date_cols]


    print(f"\n📊 Categorical Columns: {len(categorical_cols)}")
    print(f"📈 Numerical Columns: {len(numerical_cols)}")
    print(f"📅 Converted Date Columns (now 'object' dtype): {len(converted_date_cols)}")
    return temp_df