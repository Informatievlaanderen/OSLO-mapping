import rdflib
import json

    # Importeer de json module om json-ld bestanden te lezen en schrijven

    # Definieer een functie die de URI van een klasse of eigenschap vindt in de context van een json-ld bestand


def find_uri(term, context):
    # Als de term al een URI is, geef het dan terug
    if term.startswith("http://") or term.startswith("https://"):
        return term
    # Anders, zoek de term op in de context
    else:
        # Als de term een sleutel is in de context, geef dan de waarde terug
        if term in context:
            return context[term]
        # Anders, splits de term op in een prefix en een lokale naam
        else:
            prefix, local_name = term.split(":")
            # Als de prefix een sleutel is in de context, voeg dan de waarde toe aan de lokale naam en geef het terug
            if prefix in context:
                return context[prefix] + local_name
            # Anders, geef een foutmelding terug
            else:
                return f"Error: {term} not found in context"


# Lees het json-ld bestand in als een Python dictionary
with open("verkeersmetingen_ap.jsonld", "r") as f:
    data = json.load(f)


# Haal de context uit de data
context = data["@context"]


# Maak een lege lijst om de gevonden URI's op te slaan
uris = []

d = {}

# Doorloop alle sleutels en waarden in de data
for key, value in context.items():
    
    # Als de sleutel geen @ teken bevat, beschouw het dan als een klasse of eigenschap
    if not key.startswith("@"):
        # Vind de URI van de sleutel en voeg het toe aan de lijst
        uri = find_uri(key, context)
        uris.append(uri)
        # Als de waarde een lijst is, doorloop dan alle elementen in de lijst
        if isinstance(value, list):
            
            d[key]=value
            for element in value:
                
                # Als het element een dictionary is, doorloop dan alle sleutels en waarden in het element
                if isinstance(element, dict):
                    
                    for k, v in element.items():
                        # Als de sleutel geen @ teken bevat, beschouw het dan als een klasse of eigenschap
                        if not k.startswith("@"):
                            # Vind de URI van de sleutel en voeg het toe aan de lijst
                            uri = find_uri(k, context)
                            uris.append(uri)
                # Anders, beschouw het element als een klasse of eigenschap
                else:
                    # Vind de URI van het element en voeg het toe aan de lijst
                    uri = find_uri(element, context)
                    uris.append(uri)
        # Anders, beschouw de waarde als een klasse of eigenschap
        else:
            if isinstance(value, dict):
                
                d[key]=value['@id']
                continue
            else:
                
                d[key]=value
                # Vind de URI van de waarde en voeg het toe aan de lijst
                uri = find_uri(value, context)
                uris.append(uri)


# Open the jsonld file in read mode
with open("test.jsonld", "r") as f:
    # Load the jsonld data as a dictionary
    data = json.load(f)

test = str(data)

for i in range(len(data["@graph"])):
    # Loop through the keys of the data dictionary
    for key in data["@graph"][i]:
        # Append the key to the keys list
        if key != '@id' and key != '@type':
            if d.get(key):
                print(key)
                print(d[key])
                test = test.replace(key, str(d[key]))



# Convert the dictionary to a json string
json_string = json.dumps(test, indent=2)

# Write the json string to a file
with open("output.jsonld", "w") as f:
  f.write(json_string)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              