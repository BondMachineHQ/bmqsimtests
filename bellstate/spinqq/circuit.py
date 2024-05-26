#!/usr/bin/env python
from spinqit import get_nmr, get_compiler, Circuit, NMRConfig
from spinqit import H, CX, X
import json, os

if os.path.exists("vars.py"):
    from vars import user, password, qhost

engine = get_nmr()
comp = get_compiler("native")

circ = Circuit()

q = circ.allocateQubits(2)
circ << (X, q[0])
circ << (CX, q[0], q[1])

exe = comp.compile(circ, 0)
config = NMRConfig()
config.configure_shots(1024)
config.configure_ip(qhost)
config.configure_port(55444)
config.configure_account(user, password)
config.configure_task("task1", "GHZ")

result = engine.execute(exe, config)

p=result.probabilities

outputs = []
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
