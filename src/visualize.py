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
    
def plot_comunidades_com_pagerank(G: nx.Graph, comunidades_dict: dict, pagerank_dict: dict, num_top: int = 5):
    """
    Plota um grafo com cores diferentes para cada comunidade e destaca os nós com maior PageRank.
    """
    pos = nx.spring_layout(G, seed=42)

    # Define as cores das comunidades (baseado no valor inteiro da comunidade)
    cores = [comunidades_dict[n] for n in G.nodes]
    
    # Normaliza os tamanhos com base no PageRank
    tamanhos = [pagerank_dict[n] * 5000 for n in G.nodes]

    # Define cor vermelha para os top influentes (por cima das cores de comunidade)
    top_influentes = sorted(pagerank_dict, key=pagerank_dict.get, reverse=True)[:num_top]

    plt.figure(figsize=(12, 10))
    nx.draw(G, pos,
            node_color=cores,
            cmap=plt.cm.Set3,
            node_size=tamanhos,
            edge_color="lightgray",
            with_labels=False)

    # Destaca os top N com borda vermelha
    nx.draw_networkx_nodes(G, pos,
                           nodelist=top_influentes,
                           node_color='none',
                           edgecolors='red',
                           linewidths=2.5,
                           node_size=[pagerank_dict[n]*5000 for n in top_influentes])

    plt.title(f"Comunidades com destaque para os Top {num_top} influentes (PageRank)")
    plt.axis("off")
    plt.show()


def exportar_para_gephi(G: nx.Graph, caminho_saida: str = "grafo_para_gephi.gexf"):
    """
    Exporta o grafo para um arquivo .gexf (compatível com o Gephi).
    """
    nx.write_gexf(G, caminho_saida)
    print(f"Grafo exportado para: {caminho_saida}")
    
def exportar_para_gephi_com_atributos(
    G: nx.Graph,
    pagerank_dict: dict,
    comunidades_dict: dict,
    caminho_saida: str = "grafo_para_gephi.gexf"
    ):
    """
    Exporta o grafo para um arquivo GEXF com atributos de PageRank e Comunidade,
    prontos para visualização no Gephi.
    """
    # Atribui os atributos aos nós
    nx.set_node_attributes(G, pagerank_dict, "pagerank")
    nx.set_node_attributes(G, comunidades_dict, "comunidade")

    # Exporta para arquivo GEXF
    nx.write_gexf(G, caminho_saida)
    print(f"Grafo exportado para '{caminho_saida}' com atributos.")