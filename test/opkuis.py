# import json library
import json

# define a function to compact a json-ld object


def compact_json_ld(obj):
  # if the object is a list
  if isinstance(obj, list):
    # if the list has only one element
    if len(obj) == 1:
      # return the compacted element
      return compact_json_ld(obj[0])
    # else, return the list of compacted elements
    else:
      return [compact_json_ld(e) for e in obj]
  # if the object is a dictionary
  elif isinstance(obj, dict):
    # create a new dictionary to store the compacted key-value pairs
    new_obj = {}
    # iterate over the key-value pairs in the object
    for k, v in obj.items():
      # if the key is "@id" and the value starts with "_:"
        new_obj[k] = compact_json_ld(v)
    # return the new dictionary
    return new_obj
  # else, return the object as it is
  else:
    return obj



# read the input json-ld file as a python object
with open("expanded.jsonld", "r") as f:
  input_obj = json.load(f)

# compact the input object using the function defined above
output_obj = compact_json_ld(input_obj)

flattend = flatten_jsonld(output_obj)

# write the output object as a json-ld file with indentation
with open("output.json", "w") as f:
  json.dump(flattend, f, indent=2)
