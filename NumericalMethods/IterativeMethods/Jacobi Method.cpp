#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <fstream>
#include <iostream>
#include <iostream>
#include <iomanip>
#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

int main()
{
	const int n = 4;
	int size;
	ifstream myfile;

	long double a[n][n + 1];

	myfile.open("C:\\Users\\HP\\Desktop\\Politeh\\Чисельні методи\\input2.txt");
	myfile >> size;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n + 1; j++) {
			myfile >> a[i][j];
			cout << a[i][j] << " ";
		}
		cout << endl;
	}
	myfile.close();
	cout << endl;
	int sum;
	sum = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			sum += fabs(a[i][j]);
		}
		if (fabs(2 * a[i][i]) < fabs(sum)) {
			cout << "The matrix has no a diagonal advantage";
			return 1;
		}
		sum = 0;
	}
	cout << "The matrix has a diagonal advantage" << endl;
	long double eps;
	cout << "Enter eps:";
	cin >> eps;
	long double l[n][n];


		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				l[i][j] = 0;
			}
		}
	for (int i = n - 2; i >= 0; i--) {
		for (int j = n - 1; j > i; j--) {
			l[i][j] = a[i][j];
		}
	}
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			if (j < i) {
				l[i][j] = a[i][j];
			}
		}
	}
	long double diagonalna[n][n];
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			diagonalna[i][j] = 0;
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			diagonalna[i][i] = 1 / a[i][i];//обернена
		}
	}
	long double c[n][n];
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			c[i][j] = 0;
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < n; k++)
			{
				c[i][j] += -(diagonalna[i][k] * l[k][j]);
			}
		}
	}
	long double q;
	long double max_q;
	max_q = 0;
	for (int i = 0; i < n; i++) {
		q = 0;
		for (int j = 0; j < n; j++) {
			q += fabs(c[i][j]);
		}
		if (q <= 1) {
			if (q > max_q) {
				max_q = q;
			}
		}
		if (max_q > 1) {
			cout << "No result" << endl;
			return 2;
		}
	}

		long double b[n][n];
	long double x0[n][n];
	long double x[n][n];
	for (int i = 0; i < n; i++) {
		b[i][0] = diagonalna[i][i] * a[i][n];
	}
	long double norma;
	long double tempx[n][n], normatemp[n][n];
	int counter, t;
	norma = 0;
	counter = 0;
	t=1;
	if (t == 0) {
		for (int i = 0; i < n; i++) {
			tempx[i][0] = b[i][0];
		}
	}
	else {
		cout << "Okay, enter x0(" << n << " elements)" << endl;
		for (int i = 0; i < n; i++) {
			cin >> tempx[i][0];
		}
	}
	if (max_q = 1) {
		do {
			norma = 0;
			for (int i = 0; i < n; i++) {
				x[i][0] = 0;
				for (int k = 0; k < n; k++) {
					x[i][0] += c[i][k] * tempx[k][0];
				}
				x[i][0] += b[i][0];
				norma += (x[i][0] - tempx[i][0]) * (x[i][0] -
					tempx[i][0]);
			}
			for (int i = 0; i < n; i++) {
				tempx[i][0] = x[i][0];
			}
			counter++;
		} while (sqrt(norma) > eps);
	}
	else {
		do {
			norma = 0;
			for (int i = 0; i < n; i++) {
				x[i][0] = 0;
				for (int k = 0; k < n; k++) {
					x[i][0] += c[i][k] * tempx[k][0];
				}
				x[i][0] += b[i][0];
				norma += (x[i][0] - tempx[i][0]) * (x[i][0] -
					tempx[i][0]);
			}
			for (int i = 0; i < n; i++) {
				tempx[i][0] = x[i][0];
			}
			counter++;
		}

			while (sqrt(norma) > eps * (max_q) / (1 - max_q));
	}

	for (int i = 0; i < n; i++) {
		cout << "x" << i + 1 << "= " << x[i][0] << endl;
	}
	fstream f;

	f.open("C:\\Users\\HP\\Desktop\\Politeh\\Чисельні методи\\rez3.txt", fstream::in | fstream::out);
	for (int i = 0; i < n; i++) {
		f << std::setprecision(100)<< "x" << i + 1 << "= " << x[i][0] << endl;
	}

	return 0;
}
