from molecular_dock import MolecularDocking
import pandas as pd
import os
from urllib.request import urlretrieve
import numpy as np
from datetime import datetime

def download_pdb():
    """Download the 5-HT2A receptor PDB file"""
    pdb_path = "data/5ht2a.pdb"
    if not os.path.exists("data"):
        os.makedirs("data")
    
    pdb_url = "https://files.rcsb.org/download/4oaj.pdb"
    if not os.path.exists(pdb_path):
        print("Downloading PDB file...")
        urlretrieve(pdb_url, pdb_path)
        print("Download complete!")

def run_multiple_simulations(docking, n_simulations=10):
    """Run multiple docking simulations and collect statistics"""
    all_scores = []
    for i in range(n_simulations):
        print(f"\rRunning simulation {i+1}/{n_simulations}", end="")
        score = docking.run_docking_simulation()
        all_scores.append(score)
    print("\n")
    return all_scores

def analyze_results(scores):
    """Analyze docking results"""
    results = {
        'Best Score': min(scores),
        'Average Score': np.mean(scores),
        'Standard Deviation': np.std(scores),
        'Median Score': np.median(scores),
        'Score Range': max(scores) - min(scores)
    }
    return results

def save_results(results, scores):
    """Save results to CSV file"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"data/docking_results_{timestamp}.csv"
    
    # Save detailed scores
    df = pd.DataFrame({
        'Simulation': range(1, len(scores) + 1),
        'Binding Score': scores
    })
    df.to_csv(filename, index=False)
    print(f"Detailed results saved to {filename}")

def main():
    download_pdb()
    
    docking = MolecularDocking()
    serotonin_smiles = "NCCC1=CC2=C(C=C1)C(=CN2)C"
    
    receptor = docking.load_receptor("data/5ht2a.pdb")
    ligand = docking.prepare_ligand(serotonin_smiles)
    
    # Run multiple simulations
    print("Starting docking simulations...")
    scores = run_multiple_simulations(docking, n_simulations=20)
    
    # Analyze results
    results = analyze_results(scores)
    
    # Display results
    print("\nDocking Results:")
    print("---------------")
    print(f"Ligand: Serotonin")
    print(f"Receptor: 5-HT2A")
    print(f"Number of simulations: {len(scores)}")
    print("\nStatistical Analysis:")
    print(f"Best binding score: {results['Best Score']:.2f} kcal/mol")
    print(f"Average binding score: {results['Average Score']:.2f} kcal/mol")
    print(f"Standard deviation: {results['Standard Deviation']:.2f}")
    print(f"Median score: {results['Median Score']:.2f} kcal/mol")
    print(f"Score range: {results['Score Range']:.2f} kcal/mol")
    print(f"\nBinding strength: {'Strong' if results['Best Score'] < -8 else 'Moderate' if results['Best Score'] < -6 else 'Weak'}")
    
    # Save results
    save_results(results, scores)

if __name__ == "__main__":
    main()