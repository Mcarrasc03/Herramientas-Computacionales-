#include <iostream>
#include <random>
#include <array>
#include <valarray>
#include <fstream>
//double funcion(t);
int main(){
//Euler
const double N = 2001;
const int n = 2001;
//Me toco crear estas dos por aparte porque si dejo solo int al sacar el h =double/int trunco todo a 0, 
//pero como doble no lo puedo poner en los arreglos, por eso esta n y N iguales solo que diferentes tipos
std::array<double, n> ArT;
const double t_final= 2; // t_0 = 0 
const double h = 2/(N-1);
std::cout<<"h es igual a "<<h <<"\n";
std::array<double, n> ArY;
for (double i = 0; i<n; i++){
    ArT[i]=(h*i);
}
ArY[0]=1;
for (double i = 1; i<N; i++){
    ArY[i]=ArY[i-1]- h*ArY[i-1];
}
std::cout<< "\n";
std::ofstream archivo ("Prueba.txt");
for (int i = 0; i<N; i++){
    archivo<< ArT[i]<<", "<< ArY[i]<< "\n";
}
archivo.close();
return 0;
//Me demore mucho en esto por lo que el h me daba 0 por la division entera :( ---> 10:38 empezando RK4
// std::array<double, n> ArYRK;
// double k1;
// double k2;
// double k3;
// double k4;
// for (double i = 0; i<n; i++){
//     k1= h*ArYRK[i-1]
//     ArYRK[i]=ArYRK[i-1] + (1/6)*(k1+2*k2+2*k3+k4);
// }
}