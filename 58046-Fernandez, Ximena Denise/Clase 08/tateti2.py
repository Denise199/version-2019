from tablero2 import draw_tablero, win, validate, full
numeros=[ ]
tablero=[ ]
for i in range(0,9):
    tablero.append(" ")
    numeros.append(str(i+1))
draw_tablero(numeros)
while win(tablero) == False and full(tablero) == False:
    print("Turno de la X")
    valido=False
    while not valido:
        print("Ingrese una posicion valida de 1 a 9 (X) ")
        posicion=int(input())
        valido= validate(tablero, posicion)
        if not valido:
            print("Error de posicion")
    tablero[posicion-1]= numeros[posicion-1]="X"
    draw_tablero(numeros)
    gano=win(tablero)
    if gano:
        print("Gano X")
    else:
        print("Turno de la O")
        valido=False
        while not valido:
            print("Ingrese una posicion valida de 1 a 9 (O) ")
            posicion=int(input())
            valido= validate(tablero, posicion)
            if not valido:
                print("Error de posicion")
        tablero[posicion-1]=numeros[posicion-1]="O"
        draw_tablero(numeros)
        gano=win(tablero)
        if gano:
            print("Gano O")
if full(tablero) and not win(tablero):
    print("Nadie gano")

