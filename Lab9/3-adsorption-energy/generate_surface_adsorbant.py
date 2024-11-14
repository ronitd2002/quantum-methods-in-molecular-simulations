from ase import Atoms
from ase.build import diamond111
from ase.io import write
import numpy as np
from ase.build import molecule


# Define lattice constant for Si diamond structure
a = 5.4 

# Generate diamond(111) surface
diamond_111 = diamond111('Si', size=(4, 4, 4), a=a, vacuum=10.0)

# Calculate the center of the surface
center = np.mean(diamond_111.positions[:, :2], axis=0)  # Calculate mean of x and y coordinates

# Create a molecule
adsorbant = molecule('H2O', vacuum=0.0)

# Place adsorbant molecule at the center of the surface only along x and y directions
adsorbant.translate(np.hstack((center - adsorbant.positions[0][:2], 0)))

# Calculate distance from top layer
distance = 2.5  # Distance in angstroms
z_top = max(diamond_111.positions[:, 2])  # Maximum z-coordinate of Si atoms
z = z_top + distance
adsorbant.translate([0, 0, z])

# Add adsorbant molecule to surface
surface_with_adsorbant = diamond_111 + adsorbant

# Save Si(111) surface with CO molecule as PDB file
write("si_111_with_adsorbant.pdb", surface_with_adsorbant)

