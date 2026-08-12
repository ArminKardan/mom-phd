import pandas as pd
import os

def fill_missing_values(input_file, output_file):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(input_file)

    # Print the initial DataFrame (for debugging purposes)
    print("Initial DataFrame:")
    print(df)

    # Fill missing values with the mean of each column
    df_filled = df.fillna(df.mean(numeric_only=True))

    # Print the DataFrame after filling missing values (for debugging purposes)
    print("\nDataFrame after filling missing values:")
    print(df_filled)

    # Save the updated DataFrame to a new CSV file
    df_filled.to_csv(output_file, index=False)

    print(f"\nNew CSV file saved as: {output_file}")

# Replace 'input.csv' with the name of your input CSV file
# Replace 'output.csv' with the name of your output CSV file



fill_missing_values("./VOXEL.csv", "./FilledData/VOXEL.csv")







