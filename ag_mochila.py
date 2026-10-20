import random


PESOS = [12, 7, 11, 8, 9, 6, 14, 5, 4, 3, 10, 15, 2, 8, 13]
VALORES = [24, 13, 23, 15, 16, 11, 28, 9, 6, 5, 19, 30, 3, 14, 25]
CAPACIDADE_MAXIMA = 60
TAM_CROMOSSOMO = len(PESOS)


def aptidao(cromossomo):
    peso_total = sum(
        gene * peso for gene, peso in zip(cromossomo, PESOS)
    )
    valor_total = sum(
        gene * valor for gene, valor in zip(cromossomo, VALORES)
    )

    if peso_total > CAPACIDADE_MAXIMA:
        return 0

    return valor_total


def criar_populacao(tam_pop, tam_crom):
    return [
        [random.randint(0, 1) for _ in range(tam_crom)]
        for _ in range(tam_pop)
    ]


def crossover_um_ponto(pai1, pai2):
    ponto = random.randint(1, len(pai1) - 1)
    return pai1[:ponto] + pai2[ponto:]


def taxa_adaptativa(geracao, max_geracoes,
                    pm_inicial=0.10, pm_final=0.001):
    if max_geracoes <= 1:
        return pm_final

    progresso = geracao / (max_geracoes - 1)
    pm = pm_inicial - progresso * (pm_inicial - pm_final)
    return pm


def mutacao(cromossomo, pm):
    return [
        1 - gene if random.random() < pm else gene
        for gene in cromossomo
    ]


def ag(tam_pop=50, tam_crom=TAM_CROMOSSOMO,
       geracoes=80, n_elite=2):

    pop = criar_populacao(tam_pop, tam_crom)

    print("Iniciando a evolução!\n")

    for ger in range(geracoes):
        apts = [aptidao(ind) for ind in pop]
        pm = taxa_adaptativa(ger, geracoes)

        idx_ord = sorted(
            range(len(apts)),
            key=lambda i: apts[i],
            reverse=True
        )

        nova_pop = [pop[i].copy() for i in idx_ord[:n_elite]]

        while len(nova_pop) < tam_pop:
            t1 = random.sample(range(tam_pop), 3)
            t2 = random.sample(range(tam_pop), 3)

            pai1 = pop[max(t1, key=lambda i: apts[i])]
            pai2 = pop[max(t2, key=lambda i: apts[i])]

            filho = crossover_um_ponto(pai1, pai2)
            filho = mutacao(filho, pm)

            nova_pop.append(filho)

        pop = nova_pop

        if ger == 0 or (ger + 1) % 10 == 0 or ger == geracoes - 1:
            apts_atual = [aptidao(ind) for ind in pop]
            validas = [a for a in apts_atual if a > 0]
            media = sum(validas) / len(validas) if validas else 0
            melhor_atual = max(apts_atual)

            print(
                f"Geração {ger + 1:3d}: "
                f"Melhor aptidão = {melhor_atual:3d} | "
                f"Média válida = {media:.1f} | "
                f"pm = {pm:.4f}"
            )

    return pop


ultima_populacao = ag()

apts_finais = [aptidao(ind) for ind in ultima_populacao]
melhor_indice = apts_finais.index(max(apts_finais))
melhor_solucao = ultima_populacao[melhor_indice]

peso_final = sum(
    gene * peso for gene, peso in zip(melhor_solucao, PESOS)
)

print("\n--- RESULTADO FINAL ---")
print("Melhor cromossomo:", melhor_solucao)
print("Aptidão (valor total):", max(apts_finais))
print(f"Peso total na mochila: {peso_final} / {CAPACIDADE_MAXIMA}")