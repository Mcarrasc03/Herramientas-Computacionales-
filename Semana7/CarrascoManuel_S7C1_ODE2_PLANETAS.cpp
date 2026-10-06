#include <iostream>
#include <random>
#include <array>
#include <valarray>
#include <fstream>
#include <cmath>
//Funciones 
double dvxdt(double x, double y, double m);
double dvydt(double x, double y, double m);
//Constantes
double G = 0.00029591220828;
double M_sol = 1; //Masas solares 
double m_tierra = 0.000003; //Masa solares
//Condiciones iniciales
double x_0 = 0.98329;
double y_0 = 0;
double vx_0 = 0;
double vy_0 = 0.0175;
//Sol
double xs_0 = -(m_tierra/M_sol)*x_0;
double ys_0 = 0;
double vxs_0 = 0;
double vys_0 = -(m_tierra/M_sol)*vy_0;

int main(){
const double N = 366*2;
const int n = 366*2;
const double t_final= 366; // t_0 = 0 
const double h = t_final/(N-1);
std::cout<<"h es igual a "<<h <<"\n";
std::cout<< m_tierra/M_sol <<"\n";
//Euler

// std::array<double, n> ArT;
// for (double i = 0; i<n; i++){
//     ArT[i]=(h*i);
// }
// std::array<double, n> ArVx;
// std::array<double, n> ArX;
// std::array<double, n> ArVy;
// std::array<double, n> ArY;
// ArVx[0]=vx_0;
// ArX[0]=x_0;
// ArVy[0]=vy_0;
// ArY[0]=y_0;
// for (double i = 1; i<n; i++){
//     ArVx[i]=ArVx[i-1] + h*dvxdt(ArX[i-1],ArY[i-1], M_sol);
//     ArX[i]=ArX[i-1] + h*ArVx[i-1]; 

//     ArVy[i]=ArVy[i-1] + h*dvydt(ArX[i-1],ArY[i-1], M_sol);
//     ArY[i]=ArY[i-1] + h*ArVy[i-1]; 
// }
// std::ofstream archivo ("DatosEulerOr.txt");
// for (int i = 0; i<n; i++){
//     archivo<< ArT[i]<<", "<< ArX[i]<< ", "<<ArVx[i]<< ", "<< ArY[i]<< ", "<<ArVy[i]<< "\n";
// }
// archivo.close();

//LeapFrog
std::array<double, 2*n> ArTLF;
for (double i = 0; i<2*n; i++){
    ArTLF[i]=((h/2)*i);
}
//Tierra
std::array<double, n> ArVxLFT;
std::array<double, n> ArXLFT;
std::array<double, n> ArVyLFT;
std::array<double, n> ArYLFT;
ArVxLFT[0]=vx_0+(1/2)*h*dvxdt(x_0, y_0, M_sol);
ArXLFT[0]=x_0;
ArVyLFT[0]=vy_0+(1/2)*h*dvydt(x_0, y_0, M_sol);
ArYLFT[0]=y_0;
//Sol
std::array<double, n> ArVxLFS;
std::array<double, n> ArXLFS;
std::array<double, n> ArVyLFS;
std::array<double, n> ArYLFS;
ArVxLFS[0]=vxs_0+(1/2)*h*dvxdt(-x_0+xs_0, -y_0+ys_0, m_tierra);
ArXLFS[0]=xs_0;
ArVyLFS[0]=vys_0+(1/2)*h*dvydt(-x_0+xs_0, -y_0+ys_0, m_tierra);
ArYLFS[0]=ys_0;

for (double i = 1; i<n; i++){
    ArXLFT[i]=ArXLFT[i-1] + h*ArVxLFT[i-1]; 
    ArYLFT[i]=ArYLFT[i-1] + h*ArVyLFT[i-1]; 
    ArXLFS[i]=ArXLFS[i-1] + h*ArVxLFS[i-1]; 
    ArYLFS[i]=ArYLFS[i-1] + h*ArVyLFS[i-1]; 
    ArVxLFT[i]=ArVxLFT[i-1] + h*dvxdt(ArXLFT[i]-ArXLFS[i], ArYLFT[i]-ArYLFS[i], M_sol);
    ArVyLFT[i]=ArVyLFT[i-1] + h*dvydt(ArXLFT[i]-ArXLFS[i], ArYLFT[i]-ArYLFS[i], M_sol);
    ArVxLFS[i]=ArVxLFS[i-1] + h*dvxdt(-ArXLFT[i]+ArXLFS[i], -ArYLFT[i]+ArYLFS[i], m_tierra);
    ArVyLFS[i]=ArVyLFS[i-1] + h*dvydt(-ArXLFT[i]+ArXLFS[i], -ArYLFT[i]+ArYLFS[i], m_tierra);
}


std::ofstream archivo1 ("DatosLFOr.txt");
for (int i = 0; i<n; i++){
    archivo1<< ArTLF[2*i]<<", "<< ArTLF[(2*i)+1]<<", "<< ArXLFT[i]<<", "<< ArYLFT[i]<<", "<< ArVxLFT[i]<<", "<< ArVyLFT[i]<<", "
    << ArXLFS[i]<<", "<< ArYLFS[i]<<", "<< ArVxLFS[i]<<", "<< ArVyLFS[i]<<"\n";
}
archivo1.close();

return 0;
}
double dvxdt(double x, double y, double m){
    return -(G*m*x) /(std::pow((x*x + y*y), 1.5));
}
double dvydt(double x, double y, double m){
    return -(G*m*y) /(std::pow((x*x + y*y), 1.5));
}