# Molecular Docking Analysis Tool

A Python-based tool for analyzing molecular docking interactions between ligands and the 5-HT2A receptor, with a focus on binding energy calculations and structural analysis.

## Features

- Receptor structure loading and preparation
- Ligand preparation from SMILES notation
- Detailed binding energy calculations including:
  - Van der Waals interactions
  - Electrostatic forces
  - Hydrogen bonding
  - Desolvation energy
  - Pi-stacking interactions
  - Hydrophobic interactions
  - Entropy contributions

- Molecular property analysis:
  - Molecular weight
  - LogP calculations
  - Topological polar surface area (TPSA)
  - Hydrogen bond donors/acceptors
  - Rotatable bonds

## Project Structure

```plaintext
molecular-docking/
├── src/
│   ├── molecular_dock.py      # Main docking implementation
│   ├── generate_report.py     # PDF report generation
│   ├── display_results.py     # Results visualization
│   └── setup_project.py       # Project structure setup
├── data/
│   ├── raw/                   # Original PDB files
│   └── processed/             # Generated results
├── tests/
│   └── test_molecular_dock.py # Unit tests
├── docs/
│   └── api.md                 # API documentation
└── notebooks/
    └── analysis.ipynb         # Jupyter notebooks for analysis
```

- `receptor_preparation.py`: Functions for loading and preparing the receptor structure.
- `ligand_preparation.py`: Functions for preparing ligands from SMILES notation.
- `binding_energy_calculation.py`: Functions for calculating binding energies and their contributions.
- `molecular_property_analysis.py`: Functions for analyzing molecular properties.
- `main.py`: Main script for running the analysis.

## Usage

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the main script:
   ```bash
   python main.py
   ```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

