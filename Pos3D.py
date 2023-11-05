import numpy as np
def getPositions(NAtoms, step=2.5):
	positions = [np.array([0, 0, 0])]
	atomsPlaced = 1
	agotadas = True
	cornerPos = positions[0]
	dim = 0
	adderMult = 1
	while atomsPlaced < NAtoms:
		if dim > 2:
			dim = 0
			adderMult = 1
			agotadas = True
			continue
		if agotadas:
			cornerPos = np.array([cornerPos[0] + step, cornerPos[1] + step, cornerPos[2] + step])
			positions.append(cornerPos)
			atomsPlaced += 1
			agotadas = False
			continue
		adder = np.zeros(3)
		adder[dim] = step
		newAtomPos = cornerPos - adder * adderMult
		if newAtomPos[dim] < 0:
			dim += 1
			adderMult = 1
			continue
		positions.append(newAtomPos)
		atomsPlaced += 1
		adderMult += 1
	return positions