#include <iostream>
#include <fstream>
#include <array>
//Constantes
const double Nx = 10; 
const int nx = 10; 
const double L = 1;
const double dx = L/(Nx-1);
const double nu = 0.01; 
const double t_final = 2500;
const double dt = (0.2*(dx*dx))/nu;
const int nt = (t_final/dt) +1; 
const double Nt = (t_final/dt) +1; 

int main(){
std::cout<<dx<<"\n";
    /*    
std::array<std::array<double, nx>,nx> Minicial;
for (int i = 0; i<nx; i++){
    for (int j=0; j<nx; j++){
        Minicial[i][j]= 50;
    }
}
for (int i = 0; i<nx; i++){
    for (int j=0; j<nx; j++){
        Minicial[i][j]= 50;
    }
}
for (int i = 0; i<nx; i++){
    for (int j=0; j<nx; j++){
        std::cout<< Minicial[i][j]<<" ";
    }
    std::cout<<"\n";
}   
    */
}