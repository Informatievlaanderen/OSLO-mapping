import json
from pyld import jsonld


# Load the JSON-LD document from a file
with open('compact.jsonld') as f:
    data = json.load(f)


# Expand the JSON-LD document
expanded = jsonld.expand(data)


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
    

# compact the input object using the function defined above
output_obj = compact_and_flatten_json_ld(expanded)


# write the output object as a json-ld file with indentation
with open("output.json", "w") as f:
  json.dump(output_obj, f, indent=2)
