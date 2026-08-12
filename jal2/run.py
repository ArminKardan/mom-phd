import os
import pandas as pd
import pyreadstat

def convert_sav_to_csv(directory):
    # Get a list of all .sav files in the directory
    sav_files = [f for f in os.listdir(directory) if f.endswith('.sav')]
    
    if not sav_files:
        print("No .sav files found in the directory.")
        return
    
    for sav_file in sav_files:
        # Construct full file path
        sav_path = os.path.join(directory, sav_file)
        
        # Read the .sav file
        df, meta = pyreadstat.read_sav(sav_path)
        
        # Construct the output .csv file path
        csv_file = sav_file.replace('.sav', '.csv')
        csv_path = os.path.join(directory, csv_file)
        
        # Save the DataFrame to a .csv file
        df.to_csv(csv_path, index=False)
        
        print(f"Converted {sav_file} to {csv_file}")

if __name__ == "__main__":
    # Get the directory where the script is located
    script_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Convert all .sav files in the script directory to .csv
    convert_sav_to_csv(script_directory)