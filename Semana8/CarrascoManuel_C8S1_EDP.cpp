#include <iostream>
#include <fstream>
#include <cmath>
#include <array>
//Constantes
const double N = 101;
const int n = 101;
const double L = 2;
const double c = 300;
const double dx = L/(N-1);
const double dt1 = 0.5*dx/c;
const double dt2 = 3*dx/c;
const double t_final = 0.1;
const double m = 0.1;
const int nt1= (t_final/dt1) + 1; 
const int nt2= (t_final/dt2) + 1; 
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

std::array<double, n>upasado;
for(int i=0;  i<n; i++){
    upasado[i]=uinicial[i];
}
std::array<double, n>upresente;
upresente[0]= 0;
upresente[n-1]= 0;
for(int i = 1;  i<n-1; i++){
    upresente[i]=upasado[i]+ 0.5*(c*c)*(dt1*dt1)/(dx*dx)*(upasado[i+1]-2*upasado[i]+ upasado[i-1]);
}
std::array<double, n>ufuturo;
ufuturo[0]= 0;
ufuturo[n-1]= 0;
std::ofstream archivo1("ExtremosFijos.txt");
for (int i = 0; i<n-1; i++){
    archivo1<< i*dx<<", ";
}
archivo1<<(n-1)*dx<<"\n";
for (int i = 0; i<n-1; i++){
    archivo1<< uinicial[i]<<", ";
}
archivo1<<uinicial[n-1]<<"\n";
for (int i = 0; i<n-1; i++){
    archivo1<< upresente[i]<<", ";
}
archivo1<< upresente[n-1];
for (int t = 2; t<nt1; t++){
    archivo1 <<"\n"<< ufuturo[0]<< ", ";
    for (int i = 1; i<n-1 ; i++){
        ufuturo[i]=2*upresente[i]- upasado[i] + 0.5*(c*c)*(dt1*dt1)/(dx*dx)* (upresente[i+1]-2*upresente[i]+ upresente[i-1]);
    archivo1 << ufuturo[i]<< ", ";       
    }
    archivo1 << ufuturo[n-1];    
    for (int j = 1; j<n-1;j++){
        upasado[j] = upresente[j];
        upresente[j]= ufuturo[j];
    }  
}
archivo1.close();
//dt malo 
std::array<double, n>upasador;
for(int i=0;  i<n; i++){
    upasador[i]=uinicial[i];
}
std::array<double, n>upresenter;
upresenter[0]= 0;
upresenter[n-1]= 0;
for(int i = 1;  i<n-1; i++){
    upresenter[i]=upasador[i]+ 0.5*(c*c)*(dt2*dt2)/(dx*dx)*(upasador[i+1]-2*upasador[i]+ upasador[i-1]);
}
std::array<double, n>ufuturor;
ufuturor[0]= 0;
ufuturor[n-1]= 0;
std::ofstream archivo2("ExtremosFijosRaro.txt");
for (int i = 0; i<n-1; i++){
    archivo2<< i*dx<<", ";
}
archivo2<<(n-1)*dx<<"\n";
for (int i = 0; i<n-1; i++){
    archivo2<< uinicial[i]<<", ";
}
archivo2<<uinicial[n-1]<<"\n";
for (int i = 0; i<n-1; i++){
    archivo2<< upresenter[i]<<", ";
}
archivo2<< upresenter[n-1];
for (int t = 2; t<nt1; t++){
    archivo2 <<"\n"<< ufuturor[0]<< ", ";
    for (int i = 1; i<n-1 ; i++){
        ufuturor[i]=2*upresenter[i]- upasador[i] + 0.5*(c*c)*(dt2*dt2)/(dx*dx)* (upresenter[i+1]-2*upresenter[i]+ upresenter[i-1]);
    archivo2 << ufuturor[i]<< ", ";       
    }
    archivo2 << ufuturor[n-1];    
    for (int j = 1; j<n-1;j++){
        upasador[j] = upresenter[j];
        upresenter[j]= ufuturor[j];
    }  
}
archivo2.close();

//Caso Extremo forzado

const double w = M_PI*800;
//Posición inicial 
std::array<double, n>upasadoF;
for (int i = 0; i<n; i++){
    upasadoF[i]= uinicial[i];
}
std::array<double, n>upresenteF;
upresenteF[0]= 0;
upresenteF[n-1]= std::sin(w*dt1)*0.05;
for(int i = 1;  i<n-1; i++){
    upresenteF[i]=upasadoF[i]+ 0.5*(c*c)*(dt1*dt1)/(dx*dx)*(upasadoF[i+1]-2*upasadoF[i]+ upasadoF[i-1]);
}
std::array<double, n>ufuturoF;
ufuturoF[0]= 0;
std::ofstream archivo3("ExtremoForzado.txt");
for (int i = 0; i<n-1; i++){
    archivo3<< i*dx<<", ";
}
archivo3<<(n-1)*dx<<"\n";
for (int i = 0; i<n-1; i++){
    archivo3<< uinicial[i]<<", ";
}
archivo3<<uinicial[n-1]<<"\n";
for (int i = 0; i<n-1; i++){
    archivo3<< upresenteF[i]<<", ";
}
archivo3<< upresenteF[n-1];
for (int t = 2; t<nt1; t++){
    archivo3 <<"\n"<< ufuturoF[0]<< ", ";
    for (int i = 1; i<n-1 ; i++){
        ufuturoF[i]=2*upresenteF[i]- upasadoF[i] + 0.5*(c*c)*(dt1*dt1)/(dx*dx)* (upresenteF[i+1]-2*upresenteF[i]+ upresenteF[i-1]);
        archivo3 << ufuturoF[i]<< ", ";
    }
    ufuturoF[n-1]=0.05*(std::sin(w*dt1*t));
    archivo3 << ufuturoF[n-1];    
    for (int j = 1; j<n;j++){
        upasadoF[j] = upresenteF[j];
        upresenteF[j]= ufuturoF[j];
    }  
}
archivo3.close();

}
