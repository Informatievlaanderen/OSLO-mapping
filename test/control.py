# Import the json module
import json

# Import the rdflib module
import rdflib

# Open the jsonld file in read mode
with open("test.jsonld", "r") as f:
    # Load the jsonld data as a dictionary
    data = json.load(f)


# Initialize an empty list to store the keys
keys = []


for i in range(len(data["@graph"])):
    # Loop through the keys of the data dictionary
    for key in data["@graph"][i]:
        # Append the key to the keys list
        keys.append(key)

# Define the python list of words to check
words = keys


# Open the jsonld file in read mode
with open("verkeersmetingen_ap.jsonld", "r") as f:
    # Load the jsonld data as a dictionary
    data = json.load(f)


# Initialize a boolean variable to store the result
all_words_present = True

# Loop through the words in the list
for word in words:
    # Check if the word is in the jsonld data as a key or a value
    if word not in str(data):
        # Set the result to False and break the loop
        print(word)
        all_words_present = False

# Print the result
print(all_words_present)
