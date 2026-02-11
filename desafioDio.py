# //  Desafio Classificador de nível de Herói 

# // ** Que deve ser utilizado **
# // - Variáveis
# // - Operadores
# // - Laços de repetição
# // - Estruturas de decisões
# // - Qualquer linguagem pode ser utilizado

# // ## Objetivo
# // Crie uma variáve para armazenar o nome e a quantidade de
# // experiência (XP) de um herói, depois utilize uma estrutura
# // de decisão para apresentar alguma das mensagens abaixo:

# // Se XP for menor do que 1.000 = Ferro
# // Se XP for entre 1.001 e 2.000 = Bronze
# // Se XP for entre 2.001 e 5.000 = Prata
# // Se XP for entre 6.001 e 7.000 = Ouro
# // Se XP for entre 7.001 e 8.000 = Platina
# // Se XP for entre 8.001 e 9.000 = Ascendente
# // Se XP for entre 9.001 e 10.000 = Imortal
# // Se XP for maior ou igual a 10.001 = Radiante


# // #SAIDA
# // Âo final deve se exibir uma mensagem:
# // "O Herói de nome {nome} está no nível de {nivel}}



nome = input("Qual o nome do heroi? \n")
xp = int(input("\nQual o level do heroi? \n\n"))


if xp < 1000 :
    xp = "Ferro"
    print(f"O Herói de nome {nome} está no nível de {xp}")
elif xp >= 1001 and xp <= 2000 :
    xp = "Bronze"
    print(f"O Herói de nome {nome} está no nível de {xp}")
elif xp >= 2001 and xp <= 5000 :
    xp = "Prata"
    print(f"O Herói de nome {nome} está no nível de {xp}")
elif xp >= 5001 and xp <= 7000 :
    xp = "Ouro"
    print(f"O Herói de nome {nome} está no nível de {xp}")
elif xp >= 7001 and xp <= 8000 :
    xp = "Platina"
    print(f"O Herói de nome {nome} está no nível de {xp}")
elif xp >= 8001 and xp <= 9000 :
    xp = "Ascendente"
    print(f"O Herói de nome {nome} está no nível de {xp}")
elif xp >= 9001 and xp <= 10000 :
    xp = "Imortal"
    print(f"O Herói de nome {nome} está no nível de {xp}")
elif xp >= 10001 :
    xp = "Radiante"
    print(f"O Herói de nome {nome} está no nível de {xp}")
else :
    print("Valor de XP inválido")