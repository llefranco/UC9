print('''Olá, digite seu nome e o turno em que irá trabalhar.''')

usuario = input("Digite o seu nome: ")
periodo = input("Digite seu turno de trabalho: ")

'''
Entrada de dados:
usuario = nome da pessoa
periodo = turno que a pessoa trabalha (manhã, tarde, noite)
'''

match periodo:
    case "M" | "manhã" | "manha"| "Manhã" | "Manha":
        print("Bom dia, ",usuario)
    case "T" | "t" | "Tarde" | "tarde":
        print("Boa tarde, ",usuario)
    case "N" | "n" | "Noite" | "noite":
        print("Boa noite, ",usuario)
    case _:
        print("Período desconhecido, tente novamente.")
    