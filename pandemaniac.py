import json
import argparse 
import networkx as nx
import heapq
import operator
import random

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

    c = nx.eigenvector_centrality(G)
    d = dict(heapq.nlargest(num_seeds, c.items(), key=operator.itemgetter(1)))
    
    file = open("seed_nodes.txt", "w")
    for i in range(NUM_ROUNDS):
        for key in d:
            file.write(key + '\n')  
    file.close()  

    return d.keys()

# closeness centrality
def closeness_run(graph, num_seeds, num_players):
    json_data = open(graph).read()
    graph = json.loads(json_data)

    G = nx.Graph()
    degree_sum = 0
    for node in graph:
        G.add_node(node)
        for link in graph[node]:
            G.add_node(link)
            G.add_edge(node,link)

    c = nx.closeness_centrality(G)
    d = dict(heapq.nlargest(num_seeds, c.items(), key=operator.itemgetter(1)))
    
    file = open("seed_nodes.txt", "w")
    for i in range(NUM_ROUNDS):
        for key in d:
            file.write(key + '\n')  
    file.close()  

    return d.keys()

# eignenvector centrality
def eigen_spread_run(graph, num_seeds, num_players):
    json_data = open(graph).read()
    graph = json.loads(json_data)

    G = nx.Graph()
    degree_sum = 0
    for node in graph:
        G.add_node(node)
        for link in graph[node]:
            G.add_node(link)
            G.add_edge(node,link)

    c = nx.eigenvector_centrality(G)
    d = dict(c.items())
    eig_values = sorted(d.values(), reverse = True)
    nodes = d.keys()
    ordered_nodes = [None] * len(nodes)
    for node in nodes:

        ordered_nodes[eig_values.index(d[node])] = node

    for i in range(len(ordered_nodes)):
        if ordered_nodes[i] == None:

            value = d[ordered_nodes[i-1]]
            for key in d:
                if d[key] == value:
                    if key not in ordered_nodes:
                        ordered_nodes[i] = key
                        break
    seed_nodes = [ordered_nodes[0]]
    
    for node in ordered_nodes:
        if len(seed_nodes) < num_seeds:
            too_close = 0
            if node not in seed_nodes:
                for i in G.neighbors(node):
                    if i in seed_nodes:
                        too_close = 1
                if too_close == 0:
                    seed_nodes.append(node)
        else:
            break

    file = open("seed_nodes.txt", "w")
    for i in range(NUM_ROUNDS):
        for i in seed_nodes:
            file.write(i + '\n')  
    file.close()  


    return seed_nodes

def eigen_2_run(graph, num_seeds, num_players):
    json_data = open(graph).read()
    graph = json.loads(json_data)

    G = nx.Graph()
    degree_sum = 0
    for node in graph:
        G.add_node(node)
        for link in graph[node]:
            G.add_node(link)
            G.add_edge(node,link)

    c = nx.eigenvector_centrality(G)
    d = dict(c.items())
    eig_values = sorted(d.values(), reverse = True)
    nodes = d.keys()
    ordered_nodes = [None] * len(nodes)
    for node in nodes:

        ordered_nodes[eig_values.index(d[node])] = node

    for i in range(len(ordered_nodes)):
        if ordered_nodes[i] == None:

            value = d[ordered_nodes[i-1]]
            for key in d:
                if d[key] == value:
                    if key not in ordered_nodes:
                        ordered_nodes[i] = key
                        break
    top_nodes = ordered_nodes[:num_seeds]
    seed_nodes = []
    for node in ordered_nodes:
        count = 0
 
        for seed in G.neighbors(node):
        
            if ((len(seed_nodes) < num_seeds) and (count < 2)):
                if seed not in top_nodes:
                    if seed not in seed_nodes:
                        seed_nodes.append(seed)
                        count += 1
    if len(seed_nodes) < num_seeds:
        seed_nodes.append(top_nodes[:(num_seeds - len(seed_nodes))])


        



    file = open("seed_nodes.txt", "w")
    for i in range(NUM_ROUNDS):
        for i in seed_nodes:
            file.write(i + '\n')  
    file.close()  
    # print seed_nodes
    # print top_nodes
    # for node in top_nodes:
    #     print G.neighbors(node)

    return seed_nodes

