#include <iostream>
#include <fstream>
#include <array>
//Constantes
const double Nx = 100; 
const int nx = 100; 
const double L = 1;
const double dx = L/(Nx-1);
const double nu = 0.01; 
const double t_final = 1000;
const double dt = (0.2*(dx*dx))/nu;
const int nt = (t_final/dt) +1; 
const double Nt = (t_final/dt) +1; 

int main(){

      
std::array<std::array<double, nx>,nx> Minicial;
for (int i = 0; i<nx; i++){
    for (int j=0; j<nx; j++){
        Minicial[i][j]= 50;
    }
}
for (int i = 40; i<60; i++){
    for (int j=20; j<40; j++){
        Minicial[i][j]= 100;
    }
}


    

//Extremos fijos 
std::array<std::array<double, nx>,nx> Mpasado;
for (int i = 0; i<nx; i++){
    for (int j=0; j<nx; j++){
        Mpasado[i][j]=Minicial[i][j];
    }
}
std::array<std::array<double, nx>,nx> Mpresente;
for (int i = 0; i<nx; i++){
    for (int j=0; j<nx; j++){
        Mpresente[i][j]=Minicial[i][j];
    }
}
for (int i = 1; i<nx-1; i++){
    for (int j=1; j<nx-1; j++){
        Mpresente[i][j]=Mpasado[i][j] + ((dt*nu)/dx*dx)*(Mpasado[i+1][j]+Mpasado[i-1][j]+Mpasado[i][j+1]+Mpasado[i][j-1]-(4*Mpasado[i][j]));
    }
}

std::array<std::array<double, nx>,nx> Mfuturo;
for (int i = 0; i<nx; i++){
    for (int j=0; j<nx; j++){
        Mfuturo[i][j]=Minicial[i][j];
    }
}
std::ofstream archivo1("Temperatura_ExtremosFijos100.txt");
archivo1<<"#Paso numero 1"<<"\n"; 
for (int i = 0; i<nx; i++){
    for (int j=0; j<nx-1; j++){
        archivo1<< Minicial[i][j]<<", ";
    }
    archivo1<<Minicial[i][nx-1]<<"\n";
}    
archivo1<<"#Paso numero 2"<<"\n"; 
for (int i = 0; i<nx; i++){
    for (int j=0; j<nx-1; j++){
        archivo1<< Mpresente[i][j]<<", ";
    }
    archivo1<<Mpresente[i][nx-1]<<"\n";
}  
for (int t = 2; t<nt; t++){
    archivo1<<"#Paso numero "<< t+1<<"\n";
    for (int i = 0; i<nx-1; i++){
    archivo1<<Mfuturo[0][i]<<", "; 
    }
archivo1<<Mfuturo[0][nx-1]<<"\n";
    
    for (int i = 1; i<nx-1; i++){
        archivo1<< Mfuturo[i][0]<<", ";
        for (int j=1; j<nx-1; j++){
            Mfuturo[i][j]=Mpresente[i][j] + ((dt*nu)/dx*dx)*(Mpresente[i+1][j]+Mpresente[i-1][j]+Mpresente[i][j+1]+Mpresente[i][j-1]-(4*Mpresente[i][j]));
           archivo1<< Mfuturo[i][j]<<", ";
    }
    archivo1<< Mfuturo[i][nx-1]<<"\n";
    }
    for (int i = 0; i<nx-1; i++){
    archivo1<<Mfuturo[nx-1][i]<<", "; 
    }
    archivo1<<Mfuturo[nx-1][nx-1]<<"\n";
    for (int i = 0; i<nx; i++){
        for (int j=0; j<nx; j++){
            Mpresente[i][j]=Mfuturo[i][j];
        }
    }
}
archivo1.close();


//Abierto

std::array<std::array<double, nx+2>,nx+2> MpasadoA;
for (int i = 0; i<nx; i++){
    for (int j=0; j<nx; j++){
        MpasadoA[i+1][j+1]=Minicial[i][j];
    }
}
MpasadoA[0][0]= 0;
MpasadoA[0][nx+1]= 0;
MpasadoA[nx+1][0]= 0;
MpasadoA[nx+1][nx+1]= 0;
for (int i = 1; i<nx+1;i++){
    MpasadoA[0][i]=MpasadoA[1][i];
}
for (int i = 1; i<nx+1;i++){
    MpasadoA[i][0]=MpasadoA[i][1];
}
for (int i = 1; i<nx+1;i++){
    MpasadoA[i][nx+1]=MpasadoA[i][nx];
}
for (int i = 1; i<nx+1;i++){
    MpasadoA[nx+1][i]=MpasadoA[nx][i];
}
std::cout<<"\n";
for (int i = 0; i<nx+2; i++){
    for (int j=0; j<nx+2; j++){
        std::cout<< MpasadoA[i][j]<<" ";
    }
    std::cout<<"\n";
}   
std::array<std::array<double, nx+2>,nx+2> MpresenteA;
MpresenteA[0][0]= 0;
MpresenteA[0][nx+1]= 0;
MpresenteA[nx+1][0]= 0;
MpresenteA[nx+1][nx+1]= 0;
for (int i = 1; i<nx+1; i++){
    for (int j=1; j<nx+1; j++){
        MpresenteA[i][j]=MpasadoA[i][j] + ((dt*nu)/dx*dx)*(MpasadoA[i+1][j]+MpasadoA[i-1][j]+MpasadoA[i][j+1]+MpasadoA[i][j-1]-(4*MpasadoA[i][j]));
    }
}
for (int i = 1; i<nx+1;i++){
    MpresenteA[0][i]=MpresenteA[1][i];
}
for (int i = 1; i<nx+1;i++){
    MpresenteA[i][0]=MpresenteA[i][1];
}
for (int i = 1; i<nx+1;i++){
    MpresenteA[i][nx+1]=MpresenteA[i][nx];
}
for (int i = 1; i<nx+1;i++){
    MpresenteA[nx+1][i]=MpresenteA[nx][i];
}
std::cout<<"\n";


std::array<std::array<double, nx+2>,nx+2> MfuturoA;
MfuturoA[0][0]= 0;
MfuturoA[0][nx+1]= 0;
MfuturoA[nx+1][0]= 0;
MfuturoA[nx+1][nx+1]= 0;
std::ofstream archivo2("Temperatura_ExtremosAbiertos100.txt");
archivo2<<"#Paso numero 1"<<"\n"; 
for (int i = 0; i<nx; i++){
    for (int j=0; j<nx-1; j++){
        archivo2<< Minicial[i][j]<<", ";
    }
    archivo2<<Minicial[i][nx-1]<<"\n";
}    
archivo2<<"#Paso numero 2"<<"\n"; 
for (int i = 1; i<nx+1; i++){
    for (int j=1; j<nx; j++){
        archivo2<< MpresenteA[i][j]<<", ";
    }
    archivo2<<MpresenteA[i][nx+1]<<"\n";
}  
for (int t = 2; t<nt; t++){
    archivo2<<"#Paso numero "<< t+1<<"\n";
    
    for (int i = 1; i<nx+1; i++){
        for (int j=1; j<nx+1; j++){
            MfuturoA[i][j]=MpresenteA[i][j] + ((dt*nu)/dx*dx)*(MpresenteA[i+1][j]+MpresenteA[i-1][j]
                +MpresenteA[i][j+1]+MpresenteA[i][j-1]-(4*MpresenteA[i][j]));
    }
        for (int j =1; j<nx; j++){
            archivo2<< MfuturoA[i][j]<<", ";
        }
    archivo2<< MfuturoA[i][nx]<<"\n";
    }

    for (int i = 1; i<nx+1; i++){
        for (int j=1; j<nx+1; j++){
            MpresenteA[i][j]=MfuturoA[i][j];
        }
    }
    for (int i = 1; i<nx+1;i++){
        MpresenteA[0][i]=MpresenteA[1][i];
    }
    for (int i = 1; i<nx+1;i++){
        MpresenteA[i][0]=MpresenteA[i][1];
    }
    for (int i = 1; i<nx+1;i++){
        MpresenteA[i][nx+1]=MpresenteA[i][nx];
    }
    for (int i = 1; i<nx+1;i++){
        MpresenteA[nx+1][i]=MpresenteA[nx][i];
    }   
}
archivo2.close();
}