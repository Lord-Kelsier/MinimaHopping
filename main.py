from ase import Atoms
import time as t
from ase.optimize.minimahopping import MinimaHopping
from ase.calculators.emt import EMT
from ase.optimize.minimahopping import MHPlot
from Pos3D import getPositions 
import os
steps = 500
T0=1000
for AuAtoms in range(2, 100):
	system = Atoms(f'Au{AuAtoms}', positions=getPositions(AuAtoms))
	system.set_calculator(EMT())
	opt = MinimaHopping(atoms=system, T0=T0)
	startT = t.time()
	opt(totalsteps=steps)
	endT = t.time()
	with open('timeSummary.txt', '+a') as f:
		print(f"Time: {endT - startT}|Steps: {steps}|T0: {T0}", file=f)

	mhplot = MHPlot()
	mhplot.save_figure(f'summaryAu{AuAtoms}.png')
	os.rename('minima.traj', f"minimaAu{AuAtoms}.traj")
	os.rename('hop.log', f"hopAu{AuAtoms}.log")
	for i in range(0, steps):
		if i > 0:
			os.remove(f'md{i:05d}.log')
			os.remove(f'md{i:05d}.traj')
		os.remove(f'qn{i:05d}.log')
		os.remove(f'qn{i:05d}.traj')
	del system, opt, mhplot
