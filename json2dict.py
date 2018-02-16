import json
import argparse 

def convert(filename):
    json_data = open(filename).read()
    data = json.loads(json_data)

    return data