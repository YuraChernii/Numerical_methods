#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <fstream>
#include <iostream>
#include <iostream>     // std::cout, std::fixed
#include <iomanip>

#define N 4

using namespace std;
double A[N][N];
double F[N];
double U[N][N] = { 0 };
double V[N][N] = { 0 };
double L[N] = { 0 };
double temp[N];
double H[N];
double myvector[N];




double scalar(double* a, double* b) {
    double P = 0;
    for (int j = 0; j < N; j++) {
        P += a[j] * b[j];
    }
    return P;
}

int main() {
    setlocale(LC_ALL, "RUS");
    ifstream in("matr1.txt");
    if (in.is_open())
    {
        int count = 0;
        int temp;

        while (!in.eof())
        {
            in >> temp;
            count++;
        }
        in.seekg(0, ios::beg);
        in.clear();


        int count_space = 0;
        char symbol;
        while (!in.eof())
        {

            in.get(symbol);
            if (symbol == ' ') count_space++;
            if (symbol == '\n') break;
        }

        in.seekg(0, ios::beg);
        in.clear();


        int n = count / (count_space + 1);
        int m = count_space + 1;
        double** x;
        x = new double* [n];
        for (int i = 0; i < n; i++) x[i] = new double[m];


        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++) {

                if (j == m-1) {
                    in >> F[i];
                }
                else{ in >> A[i][j]; }

            }

        cout << "Матриця A:" << endl;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                cout << A[i][j] << "  ";
            }
            cout << endl;
        }

        cout << "\nВектор F:" << endl;
        for (int l = 0; l < N; l++) {
            cout << F[l] << endl;
        }
        cout << endl;

        for (int i = 0; i < n; i++) delete[] x[i];
        delete[] x;

        in.close();
    }
    else
    {

        cout << "Файл не найдений.";
    }

    int count = 1;
    int n = 0;
    double t;
    double T[N];
    for (int i = 0; i < N; i++) {
        U[0][i] = (A[0][i]);
    }
    L[0] = sqrt(scalar(U[0], U[0]));
    for (int i = 0; i < N; i++) {
        V[0][i] = U[0][i] * (1 / L[0]);
    }

    T[0] = F[0] / L[0];

    do {
        double temp_h;
        temp_h = 0;

        for (int i = 0; i < N; i++) {
            temp[i] = 0;
        }

        for (int j = 0; j <= count - 1; j++) {
            t = scalar(A[count], V[j]);

            for (int i = 0; i < N; i++) {
                temp[i] = temp[i] + (t * V[j][i]);

            }
            temp_h += t * T[j];
        }

        for (int i = 0; i < N; i++) {
            U[count][i] = A[count][i] - temp[i];
        }


        L[count] = sqrt(scalar(U[count], U[count]));


        T[count] = (F[count] - temp_h) / (L[count]);


        for (int i = 0; i < N; i++) {
            V[count][i] = (1 / L[count]) * (U[count][i]);
        }

        n++;
        count++;

    } while (count < N);


    cout << "\n\n";

    double x = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            x += V[j][i] * T[j];
        }
        cout << "X_" << i + 1 << " = " << x << endl;
        myvector[i] = x;
        x = 0;
    }

    fstream f;
    f.open("matr1(res).txt", fstream::in | fstream::out);

    x = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            x += V[j][i] * T[j];
        }
        f << std::setprecision(9) << "X_" << i + 1 << " = " << x << endl;
        x = 0;
    }

    cout << "Матриця A:" << endl;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cout << A[i][j] << "  ";
        }
        cout << endl;
    }

    double* res_vector;
    res_vector = new double[N];
    double* res_vector2;
    res_vector2 = new double[N];
    for (int i = 0; i < N; ++i)
        res_vector[i] = 0;
    std::cout << "Result: " << std::endl;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j)
            res_vector[i] += A[i][j] * myvector[j];
        res_vector2[i] = abs(res_vector[i] - F[i]);
        std::cout << std::setprecision(100)<< res_vector2[i] << ' ';
    }
    double sum = 0;
    for (int i = 0; i < N; ++i) {
        sum += pow((res_vector2[i]),double(2));
    }
    f <<endl<<"Похибка: "<< std::setprecision(100) << sqrt(sum) << endl;
    std::cout << endl << std::setprecision(100) << sqrt(sum) << endl;

    delete[] res_vector;

    const double EPS = 1E-9;
    n = N;

        double det = 1;
    for (int i = 0; i < n; ++i) {
        int k = i;
        for (int j = i + 1; j < n; ++j)
            if (abs(A[j][i]) > abs(A[k][i]))
                k = j;
        if (abs(A[k][i]) < EPS) {
            det = 0;
            break;
        }
        swap(A[i], A[k]);
        if (i != k)
            det = -det;
        det *= A[i][i];
        for (int j = i + 1; j < n; ++j)
            A[i][j] /= A[i][i];
        for (int j = 0; j < n; ++j)
            if (j != i && abs(A[j][i]) > EPS)
                for (int k = i + 1; k < n; ++k)
                    A[j][k] -= A[i][k] * A[j][i];
    }
    f << "det: " << det;
    cout <<endl<<"det: "<< det;

    f.close();

    return 0;
}

//Результати:
//1)
//X_1 = 0.2016675088428498963111223929445259273052215576171875
//X_2 = 0.4372662961091460243068240743014030158519744873046875
//X_3 = -0.07589691763516927258681477042046026326715946197509765625
//X_4 = -0.06399696816574028390700590307460515759885311126708984375

//Похибка: 9.93013661298909247077783098936529308821950269570155711562620126642286777496337890625e-16
//det: 316639.9999999999417923390865325927734375
//2)
//X_1 = 0.1942446043165467484126196495708427391946315765380859375
//X_2 = 0.2122302158273381422759484848938882350921630859375
//X_3 = -0.125899280575539618265423769116750918328762054443359375

//Похибка: 9.48574968053509423469206089723897753902996719636842026801559768500737845897674560546875e-16
//det: -3892.00000000000045474735088646411895751953125
//3)
//X_1 = 1.0000000000000002220446049250313080847263336181640625
//X_2 = 1
//X_3 = 1

//Похибка: 3.7682219008410598084868777145595696051084294055100176734640626818872988224029541015625e-15
//det: 369

