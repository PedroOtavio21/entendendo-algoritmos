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

## Listas encadeadas

Com as listas encadeadas, seus dados podem estar armazenados em **qualquer lugar da memória**. Cada item armazena o endereço do próximo item da lista. Um monte de endereços aleatórios de memória estão ligados.

Adicionar um item na lista encadeado é fácil: você coloca em **qualquer lugar da memória** e **armazena o endereço do item anterior**. 