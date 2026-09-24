#include <iostream>
#include <random>
#include <array>
float div_f(float mivaflotante, int mivaentera);

int main(){
std::cout<< "1. \n"; 
//Primer punto
int m = 19;
float a = 15.11;
//Segundo punto
std::cout<< "Primer punto terminado, variables m y a inicializadas \n";
std::cout<< "2. m = "<< m << " a = "<< a<<"\n";  
//Tercer punto
float z = a/m;
std::cout<< "3. a/m= "<< z<<"\n";
//Cuarto punto 

std::array<int, 300> Ar;
std::random_device rd;   // non-deterministic generator
std::mt19937 gen(rd());  // to seed mersenne twister.
std::uniform_int_distribution<int> dist(0,900);
for (int i = 0; i<300; i++){
    Ar[i]=dist(gen);
}
std::cout<<"4. El arreglo fue creado";

//Quinto punto 
std::cout<< "5. El arreglo es: ";
for (int i = 0; i<300; i++){
    std::cout << Ar[i]<<" "; 
}
std::cout<<"\n";
//Sexto punto 
std::cout<< "6. El quinto elemento del arreglo es "<< Ar[4]<< "\n";
//Septimo Punto float 
int Tam= std::size(Ar);
std::cout <<"7. La longitud del arreglo es "<<Tam<<"\n";
//Ocravo punto 

std::cout<<"8. Función creada\n";
//Noveno punto 
float r=div_f(17.5, 5);
std::cout<<"9. El resultado es "<< r<<"\n";

}
float div_f(float mivaflotante, int mivaentera){
    return mivaflotante/mivaentera;
}
