#include <iostream>
#include <random>
#include <array>
#include <valarray>
#include <fstream>
//Constantes
double k = 50; //N/m
double m = 0.2; //kg 
double b = 0.8;
//Condiciones iniciales
double x_0 = 0.1; //m
double v_0 = 0.0; //m/s

double funciondd(double x);
double funcionddf(double x, double v);
double funcionddfX(double v);
int main(){
//Euler
const double N = 6001;
const int n = 6001;

const double t_final= 2; // t_0 = 0 
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

Luego de investgar, esta implementación se llama Euler-Cromer, una versión de Euler que no 
diverje. 
Abajo si esta la implementación de euler normal
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
std::cout<< "Archivo con datos de Euler creado en \"DatosEuler.txt\""<< "\n";
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
std::cout<< "Archivo con datos de Leap Frog creado en \"DatosLF.txt\""<< "\n";
//----------------------------------------------------------------------------------------
//Fricción
 
//Euler Fricción 
std::array<double, n> ArVFRIC;
std::array<double, n> ArXFRIC;
ArVFRIC[0]=v_0;
ArXFRIC[0]=x_0;

for (double i = 1; i<n; i++){
    ArVFRIC[i]=ArVFRIC[i-1] + h*funcionddf(ArXFRIC[i-1], ArVFRIC[i-1]);
    ArXFRIC[i]=ArXFRIC[i-1] + h*ArVFRIC[i-1]; 
}
std::ofstream archivoF ("DatosEulerFric.txt");
for (int i = 0; i<n; i++){
    archivoF<< ArT[i]<<", "<< ArXFRIC[i]<< ", "<<ArVFRIC[i]<< "\n";
}
archivoF.close();
std::cout<< "Archivo con datos de Euler con fricción creado en \"DatosEulerFric.txt\""<< "\n";

//RK fricción 
std::array<double, n> ArXRK;
std::array<double, n> ArVRK;
ArXRK[0]=0.1;
ArVRK[0]=0;
for (double i = 1; i<n; i++){
    double x_prev = ArXRK[i - 1];
    double v_prev = ArVRK[i - 1];
    
    double kx1 = h*funcionddfX(v_prev);
    double kx2 = h*funcionddfX(v_prev + (kx1)/2);
    double kx3 = h*funcionddfX(v_prev+ (kx2)/2);
    double kx4 = h*funcionddfX(v_prev+ (kx3));
    
    double kv1 = h*funcionddf(x_prev, v_prev);
    double kv2 = h*funcionddf(x_prev + (kx1)/2, v_prev + (kv1)/2);
    double kv3 = h*funcionddf(x_prev + (kx2)/2, v_prev + (kv2)/2);
    double kv4 = h*funcionddf(x_prev + (kx3), v_prev + (kv3));
    ArVRK[i]= v_prev + (kv1 + 2.0 * kv2 + 2.0 * kv3 + kv4) / 6.0;
    ArXRK[i]= x_prev + (kx1 + 2.0 * kx2 + 2.0 * kx3 + kx4) / 6.0;
}
std::ofstream archivo2 ("DatosRK4Fric.txt");
for (int i = 0; i<n; i++){
    archivo2<< ArT[i]<<", "<< ArXRK[i]<<", "<< ArVRK[i]<<"\n";
}
archivo2.close();
std::cout<< "Archivo con datos de Runge Kutta con fricción creado en \"DatosRK4Fric.txt\""<< "\n";
return 0;
}
double funciondd(double x){
    return -(k/m)*x;
}
double funcionddf(double x, double v){
    return -(k/m)*x - b*v;
}
double funcionddfX(double v){
    return v;
}