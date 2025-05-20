import networkx as nx
from typing import Dict, Tuple, List

# 1. PageRank
def calcular_pagerank(G: nx.DiGraph) -> Dict[str, float]:
    """
    Calcula o PageRank dos nós do grafo.
    """
    return nx.pagerank(G, alpha=0.85, weight="weight")


# 2. Centralidades
def calcular_centralidades(G: nx.DiGraph) -> Dict[str, Dict[str, float]]:
    """
    Calcula três medidas de centralidade:
    - Grau
    - Intermediação (betweenness)
    - Proximidade (closeness)
    """
    grau = nx.degree_centrality(G)
    intermediação = nx.betweenness_centrality(G)
    proximidade = nx.closeness_centrality(G)

    return {
        "grau": grau,
        "intermediacao": intermediação,
        "proximidade": proximidade
    }


# 3. Comunidades (Louvain)
def detectar_comunidades_louvain(G: nx.Graph) -> Dict[str, int]:
    """
    Detecta comunidades com o algoritmo de Louvain.
    Retorna um dicionário: nó → comunidade
    """
    try:
        import community as community_louvain  # pacotes python-louvain
    except ImportError:
        raise ImportError("Você precisa instalar o pacote `python-louvain` (pip install python-louvain)")

    # Louvain só funciona com grafos não direcionados
    G_undirected = G.to_undirected()
    partition = community_louvain.best_partition(G_undirected)

    return partition


# 4. Comunidades (Girvan-Newman - limitado)
def detectar_comunidades_girvan_newman(G: nx.Graph, num_comunidades: int = 5) -> List[List[str]]:
    """
    Detecta comunidades com Girvan-Newman.
    Retorna uma lista de grupos de nós (limitado ao número de comunidades desejado).
    """
    from networkx.algorithms.community import girvan_newman

    G_undirected = G.to_undirected()
    comunidades = girvan_newman(G_undirected)
    
    # Pega as primeiras k divisões
    for i, comunidades_atual in enumerate(comunidades):
        if i == num_comunidades - 2:
            return [list(c) for c in comunidades_atual]

    return []