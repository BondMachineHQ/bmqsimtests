#!/usr/bin/env python

from spinqit import get_basic_simulator, get_compiler, Circuit, BasicSimulatorConfig
from spinqit import H, CX, Rx, X
from math import pi
import json

circ = Circuit()
q = circ.allocateQubits(2)

circ << (X, q[0])

comp = get_compiler("native")
engine = get_basic_simulator()

optimization_level = 0
exe = comp.compile(circ, optimization_level)

config = BasicSimulatorConfig()
result = engine.execute(exe, config)

values=result.states

outputs = []
outlist=[]
for coef in values:
	outlist.append([coef.real,coef.imag])
outputs.append(outlist)

# Write the output to the outputs file as json
with open('outputs.json', 'w') as outfile:
    json.dump(outputs, outfile)

