valor = float(input("Digite o valor da casa para calcularmos o empréstimo: "))
salario = float(input("Quanto é o seu salário atual? "))
anos = int(input("Em quantos anos vc irá pagar o empréstimo? "))

prestaçoes = valor / (anos * 12)

if prestaçoes > salario * 0.30:
    print("O Empréstimo foi negado pois passa o limite máximo permitido! Lamentamos!")
else:
    print(
        "Empréstimo será de {:.1f}, será pago em {} (valor em meses), no valor de R${:.2f}. ".format(
            valor, anos * 12, prestaçoes
        )
    )
