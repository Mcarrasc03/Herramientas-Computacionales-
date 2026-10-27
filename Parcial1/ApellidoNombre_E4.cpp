/*
 * EJERCICIO 4
 *
La ecuación diferencial ordinaria del enunciado
d²x(t)/dt²+m*g-const*v²(t)=0
es una ecuacion que describe el caida de un objeto debido a su peso (m*g) cuando hay una fuerza de fricción es const*v²(t). Usando el metodo de Euler, encuentre x(t) desde t=0.0s hasta t=5.5s. Tome m=2.0k, g=-9.8m/s² y const=0.0035. Escoja un dt apropiado.

El script .cpp debe generar los datos de x(t) y de v(t) en funcion del tiempo.
Complete el script ApellidoNombre_plot_E4.py, para hacer una una grafica de su solucion x en funcion de t y otra gráfica de v en función de t. El script de python debe mostrar estas graficas (use plt.show()).
*/

#include <fstream>
#include <iostream>
#include <math.h>
#include <stdio.h>
#include <array>

int main()
	{
	std::cout<<" +++++++++++++++++++++++++++++++++++++"<<std::endl;
	std::cout<<" +++++++++++++++++++++++++++++++++++++"<<std::endl;
	std::cout<<" +++++++++ Ejercicio 4: ODEs +++++++++"<<std::endl;
	std::cout<<" +++++++++++++++++++++++++++++++++++++"<<std::endl;
	std::cout<<" +++++++++++++++++++++++++++++++++++++"<<std::endl;
	
	//PARA ESCRIBIR UN ARCHIVO DE DATOS
	// open a file in write mode.
	std::ofstream outfile;
	outfile.open("XXXXXX.dat");
	
	//write file
  	outfile <<"XXXXXXXXXXXXXXXXXXXXXXXX"<<std::endl;
	
	// close the opened file.
 	outfile.close();

	return 0;
	}
