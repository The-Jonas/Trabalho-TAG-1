## Construção do grafo a partir do dataset ##

import networkx as nx
import os

def load_graph_from_edges(file_path: str) -> nx.DiGraph:

    """Lê um arquivo .edges ou .txt com pares de usuários e retorna um grafo direcionado."""
    
    G = nx.read_edgelist(file_path, create_using=nx.DiGraph(), nodetype=int)
    return G    

def load_all_graphs_from_folder(folder_path: str) -> dict:
    
    """
    Lê todos os arquivos .edges dentro de uma pasta e cria um dicionário de grafos.
    Chave: nome base do arquivo (ex: '104615636')
    Valor: grafo NetworkX correspondente
    """
    
    graphs = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".edges"):
            base = filename.split(".")[0]
            path = os.path.join(folder_path, filename)
            G = load_graph_from_edges(path)
            graphs[base] = G
    return graphs