# Trabalho-TAG-1

Este projeto visa analisar redes sociais reais e identificar espalhadores de notícias falsas usando algoritmos de grafos aplicados a dados do Twitter.

## 📁 Estrutura do Projeto

grafo-fake-news/
│
├── data/ # Dados reais do Twitter
│ └── twitter_combined.txt
│
├── src/ # Código-fonte do projeto
│ ├── build_graph.py
│ ├── analysis.py
│ └── visualize.py
│
├── main.ipynb # Notebook com explicações e análises
├── requirements.txt # Lista de bibliotecas usadas
└── README.md 

## ⚙️ Como rodar o projeto


1. ** Instale as dependências ** 

pip install -r requirements.txt

2. ** Abra o notebook no navegador **

jupyter notebook

## 📌 Algoritmos aplicados:

PageRank

Centralidade de Grau, Intermediação e Proximidade

Detecção de comunidades (Louvain, Girvan-Newman)

Visualização com matplotlib e exportação para Gephi