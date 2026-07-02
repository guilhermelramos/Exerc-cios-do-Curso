# 🐍 Curso de Python — Exercícios

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-green)
![License](https://img.shields.io/badge/License-MIT-blue)

Repositório com exercícios e projetos práticos do curso de Python, organizados por níveis de dificuldade. Cada exercício explora conceitos fundamentais da linguagem, desde manipulação de strings até estruturas de repetição e condicionais aninhadas.

---

## 📁 Estrutura
```
📦 Exerc-cios-do-Curso
├── 📂 Mundo_01 - Fundamentos
│   ├── 📂 Aula09 - Manipulação de Strings
│   └── 📂 Aula10 - Condicionais
│       └── ex028.py  → Jogo de Adivinhação
├── 📂 Mundo_02 - Intermediário
│   ├── 📂 Aula12 - Condicionais Aninhadas
│   │   ├── ex036.py  → Empréstimo Bancário
│   │   ├── ex042.py  → Formador de Triângulo
│   │   └── ex043.py  → Calculadora de IMC
│   └── 📂 Aula13 - Estruturas de Repetição
│       ├── ex052.py  → Verificador de Número Primo
│       └── ex053.py  → Verificador de Palíndromo
└── README.md
```

---

## 🚀 Exercícios em Destaque

| Emoji | Nome | Arquivo |
|-------|------|---------|
| 🎮 | **Pedra, Papel, Tesoura** | `ex042.py` |
| 🔢 | **Verificador de Número Primo** | `ex052.py` |
| 🏥 | **IMC com Cores** | `ex043.py` |
| 💰 | **Empréstimo Bancário** | `ex036.py` |
| 🎯 | **Jogo de Adivinhação** | `ex028.py` |
| 📝 | **Verificador de Palíndromo** | `ex053.py` |

---

## ▶️ Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/guilhermelramos/Exerc-cios-do-Curso.git
   cd Exerc-cios-do-Curso
   ```

2. Instale as dependências (se necessário):
   ```bash
   pip install -r requirements.txt
   ```

3. Execute qualquer exercício:
   ```bash
   python ex052.py
   ```

---

## 📦 Requisitos

- **Python 3.x**
- **`unidecode`** — utilizado no verificador de palíndromo (`ex053.py`)

```bash
pip install unidecode
```

---

## 👀 Preview

### 🔢 Verificador de Número Primo (`ex052.py`)

Output colorido no terminal mostrando os divisores em verde e os não-divisores em vermelho:

```bash
Digite um numero: 17
[36m1[m  [31m2[m  [31m3[m  [31m4[m  [31m5[m  [31m6[m  [31m7[m  [31m8[m  [31m9[m  [31m10[m  [31m11[m  [31m12[m  [31m13[m  [31m14[m  [31m15[m  [31m16[m  [36m17[m
O numero 17 foi divisivel 2 vezes
Ele é primo!
```

### 🏥 IMC com Cores (`ex043.py`)

Classificação do Índice de Massa Corporal com saída colorida no terminal:

```bash
Digite sua altura em centimetros: 175
Digite seu peso: 70
Sua situação está assim seu IMC é de 22.86, e se encaixa como Peso ideal
```

---

## 🛠️ Tecnologias Utilizadas

- **Python 3** — Linguagem principal
- **Módulos padrão:** `random`, `time`, `datetime`
- **Bibliotecas externas:** `unidecode`

---

## 📚 Conceitos Abordados

| Módulo | Conceitos |
|--------|-----------|
| Aula 09 | Manipulação de strings (`upper`, `lower`, `split`, `count`, `find`) |
| Aula 10 | Condicionais simples (`if` / `else`) |
| Aula 12 | Condicionais aninhadas (`if` / `elif` / `else`), operadores lógicos |
| Aula 13 | Loops (`for`, `while`), acumuladores, `range()` |

---

## 🤝 Contribuições

Sugestões e melhorias são sempre bem-vindas! Sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

---

## 📄 Licença

Este projeto está sob a licença MIT.

---

<p align="center">Feito com 💙 e muito ☕ durante o curso de Python.</p>
