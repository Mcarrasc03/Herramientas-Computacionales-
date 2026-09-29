#include <iostream>
#include <vector>
#include <array>
#include <fstream>
#include <cmath>

int main() {
    std::array<double, 1000> ErrorPEu;
    std::array<double, 1000> ErrorPRK;

for (int j = 0; j < 1000; j++) {
    int nr = 21 + j * 20;
    double Nr = static_cast<double>(nr);
       
    const double t_final = 2.0; 
    double h = t_final / (Nr - 1.0);

    std::vector<double> ArT(nr);
    for (int i = 0; i < nr; i++) {
        ArT[i] = h * i;
    }

//Euler
    std::vector<double> ArY(nr);
    ArY[0] = 1.0;
    for (int i = 1; i < nr; i++) {
        ArY[i] = ArY[i - 1] - h * ArY[i - 1];
    }
    std::vector<double> ErrEu(nr);
    double sumaEu = 0.0;
    for (int i = 1; i < nr; i++) {
        ErrEu[i] = std::abs(ArY[i] - std::exp(-ArT[i]));
        sumaEu += ErrEu[i];
    }
    ErrorPEu[j] = sumaEu / Nr;
//RungeKutta
    std::vector<double> ArYRK(nr);
    ArYRK[0] = 1.0;
    std::vector<double> ErrRK(nr);
    double sumaRK = 0.0;
    for (int i = 1; i < nr; i++) {
        double y_prev = ArYRK[i - 1];
        double k1 = -h * y_prev;
        double k2 = -h * (y_prev + k1 / 2.0);
        double k3 = -h * (y_prev + k2 / 2.0);
        double k4 = -h * (y_prev + k3);
        double y_n= y_prev + (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0;
        ArYRK[i] = y_n;
        ErrRK[i] = std::abs(std::exp(-ArT[i])-y_n);
        sumaRK += ErrRK[i];        
    }
    ErrorPRK[j] = sumaRK / Nr;
}

    std::ofstream archivo("ErroresEDO.txt");
    for (int i = 0; i < 1000; i++) {
        archivo << 21 + (i * 20) << ", " << ErrorPEu[i] << ", " << ErrorPRK[i] << "\n";
    }
    archivo.close();
    return 0;
}