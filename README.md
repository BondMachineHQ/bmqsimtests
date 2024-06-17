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



## TODO `config.py` parameters

## Supported simulators

- ### qiskit

- ### quest

- ### pennylane

- ### bmqsim

- ### spinq

## Special case: the random circuit folder

The folder `random` contains a random quantum circuit generator. Refer to the README.md file in the folder for more information.