import pandas as pd
import numpy as np

# Read the CSV file
df = pd.read_csv('c:\\Users\\PC\\Documents\\New Bioinformatics\\data\\docking_poses_results_formatted.csv')

# Group the columns by type
energy_cols = [col for col in df.columns if col.startswith('Energy_')]
property_cols = [col for col in df.columns if col.startswith('Property_')]

# Create separate DataFrames for better visualization
energy_df = df[['Pose', 'Binding_Score'] + energy_cols].set_index('Pose')
property_df = df[['Pose'] + property_cols].set_index('Pose')

# Display results
print("\nBinding Energies (kcal/mol):")
print("=" * 80)
print(energy_df)

print("\nMolecular Properties:")
print("=" * 80)
print(property_df)

# Display statistics for binding scores
print("\nBinding Score Statistics:")
print("=" * 80)
print(f"Best Pose: {df.loc[df['Binding_Score'].idxmin(), 'Pose']} (Score: {df['Binding_Score'].min():.4f})")
print(f"Average Score: {df['Binding_Score'].mean():.4f}")
print(f"Standard Deviation: {df['Binding_Score'].std():.4f}")