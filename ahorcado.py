import random
from os import system

system("cls")

intentos = 0
bandera = 0
limite = 6
lenguajes = ["Java", "Python", "C", "Go", "JavaScript", "PHP", "Ensamblador", "COBOL"];
wordUser = []

i = 0

palabra = random.choice(lenguajes)

tamanio = len(palabra)

for i in range(tamanio):
    wordUser.append("")

print("\nTamaño palabra: ", tamanio)

while(intentos < limite):
    word = input("\nDigita una letra: ")

    i = 0
    
    for letra in palabra:
        if (word == letra):
            wordUser[i] = word
            bandera = 0
        else:
            if wordUser[i] != "_":
                pass
            else:
                wordUser[i] = "_"
            bandera = 1
        
        i += 1

    print("\n", wordUser)

    if bandera == 1:
        intentos += 1
  
    respuesta = input("\n¿Ya sabes la palabra? s/n \t")
    respuesta = respuesta.lower()
    
    if respuesta == "si" or respuesta == "s" or respuesta == "yes":
        respuesta = input("\nDigita la palabra: \t")
  
        if respuesta == palabra:
            print("\nFelicidades, ganaste!")
            bandera = 0
            break
   
        else:
            print("\nMurio el monito ahorcado :(")
            bandera = 1
            break
   
    print("\nTe quedan: ", limite - intentos, " intentos")

if bandera == 1:
    print("\nNo adviniaste :(, el muñequito está ahorcado :(")