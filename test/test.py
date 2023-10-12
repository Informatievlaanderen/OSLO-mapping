# Import the json module
import json

# Import the rdflib module
import rdflib

# Open the jsonld file in read mode
with open("test.jsonld", "r") as f:
    # Load the jsonld data as a dictionary
    data = json.load(f)
    
print(data["@graph"])

# Create a graph object from rdflib
g = rdflib.Graph()

# Parse the jsonld data into the graph object
g.parse(data=data, format="json-ld")

# Loop through all the triples in the graph object
for s, p, o in g:
    # Print the subject, predicate and object of each triple
    print(s)
