numero1 = float(input("Introduce el primer numero"))
numero2 = float(input("Introduce el segundo numero"))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
potencia = numero1 % numero2
residuo = numero1 ** numero2

print ("la suma es"+ str(suma))
print ("la resta es" + str(resta))
print ("la multiplicacion es" + str(multiplicacion))
print ("la division es" + str(division))
print ("la potencia es" + str(potencia))
print ("el residuo es" + str(residuo))

if numero1 == numero2:
    print("Son el mismo valor")
elif numero1 > numero2:
    print("el numero"+str(numero1)+"es mayor a"+str(numero2))
else:
    print("el numero"+str(numero2)+"es mayor a"+str(numero1))        