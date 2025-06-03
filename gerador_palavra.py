#vai sortear as palavras

import random


def palavra_sortear(caminho= "palavras.txt"):
    with open(caminho,"r", encoding="UTF-8") as f:
        palavras = [linha.strip() for linha in f if linha.strip()]
    return random.choice(palavras)