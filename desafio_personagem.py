'''🧠 Atividade Prática Classificador de Personagens + Escolha de Ação | Dia 04/02

📋 Descrição da Tarefa:


Você está criando um pequeno sistema de um jogo de aventura onde o jogador será classificado por sua experiência e, com base em sua escolha, executará uma ação dentro do jogo.

 
🔧 O que seu programa deve fazer:

 
1.Pedir ao jogador quantos pontos de experiência ele tem (XP):

Menos de 100 → "Iniciante"

Entre 100 e 500 → "Intermediário"

Mais de 500 → "Veterano"

Use if/elif/else para essa classificação.


2. Depois, o programa deve perguntar qual ação o jogador deseja executar (usar match case):

"A" → Atacar

"D" → Defender

"F" → Fugir

Qualquer outra tecla → "Ação inválida"


Mostre uma mensagem apropriada para cada ação, como:

"Você avançou para o ataque!"

"Você levantou o escudo!"

"Você fugiu da batalha!"

 📝 Regras de Entrega:

Crie seu código em um arquivo .py
Faça testes com diferentes níveis de XP e ações
Envie o código por GitHub ou por sua plataforma de aulas

'''
print("Bem vindo ao Coliseu, vamos nos preparar para a luta!")

experiencia = int(input("Quantos pontos de experiência você possui, aventureiro?: "))


if experiencia < 100: 
    print ("Você é um aventureiro iniciante, então irá lutar contra o Lobo Faminto.")
elif  100 >= experiencia < 500:
    print ("Hum... um aventureiro intermediário, você irá lutar contra o Leão!")
else:
    print ("Que honra, um aventureiro veterano! Você irá lutar contra o ciclope.")

print("Certo, lembre-se que na batalha você pode Atacar (A), Defender (D) ou Fugir (F), boa sorte!")

acao = input("Começou a luta! Qual será sua ação?: ")

match acao:
    case "A":
        print ("Você ataca o inimigo com sua espada!")
    case "D":
        print ("Você levanta seu escudo e entra em uma posição defensiva!")
    case "F":
        print ("Você tenta fugir, mas tropeça e cai no chão!")
    case _:
        print ("Esse comando não existe, use (A) para atacar, (D) para defender ou (F) para fugir.")

