import json

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


# read the input json-ld file as a python object
with open("expanded.jsonld", "r") as f:
  input_obj = json.load(f)

# compact the input object using the function defined above
output_obj = compact_and_flatten_json_ld(input_obj)


# write the output object as a json-ld file with indentation
with open("output.json", "w") as f:
  json.dump(output_obj, f, indent=2)

