#include <cmath>
#include <iostream>
#include <fstream>
using namespace std;
int const N = 4;
void Matr(int A[][N], int n)
{
    float w0[N], w[N], summ = 0, w0norm[N], e, d, d0;
    int i, j, k;
    for (i = 0; i < n; i++)
        w0[i] = 0;
    w0[0] = 1;
    do
    {
        for (i = 0; i < n; i++)
            summ = summ + w0[i] * w0[i];
        d0 = sqrt(summ);
        for (i = 0; i < n; i++)
            w0norm[i] = w0[i] / d0;
        for (i = 0; i < n; i++)
        {
            w[i] = 0;
            for (j = 0; j < n; j++)
                w[i] = w[i] + A[i][j] * w0norm[j];
        }
        summ = 0;
        for (i = 0; i < n; i++)
            summ = summ + w[i] * w[i];
        d = sqrt(summ);
        e = fabs(d - d0);
        for (i = 0; i < n; i++)
            w0[i] = w[i];
        summ = 0;
    } while (e > 0.0000000000001);
    std::cout << "\nMatrix:\n";
    for (i = 0; i < n; i++) {

        std::cout << " = " << w0norm[i] << std::endl;
    }
    std::cout << "\nL = " << d << std::endl;
}

int main()
{
    ifstream myfile;
    int n, A[N][N];
    myfile.open("C:\\Users\\HP\\Desktop\\Politeh\\Чисельні методи\\input2.txt");
    myfile >> n;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            myfile >> A[i][j];
            cout << A[i][j] << " ";
        }
        cout << endl;
    }
    myfile.close();
    //std::cout << "Enter N = ";
    //std::cin >> n;
    //Input(n, A);
    Matr(A, n);

    std::cin.get();
    std::cin.get();
    return 0;
}
