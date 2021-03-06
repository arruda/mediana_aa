# -*- coding: utf-8 -*-
import random


def select_mediana(s, k):

    n_s = len(s)
    s_maiores = []
    s_medianas = []
    s_menores = []

    #: rand alguma posicao valida, que nao seja a primeira
    i = random.randint(0, n_s-1)

    #: arruma os sub conjuntos
    for j in xrange(0, n_s):
        if s[j] > s[i]:
            s_maiores.append(s[j])

        elif s[j] < s[i]:
            s_menores.append(s[j])
        else:
            s_medianas.append(s[j])

    n_s_medianas = len(s_medianas)
    n_s_menores = len(s_menores)

    #: faz as selecoes nos subconjuntos
    if k <= n_s_menores:
        #: nesse caso k é maior ou iqual ao numero de elementos
        #: no subconjuntos dos menores elementos

        #: logo fazemos uma busca pela mediana no grupo dos menores elementos.
        return select_mediana(s_menores, k)

    elif k > n_s_menores + n_s_medianas:
        #: nesse caso verificamos se K é maior que o num elementos
        #: no subconjunto dos menores e do subconjunto dos medianos juntos

        #: então fazemos uma busca no vetor dos maiores elementos,
        #: sendo que o novo K passa a ser K menos o numero de
        #: elementos em s_menores menos o numero de elementos em s_medianas.
        return select_mediana(s_maiores, k - n_s_menores - n_s_medianas)

    else:
        #: nesse caso é quando K é parte do subconjunto dos medianos
        #: logo o indice aleatorio "i" é de fato parte dos medianos,
        #: assim, i é a mediana. então retorna essa posição
        return s[i]
