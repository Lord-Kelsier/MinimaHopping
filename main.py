from ase import Atoms
import time as t
from ase.optimize.minimahopping import MinimaHopping
from ase.calculators.emt import EMT
from ase.optimize.minimahopping import MHPlot
from Pos3D import getPositions 
steps = 100
T0=1000
for AuAtoms in range(2, 100):
	system = Atoms(f'Au{AuAtoms}', positions=getPositions(AuAtoms))
	system.set_calculator(EMT())
	opt = MinimaHopping(atoms=system, T0=T0,)
	startT = t.time()
	opt(totalsteps=steps)
	endT = t.time()
	with open('timeSummary.txt', '+a') as f:
		print(f"Time: {endT - startT}|Steps: {steps}|T0: {T0}", file=f)

	mhplot = MHPlot()
	mhplot.save_figure(f'summary{AuAtoms}.png')