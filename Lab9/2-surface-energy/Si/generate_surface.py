from ase import Atoms
from ase.build import diamond100,diamond111


a = 5.4  # Lattice constant in angstroms

# Generate diamond(100) surface
diamond_100 = diamond100('Si', size=(4, 4, 4), a=a, vacuum=10.0, orthogonal=True)

# Generate diamond(111) surface
diamond_111 = diamond111('Si', size=(4, 4, 4), a=a, vacuum=10.0)

# Visualize the structures (optional)
from ase.visualize import view
#view(diamond_100)
#view(diamond_111)

from ase.io import write

# save as xyz file - second line consists of cell parameters 
write("si_100.pdb", diamond_100)
write("si_111.pdb", diamond_111)

