from random import choice

opcoes = ["Pedra", "Tesoura", "Papel"]

pc = choice(opcoes)

print("-=-" * 25)
print("""
Selecione oq vc irá jogar:
[ 0 ] Pedra
[ 1 ] Tesoura
[ 2 ] Papel""")
print("-=-" * 25)

jogada_num = int(input("Selecione a sua jogada: "))

jogada = opcoes[jogada_num]

print(f"A sua escolha é {jogada}, e a do computador é {pc}.")

if jogada == pc:
    print("Empatou")
elif (
    (jogada == "Pedra" and pc == "Tesoura")
    or (jogada == "Tesoura" and pc == "Papel")
    or (jogada == "Papel" and pc == "Pedra")
):
    print("Vc ganhou")
else:
    print("Vc perdeu")
