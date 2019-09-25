from generador import generador_mejor, generador
adivinado=False
minimo=0
maximo=100
aleatorio=generador(0, 100)
while  adivinado == False:
    print("Ingrese un numero entre el 0 y 100")
    numero=int(input())
    if numero == aleatorio:
        print("Ganaste")
        adivinado=True
    if numero < aleatorio:
        print("El numero es mayor!!!")
    if numero > aleatorio:
        print("El numero es menor")
    if adivinado == False:
        print("Ahora le toca a la computadora")
        computadora=generador(minimo, maximo)
        print("La computadora penso: " + str(computadora))
        if computadora == aleatorio:
            print("Gano la computadora")
            adivinado=True
        if computadora < aleatorio:
            print("Computadora es MAYOR")
            minimo=computadora
        if computadora > aleatorio:
            print("Computadora es MENOR")
            maximo=computadora
        
        
        