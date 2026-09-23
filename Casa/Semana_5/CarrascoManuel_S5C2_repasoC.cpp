#include <iostream>
#include <random>
#include <array>
#include <algorithm>
float div_f(float mivaflotante, int mivaentera);
int minimo(std::array<int,300>& arr);
void impimp(std::array<int,300>&arr); //IMPrimir IMPares --> impimp
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
std::cout<<"4. El arreglo fue creado \n";

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
//Decimo punto 
std::cout<< "10. La función min fue creada \n";
int min_ar= minimo((Ar));
std::cout<<"El valor minimo del arreglo usando la función creada es "<< min_ar<<"\n";
int* min_ar2 = std::min_element(Ar.begin(), Ar.end());
std::cout<<"El valor minimo del arreglo usando std::min_element es "<< *min_ar2<<"\n";
//Onceabo punto 
std::cout<<"11. La función de imprimir impares fue creada \n";
std::cout<<"Los valores impares y menores a 800 del arreglo son: \n";
impimp(Ar);
}
float div_f(float mivaflotante, int mivaentera){
    return mivaflotante/mivaentera;
}
int minimo(std::array<int,300>& arr){
    int min = arr[0];
    for (int i = 1; i<(std::size(arr)); i++){
        if(arr[i]<min){
            min = arr[i];
        }
        else{
            continue;
        }
    }
    return min;
}
void impimp(std::array<int,300>&arr){
    for (int i=0; i<(std::size(arr)); i++){
        if (arr[i]%2 != 0 && arr[i]<800){
            std::cout << arr[i] <<" ";
        }
        else if (arr[i]>800){
            std::cout<<"\nValor mayor a 800 encontrado en la posición " << (i+1)<<"\n";
            break;
        }
        else{
            continue;
        }
    }
    std::cout<<"\n";
}