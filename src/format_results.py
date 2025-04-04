import pandas as pd

# Read the CSV file
df = pd.read_csv('c:\\Users\\PC\\Documents\\New Bioinformatics\\data\\docking_poses_results.csv')

# Format numeric columns to 4 decimal places
numeric_columns = [
    'Binding_Score', 
    'Energy_van_der_waals', 
    'Energy_electrostatic', 
    'Energy_hydrogen_bonds',
    'Energy_desolvation', 
    'Energy_pi_stacking', 
    'Energy_hydrophobic', 
    'Energy_entropy',
    'Property_MW', 
    'Property_LogP', 
    'Property_TPSA'
]

for col in numeric_columns:
    df[col] = df[col].round(4)

# Save the formatted results
df.to_csv('c:\\Users\\PC\\Documents\\New Bioinformatics\\data\\docking_poses_results_formatted.csv', index=False)