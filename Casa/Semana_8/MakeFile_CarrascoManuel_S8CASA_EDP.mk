CuerdaForzada.mp4 : ExtremoForzado.txt ANIMACION_CarrascoManuel_S8CASA_EDP.py PLOTS_CarrascoManuel_S8CASA_EDP.py
	python3 PLOTS_CarrascoManuel_S8CASA_EDP.py
	python3 ANIMACION_CarrascoManuel_S8CASA_EDP.py

ExtremoForzado.txt : CarrascoManuel_S8CASA_EDP.cpp
	g++ CarrascoManuel_S8CASA_EDP.cpp
	./a.out 

clean: 
	rm -f ExtremoForzado.txt ExtremosFijos.txt a.out