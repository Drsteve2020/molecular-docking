from molecular_dock import MolecularDocking
import pandas as pd
import numpy as np

class CompoundScreening:
    def __init__(self):
        self.docking = MolecularDocking()
        self.compounds = {
            'Serotonin': "NCCC1=CC2=C(C=C1)C(=CN2)C",
            'Psilocin': "CN(C)CCc1c[nH]c2cccc(O)c12",
            'DMT': "CN(C)CCc1c[nH]c2ccccc12",
            'LSD': "CCN(CC)C(=O)C1CN(C)C2Cc3cn(C)c4cccc(C2=C1)c34",
            '5-MeO-DMT': "CN(C)CCc1c[nH]c2ccc(OC)cc12",
            'Bufotenin': "CN(C)CCc1c[nH]c2cc(O)ccc12"
        }

    def screen_compounds(self):
        results = []
        
        for compound_name, smiles in self.compounds.items():
            print(f"\nScreening {compound_name}...")
            
            # Prepare ligand
            self.docking.prepare_ligand(smiles)
            
            # Run multiple docking attempts
            binding_scores = []
            for _ in range(5):  # 5 attempts per compound
                score, energy_components = self.docking.calculate_binding_score()
                binding_scores.append(score)
            
            # Store results
            results.append({
                'Compound': compound_name,
                'SMILES': smiles,
                'Best_Score': min(binding_scores),
                'Average_Score': np.mean(binding_scores),
                'StdDev': np.std(binding_scores)
            })
        
        return pd.DataFrame(results)

    def analyze_results(self, results_df):
        # Sort compounds by binding affinity
        results_df = results_df.sort_values('Best_Score')
        
        # Save results
        results_df.to_csv('data/compound_screening_results.csv', index=False)
        print("\nScreening Results:")
        print("-" * 50)
        print(results_df)
        
        return results_df

def main():
    # Initialize receptor and run screening
    screener = CompoundScreening()
    results = screener.screen_compounds()
    screener.analyze_results(results)

if __name__ == "__main__":
    main()