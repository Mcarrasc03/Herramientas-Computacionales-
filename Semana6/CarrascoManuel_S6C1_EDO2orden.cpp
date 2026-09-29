#include <iostream>
#include <random>
#include <array>
#include <valarray>
#include <fstream>
//Constantes
double k = 50; //N/m
double m = 0.2; //kg 
//Condiciones iniciales
double x_0 = 0.1; //m
double v_0 = 0.0; //m/s

double funciondd(double x);
int main(){
//Euler
const double N = 2001;
const int n = 2001;

const double t_final= 5; // t_0 = 0 
const double h = t_final/(N-1);
std::cout<<"h es igual a "<<h <<"\n";
std::array<double, n> ArT;
for (double i = 0; i<n; i++){
    ArT[i]=(h*i);
}
std::array<double, n> ArV;
std::array<double, n> ArX;
ArV[0]=v_0;
ArX[0]=x_0;
/* Con esto salieron los datos EulerCurioso, una implementación ENtre leapFrog Y euler que da bien pero no deberia
La profe me dijo dejalo por curiosidad, esta fue la implementación 
for (double i = 1; i<n; i++){
    ArV[i]=ArV[i-1] + h*funciondd(ArX[i-1]);
    ArX[i]=ArX[i-1] + h*ArV[i]; 
}
*/
for (double i = 1; i<n; i++){
    ArV[i]=ArV[i-1] + h*funciondd(ArX[i-1]);
    ArX[i]=ArX[i-1] + h*ArV[i-1]; 
}
std::ofstream archivo ("DatosEuler.txt");
for (int i = 0; i<n; i++){
    archivo<< ArT[i]<<", "<< ArX[i]<< ", "<<ArV[i]<< "\n";
}
archivo.close();
// Leap Frog
std::array<double, 2*n> ArTLF;
for (double i = 0; i<2*n; i++){
    //double paso = h/2;
    ArTLF[i]=((h/2)*i);
}
std::array<double, n> ArVLF;
std::array<double, n> ArXLF;
ArVLF[0]=v_0+(1/2)*h*funciondd(x_0);
ArXLF[0]=x_0;
for (double i = 1; i<n; i++){
    ArXLF[i]=ArXLF[i-1] + h*ArVLF[i-1]; 
    ArVLF[i]=ArVLF[i-1] + h*funciondd(ArXLF[i]);
}
std::ofstream archivo1 ("DatosLF.txt");
for (int i = 0; i<n; i++){
    archivo1<< ArTLF[2*i]<<", "<< ArXLF[i]<<", "<< ArTLF[(2*i)+1]<< ", "<< ArVLF[i]<<"\n";
}
archivo1.close();
return 0;
}
double funciondd(double x){
    return -(k/m)*x;
}