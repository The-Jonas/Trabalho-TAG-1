import networkx as nx
import matplotlib.pyplot as plt

def plot_grafo_basico(G: nx.Graph, num_nodes: int = 200):
    """
    Mostra uma visualização rápida de uma amostra do grafo.
    """
    if G.number_of_nodes() > num_nodes:
        # Amostra para evitar sobrecarregar a tela
        G = G.subgraph(list(G.nodes)[:num_nodes])

    pos = nx.spring_layout(G, seed=42)  # Layout por força

    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, node_size=30, edge_color="gray", node_color="skyblue", with_labels=False)
    plt.title("Visualização básica do grafo")
    plt.show()


def plot_pagerank(G: nx.Graph, pagerank_dict: dict, num_nodes: int = 200):
    """
    Mostra o grafo com tamanho dos nós baseado no PageRank.
    """
    if G.number_of_nodes() > num_nodes:
        G = G.subgraph(list(G.nodes)[:num_nodes])
        pagerank_dict = {n: pagerank_dict[n] for n in G.nodes}

    pos = nx.spring_layout(G, seed=42)
    sizes = [pagerank_dict[n]*5000 for n in G.nodes]  # Escala do tamanho dos nós

    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, node_size=sizes, edge_color="gray", node_color="orange", with_labels=False)
    plt.title("Tamanho dos nós proporcional ao PageRank")
    plt.show()


def exportar_para_gephi(G: nx.Graph, caminho_saida: str = "grafo_para_gephi.gexf"):
    """
    Exporta o grafo para um arquivo .gexf (compatível com o Gephi).
    """
    nx.write_gexf(G, caminho_saida)
    print(f"Grafo exportado para: {caminho_saida}")