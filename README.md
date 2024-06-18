# bmqsimtest

This is a test repository for the bmqsim package. It contains examples of quantum circuits that can be simulated using the bmqsim package and compared with the results of others quantum simulators.
The repository is organized as follows:

Each folder (**circuit folder**) contains a specific example of a quantum circuit. For example, the folder `bellstate` contains the quantum circuit that generates a Bell state. It also contains subfolders (**simulator subfolder**) each containing the implementation of that quantum circuit in a specific quantum programming language and/or quantum simulator. So for example, the folder `bellstate/qiskit` contains the implementation of the Bell state quantum circuit using the Qiskit library.

## Organization of the circuit folders

A file README.md that explains the quantum circuit is present in each circuit folder.
All the circuit folders share a jupyter notebook called `analyze.ipynb` that compares the results of the simulation of the quantum circuit using the different quantum simulators present in the simulator subfolders.
The `analyze.ipynb` file is a symbolic link to the file `analyze.ipynb` in the root folder of the repository.
The `analyze.ipynb` reads the configuration parameters from the file `config.py` in circuit folder. See the section **`config.py` parameters** for more information.

## Organization of the simulator subfolders

 For each simulator the inputs for the quantum circuit, stored in a file called `inputs.json` or `inputs.txt` are present. Similarly, the expected results of the simulation of the quantum circuit using the specific quantum simulator are stored in a file called `outputs.json` or `outputs.txt`.
 The other files in the simulator subfolder are the specific to the quantum programming language or quantum simulator used to implement the quantum circuit, see the section `Supported simulators` for more information.
 This directory can also contain an additional `config.py` file that contains the configuration parameters for the specific quantum simulator whose parameters are appended to the global configuration parameters in the `config.py` file in the circuit folder. 
 ## TODO parametrize the `config.py` file in the simulator subfolder
## TODO active, base

To fully understand the predictive operation of the bmqsim package and other available simulators, it is essential to compare the quantum states obtained with those generated by a reference simulator, in this case qiskit, referred to as the "base".

Within each subrepository, such as `Xgate/quest`, there is a text file called `active` (e.g., `xgate/quest/active`). This file is essential for the specific simulator, in this case `quest`, to be taken into account when comparing the vatious simulators.

If the `active` file is not in a subrepository, the related quantum simulator will not be used and therefore will not generate any results.(For more details, refer to the `analyze.ipynb` file in the root repository.)

In the case of the `qiskit` subrepository (`xgate/qiskit`) both the `active` file and the `base` file are present. As mentioned, the idea is to make comparisons between various simulation technologies, using qiskit as a reference.

The results generated by any simulator other than `qiskit` must match those of qiskit within a certain margin of error. If the results match within this margin, the test is considered passed; otherwise, the test fails.

## TODO `config.py` parameters

Within each subfolder of the simulator is the `config.py` file. This file is read by the `analyze.ipynb` notebook, which extracts the parameters needed to implement the quantum circuits.

Regardless of the mode of operation, there are four parameters that are always used:
- **qbits**: indicates the number of qubits that make up the circuit.
- **passthreshold**: comparison threshold between the states generated by the active simulators and the reference one (qiskit).
- **quiet**: sets the verbosity of the process.
- **useprob**: if set to True, the probability coefficients (amplitudes) of the states produced by the various quantum simulators are calculated.

Depending on the values of certain **parameters**, the code in the `analyze.ipynb` file behaves differently. There are three modes of operation:
- 1) `fundamental` = False:
     - in this case, the `numiter` and `staticdata` parameters are ignored.
     - The initial state is always the fundamental. An `inputs.txt/inputs.json` file is created with the data     forming a fundamental vector (e.g., for 2 qubits, the state is |1000>).

- 2) `fundamental` = False and `staticdata` = True:
     - The circuit starts from a generic state formed by the values given in the `inputs.txt/inputs.json` files.
     - This state is a linear combination of the base of qubits (e.g., `A|01> + B|10>`, with A and B complex numbers).

- 3) `fundamental` = False and `staticdata` = False:
     - The parameter numiter is used.
     - In this case, as many generic states are generated as are indicated by the `numiter parameter` (for example, if `numiter=100`, 100 possible vectors will be created and the predetermined circuit will be executed for each).



## Supported simulators

- ### qiskit

- ### quest

- ### pennylane

- ### bmqsim

- ### spinq

## Special case: the random circuit folder

The folder `random` contains a random quantum circuit generator. Refer to the README.md file in the folder for more information.
