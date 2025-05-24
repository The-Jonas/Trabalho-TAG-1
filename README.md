# Trabalho-TAG-1

## 🧷Autores

João Victor Pereira Vieira  
Albert Teixeira Soares  
Marcus Paulo Kaller Vargas  

## 📊 Detecção de Desinformação em Redes Sociais com Teoria dos Grafos

Este projeto foi desenvolvido para a disciplina de **Teoria e Aplicação de Grafos (TAG)** e tem como objetivo aplicar conceitos de grafos para identificar **nós influentes** e **padrões de desinformação** em redes sociais.

## 📊 Exemplos de Aplicação
*Identificação de usuários espalhadores de fake news*  
*Visualização de bolhas de interação*  
*Estudo da difusão de informação em redes complexas*

## 📁 Estrutura do Projeto

```plaintext
Trabalho-Tag-1/  
│  
├── data/                                                   # Dados reais do Twitter  
│ └── twitter_combined.txt  
│  
├── src/                                                    # Código-fonte do projeto  
│ ├── build_graph.py                                        # Construção do Grafo  
│ ├── analysis.py                                           # Análise de centralidades, comunidades e PageRank  
│ └── visualize.py                                          # Visualizações e exportação para Gephi  
│  
├── main.ipynb # Notebook com explicações e análises        # Notebook principal de execução  
├── requirements.txt # Lista de bibliotecas usadas          # Dependências do projeto  
├── README.md                                               # Este arquivo  
└── proj1-tag-a-2025-1.pdf                                  # Descrição do trabalho  
```
## 📌 Algoritmos aplicados:

- PageRank

- Centralidade de Grau, Intermediação e Proximidade

- Detecção de comunidades (Louvain, Girvan-Newman)

- Visualização com matplotlib e exportação para Gephi

## 📥 Dataset:

Utilizamos o dataset twitter_combined.txt, que representa interações entre usuários no Twitter.
Cada linha possui dois usuários (user1 user2), indicando que user1 interagiu com user2.

## ⚙️ Como rodar o projeto

1. **Instale as dependências** 

🧪 Requisitos
- Python 3.9+

- NetworkX

- Matplotlib

- Pandas

- python-louvain

- notebook (Jupyter)

*Instale tudo com:*
```bash
pip install -r requirements.txt
```
2. **Se quiser, abra o notebook no navegador utlizando no terminal o código (opcional)**

```bash
jupyter notebook
```
# 🔧 Funcionalidades
As principais funções implementadas são:

### 📌 1. Construção do Grafo

```plaintext
from src.build_graph import build_graph_from_txt
G = build_graph_from_txt("data/twitter_combined.txt")
```
Cria um grafo direcionado com pesos nas arestas com base na frequência de interação entre usuários.

---

### 📌 2. Análise de Influência e Centralidades

```plaintext
from src.analysis import calcular_pagerank, calcular_centralidades
pagerank = calcular_pagerank(G)
centralidades = calcular_centralidades(G)
```
- **PageRank:** identifica os nós mais influentes.

- **Centralidade de Grau:** quem compartilha mais.

- **Centralidade de Intermediação:** quem conecta comunidades.

- **Centralidade de Proximidade:** quem espalha mais rápido.

---

### 📌 3. Detecção de Comunidades

```plaintext
from src.analysis import detectar_comunidades_louvain, detectar_comunidades_girvan_newman
particoes = detectar_comunidades_louvain(G)                 # Método eficiente
comunidades = detectar_comunidades_girvan_newman(G, 5)      # Método hierárquico
```
Permite identificar agrupamentos que podem indicar bolhas de desinformação.

---

### 📌 4. Visualizações

```plaintext
from src.visualize import plot_grafo_basico, plot_pagerank, plot_comunidades_com_pagerank
```

- **plot_grafo_basico:** visualização simples

- **plot_pagerank:** tamanho dos nós proporcional à influência

- **plot_comunidades_com_pagerank:** cores por comunidade + destaque aos influentes

---

### 📌 5. Exportação para Gephi

```plaintext
from src.visualize import exportar_para_gephi_com_atributos
exportar_para_gephi_com_atributos(G, pagerank, particoes)
```
Exporta o grafo com atributos de pagerank e comunidade para uso no Gephi.

  



