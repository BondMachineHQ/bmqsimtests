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

		controlledNot(qubits, 2, 0);
rotateZ(qubits, 0, 0.31109400916672314);
rotateY(qubits, 2, 4.088097603329812);
controlledNot(qubits, 1, 0);
hadamard(qubits, 1);
controlledPhaseFlip(qubits, 2, 1);
rotateX(qubits, 1, 0.7125486369232711);
hadamard(qubits, 2);
hadamard(qubits, 0);
rotateZ(qubits, 2, 2.9685518997769216);
hadamard(qubits, 2);
hadamard(qubits, 0);
rotateX(qubits, 0, 5.35415754548599);
rotateZ(qubits, 1, 3.7470647842054112);
rotateZ(qubits, 1, 3.7693783925451876);
pauliZ(qubits, 0);
pauliZ(qubits, 2);
controlledNot(qubits, 1, 2);
rotateX(qubits, 0, 5.138289253083489);
controlledNot(qubits, 2, 1);
pauliX(qubits, 0);
rotateX(qubits, 1, 2.462074938753762);
controlledPhaseFlip(qubits, 0, 1);
controlledPhaseFlip(qubits, 1, 2);
rotateX(qubits, 1, 0.2827025860612343);
controlledPhaseFlip(qubits, 1, 2);
rotateY(qubits, 0, 2.131948830535125);
rotateY(qubits, 1, 6.243854397463626);
pauliZ(qubits, 1);
rotateY(qubits, 2, 6.242549315047099);
controlledPhaseFlip(qubits, 1, 0);
controlledPhaseFlip(qubits, 0, 1);
pauliX(qubits, 2);
hadamard(qubits, 0);
rotateX(qubits, 1, 1.8334058932670556);
rotateZ(qubits, 0, 1.6586026145730146);
pauliY(qubits, 2);
rotateY(qubits, 0, 1.2139126046858053);
rotateY(qubits, 1, 3.520786813265278);
rotateX(qubits, 2, 0.9332390603208457);
pauliX(qubits, 1);
pauliY(qubits, 2);
rotateZ(qubits, 2, 2.7688502758899287);
controlledNot(qubits, 1, 0);
rotateY(qubits, 0, 0.752399258956447);
pauliX(qubits, 2);
rotateX(qubits, 2, 0.15919099347969246);
rotateZ(qubits, 0, 1.3169538220273753);
controlledNot(qubits, 2, 1);
pauliX(qubits, 2);


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
