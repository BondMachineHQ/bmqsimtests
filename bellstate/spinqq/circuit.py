#!/usr/bin/env python
import os
import json
import math

from scipy.optimize import minimize
from qiskit.quantum_info import Statevector
from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp,Operator
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit.quantum_info import Statevector

from spinqit import get_basic_simulator, get_compiler, Circuit, BasicSimulatorConfig
from spinqit import H, CX, Rx, X, Ry, Rz, CZ
from math import pi

from spinqit import get_nmr, get_compiler, Circuit, NMRConfig

with open('inputs.json') as json_file:
        inputs = json.load(json_file)

qbits = int(math.log2(len(inputs[0])))

if os.path.exists("vars.py"):
    from vars import user, password, qhost

rot = False
if os.path.exists("rotations"):
	rot = True
	with open('rots.json') as json_file:
		rots = json.load(json_file)

def get_qc(qbits, rot, rotTarget):
	circ = Circuit()
	q = circ.allocateQubits(qbits)

	if rot:
		rotations = rots[rotTarget]
		# print (rotations)
		for i in range(qbits):
			if rotations[3*i] != 0.0:
				circ << (Rx, q[i], rotations[3*i])
			if rotations[3*i+1] != 0.0:
				circ << (Ry, q[i], rotations[3*i+1])
			if rotations[3*i+2] != 0.0:
				circ << (Rz, q[i], rotations[3*i+2])

	circ << (H, q[0])
	circ << (CX, (q[0], q[1]))
	return circ

outputs = []

for currI in range(len(inputs)):
    input = inputs[currI]

    circ=get_qc(qbits, rot, currI)

    engine = get_nmr()
    comp = get_compiler("native")

    exe = comp.compile(circ, 0)
    config = NMRConfig()
    config.configure_shots(1024)
    config.configure_ip(qhost)
    config.configure_port(55444)
    config.configure_account(user, password)
    config.configure_task("task1", "GHZ")

    result = engine.execute(exe, config)

    p=result.probabilities

    outlist=[]

    for i in range(2**2):
        if f"{i:02b}" in p:
            outlist.append(p[f"{i:02b}"])
        else:
            outlist.append(0.0)

    outputs.append(outlist)

# Write the output to the outputs file as json
with open('probs.json', 'w') as outfile:
    json.dump(outputs, outfile)
