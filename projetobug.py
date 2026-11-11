#==========================================================================================================
#informações básicas
projeto= "ShopVibe E-commerce"
modulo = "Carrinho de compras e Cupom de Desconto"
responsavel="Lucas Oliveira"
data = "10/11/2026"

#quantidade de testes
aprovados = 35 
reprovados = 10
nao_executados = 5

#cálculos de taxas, totais etc. (Não alterar)
total_testes = aprovados + reprovados + nao_executados
testes_executados = aprovados + reprovados
taxa_de_aprovação = (aprovados / testes_executados) * 100 
taxa_de_reprovação = (reprovados / testes_executados) * 100
taxa_de_nao_executados = (nao_executados / total_testes) * 100  

#==========================================================================================================

#ORGANIZAÇÃO RELATÓRIO DE TESTES (PROJETO, MÓDULO, RESPONSÁVEL E DATA DE EXECUÇÃO.)
print(50*"=")
print(10*" " , "RELATÓRIO DE TESTES")
print(50*"=")

#PRINT RELATÓRIO DE TESTES (PROJETO, MÓDULO, RESPONSÁVEL E DATA DE EXECUÇÃO.)
print(f"Projeto Testado: {projeto}")
print(f"Módulo Testado: {modulo}")
print (f"Responsável pelo teste: {responsavel}")
print (f"Data de execução: {data}")

#ORGANIZAÇÃO RESULTADOS REGISTRADOS (TESTES APROVADOS, REPROVADOS, NÃO EXECUTADOS ETC.)
print(50*"=")
print(10*" " , "RESULTADOS REGISTRADOS ")
print(50*"=")


#PRINT RESULTADOS REGISTRADOS (TESTES APROVADOS, REPROVADOS, NÃO EXECUTADOS ETC.)
print (f"Testes aprovados: {aprovados}")
print (f"Testes reprovados {reprovados}")
print (f"Testes não executados: {nao_executados}")
print (f"Total de testes: {total_testes}")
print (f"Testes executados: {testes_executados}")
print (f"Taxa de aprovação: {taxa_de_aprovação:.2f}%")
print (f"Taxa de reprovação: {taxa_de_reprovação:.2f}%")
print(f"Taxa de não executados: {taxa_de_nao_executados:.2f}%")
print(50*"=")
