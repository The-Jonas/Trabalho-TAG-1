# Não esquecer de utilizar "pip install -r requirements.txt" no terminal antes

import networkx as nx
import pandas as pd
from collections import defaultdict

def build_graph_from_txt(path: str) -> nx.DiGraph:
    """
    Lê um arquivo com interações (user1 user2 por linha)
    e retorna um DiGraph com pesos baseados na frequência de interação.
    """

    edge_weights = defaultdict(int)  # Cria um dicionário para contar interações entre pares

    # Lê o arquivo linha por linha
    with open(path, "r") as file:
        for line in file:
            u1, u2 = line.strip().split()
            edge_weights[(u1, u2)] += 1  # Conta quantas vezes (u1 -> u2) aparece

    # Cria o grafo direcionado
    G = nx.DiGraph()
    for (u1, u2), weight in edge_weights.items():
        G.add_edge(u1, u2, weight=weight)  # Arestas com peso baseado na frequência

    return G