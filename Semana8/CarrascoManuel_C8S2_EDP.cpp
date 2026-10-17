#include <iostream>
#include <fstream>
#include <array>
//Constantes
const double Nx = 10; 
const int nx = 10; 
const double L = 1;
const double dx = L/(Nx-1);
const double nu = 0.01; 
const double t_final = 1100;
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
Minicial[4][2]= 100;
Minicial[4][3]= 100;
Minicial[5][2]= 100;
Minicial[5][3]= 100;
for (int i = 0; i<nx; i++){
    for (int j=0; j<nx; j++){
        std::cout<< Minicial[i][j]<<" ";
    }
    std::cout<<"\n";
}      

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
std::ofstream archivo1("Temperatura.txt");
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

}