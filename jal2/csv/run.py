import os
import pandas as pd

def list_csv_files_and_columns(directory):
    # Get a list of all .csv files in the directory
    csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]
    
    if not csv_files:
        print("No .csv files found in the directory.")
        return
    
    for csv_file in csv_files:
        # Construct full file path
        csv_path = os.path.join(directory, csv_file)
        
        # Read the .csv file
        try:
            df = pd.read_csv(csv_path)
            
            # Print the file name
            print(f"File: {csv_file}")
            
            # Print the column names in a hierarchical way
            for i, column in enumerate(df.columns, 1):
                print(f"  Column {i}: {column}")
            
            print("\n")  # Add a newline for better readability
        
        except Exception as e:
            print(f"Error reading {csv_file}: {e}")

if __name__ == "__main__":
    # Get the directory where the script is located
    script_directory = os.path.dirname(os.path.abspath(__file__))
    
    # List all .csv files and their columns
    list_csv_files_and_columns(script_directory)