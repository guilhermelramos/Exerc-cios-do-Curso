cal = 0
velho = 0
qts_M = 0
for g in range(4):
    print("----- {}ª PESSOA -----".format(g + 1))
    nome = input("Nome: ").strip()
    idade = int(input("Idade: ").strip())
    sexo = input("Sexo [M/F]: ").strip().upper()
    cal += idade
    if sexo == "M" and velho < idade:
        velho = idade
        mais_velho = nome
    elif sexo == "F" and idade <= 20:
        qts_M += 1
print("A média de idade do grupo é de {:.1f} anos. ".format(cal / 4))
print("O homem mais velho tem {} anos e é o {}.".format(velho, mais_velho))
print("Ao todo são {} mulheres que tem menos de 20 anos!".format(qts_M))
