import json
import argparse 
import networkx as nx
import heapq
import operator

NUM_ROUNDS = 50

def run(graph, num_seeds, num_players):
    json_data = open(graph).read()
    graph = json.loads(json_data)

    G = nx.Graph()
    degree_sum = 0
    for node in graph:
        G.add_node(node)
        for link in graph[node]:
            G.add_node(link)
            G.add_edge(node,link)
    
    nodes = list(G)
    votes = {}
    for node in nodes:
        votes[node] = [0, 1]
        degree_sum += G.degree(node)
    avg_degree = degree_sum/len(nodes)

    seed_count = 0
    seeds = []

    while seed_count < num_seeds:
        for node in nodes:
            for neighbor in G.neighbors(node):
                votes[neighbor][0] = votes[neighbor][0] + votes[node][1]
        max_vote = 0

        for node in votes:
            if node not in seeds:
                if votes[node] > max_vote:
                    max_vote = votes[node]
                    influential = node
        votes[influential][1] = 0
        seeds.append(influential)
        for node in G.neighbors(influential):
            votes[node][1] = votes[node][1] - ( 1. / float(avg_degree))
        seed_count += 1

    print seeds


    eig = nx.eigenvector_centrality(G)
    deg = nx.degree_centrality(G)
    eig_d = dict(heapq.nlargest(num_seeds, eig.items(), key=operator.itemgetter(1)))
    deg_d = dict(heapq.nlargest(num_seeds, deg.items(), key=operator.itemgetter(1)))
    print eig_d.keys()

    file = open("seed_nodes.txt", "w")
    for i in range(NUM_ROUNDS):
        for key in eig_d:
            file.write(key + '\n')  
    file.close()  

if __name__ == '__main__':
    run('testgraph2.json', 50, 1)