def eigen_neighbor_run(graph, num_seeds, num_players):
    json_data = open(graph).read()
    graph = json.loads(json_data)

    G = nx.Graph()
    degree_sum = 0
    for node in graph:
        G.add_node(node)
        for link in graph[node]:
            G.add_node(link)
            G.add_edge(node,link)

    c = nx.eigenvector_centrality(G)
    d = dict(c.items())
    eig_values = sorted(d.values(), reverse = True)
    nodes = d.keys()
    ordered_nodes = [None] * len(nodes)
    for node in nodes:

        ordered_nodes[eig_values.index(d[node])] = node

    for i in range(len(ordered_nodes)):
        if ordered_nodes[i] == None:

            value = d[ordered_nodes[i-1]]
            for key in d:
                if d[key] == value:
                    if key not in ordered_nodes:
                        ordered_nodes[i] = key
                        break
    seed_nodes_new = []
    for node in ordered_nodes:

        if len(seed_nodes_new) < num_seeds:
            seed = G.neighbors(node)[random.randint(0,len(G.neighbors(node)) - 1)]
            if seed not in seed_nodes_new:
                seed_nodes_new.append(seed)
        else:
            break


    file = open("seed_nodes.txt", "w")
    for i in range(NUM_ROUNDS):
        for i in seed_nodes_new:
            file.write(i + '\n')  
    file.close()  


    return seed_nodes_new

# eignenvector centrality
def eigen_spread_neighbor_run(graph, num_seeds, num_players):
    json_data = open(graph).read()
    graph = json.loads(json_data)

    G = nx.Graph()
    degree_sum = 0
    for node in graph:
        G.add_node(node)
        for link in graph[node]:
            G.add_node(link)
            G.add_edge(node,link)

    c = nx.eigenvector_centrality(G)
    d = dict(c.items())
    eig_values = sorted(d.values(), reverse = True)
    nodes = d.keys()
    ordered_nodes = [None] * len(nodes)
    for node in nodes:

        ordered_nodes[eig_values.index(d[node])] = node

    for i in range(len(ordered_nodes)):
        if ordered_nodes[i] == None:

            value = d[ordered_nodes[i-1]]
            for key in d:
                if d[key] == value:
                    if key not in ordered_nodes:
                        ordered_nodes[i] = key
                        break
    seed_nodes = [ordered_nodes[0]]
    
    for node in ordered_nodes:

        too_close = 0
        if node not in seed_nodes:
            for i in G.neighbors(node):
                if i in seed_nodes:
                    too_close = 1
            if too_close == 0:
                seed_nodes.append(node)

    seed_nodes_new = []
    for node in seed_nodes:

        if len(seed_nodes_new) < num_seeds:
            seed = G.neighbors(node)[random.randint(0,len(G.neighbors(node)) - 1)]
            if seed not in seed_nodes_new:
                seed_nodes_new.append(seed)
        else:
            break



    file = open("seed_nodes.txt", "w")
    for i in range(NUM_ROUNDS):
        for i in seed_nodes_new:
            file.write(i + '\n')  
    file.close()  
    

    return seed_nodes_new




# degree centrality
def degree_run(graph, num_seeds, num_players):
    json_data = open(graph).read()
    graph = json.loads(json_data)

    G = nx.Graph()
    degree_sum = 0
    for node in graph:
        G.add_node(node)
        for link in graph[node]:
            G.add_node(link)
            G.add_edge(node,link)

    b = nx.degree_centrality(G)
    d = dict(heapq.nlargest(num_seeds, b.items(), key=operator.itemgetter(1)))
    
    file = open("seed_nodes.txt", "w")
    for i in range(NUM_ROUNDS):
        for key in d:
            file.write(key + '\n')  
    file.close()  

    return d.keys()

# probabilistic eignenvector centrality
def eigen_prob_run(graph, num_seeds, num_players):
    json_data = open(graph).read()
    graph = json.loads(json_data)

    G = nx.Graph()
    degree_sum = 0
    for node in graph:
        G.add_node(node)
        for link in graph[node]:
            G.add_node(link)
            G.add_edge(node,link)

    c = nx.eigenvector_centrality(G)
    d = dict(heapq.nlargest(num_seeds*2, c.items(), key=operator.itemgetter(1)))
    seeds = random.sample(list(d), num_seeds)

    file = open("seed_nodes.txt", "w")
    for i in range(NUM_ROUNDS):
        for node in seeds:
            file.write(node + '\n')  
    file.close()  

    return seeds

def voting_run(graph, num_seeds, num_players):
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

    file = open("seed_nodes.txt", "w")
    for i in range(NUM_ROUNDS):
        for i in seeds:
            file.write(key + '\n')  
    file.close()  

    return seeds


if __name__ == '__main__':
    eigen_2_run('8.20.6.json', 20, 1)

  


