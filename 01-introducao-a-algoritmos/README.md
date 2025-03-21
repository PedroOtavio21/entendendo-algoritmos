# Capítulo 1 - Introdução a algoritmos
Neste capítulo:
- Você terá acesso ao fundamental para compreender o restante do livro
- Escreverá seu primeiro algoritmo de busca (pesquisa binária)
- Aprenderá como falar sobre o tempo de execução de um algoritmo (na notação Big O)
- Será apresentado a uma prática comum para projetar algoritmos (recursão)

## Introdução
"Um algoritmo é um conjunto de instruções que realizam uma tarefa".

Boa parte dos algoritmos do livro são usados para acelerar uma solução, ou solucionar um problema específico, ou ambos.

Cada algoritmo sempre seguirá o seguinte passo:
1. Descrição do algoritmo
2. Exemplo de código
3. Tempo de execução em notação "Big O".

## O que será aprendido sobre desempenho 
Neste capítulo, será abordado a comparação entre desempenho de diferentes algoritmos

Exemplo: "Você deverá utilizar merge sort (ordenação por mistura) ou quicksort (ordenação rápida)?", "Você deverá utilizar uma lista ou um array?"

## O que você aprenderá sobre solução de problemas?
Ao terminar o livro, certamente você aprenderá algoritmos de melhor aplicabilidade.

OBS.: Necessário ter conhecimento de algebra básica antes de iniciar a leitura do livro. Além disso, é necessário conhecer alguma linguagem de programação.

## Pesquisa binária
Vamos supor que você deseja encontrar uma palavra em inglês de um dicionário, que começa com a "K". Você começaria pelo início ou pela metade? A melhor resposta seria pelo meio, indo para cima ou para baixo.

Este é um **problema de busca**. Geralmente casos como este usam um algoritmo chamado de **pesquisa binária**.

A sua entrada é uma lista **ordenada de elementos**. Se o elemento que você busca está dentro desta lista, ele retornará a sua localização. Se não, retornará *null*.

### Exemplo de caso: "Estou pensando em um número entre 1 e 100".
Você deverá encontrar o número em que estou pensando em poucas tentativas possíveis. A cada tentativa, falarei se você está chutando muito para cima ou para baixo.

Digamos que você começou tentando com 1, 2, 3, 4... e assim por diante. Isso se chama de ***pesquisa simples***, e a cada tentativa, você está eliminando apenas **um número por vez**.

Uma técnica melhor seria começar pelo 50. Se eu falar "muito abaixo", você terá eliminado todos os números anteriores! (abaixo de 50). Na próxima tentativa, você tenta 75, e eu digo "muito alto", e novamente você elimina outros números (acima de 75). 

Com a ***pesquisa binária***, *você chuta um número intermediário e elimina a metade dos números restantes a cada tentativa*.

### Exemplo de caso: Palavra em dicionário.
Suponha que você esteja procurando uma palavra em um dicionário de 240000 palavras. ***No pior caso***, de quantas etapas você acha que a pesquisa precisaria?

Pesquisa simples: 240.000 etapas
Pesquisa binária: 18 etapas

Este número pequeno se deve ao fato de **estar sempre eliminando o número de palavras pela metade até restar apenas uma palavra**. 

De modo geral, para uma **lista** de ***n* números**, a pesquisa binária precisa do **Logarítmo de n na base 2**, enquanto uma pesquisa simples precisa de ***n*** tentativas.

### Exemplo prático 01:
Veja o exemplo de código em Python no arquivo "exemplo_01.py"

Para melhor entendimento pense nos seguintes passos:
- Entenda o escopo da função (Ela trabalha com uma lista ordenada e um item escolhido a ser procurado)
- Deverá ter um intervalo de busca ([0, 1, 2, ... , n - 1, n])
- O meio será sempre a metade (valor_inicial + valor_final / 2)
- O chute será sempre o meio da lista (lista[meio])
- O algoritmo deverá retornar o valor ou não (Null) 

## Tempo de execução
Geralmente, no meio da programação como um todo, é comum utilizar um algoritmo que otimize o máximo de tempo possível com o máximo de eficiência.

