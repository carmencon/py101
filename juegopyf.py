import random
numero = []
while True:
    cantidad = int(input("ingrese la cantidad digitos a jugar:  ")
    if cantidad in [3,4,5]:
                   break

while len(numero) < cantidad:
    digito = random.randint(0,9)
    if digito not in numero:
                    numero.append(digito)

print(numero)
While True:
    while True:
        intento = input("ingrese un numero")

        usuario = []
            for i in intento:
                if int(i) not in usuario:
                   usuario.append(int(i))

            if len(usuario) != len(numero):
                   print("intento no valido")
            else:
                break

    fijas = 0
    picas = 0

    for i in range(len(numero)):
        if numero(i) == digito[i]:
                   fijas += 1

        

    
