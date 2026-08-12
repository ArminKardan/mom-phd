import pandas as pd
import numpy as np
import torch

# Load the CSV file
file = "VOXEL"
df = pd.read_csv(f'./{file}.csv')
try:
    df.drop(columns=['subject'], inplace=True)
except:
    pass

try:
    df.drop(columns=['subNO'], inplace=True)
except:
    pass

target_rows_per_group = 50
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
numeric_cols.remove('group')  # Remove the group column from features to augment

augmented_data = []

for group in range(1, 7):
    # Filter group data
    group_df = df[df['group'] == group]
    if len(group_df) == 0:
        continue
        
    # Calculate how many samples to generate
    needed = target_rows_per_group - len(group_df)
    if needed <= 0:
        augmented_data.append(group_df)
        continue
    
    # Storage for synthetic data
    synthetic = {col: [] for col in numeric_cols}
    
    # Generate data for each numeric column
    for col in numeric_cols:
        original_values = group_df[col].values
        mu = original_values.mean()
        sigma = original_values.std()
        min_val = original_values.min()
        max_val = original_values.max()
        
        # Handle constant columns
        if sigma < 1e-6:
            synthetic[col] = np.full(needed, mu)
            continue
            
        # Generate initial synthetic data with constraints
        attempts = 0
        while True:
            # Generate data using PyTorch with clamping
            data = torch.normal(mean=mu, std=sigma, size=(needed * 10,))
            data = torch.clamp(data, min=min_val, max=max_val).numpy()
            
            # Randomly select 'needed' samples that meet criteria
            valid_data = data[(data >= min_val) & (data <= max_val)]
            if len(valid_data) >= needed:
                synthetic[col] = valid_data[:needed]
                break
                
            attempts += 1
            if attempts > 100:
                synthetic[col] = np.full(needed, mu)
                break
                
        # Adjust mean and std iteratively
        for _ in range(100):
            current_mu = synthetic[col].mean()
            current_std = synthetic[col].std()
            
            if abs(current_mu - mu) < 0.01 and abs(current_std - sigma) < 0.01:
                break
                
            # Apply linear transformation
            synthetic[col] = (synthetic[col] - current_mu) * (sigma / current_std) + mu
            synthetic[col] = np.clip(synthetic[col], min_val, max_val)
        
        # Final rounding
        synthetic[col] = np.round(synthetic[col], 2)
    
    # Create synthetic DataFrame
    synthetic_df = pd.DataFrame(synthetic)
    synthetic_df['group'] = group
    
    # Combine with original data
    augmented_group = pd.concat([group_df, synthetic_df], ignore_index=True)
    augmented_data.append(augmented_group)

# Combine all groups and save
final_df = pd.concat(augmented_data, ignore_index=True)
final_df.to_csv(f'./GAN/{file}.csv', index=False)
print("Augmentation complete with safe constraints!")