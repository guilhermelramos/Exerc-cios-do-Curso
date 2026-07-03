from random import randint

valor = randint(0, 5)

resposta = int(input("Adivinhe o numero de 0 a 5: "))

if valor == resposta:
    print("Acertou!")
else:
    print("Errou!")
    print("O valor era {}. ".format(valor))
