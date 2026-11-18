# criação das variaveis dos nomes dos cachorros e idade humana
nome = input("Digite o nome do cachorro: ")
idade_humana = int(input("Digite a idade humana do cachorro: ")) 
banhos = int(input("Quantos banhos ele tomou em 12 meses? "))

print("Tabela: Grande (75 e 20) | Médio (60 e 15) | Pequeno (50 e 5)")
valor_banho = float(input("Digite o valor do banho: "))
custo_banho = float(input("Digite o custo do banho: "))

# calculo da idade do cachorro vezes a idade humana 
idade_cachorro = idade_humana * 7
lucro = (valor_banho - custo_banho) * banhos

print(f"Olá, {nome} tem {idade_cachorro} anos e nos últimos 12 meses o lucro com este animal foi de R${lucro:.2f}")