#include <iostream>
#include <random>
#include <array>
#include <valarray>
#include <fstream>
#include <cmath>
//Constantes 
const double c = 300;
const double L = 2 ;
const int n = 101;
const double N = 101;
const double dx = L/(N-1);
const double dt = 0.5*dx / c;
const double t_final=0.1; 
const double m = 0.1;
const int nt= (t_final/dt) + 1; 
int main(){
//Posición inicial 
std::array<double, n>uinicial;
for (int i = 0; i<n; i++){
    if(i<=n/2){
        uinicial[i]= i*dx*m;
    }
    else {
        uinicial[i]= -i*dx*m + 0.2;
    }
}
std::ofstream archivo("Posicióninicial.txt");
for (int i = 0; i<n; i++){
    archivo<< i*dx<<", "<< uinicial[i]<<"\n";
}
archivo.close();
std::array<double, n>upasado;
for(int i=0;  i<n; i++){
    upasado[i]=uinicial[i];
}
std::array<double, n>upresente;
upresente[0]= 0;
upresente[n-1]= 0;
for(int i = 1;  i<n-1; i++){
    upresente[i]=upasado[i]+ 0.5*(c*c)*(dt*dt)/(dx*dx)*(upasado[i+1]-2*upasado[i]+ upasado[i-1]);
}
std::ofstream archivo1("SegundaPosición.txt");
for (int i = 0; i<n; i++){
    archivo1<< i*dx<<", "<< upresente[i]<<"\n";
}
archivo1.close();
std::array<double, n>ufuturo;
ufuturo[0]= 0;
ufuturo[n-1]= 0;
std::ofstream archivo2("pos.txt");
for (int i = 0; i<n; i++){
    archivo2<< i*dx<<", ";
}
for (int t = 2; t<11; t++){
    archivo2 <<"\n"<< ufuturo[0]<< ", ";
    for (int i = 1; i<n-1 ; i++){
        ufuturo[i]=2*upresente[i]- upasado[i] + 0.5*(c*c)*(dt*dt)/(dx*dx)* (upresente[i+1]-2*upresente[i]+ upresente[i-1]);
    archivo2 << ufuturo[i]<< ", ";       
    }
    for (int j = 1; j<n-1;j++){
        upasado[j] = upresente[j];
        upresente[j]= ufuturo[j];
    }  
    archivo2 << ufuturo[n-1];
}
archivo2.close();
}
