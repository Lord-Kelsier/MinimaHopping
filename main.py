from ase import Atoms
import time as t
from ase.optimize.minimahopping import MinimaHopping
from ase.calculators.emt import EMT
from ase.optimize.minimahopping import MHPlot
from Pos3D import getPositions 
import os
steps = 2000
T0=1000
positions = getPositions(13)
systems = ['Au7Ag6', 'Al6Cu7', 'Al11Cu2', 'Al5Cu8', 'Al2Cu11']
for i in range(len(systems)):
	system = Atoms(systems[i], positions=positions)
	system.set_calculator(EMT())
	opt = MinimaHopping(atoms=system, T0=T0)
	startT = t.time()
	opt(totalsteps=steps)
	endT = t.time()
	with open('timeSummary.txt', '+a') as f:
		print(f"{systems[i][0]}|Time: {endT - startT}|Steps: {steps}|T0: {T0}", file=f)

	mhplot = MHPlot()
	mhplot.save_figure(f'summary{systems[i][0]}.png')
	os.rename('minima.traj', f"minima{systems[i][0]}.traj")
	os.rename('hop.log', f"hop{systems[i][0]}.log")
	for i in range(0, steps):
		if i > 0:
			os.remove(f'md{i:05d}.log')
			os.remove(f'md{i:05d}.traj')
		os.remove(f'qn{i:05d}.log')
		os.remove(f'qn{i:05d}.traj')
	del system, opt, mhplot
