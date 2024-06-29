#!/usr/bin/env python3
import json
import os
import math

from scipy.optimize import minimize
from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp,Operator
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService, EstimatorV2 as Estimator
from qiskit.quantum_info import Statevector


with open('inputs.json') as json_file:
    	inputs = json.load(json_file)

qbits = int(math.log2(len(inputs[0])))

rot = False
if os.path.exists("rotations"):
	rot = True
	with open('rots.json') as json_file:
		rots = json.load(json_file)

def get_qc(qbits, rot, rotTarget):
	qc = QuantumCircuit(qbits)

	if rot:
		rotations = rots[rotTarget]
		# print (rotations)
		for i in range(qbits):
			if rotations[3*i] != 0.0:
				qc.rx(rotations[3*i], i)
			if rotations[3*i+1] != 0.0:
				qc.ry(rotations[3*i+1], i)
			if rotations[3*i+2] != 0.0:
				qc.rz(rotations[3*i+2], i)

	qc=qc.reverse_bits()
	return qc

# print (qc.draw())

# Load the date from the inputs file

outputs = []

for currI in range(len(inputs)):
	input = inputs[currI]
	complexArray = []
	if rot:
		complexArray.append(complex(1,0))
		for i in range(len(input)-1):
			complexArray.append(complex(0,0))
	else:
		for num in input:
			complexArray.append(complex(num[0],num[1]))

	sv=Statevector(complexArray)
	print(sv)
	# print (sv)
	# print (targetrot)
	qc = get_qc(qbits, rot,currI)
	print (qc.draw())
	sv=sv.evolve(qc)
	outlistcomplex=sv.data.tolist()
	outlist=[]
	for i in range(len(outlistcomplex)):
		outlist.append([outlistcomplex[i].real,outlistcomplex[i].imag])
	outputs.append(outlist)

# Write the output to the outputs file as json
with open('outputs.json', 'w') as outfile:
    json.dump(outputs, outfile)
