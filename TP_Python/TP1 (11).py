def puntos_del_examen():
    """El programa utiliza un valor centinela para saber cuadno terminar"""
    """El programa calcula si un alumno aprobo o no el examen"""
    #El programa solicita que se ingrese la informacion del examen como puntos totales y porcentaje minimo para aprobar
    examenes = int (input("Ingrese -1 cuadno ya no tenga mas examenes para corregir "))    
    puntos_maximos = int(input("Ingrese la cantidad total de ejercicisos del examen: "))
    porcentaje = int (input("Ingrese el porcentaje de aciertos minimno para aprobar el examen: "))
    #El programa crea un bucle en el cual,si se introduce el valor centinela, el bucle termina
    while examenes != -1: 
        #El programa pregunta al usuario cuantos puntos tiene bien resueltos el alumno, para calcular su nota
        puntos_resueltos = int (input("Cuantos ejercicios estan bien resuletos? "))
        if ((puntos_resueltos * 100) / puntos_maximos) >= (porcentaje):
            print ("El alumno aprobo el examen con un " + str((puntos_resueltos * 100) / puntos_maximos) + " porciento de respuestas corectas")
        else:
            print ("El alumno no aprobo")

        examenes = int (input("Ingrese -1 si ya no tiene examenes que corregir "))
        if examenes == -1:
            break

puntos_del_examen()
          
