#!/usr/bin/env python3

from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp,Operator
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService, EstimatorV2 as Estimator
from qiskit.quantum_info import Statevector

# Create a new circuit with two qubits
qc = QuantumCircuit(2)
 
# Add a Hadamard gate to qubit 0
#qc.h(1)
#print (Operator(qc))
 
# Perform a controlled-X gate on qubit 1, controlled by qubit 0
qc.h(0)
# print (Operator(qc.reverse_bits()))

qc.cx(0,1)
# print (Operator(qc.reverse_bits()))

# Return a drawing of the circuit using MatPlotLib ("mpl"). This is the
# last line of the cell, so the drawing appears in the cell output.
# Remove the "mpl" argument to get a text drawing.
print (qc.draw())

sv=Statevector([1, 0, 0, 0])
sv=sv.evolve(qc)
print (sv.to_dict())
