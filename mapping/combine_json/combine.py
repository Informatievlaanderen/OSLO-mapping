import json

def combine_json_members(input_file):
    with open(input_file) as file:
        data = json.load(file)

    combined_member = {}
    print(data['2505-Lommel Barrier'])
    for member in data:
        for key, value in data[member]['Attributen']['Mobiliteitsaanbod'].items():
            print(key)
            print(value)
            
            combined_member[key] = combined_member.get(key, value)

    return combined_member

def write_output_file(output_file, data):
    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)

# Usage example
input_file = 'input.json'
output_file = 'output.json'

combined_member = combine_json_members(input_file)
write_output_file(output_file, combined_member)