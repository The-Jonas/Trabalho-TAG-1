Files:

---------------------------------------------------------------------------------------------------------------------------------------------------------------

nodeId.edges : The edges in the ego network for the node 'nodeId'. Edges are undirected for facebook, and directed (a follows b) for twitter and gplus.
The 'ego' node does not appear, but it is assumed that they follow every node id that appears in this file.

Tradução resumida: trata-se das arestas na rede, elas são não direcionadas para o Facebook e direcionadas para o Twitter e Gplus.
O nó 'ego' não aparece, mas presume-se que elas sigam todos os IDs de nó que aparecem neste arquivo.

---------------------------------------------------------------------------------------------------------------------------------------------------------------

nodeId.circles : The set of circles for the ego node. Each line contains one circle, consisting of a series of node ids.
The first entry in each line is the name of the circle.

Tradução resumida: O conjunto de círculos para o nó ego. Cada linha contém um círculo, consistindo em uma série de IDs de nó. A primeira entrada em cada
linha é o nome do círculo.

---------------------------------------------------------------------------------------------------------------------------------------------------------------

nodeId.feat : The features for each of the nodes that appears in the edge file.

Tradução resumida: Os recursos para cada um dos nós que aparecem no arquivo

---------------------------------------------------------------------------------------------------------------------------------------------------------------

nodeId.egofeat : The features for the ego user.

Tradução resumida: Os recursos para o usuário.

----------------------------------------------------------------------------------------------------------------------------------------------------------------

nodeId.featnames : The names of each of the feature dimensions. Features are '1' if the user has this property in their profile, and '0' otherwise.
This file has been anonymized for facebook users, since the names of the features would reveal private data.

Tradução resumida: Os nomes de cada uma das dimensões dos recursos. Os recursos recebem o valor "1" se o usuário tiver essa propriedade em seu perfil
e "0" caso contrário.

------------------------------------------------------------------------------------------------------------------------------------------------------------