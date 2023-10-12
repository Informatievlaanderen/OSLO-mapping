# Import the required modules
import os
import json
from pyld import jsonld

# Define the function to compact and flatten the JSON-LD document


def compact_and_flatten_json_ld(obj):
    # Flattening function
    def flatten_jsonld(jsonld):
        if isinstance(jsonld, dict):
            if '@id' in jsonld and len(jsonld) == 1:
                return jsonld['@id']
            return {k: flatten_jsonld(v) for k, v in jsonld.items()}
        return jsonld

    # Compacting function
    if isinstance(obj, list):
        if len(obj) == 1:
            return compact_and_flatten_json_ld(obj[0])
        else:
            return [compact_and_flatten_json_ld(e) for e in obj]
    elif isinstance(obj, dict):
        new_obj = {}
        for k, v in obj.items():
            new_obj[k] = compact_and_flatten_json_ld(v)
        return flatten_jsonld(new_obj)
    else:
        return flatten_jsonld(obj)


def is_folder_with_compact_jsonld(path):
    # Get the list of files in the directory
    files = os.listdir(path)
    # Check if compact.jsonld is in the list
    if "compact.jsonld" in files:
        # Return True
        return True
    # Return False otherwise
    return False      
        
folders = []


# Loop through the items in the folder
for item in os.listdir("../docs/_mobility"):
    # Check if the item is a folder
    if os.path.isdir(os.path.join("../docs/_mobility/", item)):
        # Print the name of the folder
        folders.append(item)

print(folders)


# Loop through each folder
for folder in folders:
    # Get the path of the compact.jsonld file
    file_path = "../docs/_mobility/" +  str(folder) + "/compact.jsonld"
    output_path = "../docs/_mobility/"  + str(folder) + "/expanded.jsonld"
    print(file_path)
    # Load the JSON-LD document from a file
    with open(file_path) as f:
        data = json.load(f)

    # Expand the JSON-LD document
    expanded = jsonld.expand(data)

    # compact the input object using the function defined above
    output_obj = compact_and_flatten_json_ld(expanded)


    # write the output object as a json-ld file with indentation
    with open(output_path, "w") as f:
        json.dump(output_obj, f, indent=2)
    print("expanded")

