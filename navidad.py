from os import system

def copa(ancho):
    print("★".center(ancho))
    for i in range(3, ancho+1, 2):
        rama = "*"*i
        print(rama.center(ancho))

def tronco(altura, ancho_copa):
    for i in range(altura):
        print("|||".center(ancho_copa))


ANCHO = 16
ALTO_TRONCO = 2

system('clear') # Limpia el terminal

copa(ANCHO)
tronco(ALTO_TRONCO, ANCHO)
print("\n¡Feliz Navidad desde IT+School!")