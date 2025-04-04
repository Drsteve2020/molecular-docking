import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def analyze_docking_results(csv_file):
    # Read the CSV file
    df = pd.read_csv(csv_file)
    
    # Create figure with multiple subplots
    plt.figure(figsize=(15, 10))
    
    # 1. Distribution Plot
    plt.subplot(2, 2, 1)
    sns.histplot(data=df, x='Binding Score', kde=True)
    plt.title('Distribution of Binding Scores')
    plt.xlabel('Binding Score (kcal/mol)')
    
    # 2. Box Plot
    plt.subplot(2, 2, 2)
    sns.boxplot(y=df['Binding Score'])
    plt.title('Binding Score Box Plot')
    plt.ylabel('Binding Score (kcal/mol)')
    
    # 3. Time Series Plot
    plt.subplot(2, 2, 3)
    plt.plot(df['Simulation'], df['Binding Score'], marker='o')
    plt.title('Binding Score vs Simulation Number')
    plt.xlabel('Simulation Number')
    plt.ylabel('Binding Score (kcal/mol)')
    
    # Calculate statistics
    stats = {
        'Mean': df['Binding Score'].mean(),
        'Median': df['Binding Score'].median(),
        'Std Dev': df['Binding Score'].std(),
        'Best Score': df['Binding Score'].min(),
        'Worst Score': df['Binding Score'].max(),
        'Range': df['Binding Score'].max() - df['Binding Score'].min()
    }
    
    # 4. Text box with statistics
    plt.subplot(2, 2, 4)
    plt.axis('off')
    stats_text = '\n'.join([f'{k}: {v:.2f}' for k, v in stats.items()])
    plt.text(0.1, 0.5, f'Statistical Analysis:\n\n{stats_text}', 
             fontsize=10, fontfamily='monospace')
    
    plt.tight_layout()
    
    # Save the plot
    plt.savefig('data/docking_analysis.png')
    print("Analysis plot saved as 'data/docking_analysis.png'")
    
    # Print detailed analysis
    print("\nDetailed Statistical Analysis:")
    print("-" * 30)
    for key, value in stats.items():
        print(f"{key}: {value:.2f}")
    
    # Calculate success rate (scores below -8 kcal/mol considered successful)
    success_rate = (df['Binding Score'] < -8).mean() * 100
    print(f"\nSuccess Rate (scores < -8 kcal/mol): {success_rate:.1f}%")

if __name__ == "__main__":
    analyze_docking_results("c:\\Users\\PC\\Documents\\New Bioinformatics\\data\\docking_results_20250404_185034.csv")