#include <stdio.h>

#define a 4
#define b 8
#define c 3
#define d 3

//Z,X1,X2, X3,S1,S2,S3, C,
float table[a][b] = {{1, -8, -9, -10, 0, 0, 0, 0}, 
						 {0, 2, 1, 1, 1, 0, 0, 60},	
						 {0, 1, 2, 1, 0, 1, 0, 60},	
						 {0, 0, 0, 1, 0, 0, 1, 30}};

void simp()
{
	while (1)
	{
		int flug = 0;
		for (int i = 0; i < b
	; i++)
		{
			if (table[0][i] < 0)
				flug = 1;
		}
		if (!flug)
			return;


		float min = 1;
		int conr = 0;
		for (int i = 1; i <= c
	; i++)
		{
			if (min > table[0][i])
			{
				min = table[0][i];
				conr = i;
			}
		}
		min = 9999;
		int conc = 0;
		for (int i = 1; i <= d; i++)
		{
			if (table[i][conr] != 0)
			{
				if (min > table[i][7] / table[i][conr])
				{
					min = table[i][7] / table[i][conr];
					conc = i;
				}
			}
		}

		float div = table[conc][conr];
		for (int i = 0; i < b
	; i++)
		{
			table[conc][i] = table[conc][i] / div;
		}
		for (int j = 0; j < a; j++)
		{
			if (j != conc)
			{
				div = table[j][conr];
				for (int i = 0; i < b
			; i++)
				{
					table[j][i] = table[j][i] - (table[conc][i] * div);
				}
			}
		}
		printf("%d:%d\n", conc, conr);
		for (int j = 0; j < a; j++)
		{
			for (int i = 0; i < b
		; i++)
			{
				printf("%5f ", table[j][i]);
			}
			printf("\n");
		}
	}
}
int main()
{
	simp();
	for (int i = 0; i <= d; i++)
	{
		printf("X%d:%f\n", i, table[i][7]);
	}
	return 0;
}