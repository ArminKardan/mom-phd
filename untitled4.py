import numpy as np
from scipy.stats import ttest_1samp

def add_numbers_preserving_ttest(original_data, num_new):
    # Original statistics
    original_mean = np.mean(original_data)
    original_variance = np.var(original_data)
    
    # Generate new data maintaining the original mean and variance
    additional_numbers = np.random.normal(original_mean, np.sqrt(original_variance), num_new)
    
    # Combine the original data and the additional numbers
    extended_data = np.concatenate([original_data, additional_numbers])
    return extended_data

# Function to verify t-test consistency
def verify_ttest_consistency(original_data, extended_data):
    # Perform a one-sample t-test for both sets
    t_original, p_original = ttest_1samp(original_data, np.mean(original_data))
    t_extended, p_extended = ttest_1samp(extended_data, np.mean(original_data))
    return (t_original, p_original), (t_extended, p_extended)

# Original vector
data = np.array([
0.12,
0.19,
0.125,
0.1,
0.2,
0.15,
0.16,
0.15,
0.1,
0.2,
])

# Add 30 numbers to the vector
updated_data = add_numbers_preserving_ttest(data, 30)

# Verify t-test results
original_ttest, updated_ttest = verify_ttest_consistency(data, updated_data)

# Output results
print(f"Original Data T-Test: t = {original_ttest[0]:.4f}, p = {original_ttest[1]:.4f}")
print(f"Updated Data T-Test: t = {updated_ttest[0]:.4f}, p = {updated_ttest[1]:.4f}")
print("\nUpdated Data:")
print(list(np.round(updated_data, 3)))
