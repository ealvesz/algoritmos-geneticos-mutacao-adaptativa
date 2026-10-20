Algoritmos Genéticos com Mutação Adaptativa

Implementação de algoritmos genéticos em Python, utilizando uma taxa de mutação que muda ao longo das gerações. O projeto foi desenvolvido como atividade acadêmica para entender, na prática, como esse tipo de algoritmo pode ser usado para buscar soluções em problemas de otimização.

A implementação trabalha com dois problemas diferentes: maximizar a soma de uma sequência de bits e escolher itens para uma mochila respeitando um limite de peso.

A principal parte do exercício é a mutação adaptativa: em vez de manter a mesma probabilidade de mutação durante toda a execução, o algoritmo começa com uma taxa maior e a reduz gradualmente conforme as gerações avançam.

Sobre o projeto

Algoritmos genéticos são métodos de busca inspirados em processos de evolução. Em vez de testar todas as soluções possíveis, o algoritmo mantém uma população de soluções candidatas e faz essa população evoluir ao longo de várias gerações.

Cada solução é representada por um cromossomo. Durante a execução, os indivíduos são avaliados, os mais promissores têm mais chances de contribuir para a próxima geração e novas soluções são criadas por meio de cruzamento e mutação.

Neste projeto, os dois programas utilizam essa ideia, mas cada um possui uma função de aptidão adequada ao problema que precisa resolver.

Objetivos

* Implementar algoritmos genéticos utilizando Python.
* Entender como representar soluções por meio de cromossomos binários.
* Avaliar a qualidade de cada indivíduo com uma função de aptidão.
* Aplicar seleção por torneio, cruzamento de um ponto e mutação.
* Modificar a taxa de mutação de acordo com o progresso das gerações.
* Utilizar elitismo para preservar os melhores indivíduos encontrados.
* Comparar a aplicação da mesma estrutura evolutiva em dois problemas de otimização.

Como funciona a mutação adaptativa?

A mutação altera genes de um cromossomo de acordo com uma probabilidade definida. Como os cromossomos deste projeto são binários, cada gene pode assumir o valor 0 ou 1. Quando ocorre uma mutação, o valor é invertido: 0 passa a ser 1, e 1 passa a ser 0.

Uma taxa fixa de mutação mantém a mesma probabilidade durante toda a execução. Neste projeto, a taxa é ajustada linearmente conforme o número de gerações avança.

Parâmetro	Valor
Taxa inicial de mutação	0,10 (10%)
Taxa final de mutação	0,001 (0,1%)
Estratégia	Redução linear
Momento do ajuste	A cada geração

A lógica utilizada é:

def taxa_adaptativa(geracao, max_geracoes,
                    pm_inicial=0.10, pm_final=0.001):
    if max_geracoes <= 1:
        return pm_final
    progresso = geracao / (max_geracoes - 1)
    pm = pm_inicial - progresso * (pm_inicial - pm_final)
    return pm

A variável progresso representa o avanço da execução entre a primeira e a última geração. A partir dela, o programa calcula a probabilidade de mutação correspondente à geração atual.

No início, a taxa de mutação é maior, permitindo que mais genes tenham a possibilidade de mudar. Ao longo da execução, essa taxa diminui, reduzindo gradualmente a quantidade esperada de alterações aleatórias.

É importante observar que a taxa representa a probabilidade de mutação de cada gene, e não a probabilidade de modificar o cromossomo inteiro. Portanto, mesmo com uma taxa baixa, ainda pode ocorrer mutação, e uma geração não necessariamente será melhor que a anterior.

Projeto 1 — Maximização da soma de bits

Arquivo: ag_bits.py

O primeiro programa trabalha com cromossomos binários de tamanho 10. Cada indivíduo representa uma possível solução para o problema de encontrar a maior soma possível dos genes.

Como cada gene vale 0 ou 1, o objetivo é encontrar um cromossomo com o maior número possível de bits iguais a 1.

Função de aptidão

A aptidão é calculada somando todos os genes:

def aptidao(cromossomo):
    return sum(cromossomo)

Por exemplo, o cromossomo [1, 0, 1, 1, 0] possui aptidão igual a 3, pois contém três genes com valor 1.

Para um cromossomo de tamanho 10, a aptidão máxima possível é 10, alcançada quando todos os genes são iguais a 1.

Configuração da execução

* Tamanho da população: 20 indivíduos.
* Tamanho de cada cromossomo: 10 genes.
* Número de gerações: 50.
* Elitismo: preservação dos 2 melhores indivíduos.
* Seleção: torneio com 3 participantes.
* Cruzamento: um ponto.
* Mutação: adaptativa, de 10% até 0,1%.

O que acontece durante a execução?

O programa cria uma população inicial aleatória e calcula a aptidão de seus indivíduos. Em seguida, ordena as soluções por aptidão e copia os dois melhores indivíduos para a próxima geração.

Para preencher as demais posições, realiza torneios para selecionar os pais, combina partes de seus cromossomos por meio do cruzamento e aplica a mutação adaptativa aos descendentes.

Esse processo se repete até o limite de gerações definido no código. Durante a execução, o programa exibe a melhor aptidão encontrada e a taxa de mutação utilizada em determinados intervalos.

