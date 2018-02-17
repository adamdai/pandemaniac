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
    degree_sum = 0
    for node in graph:
        G.add_node(node)
        for link in graph[node]:
            G.add_node(link)
            G.add_edge(node,link)
    
    file = open("seed_nodes.txt", "w")
    for i in range(NUM_ROUNDS):
        for key in eig_d:
            file.write(key + '\n')  
    file.close()  

    return d.keys()



if __name__ == '__main__':
    eigen_run('2.5.1.json', 5, 1)
