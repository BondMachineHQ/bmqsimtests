
import pennylane as qml
import numpy as np
import json

qList = "q0,q1".split(",")
qNum = len(qList)

dev = qml.device("default.qubit", wires=qList)

@qml.qnode(dev)
def circuit(state):
    qml.QubitStateVector(state, wires=qList)
    qml.PauliX(wires="q0")
    return qml.state()

with open('inputs.json') as json_file:
    	inputs = json.load(json_file)

outputs = []

for input in inputs:
    complexArray = []
    for num in input:
        complexArray.append(num[0] + num[1] * 1j)

    normalized_state = np.array(complexArray)
    
    outputState = circuit(normalized_state)
    output = []

    for i in range(len(outputState)):
        output.append([outputState[i].real.tolist(), outputState[i].imag.tolist()])

    outputs.append(output)

# Write the output to the outputs file as json
with open('outputs.json', 'w') as outfile:
    json.dump(outputs, outfile)

# print(outputs)
