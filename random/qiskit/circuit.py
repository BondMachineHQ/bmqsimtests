#!/usr/bin/env python3
import json

from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp,Operator
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService, EstimatorV2 as Estimator
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(3)
 
qc.y(2)
qc.x(1)
qc.y(2)
qc.x(1)
qc.z(1)
qc.cx(2,1)
qc.z(0)
qc.x(0)
qc.y(1)
qc.y(1)


print (qc.draw())

qc=qc.reverse_bits()

# Load the date from the inputs file

with open('inputs.json') as json_file:
    	inputs = json.load(json_file)

outputs = []

for input in inputs:
	complexArray = []
	for num in input:
		complexArray.append(complex(num[0],num[1]))

	sv=Statevector(complexArray)
	sv=sv.evolve(qc)
	outlistcomplex=sv.data.tolist()
	outlist=[]
	for i in range(len(outlistcomplex)):
		outlist.append([outlistcomplex[i].real,outlistcomplex[i].imag])
	outputs.append(outlist)

# Write the output to the outputs file as json
with open('outputs.json', 'w') as outfile:
    json.dump(outputs, outfile)