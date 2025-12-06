# greedy.py
# Implementação simples do algoritmo de coloração Greedy
#
# Autor: Luiza da Costa Caxeixa
# Disciplina: Teoria dos Grafos
# Ano: 2025

def greedy_coloring(graph):
    """
    Executa o algoritmo Greedy de coloração de grafos.
    
    Parâmetros:
        graph (dict): grafo representado como lista de adjacência
                      {vértice: [vizinhos]}
    
    Retorna:
        dict: mapeamento {vértice: cor}
    """

    # Inicializa todas as cores como 0 (não colorido)
    color = {v: 0 for v in graph}

    # Ordena os vértices arbitrariamente (ordem dos nós)
    for v in graph:
        # Cores já usadas pelos vizinhos
        forbidden_colors = {color[u] for u in graph[v] if color[u] != 0}

        # Escolhe a menor cor disponível
        c = 1
        while c in forbidden_colors:
            c += 1
        
        color[v] = c

    return color


if __name__ == "__main__":
    # Exemplo simples (mesmo grafo usado no DSATUR)
    graph_example = {
        "A": ["B", "C"],
        "B": ["A", "C", "D", "E"],
        "C": ["A", "B", "D"],
        "D": ["B", "C", "E"],
        "E": ["B", "D"]
    }

    result = greedy_coloring(graph_example)

    print("Coloração final obtida pelo Greedy:")
    for v in sorted(result):
        print(f"Vértice {v}: cor {result[v]}")
