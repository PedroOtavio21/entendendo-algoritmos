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

