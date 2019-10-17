valor1=int (input("Ingrese primer valor: "))
valor2=int (input("Ingrese segundo valor: "))
print("1. Suma ")
print("2. Resta")
print("3. Potencia")
operacion=int (input("Ingrese operacion: "))

if operacion == 1:
  resultado = valor1 + valor2
else:
 if operacion == 2:
   resultado = valor1 - valor2
 else:
   resultado = valor1 ** valor2
   
print(resultado)
