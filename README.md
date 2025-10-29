# SASA Calculation Script

A Python script for batch calculation of Solvent Accessible Surface Area (SASA) for protein structures in PDB format.

## Overview

This script processes PDB (Protein Data Bank) files to calculate the Solvent Accessible Surface Area (SASA) for each atom using the Shrake-Rupley algorithm. The calculated SASA values are stored in the B-factor column of the output PDB files, making them easy to visualize in molecular graphics software.

## Features

- **Batch Processing**: Process multiple PDB files in a folder at once
- **SASA Calculation**: Uses the Shrake-Rupley algorithm for accurate SASA computation
- **Customizable Parameters**: Adjustable probe radius and surface point density
- **Easy Visualization**: SASA values stored in B-factor column for easy visualization in PyMOL, Chimera, etc.
- **Command-line Interface**: Simple CLI for easy integration into workflows

## Requirements

- Python 3.x
- Biopython

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Phoenix-Chen-Git/script_for_SASA_calculation.git
cd script_for_SASA_calculation
```

2. Install dependencies:
```bash
pip install biopython
```

## Usage

### Basic Usage

Process all PDB files in a folder:

```bash
python main.py input_folder output_folder
```

**Example:**
```bash
python main.py pdb pdb_sasa
```

This will process all `.pdb` files in the `pdb` folder and save the results to the `pdb_sasa` folder.

### Advanced Usage

Customize the probe radius and number of surface points:

```bash
python main.py input_folder output_folder --probe 1.4 --points 100
```

**Parameters:**
- `input_folder`: Folder containing input PDB files
- `output_folder`: Folder where output PDB files will be saved
- `--probe`: Probe radius in Ångströms (default: 1.4 Å, typically represents water molecule)
- `--points`: Number of points per atom for surface calculation (default: 100, higher = more accurate but slower)

### Help

View all available options:

```bash
python main.py --help
```

## Output

The script generates new PDB files with the suffix `_sasa_b.pdb`. For example:
- Input: `6acc.pdb`
- Output: `6acc_sasa_b.pdb`

In the output files, **each atom's SASA value is stored in the B-factor column**, allowing you to visualize SASA distribution using molecular graphics software.

## Example Workflow

1. Place your PDB files in the `pdb` folder
2. Run the script:
   ```bash
   python main.py pdb pdb_sasa
   ```
3. Find the processed files in the `pdb_sasa` folder
4. Visualize in PyMOL:
   ```
   load pdb_sasa/6acc_sasa_b.pdb
   spectrum b, rainbow
   ```

## Understanding SASA

Solvent Accessible Surface Area (SASA) is the surface area of a biomolecule that is accessible to a solvent (typically water). It's an important measure in structural biology for:
- Predicting protein stability
- Understanding protein-protein interactions
- Identifying binding sites
- Analyzing protein folding

The Shrake-Rupley algorithm calculates SASA by rolling a probe sphere (representing a solvent molecule) over the van der Waals surface of the protein.

## Algorithm Details

This script uses BioPython's implementation of the **Shrake-Rupley algorithm**:
- **Probe radius**: Default 1.4 Å (water molecule radius)
- **Surface points**: Default 100 points per atom (Fibonacci spiral algorithm)
- **Level**: Atomic level calculation (each atom gets a SASA value)

## Examples

The repository includes example PDB files in the `pdb` folder and their corresponding processed outputs in the `pdb_sasa` folder.

## Troubleshooting

**Module not found error:**
```
ModuleNotFoundError: No module named 'Bio'
```
Solution: Install Biopython using `pip install biopython`

**No output files generated:**
- Check that input folder contains `.pdb` files
- Verify that the output folder path is valid
- Ensure you have write permissions for the output folder

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## References

- Shrake, A., & Rupley, J. A. (1973). Environment and exposure to solvent of protein atoms. Lysozyme and insulin. *Journal of Molecular Biology*, 79(2), 351-371.
- BioPython: https://biopython.org/
- PDB Format: https://www.wwpdb.org/documentation/file-format

## Author

Phoenix Chen

## Acknowledgments

This script uses the BioPython library for PDB parsing and SASA calculation.
