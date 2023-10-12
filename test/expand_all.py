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


# Get the list of folders in the _mobility directory
folders = os.listdir("../docs/_mobility/")

# Loop through each folder
for folder in folders:
  # Get the path of the compact.jsonld file
  file_path = os.path.join("../docs/_mobility/", folder, "compact.jsonld")
  # Check if the file exists
  if os.path.isfile(file_path):
    # Load the JSON-LD document from the file
    with open(file_path) as f:
      data = json.load(f)
    # Expand the JSON-LD document
    expanded = jsonld.expand(data)
    # Compact and flatten the JSON-LD document using the function defined above
    output_obj = compact_and_flatten_json_ld(expanded)
    # Write the output object to a new file in the same folder
    with open(os.path.join("../docs/_mobility/", folder, "expanded.jsonld"), "w") as f:
      json.dump(output_obj, f, indent=2)
    print(folder)