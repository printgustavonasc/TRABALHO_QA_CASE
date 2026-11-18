# introdução da promoção

print("Bem vindo ao Joga Fit") # type: ignore

# criação das variaveis 

aluno = input("Qual o nome do aluno? ")
frequencia = int(input(f"Quantas vezes {aluno} compareceu? "))

# se a presença for maior que 21 é conquistado a promoção

if frequencia >= 21:
   print("Parabens, você está participando da promoção treina junto") # type: ignore

   print("Uhuul, agora você pode convidqar um amigo para treinar com você.") #type: ignore 

   print("Agora você tem 1 mês de aulas gratuitas!!") # type: ignore

# caso não tenha a presença necessaria o aluno receberá:

else:
  print("Que pena, por pouco você ganharia a promoção de 1 mês de aulas grátis") # type: ignore

  resposta = input("se interessou na promo Treina junto?")

  if resposta == "sim": 
     print("Que bom que você voltou, agora podemos iniciar uma nova contagem para conquistar a promo treina junto") # type: ignore

  if resposta == "não": 
     print("ahh, que pena, ainda te esperamos por aqui!")