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

def rotfitness(parameters, *args):
	qbits=int(len(parameters)/3)

	qc = QuantumCircuit(qbits)
	for i in range(qbits):
		qc.rx(float(parameters[3*i]), i)
		qc.ry(float(parameters[3*i+1]), i)
		qc.rz(float(parameters[3*i+2]), i)
	
	# print (qc.draw())
	qc=qc.reverse_bits()

	complexArray = []
	complexArray.append(complex(1,0))
	for i in range(2**qbits-1):
		complexArray.append(complex(0,0))

	sv = Statevector(complexArray)
	sv = sv.evolve(qc)

	outlistcomplex = sv.data.tolist()
	# print(outlistcomplex)
	# print (args)

	sigma = 0.0
	for i in range(len(outlistcomplex)):
		sigma  += abs(args[2*i] - outlistcomplex[i].real)
		sigma  += abs(args[2*i+1] - outlistcomplex[i].imag)

	sigma = sigma/len(outlistcomplex)
	# print (outlistcomplex)
	# print (args)
	# print (sigma)
	return sigma

def guessrotations(target):
	# target is a statevector
	length = len(target)
	qbits = int(math.log2(length/2))
	# print (qbits)
	initial_guess = [1.0,] * 3*qbits
	
	result = minimize(rotfitness, initial_guess, args=tuple(target),method='L-BFGS-B', options={'ftol': 1e-5, 'disp': False})
	print (result)
	return result.x

rot = False
if os.path.exists("rotations"):
	rot = True

def get_qc(rot, rottarget):
	qc = QuantumCircuit(2)

	if rot:
		rotations = guessrotations(rottarget)
		# print (rotations)
		for i in range(2):
			qc.rx(rotations[3*i], i)
			qc.ry(rotations[3*i+1], i)
			qc.rz(rotations[3*i+2], i)

	qc.x(0)

	qc=qc.reverse_bits()
	return qc

# print (qc.draw())

# Load the date from the inputs file

with open('inputs.json') as json_file:
    	inputs = json.load(json_file)

outputs = []

for input in inputs:
	complexArray = []
	targetrot = []
	if rot:
		complexArray.append(complex(1,0))
		for i in range(len(input)-1):
			complexArray.append(complex(0,0))
		for num in input:
			targetrot.append(num[0])
			targetrot.append(num[1])
	else:
		for num in input:
			complexArray.append(complex(num[0],num[1]))

	sv=Statevector(complexArray)
	# print (sv)
	# print (targetrot)
	qc = get_qc(rot,targetrot)
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
