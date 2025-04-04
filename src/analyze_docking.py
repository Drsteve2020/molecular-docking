import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the docking results
df = pd.read_csv('data/docking_poses_results.csv')

# Create a figure with multiple subplots
plt.figure(figsize=(15, 10))

# 1. Binding Score Distribution
plt.subplot(2, 2, 1)
sns.histplot(data=df, x='Binding_Score', bins=10)
plt.title('Distribution of Binding Scores')
plt.xlabel('Binding Score (kcal/mol)')

# 2. Energy Components Analysis
energy_columns = [col for col in df.columns if col.startswith('Energy_')]
energy_data = df[energy_columns].mean()

plt.subplot(2, 2, 2)
energy_data.plot(kind='bar')
plt.title('Average Energy Components')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# 3. Top Poses Analysis
plt.subplot(2, 2, 3)
top_poses = df.sort_values('Binding_Score').head()
sns.barplot(data=top_poses, x='Pose', y='Binding_Score')
plt.title('Top 5 Binding Poses')
plt.ylabel('Binding Score (kcal/mol)')

# 4. Summary Statistics
plt.subplot(2, 2, 4)
plt.axis('off')
summary_stats = {
    'Best Score': df['Binding_Score'].min(),
    'Average Score': df['Binding_Score'].mean(),
    'Standard Deviation': df['Binding_Score'].std(),
    'Success Rate (<-8)': (df['Binding_Score'] < -8).mean() * 100
}
summary_text = '\n'.join([f'{k}: {v:.2f}' for k, v in summary_stats.items()])
plt.text(0.1, 0.5, f'Summary Statistics:\n\n{summary_text}', fontsize=10)

plt.tight_layout()
plt.savefig('data/docking_analysis.png')

# Print detailed analysis
print("\nDocking Analysis Results")
print("-" * 50)
print(f"Number of poses analyzed: {len(df)}")
print(f"\nBest binding pose: {df.loc[df['Binding_Score'].idxmin(), 'Pose']}")
print(f"Best binding score: {df['Binding_Score'].min():.2f} kcal/mol")
print("\nEnergy Component Contributions:")
for component in energy_columns:
    print(f"{component.replace('Energy_', '')}: {df[component].mean():.2f} kcal/mol")