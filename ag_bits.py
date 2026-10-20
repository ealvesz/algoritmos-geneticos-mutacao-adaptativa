import random


def aptidao(cromossomo):
    return sum(cromossomo)


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


def ag(tam_pop=20, tam_crom=10, geracoes=50, n_elite=2):
    pop = criar_populacao(tam_pop, tam_crom)

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
            melhor = max(aptidao(ind) for ind in pop)
            print(
                f"Geração {ger + 1:2d}: "
                f"Melhor aptidão = {melhor} | "
                f"pm = {pm:.4f}"
            )

    return pop


melhor = max(ag(), key=aptidao)

print("\nMelhor solução:", melhor)
print("Aptidão:", aptidao(melhor)) 