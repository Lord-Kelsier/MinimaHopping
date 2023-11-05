import ase.calculators.emt as emt
import ase.io as io
atoms = io.Trajectory('minima.traj')
atoms = atoms[-1]
atoms.set_calculator(emt.EMT())
print(atoms.get_potential_energy()/13)
io.write('Aminima.png', atoms)
io.write('Aminima.xyz', atoms)