### Exemplo de casos: Pesquisa de números
Pesquisa simples em 100 números: no máximo 100 tentativas
Pesquisa binária em 100 números: no máximo 7 tentativas

Pesquisa simples em 4 bilhões números: no máximo 4 bilhões tentativas
Pesquisa binária em 4 bilhões números: no máximo 32 tentativas

Ou seja, a pesquisa binária é executada com ***tempo logarítmico***
- Pesquisa simples -> Tempo de execução linear: O(n)
- Pesquisa binária -> Tempo de execução logarítmico: O(Log n)

## Tempo de execução dos algoritmos cresce a taxas diferentes
Não basta saber quanto tempo um algoritmo leva para ser executado - você precisa saber se o tempo de execução aumenta conforme a lista aumenta! E é aí que a notação Big O entra.

A notação Big O não informa os segundos, caso esteja com dúvida. ***Ela permite que você compare o número de operações***, ou seja, **informa o quão rápido um algoritmo cresce**.

## Vendo diferentes tesmpos de execução Big O
Suponha que você tente desenhar uma grade com 16 divisões em um papel.

### Algoritmo 1
Uma forma de desenhar seria desenhar um bloco da grade por vez. Neste exemplo, você desenharia um total de 16 divisões em 16 etapas. 

Qual seria o tempo de execução? -> O(n)

### Algoritmo 2
Uma outra forma seria dobrar o papel. Dobre o papel de novo e de novo. A cada dobra, o número de divisões duplica

Logo, em 4 etapas você terá 16 dobras. Tempo de execução -> O(log n)

## Exemplos de tempo de execução Big O
Aqui estão cinco tempos de execução Big O bastante comuns, indo do mais rápido ao mais lento:

- O(log n), também conhecido como *tempo logarítmico*. Exemplo: **pesquisa binária**

- O(n), conhecido como *tempo linear*. Exemplo: **pesquisa simples**

- O(n * log n). Exemplo: um algorítmo rápido de ordenação, como a **ordenação quicksort** (capítulo 4)

- O(n²). Exemplo: um algoritmo lento de ordenação, como a **ordenação por seleção** (capítulo 2)

- O(n!). Exemplo: um algoritmo bastante lento, como o do **caixeiro-viajante** (a seguir!)

Pontos para revisar:
1. A rapidez de um algorítmo *não é medida em segundos*, mas sim pelo *crescimento do número de operações*

2. Em vez disso, discutimos sobre o *quão rapidamente o tempo de execução de um algoritmo aumenta* conforme o *número de elementos aumenta*.

3. O tempo de execução de algoritmos é expresso pela *notação Big O*.

4. **O(log n)** é *mais rápido* do que **O(n)**, e O(log n) *fica ainda mais rápido* conforme a lista **aumenta**.

## O caixeiro-viajante
"Aqui está o exemplo de um tempo de execução ruim. Ele é um problema famoso da *ciência da computação*, pois seu crescimento é apavorante e algumas pessoas muito inteligentes acreditam que ele possa ser melhorado."

Tal problema é chamado de "o problema do caixeiro-viajante."

### Exemplo de caso: Caixeiro-viajante
Você tem um caixeiro-viajante. O caixeiro precisa ir a 6 cidades. Tal sujeito quer passar por todas as cidades percorrendo uma distância mínima.

Podemos enxergar a solução da seguinte forma: analisar cada ordem possível de cidades para visitar. É somada a distância total e escolhido o caminho com menor distância percorrida. Com isso, existem 120 permutações para cinco cidades, logo, precisa-se de 120 operações para resolver o problema das 5 cidades. Para 6 cidades, precisa-se de 720 operações (ou permutações). Para 7 cidades são necessárias 5.050 operações, e assim por diante. 

De maneira geral, para n itens, é necessário n! operações para se chegar em um resultado. Portanto, seu tempo de execução é O(n!) ou *tempo fatorial*. Tal algoritmo, consome muitas operações, exceto em casos de números pequenos.

Você deve estar pensando: "Não haveria outra forma de resolver este algoritmo terrível?" Porém, não. Este é um problema sem uma solução, ou seja, não há um algoritmo mais rápido para resolver este problema.