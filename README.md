# Trabalho-TAG-1

# 📊 Detecção de Desinformação em Redes Sociais com Teoria dos Grafos

Este projeto foi desenvolvido para a disciplina de **Teoria e Aplicação de Grafos (TAG)** e tem como objetivo aplicar conceitos de grafos para identificar **nós influentes** e **padrões de desinformação** em redes sociais.

###📎 Autores**

João Victor Pereira Vieira
Albert Teixeira Soares
Marcus Paulo Kaller Vargas

## 📁 Estrutura do Projeto

Trabalho-Tag-1/
│
├── data/ # Dados reais do Twitter
│ └── twitter_combined.txt
│
├── src/ # Código-fonte do projeto
│ ├── build_graph.py                                        # Construção do Grafo
│ ├── analysis.py                                           # Análise de centralidades, comunidades e PageRank
│ └── visualize.py                                          # Visualizações e exportação para Gephi
│
├── main.ipynb # Notebook com explicações e análises        # Notebook principal de execução
├── requirements.txt # Lista de bibliotecas usadas          # Dependências do projeto
├── README.md                                               # Este arquivo
└── proj1-tag-a-2025-1.pdf                                  # Descrição do trabalho

## ⚙️ Como rodar o projeto

1. ** Instale as dependências ** 

🧪 Requisitos
- Python 3.9+

- NetworkX

- Matplotlib

- Pandas

- python-louvain

- notebook (Jupyter)

*Instale tudo com:*

pip install -r requirements.txt

2. ** Se quiser, abra o notebook no navegador **

Utilize no terminal: "jupyter notebook"

## 📌 Algoritmos aplicados:

PageRank

Centralidade de Grau, Intermediação e Proximidade

Detecção de comunidades (Louvain, Girvan-Newman)

Visualização com matplotlib e exportação para Gephi

## 📥 Dataset:

Utilizamos o dataset twitter_combined.txt, que representa interações entre usuários no Twitter.
Cada linha possui dois usuários (user1 user2), indicando que user1 interagiu com user2.