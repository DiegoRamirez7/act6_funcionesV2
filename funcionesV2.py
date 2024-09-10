print("Mas sobre funciones")
# Aqui se escriben las funciones
def suma_ab(a,b):
    s=a+b
    return s
def resta_ab(a1,b1):
    r=a1-b1
    return r
def mul_ab(a2,b2):
    m=a2*b2
    return m
def div_ab(a3,b3):
    d=a3/b3
    return d

# llamadas a funciones
#SUMA
print("Calculando suma")
n1=int(input("Ingresa el primer Numero "))
n2=int(input("Ingresa el segundo Numero "))
suma=suma_ab(n1,n2)
print(f"la suma de {n1} + {n2} es: {suma}")
#RESTA
nr=int(input("Ingresa el primer Numero "))
nr1=int(input("Ingresa el segundo Numero "))
print("Calculando resta")
resta=resta_ab(nr,nr1)
print(f"la resta de {nr} - {nr1} es: {resta}")
#MULTIPLICACION
nm=int(input("Ingresa el primer Numero "))
nm1=int(input("Ingresa el segundo Numero "))
mul=mul_ab(nm,nm1)
print(f"la Multiplicacion de {nm} * {nm1} es: {mul}")
#DIVISION
nd=int(input("Ingresa el primer Numero "))
nd2=int(input("Ingresa el segundo Numero "))
div=div_ab(nd,nd2)
print(f"la division de {nd} / {nd2} es: {div}")
