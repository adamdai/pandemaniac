import json
import argparse 
import networkx as nx
import heapq
import operator

def run(graph, num_seeds, num_players):
    json_data = open(graph).read()
    graph = json.loads(json_data)

    G = nx.Graph()

    for node in graph:
        G.add_node(node)
        for link in graph[node]:
            G.add_node(link)
            G.add_edge(node,link)

    c = nx.eigenvector_centrality(G)
    d = dict(heapq.nlargest(num_seeds, c.items(), key=operator.itemgetter(1)))

    print d

if __name__ == '__main__':
    run('testgraph1.json', 20, 1)