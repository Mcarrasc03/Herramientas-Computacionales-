#include <iostream>
#include <random>
#include <array>
#include <valarray>
#include <fstream>
#include <cmath>
//Funciones 
double dvxdt(double x, double y);
double dvydt(double x, double y);
//Constantes
double G = 0.00029591220828;
double M_sol = 1; //Masas solares 
double m_tierra = 0.000003; //Masa solares
double r = 1; //UA
//Condiciones iniciales
double x_0 = 1;
double y_0 = 0;
double vx_0 = 0;
double vy_0 = 0.017211;
//Sol
double xs_0 = 0;
double ys_0 = 0;
double vxs_0 = 0;
double vys_0 = 0;

int main(){
//Euler
const double N = 5001;
const int n = 5001;

const double t_final= 365; // t_0 = 0 
const double h = t_final/(N-1);
std::cout<<"h es igual a "<<h <<"\n";
std::array<double, n> ArT;
for (double i = 0; i<n; i++){
    ArT[i]=(h*i);
}
std::array<double, n> ArVx;
std::array<double, n> ArX;
std::array<double, n> ArVy;
std::array<double, n> ArY;
ArVx[0]=vx_0;
ArX[0]=x_0;
ArVy[0]=vy_0;
ArY[0]=y_0;
for (double i = 1; i<n; i++){
    ArVx[i]=ArVx[i-1] + h*dvxdt(ArX[i-1],ArY[i-1]);
    ArX[i]=ArX[i-1] + h*ArVx[i-1]; 

    ArVy[i]=ArVy[i-1] + h*dvydt(ArX[i-1],ArY[i-1]);
    ArY[i]=ArY[i-1] + h*ArVy[i-1]; 
}
std::ofstream archivo ("DatosEulerOr.txt");
for (int i = 0; i<n; i++){
    archivo<< ArT[i]<<", "<< ArX[i]<< ", "<<ArVx[i]<< ", "<< ArY[i]<< ", "<<ArVy[i]<< "\n";
}
archivo.close();
return 0;
}
double dvxdt(double x, double y){
    return -(G*M_sol*x) /(std::pow((x*x + y*y), 1.5));
}
double dvydt(double x, double y){
    return -(G*M_sol*y) /(std::pow((x*x + y*y), 1.5));
}