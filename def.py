from calc import *

def ec(o) :
	if o != "+" and o != "-" and o != "*" and o != "/" :
		valido = False
	else:
		valido = True
	return valido

print("Bienvenido a la calculadora")
nombre = input("Escriba su usuario ")
operacion = input("Indique la operacion (+, -, *, /): ")
while ec(operacion) == False:
	print("No es una operacion valida")
	operacion = input("Indique la operacion (+, -, *, /): ")
else:
	oper1 = input("Indique el primer numero:")
	oper2 = input("Indique el segundo numero:")
if ec(oper1) and ec(oper2) :
    oper1 = int(oper1)
    oper2 = int(oper2)
    if operacion == "+" :
        print(suma(oper1,oper2))
    elif operacion == "-" :
        print(resta(oper1, oper2))
    elif operacion == "*" :
        print(multiplicacion(oper1, oper2))
    elif operacion == "/" :
        print(division(oper1, oper2))
    else :
        print("Error! Eso no es una operación válida!")
else :
        print("Error! Ambos números deben tener formato numérico.")