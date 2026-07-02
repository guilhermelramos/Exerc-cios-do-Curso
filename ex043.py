altura = int(input("Digite sua altura em centimetros: "))
peso = float(input("Digite seu peso: "))

imc = (peso / (altura * altura)) * 10000

status = ""

if imc < 18.5:
    status = "\033[0;33mAbaixo do peso\033[m"
elif 18.5 <= imc <= 25:
    status = "\033[1;32mPeso ideal\033[m"
elif 25.1 <= imc <= 30:
    status = "\033[1;33mSobrepeso\033[m"
elif 30.1 <= imc <= 40:
    status = "\033[0;31mObesidade\033[m"
elif imc > 40:
    status = "\033[1;31mObesidade Mórbida\033[m"

print(
    "Sua situação está assim seu IMC é de {:.2f}, e se encaixa como {} ".format(
        imc, status
    )
)
