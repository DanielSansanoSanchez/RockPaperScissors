import random

opciones= ["piedra,  papel,  tijeras"]

jugador= input("elige una opcion ")
pc = random.choice (["piedra" , "papel", "tijeras"])

if jugador == "piedra" :
    if pc == "piedra" :
        print( "ambos alegisteis piedra empate" )
    elif pc == "papel" :
        print ( "pc ha elegido papel, papel gana a piedra ,has perdido ")
    else:
        print ("pc ha elegido tijeras, piedra gana a tijeras ,has ganado")
elif jugador == "papel" :
    if pc == "piedra" :
        print ("pc ha elegido piedra ,papel gana a piedra ,has ganado ")
    elif pc == "papel" :
        print ("ambos eligieron papel empate")
    else:
        print ("pc escogio tijeras, papel pierde contra tijeras ,has perdido")
elif jugador == "tijeras" :
    if pc == "piedra" :
        print ("pc ha elegido piedra ,piedra gana a tijeras ,has perdido ")
    elif pc == "papel" :
        print ("pc ha elegido papel ,papel pierde contra tijeras ,has ganado")
    else:
        print ("ambos eligieron tijeras, empate ")
else:
    print (" no has elegido una opcion correcta ")

seguir = ""
while seguir != "n" or seguir != "s" :
    seguir = input("deseas volver a jugar si/no: ")
    if seguir == "n":
        jugando= False
        break
    elif seguir == "s":
        break
    else:
        print("no has seleccionado una opcion correcta")
