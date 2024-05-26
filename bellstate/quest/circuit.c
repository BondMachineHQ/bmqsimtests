#include <stdio.h>
#include <stdlib.h>
#include "QuEST.h"

int main(int narg, char *varg[])
{
	QuESTEnv env = createQuESTEnv();

	Qureg qubits = createQureg(2, env);

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

		pauliX(qubits, 1);
		controlledNot(qubits, 1, 0);
		

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
