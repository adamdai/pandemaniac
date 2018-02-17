import json
import argparse 
import networkx as nx
import heapq
import operator

NUM_ROUNDS = 50

# eignenvector centrality
def eigen_run(graph, num_seeds, num_players):
    json_data = open(graph).read()
    graph = json.loads(json_data)

    G = nx.Graph()

    for node in graph:
        G.add_node(node)
        for link in graph[node]:
            G.add_node(link)
            G.add_edge(node,link)

    c = nx.eigenvector_centrality(G)
    b = nx.degree_centrality(G)
    d = dict(heapq.nlargest(num_seeds, c.items(), key=operator.itemgetter(1)))
    d1 = dict(heapq.nlargest(num_seeds, b.items(), key=operator.itemgetter(1)))
    
    file = open("seed_nodes.txt", "w")
    for i in range(NUM_ROUNDS):
    	for key in d:
    		file.write(key + '\n')
    file.close()

    return d.keys()

if __name__ == '__main__':
    eigen_run('2.5.1.json', 5, 1)