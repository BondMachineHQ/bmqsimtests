#include <stdio.h>
#include <stdlib.h>
#include "QuEST.h"

int main(int narg, char *varg[])
{
	QuESTEnv env = createQuESTEnv();

	Qureg qubits = createQureg(3, env);

	FILE *f;

	f = fopen("inputs.txt", "r");
	if (f == NULL)
	{
		printf("Error! Could not open file\n");
		exit(-1);
	}

	float a;
	float b;
	int finished = 0;

	for (;;)
	{
		for (int i = 0; i < qubits.numAmpsTotal; i++)
		{
			fscanf(f, "%f", &a);
			if (feof(f))
			{
				finished = 1;
				break;
			}
			fscanf(f, "%f", &b);
			if (feof(f))
			{
				finished = 1;
				break;
			}
			qubits.stateVec.real[i] = a;
			qubits.stateVec.imag[i] = b;
		}

		if (finished == 1)
			break;

		rotateY(qubits, 0, 6.058874649156427);
rotateY(qubits, 2, 0.09033267550125064);
controlledNot(qubits, 1, 2);
controlledPhaseFlip(qubits, 1, 2);
pauliX(qubits, 1);
pauliZ(qubits, 0);
pauliX(qubits, 2);
controlledNot(qubits, 2, 0);
rotateY(qubits, 1, 1.7006899709461898);
rotateX(qubits, 0, 0.5684065076559722);
rotateZ(qubits, 0, 3.2426168414219103);
pauliZ(qubits, 2);
rotateZ(qubits, 2, 4.662294893676382);
hadamard(qubits, 2);
pauliY(qubits, 0);
rotateX(qubits, 0, 3.306632513672049);
hadamard(qubits, 2);
pauliX(qubits, 1);
pauliY(qubits, 1);
controlledNot(qubits, 2, 0);
rotateZ(qubits, 2, 1.1451833503962476);
rotateZ(qubits, 0, 3.310722711576425);
hadamard(qubits, 0);
pauliX(qubits, 1);
controlledNot(qubits, 2, 0);
controlledNot(qubits, 0, 2);
pauliZ(qubits, 2);
pauliZ(qubits, 2);
rotateY(qubits, 2, 0.6309999791195642);
rotateX(qubits, 2, 4.563646154967166);
rotateX(qubits, 1, 2.2576110840133605);
rotateZ(qubits, 2, 3.3566199610903515);
rotateY(qubits, 2, 3.5204479951105467);
controlledNot(qubits, 1, 2);
rotateY(qubits, 1, 4.877513333267503);
pauliZ(qubits, 2);
controlledPhaseFlip(qubits, 2, 1);
rotateY(qubits, 1, 4.859177850793288);
pauliX(qubits, 2);
pauliY(qubits, 2);
controlledNot(qubits, 2, 1);
rotateY(qubits, 1, 4.540325181428698);
controlledPhaseFlip(qubits, 1, 2);
controlledNot(qubits, 0, 1);
controlledPhaseFlip(qubits, 0, 2);
rotateX(qubits, 2, 5.358896856469312);
pauliY(qubits, 2);
rotateY(qubits, 1, 2.1730653355344893);
rotateY(qubits, 2, 6.192963939541379);
rotateY(qubits, 0, 1.2253626109824007);


		for (int i = 0 ; i < qubits.numAmpsTotal; i++)
		{
			printf("%.16f\n", qubits.stateVec.real[i]);
			printf("%.16f\n", qubits.stateVec.imag[i]);
		}

		if (feof(f))
			break;
	}

	destroyQureg(qubits, env);
	destroyQuESTEnv(env);
}
