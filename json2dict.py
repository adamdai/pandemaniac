import json
import argparse 

def convert(filename):
    json_data = open(filename).read()
    data = json.loads(json_data)
    graph = {}
    for node in data:
        graph[node] = data[node]
    #print (graph)

    return graph