from unidecode import unidecode

n1 = unidecode("APÓS A SOPA").lower()
texto_sem_espacos = n1.replace(" ", "")
inverso = texto_sem_espacos[::-1]

if inverso == texto_sem_espacos:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo")
