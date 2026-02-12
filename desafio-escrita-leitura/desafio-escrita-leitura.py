''' 

- Ler o arquivo nome_ficticios.txt
- Transformar em lower case
- Ordem alfabética

'''

with open('nomes_ficticios.txt', 'r', encoding='utf-8') as arquivo_nomes:
  nomes = arquivo_nomes.readlines()

with open('nomes_organizados.txt', 'w', encoding='utf-8') as arquivo_saida:

  nomes.sort()      

  for nome in nomes:
    arquivo_saida.write(nome.lower())

print("Arquivo nomes_organizados.txt criado com sucesso.")