projeto = "ShopVibe E-commerce"
modulo = "Carrinho de compras e Cupom de desconto"
responsavel = "Lucas Oliveira"
data_de_execucao = "10/11/2026"


print(50*"=")
print(10*" " , "Registro de Execução de Testes")
print(50*"=")

print (50*"-")
print(f"Módulo testado: {projeto}")
print (50*"-")
print(f"Projeto testado: {projeto}")
print (50*"-")
print(f"Responsável pelo teste: {responsavel}")

print (50*"-")
print(f"Data de execução: {data_de_execucao}")
print (50*"-")
print(f"Testes aprovados: 35")
print(f"Testes reprovados: 10")
print(f"Testes não executados: 5")

#---------------------------------------------------
aprovados= 35
reprovados = 10
naoexecutados = 5
#-------------------

total_de_testes = aprovados + reprovados + naoexecutados
testesexecutados= aprovados+ reprovados
taxadereprovação = (reprovados /testesexecutados) * 100
taxadeaprovacao =(aprovados /testesexecutados) *100
taxadenaoexecutados = (naoexecutados / total_de_testes) * 100
print (f"total_de_testes{total_de_testes}")
print (f"testes executados: {testesexecutados}")
print (f"testes aprovados: {aprovados}")
print (f"taxa de nao executados: { naoexecutados}")