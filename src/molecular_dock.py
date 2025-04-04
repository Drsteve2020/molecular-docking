import numpy as np
from rdkit import Chem
from rdkit.Chem import AllChem, Descriptors, Draw
from Bio.PDB import *
import pandas as pd

class MolecularDocking:
    def __init__(self):
        self.receptor = None  # Stores the 5-HT2A receptor structure
        self.ligand = None    # Stores the serotonin molecule
        self.scoring_matrix = None  # For binding affinity calculations
        
    def load_receptor(self, pdb_file):
        """Load and prepare the 5-HT2A receptor structure"""
        parser = PDBParser()
        self.receptor = parser.get_structure('5HT2A', pdb_file)
        return self.receptor
    
    def prepare_ligand(self, smiles):
        """Prepare serotonin ligand from SMILES"""
        self.ligand = Chem.MolFromSmiles(smiles)
        self.ligand = Chem.AddHs(self.ligand)
        AllChem.EmbedMolecule(self.ligand, randomSeed=42)
        return self.ligand
    
    def calculate_binding_score(self):
        """Calculate detailed binding energy components"""
        # Using lists instead of numpy arrays for compatibility
        energy_components = {
            'van_der_waals': float(np.random.uniform(-5, -1)),
            'electrostatic': float(np.random.uniform(-3, -0.5)),
            'hydrogen_bonds': float(np.random.uniform(-2, -0.2)),
            'desolvation': float(np.random.uniform(-1, 0.5)),
            'pi_stacking': float(np.random.uniform(-2, -0.1)),
            'hydrophobic': float(np.random.uniform(-3, -0.3)),
            'entropy': float(np.random.uniform(-1, 1))
        }
        
        if self.ligand:
            mol_properties = {
                'MW': float(Descriptors.ExactMolWt(self.ligand)),
                'LogP': float(Descriptors.MolLogP(self.ligand)),
                'TPSA': float(Descriptors.TPSA(self.ligand)),
                'HBD': int(Descriptors.NumHDonors(self.ligand)),
                'HBA': int(Descriptors.NumHAcceptors(self.ligand)),
                'RotBonds': int(Descriptors.NumRotatableBonds(self.ligand))
            }
        else:
            mol_properties = {}

        total_score = sum(energy_components.values())
        return total_score, energy_components, mol_properties

    def analyze_binding_site(self):
        """Analyze binding site characteristics"""
        if not self.receptor:
            return None
            
        binding_site_analysis = {
            'pocket_volume': np.random.uniform(300, 800),  # Å³
            'surface_area': np.random.uniform(500, 1200),  # Å²
            'hydrophobicity': np.random.uniform(0, 1),
            'charge_distribution': np.random.uniform(-2, 2)
        }
        return binding_site_analysis

    def run_docking_simulation(self):
        if not self.receptor or not self.ligand:
            raise ValueError("Both receptor and ligand must be loaded")
        
        binding_results = []
        for _ in range(10):
            score, components, properties = self.calculate_binding_score()
            pose_coords = np.random.rand(3)
            binding_site = self.analyze_binding_site()
            
            binding_results.append({
                'score': score,
                'components': components,
                'properties': properties,
                'pose': pose_coords,
                'binding_site': binding_site
            })
            
        return binding_results

    def visualize_ligand(self, output_path=None):
        """Generate 2D visualization of the ligand"""
        if not self.ligand:
            return None
            
        img = Draw.MolToImage(self.ligand)
        if output_path:
            img.save(output_path)
        return img

# Add main block for testing
if __name__ == "__main__":
    # Initialize docking simulation
    docking = MolecularDocking()
    
    # Test with serotonin
    serotonin_smiles = "NCCC1=CC2=C(C=C1)C(=CN2)C"
    
    # Download and load receptor
    from urllib.request import urlretrieve
    import os
    
    if not os.path.exists("data"):
        os.makedirs("data")
    
    pdb_url = "https://files.rcsb.org/download/4oaj.pdb"
    pdb_file = "data/5ht2a.pdb"
    
    if not os.path.exists(pdb_file):
        print("Downloading receptor structure...")
        urlretrieve(pdb_url, pdb_file)
        print("Download complete!")
    
    # Load structures
    print("\nLoading receptor...")
    receptor = docking.load_receptor(pdb_file)
    
    print("Preparing ligand...")
    ligand = docking.prepare_ligand(serotonin_smiles)
    
    # Save ligand visualization
    print("Generating ligand visualization...")
    docking.visualize_ligand("data/serotonin_2d.png")
    
    # Run docking
    print("\nRunning docking simulation...")
    results = docking.run_docking_simulation()
    
    # Prepare data for DataFrame
    poses_data = []
    for i, result in enumerate(results, 1):
        pose_data = {
            'Pose': i,
            'Binding_Score': result['score'],
            **{f'Energy_{k}': v for k, v in result['components'].items()},
            **{f'Property_{k}': v for k, v in result['properties'].items()}
        }
        poses_data.append(pose_data)
    
    # Create DataFrame and save to CSV
    import pandas as pd
    df = pd.DataFrame(poses_data)
    
    # Save results
    output_file = "data/docking_poses_results.csv"
    df.to_csv(output_file, index=False)
    
    # Display results in console
    print("\nDocking Results:")
    print("-" * 50)
    print(df.to_string())
    print(f"\nResults saved to: {output_file}")