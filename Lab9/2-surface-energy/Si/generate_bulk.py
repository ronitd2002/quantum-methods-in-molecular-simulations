from ase import Atoms
from ase.build import bulk,  make_supercell
from ase.io import write

# Define lattice constant for Si diamond structure
a = 5.431  # Lattice constant of Si in angstroms

# Create Si diamond bulk structure
si_bulk = bulk('Si', 'diamond', a=a,  cubic=True)


# Create 6x6x6 supercell
si_supercell = make_supercell(si_bulk, [[2,0,0],[0,2,0],[0,0,2]])

# Save Si diamond bulk structure as PDB file
write('si_bulk_supercell.pdb', si_supercell)