Projeto 2 — Problema da mochila

Arquivo: ag_mochila.py

O segundo programa aplica a mesma estrutura de algoritmo genético a um problema mais próximo de uma situação real de otimização: escolher itens que proporcionem o maior valor total possível sem ultrapassar a capacidade de peso da mochila.

Cada item possui um peso e um valor. O cromossomo indica quais itens serão selecionados:

* 1: o item será colocado na mochila.
* 0: o item não será selecionado.

O objetivo é encontrar uma combinação de itens que maximize o valor total, respeitando a capacidade máxima definida no programa.

Dados do problema

* Quantidade de itens: 15.
* Capacidade máxima da mochila: 60 unidades de peso.
* Tamanho do cromossomo: 15 genes.
* Tamanho da população: 50 indivíduos.
* Número de gerações: 80.
* Elitismo: preservação dos 2 melhores indivíduos.
* Seleção: torneio com 3 participantes.
* Cruzamento: um ponto.
* Mutação: adaptativa, de 10% até 0,1%.

Os pesos e valores dos itens estão definidos nas listas PESOS e VALORES, no início do arquivo.

Cálculo da aptidão

A função de aptidão calcula o peso total e o valor total dos itens selecionados.

Se o peso ultrapassar a capacidade máxima, a solução recebe aptidão zero. Caso contrário, sua aptidão corresponde à soma dos valores dos itens escolhidos.

Dessa forma, o algoritmo favorece soluções que tenham valor elevado sem exceder o limite de peso estabelecido.

Uma solução com valor elevado, mas peso acima da capacidade, não é considerada válida pelo critério de aptidão utilizado.

Resultado apresentado

Ao longo das gerações, o programa informa a melhor aptidão encontrada, a média das aptidões válidas e a taxa de mutação.

No final, apresenta o cromossomo da melhor solução encontrada, seu valor total e o peso correspondente, permitindo conferir se a capacidade máxima foi respeitada.

Como o algoritmo utiliza operações aleatórias, os resultados podem mudar de uma execução para outra.

Etapas utilizadas nos dois algoritmos

1. Criação da população

O programa gera indivíduos aleatórios formados por genes binários. Essa população inicial representa o conjunto de soluções candidatas.

2. Avaliação da aptidão

Cada indivíduo é avaliado de acordo com o problema. No primeiro programa, a aptidão é a soma dos bits. No segundo, é o valor total dos itens, desde que o peso não ultrapasse a capacidade.

3. Seleção por torneio

O programa sorteia três indivíduos e escolhe aquele com a maior aptidão entre os participantes. Esse processo é utilizado para selecionar os pais que produzirão novos indivíduos.

4. Cruzamento de um ponto

Um ponto de corte é sorteado no cromossomo. Os genes anteriores ao corte vêm de um dos pais, enquanto os genes posteriores vêm do outro. Assim, o descendente combina características de duas soluções existentes.

5. Mutação adaptativa

Cada gene do descendente tem uma probabilidade de sofrer mutação. Essa probabilidade é calculada de acordo com a geração atual, diminuindo gradualmente do valor inicial ao final.

6. Elitismo

Os dois melhores indivíduos da população atual são copiados diretamente para a próxima geração. Isso evita que essas soluções sejam perdidas por causa das operações aleatórias de cruzamento e mutação.

7. Formação da próxima geração

Os novos indivíduos são adicionados à população até que ela alcance o tamanho definido. O processo continua até o número máximo de gerações.

Como executar o projeto

Requisitos

* Python 3 instalado.
* Visual Studio Code ou outro editor de código.
* Terminal para executar os programas.

O projeto utiliza o módulo random, que faz parte da biblioteca padrão do Python. Não é necessário instalar bibliotecas externas para executar os códigos.

Execução do primeiro algoritmo

No terminal, entre na pasta do projeto e execute:

python ag_bits.py

Execução do segundo algoritmo

python ag_mochila.py

Caso o comando python não funcione no Windows, tente:

py ag_bits.py

ou:

py ag_mochila.py

O que este projeto demonstra

Além de implementar os operadores básicos de um algoritmo genético, o projeto permite observar como a alteração de um parâmetro influencia o processo de busca.

A mutação adaptativa é uma estratégia para ajustar a exploração de novas soluções ao longo das gerações. Entretanto, reduzir a taxa de mutação não garante, por si só, que o algoritmo encontrará a solução ótima ou que a diversidade da população será sempre preservada.

Os dois programas utilizam a mesma ideia de evolução, mas mostram como a função de aptidão e as restrições precisam ser adaptadas ao problema trabalhado.

Tecnologias

* Python 3: implementação dos algoritmos.
* Visual Studio Code: ambiente utilizado no desenvolvimento.
* GitHub: armazenamento e compartilhamento do código-fonte.

Contexto acadêmico

Projeto desenvolvido como atividade acadêmica sobre implementação de mutação adaptativa em algoritmos genéticos, com foco na compreensão dos operadores evolutivos e na aplicação prática de técnicas de otimização.

Os códigos podem ser modificados para testar diferentes tamanhos de população, números de gerações e taxas de mutação, permitindo comparar o comportamento dos algoritmos em diferentes configurações.
