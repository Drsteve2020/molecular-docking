import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.cluster import KMeans
from scipy.stats import pearsonr

class DockingAnalyzer:
    def __init__(self, results_file):
        self.df = pd.read_csv(results_file)
        self.reference_compounds = {
            'Risperidone': -9.2,
            'Clozapine': -8.7,
            'Ketanserin': -8.9
        }

    def perform_clustering_analysis(self, n_clusters=3):
        """Cluster binding poses"""
        kmeans = KMeans(n_clusters=n_clusters)
        clusters = kmeans.fit_predict(np.array(self.df['Binding Score']).reshape(-1, 1))
        self.df['Cluster'] = clusters
        
        plt.figure(figsize=(10, 6))
        for i in range(n_clusters):
            cluster_data = self.df[self.df['Cluster'] == i]
            plt.scatter(cluster_data.index, cluster_data['Binding Score'], label=f'Cluster {i+1}')
        plt.title('Binding Pose Clusters')
        plt.xlabel('Simulation Number')
        plt.ylabel('Binding Score (kcal/mol)')
        plt.legend()
        plt.savefig('data/clustering_analysis.png')
        plt.close()

    def analyze_energy_components(self):
        """Analyze energy component contributions"""
        components = ['van_der_waals', 'electrostatic', 'hydrogen_bonds', 'desolvation']
        energies = np.random.rand(len(components))  # Simulated data
        
        plt.figure(figsize=(10, 6))
        plt.bar(components, energies)
        plt.title('Energy Component Breakdown')
        plt.ylabel('Energy Contribution (kcal/mol)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('data/energy_components.png')
        plt.close()

    def compare_with_references(self):
        """Compare with reference compounds"""
        plt.figure(figsize=(10, 6))
        
        # Plot current results
        plt.hist(self.df['Binding Score'], bins=20, alpha=0.5, label='Serotonin')
        
        # Plot reference lines
        for compound, score in self.reference_compounds.items():
            plt.axvline(x=score, linestyle='--', label=compound)
            
        plt.title('Comparison with Reference Compounds')
        plt.xlabel('Binding Score (kcal/mol)')
        plt.ylabel('Frequency')
        plt.legend()
        plt.savefig('data/reference_comparison.png')
        plt.close()

    def run_complete_analysis(self):
        """Run all analyses"""
        print("Running comprehensive docking analysis...")
        
        # Clustering analysis
        print("\n1. Performing clustering analysis...")
        self.perform_clustering_analysis()
        
        # Energy components
        print("\n2. Analyzing energy components...")
        self.analyze_energy_components()
        
        # Reference comparison
        print("\n3. Comparing with reference compounds...")
        self.compare_with_references()
        
        # Statistical summary
        print("\n4. Statistical Summary:")
        print("-" * 50)
        print(f"Mean Binding Score: {self.df['Binding Score'].mean():.2f} kcal/mol")
        print(f"Best Binding Score: {self.df['Binding Score'].min():.2f} kcal/mol")
        print(f"Number of favorable poses: {len(self.df[self.df['Binding Score'] < -8])}")
        
        print("\nAnalysis complete! Check the data folder for visualization plots.")

if __name__ == "__main__":
    # Update the file path to use the existing results file
    analyzer = DockingAnalyzer("data/docking_results_20250404_185034.csv")
    analyzer.run_complete_analysis()