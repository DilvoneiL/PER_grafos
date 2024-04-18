import networkx as nx
import matplotlib.pyplot as plt

def ler_grafo_arquivo(nome_arquivo):
    grafo = nx.DiGraph()
    with open(nome_arquivo, 'r') as f:
        for linha in f:
            origem, destino, peso = linha.split()
            grafo.add_edge(int(origem), int(destino), weight=int(peso))
    return grafo

def calcular_tempos(grafo):
    es = {n: 0 for n in grafo.nodes}
    for n in nx.topological_sort(grafo):
        es[n] = max([es[pred] + grafo[pred][n]['weight'] for pred in grafo.predecessors(n)], default=0)

    ts = {n: es[n] for n in grafo.nodes}
    for n in reversed(list(nx.topological_sort(grafo))):
        ts[n] = min([ts[succ] - grafo[n][succ]['weight'] for succ in grafo.successors(n)], default=es[n])

    return es, ts

def identificar_caminho_critico(grafo, es, ts):
    caminho_critico = [n for n in grafo.nodes if es[n] == ts[n]]
    return caminho_critico

def main():
    nome_arquivo = 'grafo.txt'
    grafo = ler_grafo_arquivo(nome_arquivo)
    es, ts = calcular_tempos(grafo)
    caminho_critico = identificar_caminho_critico(grafo, es, ts)

    print("Tempos mais cedo:")
    print(es)
    print("\nTempos mais tarde:")
    print(ts)
    print("\nCaminho crítico:")
    print(caminho_critico)

    nome_arquivo_saida = 'grafo_com_informacoes.png'

if __name__ == "__main__":
    main()
