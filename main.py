from Diagnostico import *
from Perguntas import *

# Inferência
se = Diagnostico()
perguntas = Perguntas()

while se.probabilidade() != 100:
    pergunta = perguntas.proxima()
    se.pergunta(pergunta[0], pergunta[1])
    print('probabilidade é %d' % (se.probabilidade()))
    print(se.resultado)
    if se.probabilidade() == 100:
        print('O seu Pet está: ', se.resultado[0])
