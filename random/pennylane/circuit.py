
import pennylane as qml
import numpy as np
import json

qList = "q0,q1,q2".split(",")
qNum = len(qList)

dev = qml.device("default.qubit", wires=qList)

@qml.qnode(dev)
def circuit(state):
	qml.QubitStateVector(state, wires=qList)
	qml.RZ(4.188990355561471, wires="q1")
	qml.RX(3.8694967319522795, wires="q1")
	qml.RX(1.2781341671239348, wires="q2")
	qml.CNOT(wires=["q2","q0"])
	qml.PauliZ(wires="q2")
	qml.Hadamard(wires="q0")
	qml.Hadamard(wires="q2")
	qml.RX(0.9230749616017531, wires="q0")
	qml.PauliX(wires="q1")
	qml.CZ(wires=["q0","q2"])
	qml.PauliZ(wires="q1")
	qml.CNOT(wires=["q2","q1"])
	qml.CNOT(wires=["q0","q1"])
	qml.RZ(4.308384027970335, wires="q1")
	qml.PauliZ(wires="q2")
	qml.RZ(4.565200797272378, wires="q1")
	qml.CZ(wires=["q2","q1"])
	qml.PauliY(wires="q2")
	qml.CZ(wires=["q2","q1"])
	qml.PauliX(wires="q2")
	qml.PauliX(wires="q0")
	qml.RY(3.438980322205421, wires="q2")
	qml.PauliZ(wires="q2")
	qml.RX(3.9503601354589852, wires="q0")
	qml.RY(2.500161420576926, wires="q0")
	qml.CZ(wires=["q2","q1"])
	qml.CNOT(wires=["q2","q0"])
	qml.CNOT(wires=["q0","q2"])
	qml.PauliZ(wires="q0")
	qml.CNOT(wires=["q1","q2"])
	qml.Hadamard(wires="q0")
	qml.Hadamard(wires="q0")
	qml.RZ(0.7131457405436546, wires="q1")
	qml.RX(3.8326881797872194, wires="q1")
	qml.PauliX(wires="q0")
	qml.RY(2.552907595513642, wires="q0")
	qml.RY(5.298820720048878, wires="q1")
	qml.RY(5.709370548871356, wires="q0")
	qml.CNOT(wires=["q2","q0"])
	qml.PauliZ(wires="q1")
	qml.PauliX(wires="q0")
	qml.RY(3.44549177857083, wires="q0")
	qml.CZ(wires=["q2","q0"])
	qml.CNOT(wires=["q1","q0"])
	qml.PauliY(wires="q1")
	qml.CNOT(wires=["q2","q0"])
	qml.PauliY(wires="q1")
	qml.PauliY(wires="q1")
	qml.CNOT(wires=["q0","q1"])
	qml.RZ(4.594847909506322, wires="q2")
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
