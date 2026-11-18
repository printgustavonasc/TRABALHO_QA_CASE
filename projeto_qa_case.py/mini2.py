nome = input("qual o seu nome? ")

nota_1 = int(input("qual a nota do primeiro bimestre? "))
nota_2 = int(input("qual a nota do segundo bimestre? "))
nota_3 = int(input("qual a nota do terceirp bimestre? "))
nota_4 = int(input("qual a nota do quarto bimestre? "))

soma = nota_1 + nota_2 + nota_3 + nota_4 
media = soma / 4

print(f"olá, {nome}! sua media foi de, {media} no total!")