from collections import deque


def caminho(pai, ondeSeChegou):
    noAtual = ondeSeChegou
    caminho = [noAtual]
    while pai[noAtual] is not None:
        caminho.append(pai[noAtual])
        noAtual = pai[noAtual]
    caminho.reverse()
    return print(caminho)


def buscaPorProfundidade(graph, pontoDePartida, ondeSeQuerChegar):
    filaDePesquisa = deque()
    paiVerticeAtual = {}
    paiVerticeAtual[pontoDePartida] = None
    if pontoDePartida == ondeSeQuerChegar:
        return print([ondeSeQuerChegar])
    # verifica se todos os parâmetros são válidos
    if graph and pontoDePartida and ondeSeQuerChegar:
        filaDePesquisa += graph[pontoDePartida]
        for filho in graph[pontoDePartida]:
            paiVerticeAtual[filho] = pontoDePartida
        verificados = []
        while filaDePesquisa:
            vertice = filaDePesquisa.pop()
            if vertice not in verificados:
                if vertice == ondeSeQuerChegar:
                    return caminho(paiVerticeAtual, vertice)
                else:
                    filaDePesquisa += graph[vertice]
                    for filho in graph[vertice]:
                        if paiVerticeAtual.get(filho) is None:
                            paiVerticeAtual[filho] = vertice
                    verificados.append(vertice)
        return print("Não é possível chegar nesse ponto")
    return print("Algum dos parâmetros está vazio")


# GRAFO criado com base nessa imagem: https://1.bp.blogspot.com/-jV48h9FYW1g/WP4AauTvCmI/AAAAAAAAAS8/ut8uvDj743A8ajByWAH83be39B-ay-JNgCLcB/s320/grafos%2Borientado%2Be%2Bn%25C3%25A3o%2Borientado.jpg
graph = {}
graph["A"] = ["B", "C"]
graph["B"] = ["C", "E"]
graph["C"] = ["D"]
graph["E"] = ["F"]
graph["D"] = ["G"]
graph["F"] = ["G", "J"]
graph["J"] = ["H"]
graph["H"] = ["I", "Z"]
graph["G"] = ["I"]
graph["I"] = []
graph["Z"] = []
buscaPorProfundidade(graph, "A", "Z")
buscaPorProfundidade(graph, "A", "G")
buscaPorProfundidade(graph, "A", "A")
