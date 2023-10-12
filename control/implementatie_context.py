# Importeer de nodige modules
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import json

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(ChromeDriverManager().install())


context_list = [
    "https://raw.githubusercontent.com/samuvack/context/main/Verkeersmetingen-ap.jsonld",
    "https://raw.githubusercontent.com/samuvack/context/main/sensoren-en-bemonstering.jsonld",
    "https://raw.githubusercontent.com/samuvack/context/main/observaties-en-metingen.jsonld",
    "https://raw.githubusercontent.com/samuvack/context/main/GEODCAT-AP-VL.jsonld",
    "https://raw.githubusercontent.com/samuvack/context/main/generiek-basis.jsonld"]


def extract_key_value(json_data, key):
    """Extracts a specific key-value pair from a JSON data"""
    data = json.loads(json_data)  # convert JSON string to Python dictionary
    value = data.get(key)  # get the value for the given key
    return value


# Definieer de namen van de context en input bestanden
input_file = "../docs/_mobility/Fietstelpunten/compact.jsonld"


with open(input_file, "r") as f:
    input = json.load(f)

# A function that takes a dictionary as an argument and returns a sorted dictionary by key
def sort_dict_by_key(d):
    # Create an empty dictionary to store the sorted key-value pairs
    sorted_dict = {}
    # Loop through the sorted keys of the original dictionary
    for key in sorted(d.keys()):
        # Assign the corresponding value to the sorted key in the new dictionary
        sorted_dict[key] = d[key]
    # Return the sorted dictionary
    return sorted_dict



# Maak een lege dictionary om de nieuwe context op te slaan
new_context = {}
for context_url in context_list:
    response = requests.get(context_url)
    context = response.json()
    # Ga door elke key en waarde in de context dictionary
    for key, value in context['@context'].items():
       
        # Als de key of de waarde voorkomt in de input dictionary
        if key in str(input):
            extract = extract_key_value(input['@context'], key)
            print(extract)
            # Voeg de key en waarde toe aan de nieuwe context dictionary
            new_context[key] = value


new_context = sort_dict_by_key(new_context)

# Schrijf de nieuwe context dictionary naar een nieuw bestand genaamd "new_context.jsonld"
with open("new_context.jsonld", "w") as f:
    json.dump(new_context, f, indent=4)

# Print een bericht dat het script klaar is
print("Het script is klaar. De nieuwe context is opgeslagen in new_context.jsonld.")
