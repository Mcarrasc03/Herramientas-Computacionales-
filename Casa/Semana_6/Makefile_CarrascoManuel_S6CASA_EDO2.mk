# Listas de archivos (agrupa tus 4 datos y tus 4 PDFs)
DATOS = DatosEuler.txt DatosLF.txt DatosEulerFric.txt DatosRK4Fric.txt
GRAFICAS = Euler.pdf LeapFrog.pdf EulerFriccion.pdf RKFriccion.pdf Fase.pdf

# Regla principal por defecto
all: $(GRAFICAS) 


# El script de Python lee los .dat y genera los 4 archivos PDF en una sola corrida
\((GRAFICAS) :\)(DATOS) plot.py
	python3 plot.py

# El C++ se compila y genera los 4 archivos .dat en una sola ejecución
$(DATOS) : CarrascoManuel_S6CASA_EDO2orden_RESORTE.cpp
	g++ CarrascoManuel_S6CASA_EDO2orden_RESORTE.cpp 
	./a.out
