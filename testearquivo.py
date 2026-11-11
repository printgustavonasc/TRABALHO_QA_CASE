# criação das variaveis
projeto = "ShopVibe E-Commerce"
modulo = "Carrinho de Compras e Cupom de Desconto"
responsavel = "Lucas Oliveira"
data_execucao = "10/11/2026"
testes_aprovados = 35
testes_reprovados = 10
testes_nao_executados = 5

# cálculo do total e dos executados
total_testes = testes_aprovados + testes_reprovados + testes_nao_executados
testes_executados = testes_aprovados + testes_reprovados

# cálculo das taxas percentuais
taxa_aprovacao = (testes_aprovados / testes_executados) * 100
taxa_reprovacao = (testes_reprovados / testes_executados) * 100
taxa_nao_executados = (testes_nao_executados / total_testes) * 100

# exibição do relatório no terminal
print("========================================")
print("     RELATÓRIO DE EXECUÇÃO DE TESTES")
print("========================================")
print(f"Projeto: {projeto}")
print(f"Módulo: {modulo}")
print(f"Responsável: {responsavel}")
print(f"Data da execução: {data_execucao}")
print("----------------------------------------")
print("RESULTADOS REGISTRADOS")
print("----------------------------------------")
print(f"Testes aprovados: {testes_aprovados}")
print(f"Testes reprovados: {testes_reprovados}")
print(f"Testes não executados: {testes_nao_executados}")
print("----------------------------------------")
print("MÉTRICAS DA EXECUÇÃO")
print("----------------------------------------")
print(f"Total de testes: {total_testes}")
print(f"Testes executados: {testes_executados}")
print(f"Taxa de aprovação: {taxa_aprovacao:.1f}%")
print(f"Taxa de reprovação: {taxa_reprovacao:.1f}%")
print(f"Taxa de não executados: {taxa_nao_executados:.2f}%")
print("----------------------------------------")
print("CÁLCULOS CONCLUÍDOS")
print("----------------------------------------")