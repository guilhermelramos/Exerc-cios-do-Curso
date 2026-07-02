r1 = float(input("Insira o tamanho da primeira reta: "))
r2 = float(input("Insira o tamanho da segunda reta: "))
r3 = float(input("Insira o tamanho da terceira reta: "))

triangulo = ""

if r1 == r2 == r3:
    triangulo = "EQUILÁTERO"

elif r1 == r2 != r3 or r2 == r3 != r1 or r1 == r3 != r2:
    triangulo = "ISÓSCELES"

elif r1 != r2 != r3:
    triangulo = "ESCALENO"


if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("O triangulo é um {}.".format(triangulo))
else:
    print("Não são compativeis! Impossivel de formar um triângulo!")
