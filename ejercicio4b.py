# coding=utf-8
__Author__="Víctor Davó Antón"

import random

# Función que determina quien gana Piedra, papel o tijera
# 0: Empate.
# 1: Gana Jugador 1.
# 2: Gana Jugador 2.

def quienGana(jugada1, jugada2) :
    if jugada1 == jugada2 :
        return 0
    elif jugada1 == "piedra" and jugada2 == "tijera" :
        return 1
    elif jugada1 == "tijera" and jugada2 == "papel" :
        return 1
    elif jugada1 == "papel" and jugada2 == "piedra" :
        return 1
    else :
        return 2

# Programa principal
def main():
    print("PIEDRA, PAPEL, ... ¡TIJERA!")

    nombre1=input("Introduzca el nombre del Jugador 1: ")
    nombre2=input("Introduzca el nombre del Jugador 2: ")
    numeroTirada=int(input("Introduzca el número de tiradas: "))

    ganadas1=0
    ganadas2=0
    empates=0

    while numeroTirada > 0 :
        print("Tirada nº ",numeroTirada,":")
        j1 = random.choice(["piedra", "papel", "tijera"])
        j2 = random.choice(["piedra", "papel", "tijera"])
        
        print("El {0} ha sacado {1}.".format(nombre1, j1))
        print("El {0} ha sacado {1}.".format(nombre2, j2))
        # Implemente los comentarios anteriores empleando print("".format())

        ganador=quienGana(j1,j2)
        
        if ganador == 0 :
            empates=empates+1
            print("Han empatado.")
        elif ganador == 1 :
            ganadas1=ganadas1+1
            print("Gana {0} la tirada {1}. Número de tiradas ganadas --> {2}".format(nombre1,numeroTirada,ganadas1))
        elif ganador == 2 :
            ganadas2=ganadas2+1
            print("Gana {0} la tirada {1}. Número de tiradas ganadas --> {2}".format(nombre2,numeroTirada,ganadas2))
        else :
            print("Error.")
        
        numeroTirada=numeroTirada-1

    
    print("RESUMEN:\n\t{0} --> {1}.\n\t{2} --> {3}.\n\tEmpates: {4}".format(nombre1,ganadas1,nombre2,ganadas2,empates))
    # Resultado final de todas las tiradas
    if ganadas1 == ganadas2 :
        print("HAN EMPATADO")
    elif ganadas1 > ganadas2 :
        print("GANA ",nombre1," (",ganadas1,")")
    else :
        print("GANA ",nombre2," (",ganadas2,")")


if __name__== "__main__" :
   main()