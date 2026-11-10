from datetime import datetime


def gerar_relatorio(
    projeto, modulo, branch, responsavel, data_execucao=None
):
    # Define a data atual automaticamente caso nenhuma seja informada
    if data_execucao is None:
        data_execucao = datetime.now().strftime("%d/%m/%Y")

    largura = 46
    linha = "=" * largura

    print(linha)
    print("RELATÓRIO DE EXECUÇÃO DE TESTES".center(largura))
    print(linha)
    print()
    print(f"Projeto: {projeto}")
    print(f"Módulo: {modulo}")
    print(f"Branch: {branch}")
    print(f"Responsável: {responsavel}")
    print(f"Data da execução: {data_execucao}")
    print()
    print(linha)
    print("INICIALIZAÇÃO CONCLUÍDA".center(largura))
    print(linha)


# Exemplo de uso
gerar_relatorio(
    projeto="Sistema Financeiro",
    modulo="Autenticação",
    branch="feature/login-seguro",
    responsavel="Ana Souza",
    data_execucao="09/11/2026",
)
