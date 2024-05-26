#!/usr/bin/env python3
import json

from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp,Operator
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService, EstimatorV2 as Estimator
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(3)
 
qc.cx(0,2)
qc.rz(0.31109400916672314,2)
qc.ry(4.088097603329812,0)
qc.cx(1,2)
qc.h(1)
qc.cz(0,1)
qc.rx(0.7125486369232711,1)
qc.h(0)
qc.h(2)
qc.rz(2.9685518997769216,0)
qc.h(0)
qc.h(2)
qc.rx(5.35415754548599,2)
qc.rz(3.7470647842054112,1)
qc.rz(3.7693783925451876,1)
qc.z(2)
qc.z(0)
qc.cx(1,0)
qc.rx(5.138289253083489,2)
qc.cx(0,1)
qc.x(2)
qc.rx(2.462074938753762,1)
qc.cz(2,1)
qc.cz(1,0)
qc.rx(0.2827025860612343,1)
qc.cz(1,0)
qc.ry(2.131948830535125,2)
qc.ry(6.243854397463626,1)
qc.z(1)
qc.ry(6.242549315047099,0)
qc.cz(1,2)
qc.cz(2,1)
qc.x(0)
qc.h(2)
qc.rx(1.8334058932670556,1)
qc.rz(1.6586026145730146,2)
qc.y(0)
qc.ry(1.2139126046858053,2)
qc.ry(3.520786813265278,1)
qc.rx(0.9332390603208457,0)
qc.x(1)
qc.y(0)
qc.rz(2.7688502758899287,0)
qc.cx(1,2)
qc.ry(0.752399258956447,2)
qc.x(0)
qc.rx(0.15919099347969246,0)
qc.rz(1.3169538220273753,2)
qc.cx(0,1)
qc.x(0)


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