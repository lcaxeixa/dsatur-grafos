from collections import defaultdict


class Graph:
    """Representação de grafo utilizando lista de adjacência."""

    def __init__(self):
        self.adj = defaultdict(list)
        self.colors = {}  # Armazena a cor final de cada vértice

    def add_edge(self, u, v):
        """Adiciona uma aresta não direcionada."""
        self.adj[u].append(v)
        self.adj[v].append(u)

    def neighbors(self, v):
        """Retorna os vizinhos do vértice v."""
        return self.adj[v]

    def saturation(self, v):
        """Calcula o grau de saturação: número de cores distintas nos vizinhos de v."""
        used_colors = {self.colors[n] for n in self.neighbors(v) if n in self.colors}
        return len(used_colors)

    def available_color(self, v):
        """Retorna a menor cor possível que não está sendo usada pelos vizinhos."""
        forbidden = {self.colors[n] for n in self.neighbors(v) if n in self.colors}
        color = 1
        while color in forbidden:
            color += 1
        return color


def dsatur(graph):
    """
    Executa o algoritmo DSATUR no grafo fornecido.
    Retorna um dicionário com a cor final de cada vértice.
    """

    # Começa com todos vértices não coloridos
    vertices = list(graph.adj.keys())

    # Escolhe o vértice inicial: o de maior grau
    start = max(vertices, key=lambda v: len(graph.neighbors(v)))
    graph.colors[start] = 1  # colore com a primeira cor

    # Enquanto existirem vértices não coloridos…
    while len(graph.colors) < len(vertices):

        # Seleciona o vértice com maior saturação
        # Em caso de empate, desempate pelo maior grau
        uncolored = [v for v in vertices if v not in graph.colors]

        v = max(
            uncolored,
            key=lambda x: (
                graph.saturation(x),
                len(graph.neighbors(x))
            )
        )

        # Atribui cor ao vértice escolhido
        graph.colors[v] = graph.available_color(v)

    return graph.colors


# ---------------------------------------------------------------------
# Exemplo de uso com o mesmo grafo de teste ilustrado no relatório
# ---------------------------------------------------------------------
if __name__ == "__main__":
    g = Graph()

    edges = [
        ("A", "B"),
        ("A", "C"),
        ("B", "C"),
        ("B", "D"),
        ("C", "D"),
        ("C", "E"),
        ("D", "E"),
    ]

    for u, v in edges:
        g.add_edge(u, v)

    result = dsatur(g)

    print("\nColoração final obtida pelo DSATUR:")
    for v in sorted(result.keys()):
        print(f"Vértice {v}: cor {result[v]}")
