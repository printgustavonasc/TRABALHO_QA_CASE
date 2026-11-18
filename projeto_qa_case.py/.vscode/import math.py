from builtins import print
import math
import time
import os

# ==========================================
# 1. CONFIGURAÇÕES
# ==========================================

TAMANHO_X = 100
TAMANHO_Y = 100

GRAVIDADE = 9.81

# Amplitude, comprimento, direção e fase
ondas = [
    (2.5, 40, 0, 0),
    (1.2, 20, math.pi / 6, 0.5),
    (0.6, 10, -math.pi / 4, 1.2)
]

# ==========================================
# 2. CÁLCULO DAS ONDAS
# ==========================================

def calcular_altura(x, y, tempo):

    altura = 0

    for amplitude, comprimento, direcao, fase in ondas:

        k = 2 * math.pi / comprimento

        omega = math.sqrt(GRAVIDADE * k)

        distancia = (
            x * math.cos(direcao)
            + y * math.sin(direcao)
        )

        onda = amplitude * math.cos(
            k * distancia - omega * tempo + fase
        )

        altura += onda

    return altura


# ==========================================
# 3. GERAÇÃO DA SUPERFÍCIE
# ==========================================

def gerar_superficie(tempo, resolucao=20):

    superficie = []

    passo_x = TAMANHO_X / resolucao
    passo_y = TAMANHO_Y / resolucao

    for linha in range(resolucao + 1):

        pontos = []

        for coluna in range(resolucao + 1):

            x = -50 + coluna * passo_x
            y = -50 + linha * passo_y

            z = calcular_altura(x, y, tempo)

            pontos.append((x, y, z))

        superficie.append(pontos)

    return superficie


# ==========================================
# 4. REPRESENTAÇÃO TEXTUAL DO OCEANO
# ==========================================

def representar_oceano(superficie):

    simbolos = " .:-=+*#%@"

    for linha in superficie:

        representacao = ""

        for x, y, z in linha:

            indice = int((z + 5) / 10 * (len(simbolos) - 1))

            indice = max(0, min(indice, len(simbolos) - 1))

            representacao += simbolos[indice]

        print(representacao)


# ==========================================
# 5. EXECUÇÃO DA SIMULAÇÃO
# ==========================================

def iniciar_simulacao():

    tempo = 0
    duracao = 50 
    fps = 5

    while tempo <= duracao:

        os.system("cls" if os.name == "nt" else "clear")

        superficie = gerar_superficie(tempo)

        print("SIMULADOR DE ONDAS OCEANICAS")
        print("--------------------------------")
        print("Tempo:", round(tempo, 2), "segundos")
        print("Gravidade:", GRAVIDADE, "m/s²")
        print("--------------------------------")

        representar_oceano(superficie)

        time.sleep(1 / fps)

        tempo += 1 / fps


# ==========================================
# 6. INICIAR
# ==========================================

iniciar_simulacao()

# ==========================================
# PLATAFORMA OFFSHORE
# ==========================================

ALTURA_CONVÉS = 8
PROFUNDIDADE = -10

LARGURA_CONVÉS = 15

# Coordenadas dos pilares
pilares = [
    (-7.5, -7.5),
    ( 7.5, -7.5),
    (-7.5,  7.5),
    ( 7.5,  7.5)
]


def verificar_plataforma(x, y):

    # Verifica se o ponto pertence ao convés
    if (
        abs(x) <= LARGURA_CONVÉS / 2
        and abs(y) <= LARGURA_CONVÉS / 2
    ):
        return True

    return False


def verificar_pilares(x, y):

    for px, py in pilares:

        if abs(x - px) <= 0.8 and abs(y - py) <= 0.8:
            return True

    return False


def calcular_estrutura(x, y, altura_onda):

    if verificar_plataforma(x, y):
        return "C"

    if verificar_pilares(x, y):
        return "P"

    return None

def representar_oceano(superficie):

    simbolos = " &&&&&&&&&&"

    for linha in superficie:

        representacao = ""

        for x, y, z in linha:

            estrutura = calcular_estrutura(x, y, z)

            if estrutura == "C":
                representacao += "C"

            elif estrutura == "P":
                representacao += "P"

            else:

                indice = int(
                    (z + 5) / 10 * (len(simbolos) - 1)
                )

                indice = max(
                    0,
                    min(indice, len(simbolos) - 1)
                )

                representacao += simbolos[indice]

        print(representacao)