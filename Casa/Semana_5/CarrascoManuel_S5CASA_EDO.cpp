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
/*Me toco crear estas dos por aparte porque si dejo solo int al sacar el 
h =double/int trunco a entero entonces daba 0(no se por que pasa porque en el ejercicio S5C1 de repaso de c++
el primero fue dividir un float con un int y aun asi ese si me daba decimal, en este caso probe con double y float y en
ambos los ponia como 0 entero, no el decimal, ni si quiera haciendo n como 21, lo que daba un h de 0.1, lo dejaba como 0).
Ademas doble o el float no lo puedo poner en el tamaño de los arreglos, por eso esta n y N iguales solo que diferentes tipos
de datos
*/
std::array<double, n> ArT;
const double t_final= 2; // t_0 = 0 
const double h = 2/(N-1);
std::cout<<"h es igual a "<<h <<"\n";
std::array<double, n> ArY;
for (double i = 0; i<n; i++){
    ArT[i]=(h*i);
}
ArY[0]=1;
for (double i = 1; i<n; i++){
    ArY[i]=ArY[i-1]- h*ArY[i-1];
}

std::ofstream archivo ("DatosEuler.txt");
for (int i = 0; i<n; i++){
    archivo<< ArT[i]<<", "<< ArY[i]<< "\n";
}
archivo.close();

//Método Runge Kutta 4
std::array<double, n> ArYRK;
ArYRK[0]=1;
for (double i = 1; i<n; i++){
    double y_prev = ArYRK[i - 1];
    double k1 = -h * y_prev;
    double k2 = -h * (y_prev + k1 / 2.0);
    double k3 = -h * (y_prev + k2 / 2.0);
    double k4 = -h * (y_prev + k3);
    ArYRK[i]= y_prev + (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0;
}
std::ofstream archivo1 ("DatosRK4.txt");
for (int i = 0; i<n; i++){
    archivo1<< ArT[i]<<", "<< ArYRK[i]<< "\n";
}
archivo1.close();
std::cout<<"Para el segundo punto (revisar el comportamiento del error en función de intevalo h), "
<<"se usó otro código llamado\n'Errores_CarrascoManuel_S5C2.cpp' con un for para ver muchos valores de h. "
<<"En este se sumó el error en cada punto evaluado y se dividió en los puntos evaluados para tener un error promedio"
<<" y este se grafica en función de la cantidad de puntos tomados para ese error.\n";
return 0;
}
