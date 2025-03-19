# Capítulo 2 - Ordenação por seleção

Neste capítulo
- Você terá conhecimento de arrays e listas encadeadas, exemplos básicos de estruturas de dados. Este capítulo irá expor os pós e contras de ambas as estruturas para que você possa decidir qual é ideal para seu algoritmo.

- Você aprenderá a fazer o seu primeiro algoritmo de ordenação. Muitos dos algoritmos só funcionam se os dados inseirdos estiverem ordenados. Este capítulo apresentará a ordenação por seleção.

## Como funciona a memória
Imagina que você possui algumas roupas passadas e deseja guardá-las no armário de seu pai. Algumas das gavetas estão disponíveis.

Cada gaveta pode guardar apenas uma roupa. Você deseja guardar duas roupas, então pede duas gavetas à seu pai. Então, você guardou suas roupas no armário. É mais ou menos assim que a memória de seu computador funciona. O ***computador*** se parece com **um grande conjunto de gavetas**, e cada gaveta possui seu **prório endereço**.

Cada vez que você quer *armazenar um item na memória*, você pede ao computador um pouco de espaço e ele te dá um **endereço** no qual você pode armazenar seu item. Se quiser armazenar múltiplos itens, existem duas maneiras para se fazer isso: **arrays** e **listas**. 

## Arrays e listas encadeadas
Suponha que você está criando uma aplicação para gerenciar uma lista de tarefas. Nesta aplicação, é preciso armazenar tais tarefas em um espaço na memória. Você deverá umas uma lista encadeada ou um array?

Entenda que, **usar um array**, significa que todas as suas tarefas serão armazenadas contiguamente (uma ao lado da outra) na memória. Suponha que você deseja armazenar mais uma tarefa, porém o próximo endereço já está armazenado por dados de outra aplicação na memória. 

É basicamente você pensar como uma fileira no cinema, e você deseja comprar alguns assentos para você e seus amigos, porém apenas 3 conseguirão sentar juntos, enquanto outros terão que pular 1 ou mais cadeiras. Neste casos, vocês precisariam se mover para encontrar um outro lugar onde todos sentassem juntos. Então, voltando ao caso do computador, você precisaria solicitar uma área da memória que coubesse todas as suas tarefas da aplicação. 

Caso apareça outro amigo, teriam que procurar um novo espaço para sentarem todos juntos, e isso é bastante incômodo! Da mesma forma, **adicionar novos itens a um array é bastante lento.** Uma maneira de se resolver isso é **armazendando lugares**: mesmo que você já possua 3 itens em sua lista de tarefas, você solicita ao computador 10 espaços, por garantia. Portanto, você poderá adicionar até 10 itens em sua lista sem precisar se preocupar em mudança de lugares. No entanto, isso possui algumas desvantagens:
- Você pode não precisar dos espaço que você armazenou, e isso pode acabar resultando em **espaço desperdiçado na memória**.

- Você precisará adicionar mais 10 itens na lista de tarefas, e então precisará mudar de local novamente com seus itens de qualquer maneira.

Em casos assim, **listas encadeadas** resolvem este problema com uma solução simples.

### Listas encadeadas

Com as listas encadeadas, seus dados podem estar armazenados em **qualquer lugar da memória**. Cada item armazena o endereço do próximo item da lista. Um monte de endereços aleatórios de memória estão ligados.

Adicionar um item na lista encadeado é fácil: você coloca em **qualquer lugar da memória** e **armazena o endereço do item anterior**. 

Ou seja, comparadas aos **arrays**, as **listas encadeadas** são *bem melhores* no quesito **inserção de dados**.

### Arrays

As **listas encadeadas** são ótimas para ***ler todos os itens de uma só vez***, porém *é péssima* para **consultar itens específicos da lista**, visto que é feita primeiro a consulta de seu endereço de memória, para assim ter acesso ao seu valor.

Já nos **arrays**, esta consulta é bem diferente, pelo simples fato de você saber o endereço de cada posição desde o início. Arrays *são ótimos* se você deseja **ler elementos aleatórios**, pois pode encontrar qualquer elemento instantaneamente em um array. 

## Terminologia

Os elementos em um array **são numerados**, com uma numeração iniciada em 0, e não em 1. Em quase todas as linguagens de programação começarão os arrays **numerando o primeiro** elemento como **0**.

A posição de um elemento do array é chamada de **índice**. Segue abaixo um exemplo de array:
```py
arr = [10, 22, 34, 46, 58]

print(arr[0]) # índice 0 = 10
print(arr[2]) # índice 2 = 34
```

Segue abaixo o tempo de execução em *operações comuns* de **arrays** e **listas**:

```
         | arrays | listas
leitura  |  O(1)  |  O(n)
inserção |  O(n)  |  O(1)

O(n) = Tempo de execução linear
O(1) = Tempo de execução constante
```

## Inserindo algo no meio da lista

Imagine um caso onde você deseja *inserir itens no meio de uma lista*. Onde seria mais eficaz utilizar esta modificação: em um array ou lista encadeada?

No casos das **listas**, basta *mudar apenas o endereço para o qual o elemento anterior está apontando*. Já para os **arrays**, você *deverá mudar todos os itens que estão abaixo do endereço de inserção*.

## Deleções

E no caso de deletar um elemento? Novamente, nas **listas** será feita apenas *a mudança do endereço apontado pelo item anterior*, enquanto nos **arrays**, *tudo precisa ser movido quando um elemento é removido*.

Ao contrário da situação de inserção, a remoção de itens sempre terá sucesso. Pois, poderá falahar quando não houver mais espaço suficiente na memória.

Novamente, aqui estão os exemplos de tempo de execução para **operações comuns** em *arrays* e *lista encadeadas*:

```
           | arrays | listas
leitura    |  O(1)  |  O(n)
inserção   |  O(n)  |  O(1)
eliminação |  O(n)  |  O(1)
```

**OBS1**: Vale mensionar que inserções e eliminações terão tempo de execução O(1) somente se você puder acessar instantaneamente o elemento a ser deletado.

**OBS2**: Para os arrays, existem dois tipos de acessos: o *sequencial* e o *aleatório*. Já para as listas, existe apenas o acesso *sequencial*