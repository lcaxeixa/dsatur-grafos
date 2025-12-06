# Algoritmos DSATUR e Greedy Coloring — Coloração de Grafos

Este repositório contém implementações didáticas dos algoritmos **DSATUR** (Degree of Saturation) e **Greedy Coloring** (Coloração Gulosa). Ambos realizam a coloração de grafos, atribuindo cores a vértices de modo que nenhum par de vértices adjacentes compartilhe a mesma cor.

O DSATUR é um dos algoritmos mais clássicos e eficientes para coloração, enquanto o Greedy é utilizado como uma estratégia simples e comparativa.

---

## Objetivo

Este repositório disponibiliza:

- Implementações claras e comentadas dos algoritmos **DSATUR** e **Greedy**.  
- Um grafo exemplo com cinco vértices (A–E).
- A saída completa gerada por cada algoritmo.
- Código pronto para ser utilizado em análises e relatórios acadêmicos.

---

## Descrição dos Algoritmos

### **DSATUR (Degree of Saturation)**

O algoritmo DSATUR colore o grafo de forma iterativa, selecionando a cada passo:

1. O vértice com **maior saturação**, isto é, o maior número de cores distintas entre os vizinhos.
2. Em caso de empate, seleciona o vértice com **maior grau**.
3. Atribui ao vértice a **menor cor disponível**.

Esse processo continua até que todos os vértices estejam coloridos.

É um algoritmo mais sofisticado e geralmente resulta em uma coloração com menos cores do que métodos simples.

---

### **Greedy Coloring (Coloração Gulosa)**

O algoritmo Greedy percorre os vértices em uma ordem pré-definida e, para cada vértice:

1. Identifica as cores usadas pelos vizinhos já coloridos.
2. Atribui a **menor cor que não conflite** com os vizinhos.

É rápido e simples, mas a qualidade depende fortemente da ordem dos vértices e não garante uso mínimo de cores.

Serve como excelente comparação com o DSATUR.

---

## Estrutura do Repositório

dsatur-grafos/
    ├── dsatur.py           # Implementação do algoritmo DSATUR
    ├── greedy.py           # Implementação do algoritmo Greedy Coloring
    └── README.md


---

## Como Executar

Requisitos: **Python 3.x**

Execute os algoritmos com:

```bash
python3 dsatur.py
python3 greedy.py
```