# Calculate Surface Energy

To determine which surface is more stable, calculate the surface energy using the following steps:

1. Verify the Python scripts. Execute them to obtain input coordinates and cell parameters for Si bulk and Si surfaces 100 and 111.

2. Generate Quantum Espresso input files for Si surfaces 100 and 111.

3. Perform self-consistent field (SCF) calculations. Note: Geometry optimization is time-consuming; hence, perform SCF calculations for now.

4. Compute the unrelaxed surface energy using the formula:
   Surface energy = (1/2) * (E_slab - N * E_bulk)

   Where:
   - E_bulk: Energy per atom, obtained by running SCF energy calculation on bulk material and then calculating energy per atom.
   - E_slab: Energy of the slab.

5. Repeat the above procedure for a new system. Work in the new directory.

