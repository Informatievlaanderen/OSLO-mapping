from pytz import timezone
from bs4 import BeautifulSoup
from selenium import webdriver
import json
import os
from concurrent.futures import ThreadPoolExecutor
import requests
import re
from datetime import datetime, timedelta

driver = webdriver.Chrome()

outputfile = 'README.md'
controle_app = 'output/controle_applicatieprofiel.md'

def create_empty_file(filename):
    """
    Create an empty file.

    Args:
        filename (str): The name of the file to be created.

    Returns:
        None
    """
    try:
        with open(filename, 'r+',encoding='latin-1') as file:
            file.truncate(0)
        print(f'Success: Empty file "{filename}" created.')
    except IOError as e:
        print(f'Error: Failed to create empty file. {e}')

def write_to_file(filename, parameter):
    """
    Write a parameter to a file.

    Args:
        parameter (str): The parameter to be written.
        filename (str): The name of the file to write to.

    Returns:
        None
    """
    try:
        with open(filename, 'a') as output:
            output.write(parameter)
        print(
            f'Success: Parameter "{parameter}" written to file "{filename}".')
    except IOError as e:
        print(f'Error: Failed to write parameter to file. {e}')
    finally:
        output.close()

# haal data uit AP


def getData(link, driver):
    driver.get(link)
    html = driver.page_source
    soup = BeautifulSoup(html, features="lxml")

    entiteiten = False
    datatypes = False
    klassen = []
    typedict = []

    for d in soup.find_all('div', attrs={"class": "region region--no-space-top"}):
        # entiteiten ophalen
        for h2 in d.find_all('h2'):
            if h2.text == "Entiteiten":
                entiteiten = True
        if entiteiten:
            datatypes = False
            for h3 in d.find_all('h3'):  # hier zit je in de box van een klasse
                for a in h3.find_all('a'):  # link van de klasse zelf in een dict
                    linkdict = {'link': a['href']}
                # hier zit je in de box met de informatie van de klasse zelf
                for dl in d.find_all('dl'):
                    beschr = False  # steek beschrijving in een dict
                    for dt in dl.find_all(['dt', 'dd']):
                        if beschr:
                            beschrijving = {'beschrijving': dt.text}
                            beschr = False
                        if dt.text == "Beschrijving":
                            beschr = True

                # enkel de beschrijving wordt opgeslagen, de rest kan maar lijkt nutteloos

                # attributen ophalen
                attributen = {}
                for tr in d.find_all('tr', attrs={"typeof": "rdfs:Property"}):
                    lijst = []
                    for td in tr.find_all('td'):
                        geenLink = True
                        for a in td.find_all('a'):
                            attrlink = {}
                            if a.text[5:10] == "     ":
                                attrlink[a.text[29:]] = a['href']
                            else:
                                attrlink[a.text] = a['href']
                            lijst.append(attrlink)
                            geenLink = False
                        if geenLink:
                            lijst.append(td.text)

                    attributen['attributen'] = lijst
                if attributen == {}:
                    attributen['attributen'] = [{'bla': 'bla'}, {
                        'bla': 'bla'}, 'bla', 'bla', 'bla', 'bla']
                klasse = [linkdict, beschrijving, attributen]
                klassen.append({h3.text: klasse})

        # datatypes ophalen
        for h2 in d.find_all('h2'):
            if h2.text == "Datatypes":
                datatypes = True
        if datatypes:
            entiteiten = False
            for h3 in d.find_all('h3'):  # hier zit je in de box van een datatype
                for a in h3.find_all('a'):  # link van het datatype zelf in een dict
                    linkdict = {'link': a['href']}
                    print(linkdict)
                # hier zit je in de box met de informatie van het datatype zelf
                for dl in d.find_all('dl'):
                    beschr = False  # steek beschrijving in een dict
                    for dt in dl.find_all(['dt', 'dd']):
                        if beschr:
                            beschrijving = {'beschrijving': dt.text}
                            beschr = False
                        if dt.text == "Beschrijving":
                            beschr = True

                # enkel de beschrijving wordt opgeslagen, de rest kan maar lijkt nutteloos

                # attributen ophalen
                attributen = {}
                for tr in d.find_all('tr', attrs={"typeof": "rdfs:Property"}):
                    lijst = []
                    for td in tr.find_all('td'):
                        geenLink = True
                        for a in td.find_all('a'):
                            attrlink = {}
                            if a.text[5:10] == "     ":
                                attrlink[a.text[29:]] = a['href']
                            else:
                                attrlink[a.text] = a['href']
                            lijst.append(attrlink)
                            geenLink = False
                        if geenLink:
                            lijst.append(td.text)

                    attributen['attributen'] = lijst
                if attributen == {}:
                    attributen['attributen'] = [{'bla': 'bla'}, {
                        'bla': 'bla'}, 'bla', 'bla', 'bla', 'bla']
                datatype = [linkdict, beschrijving, attributen]
                typedict.append({h3.text: datatype})

    stanDict = {}
    stanDict["Entiteiten"] = klassen
    stanDict["Datatypes"] = typedict
    return stanDict

# analyseer het AP
global geenfixme
geenfixme = 0
global geenbeschrijving
geenbeschrijving  = 0
global geentype
geentype  = 0
global geenkardinaliteit
geenkardinaliteit = 0
global geendefinitie
geendefinitie = 0


def analyse(data, geenfixme, geenbeschrijving, geentype, geenkardinaliteit, geendefinitie):
    resultaat = ""
    for soort in data:
        for entiteit in data[soort]:

            # link van klasse zelf checken
            if "fixme" in list(entiteit.values())[0][0]['link']:
                geenfixme += 1
                resultaat += "fixme gevonden in de link van klasse \"{}\"   ".format(
                    list(entiteit.keys())[0])
                resultaat += "\n"

            # beschrijving van de klasse zelf checken
            if list(entiteit.values())[0][1]['beschrijving'] == "":
                geenbeschrijving += 1
                resultaat += "Geen beschrijving gevonden bij klasse \"{}\"   ".format(
                    list(entiteit.keys())[0])
                resultaat += "\n"

            # attributen hier overlopen
            attribuut = list(list(list(entiteit.values())[
                             0][2].values())[0][0].keys())[0]
            attributen = list(list(entiteit.values())[0][2].values())[0]

            cel = attributen[0]
            if "fixme" in cel[list(cel.keys())[0]]:
                geenfixme += 1

                resultaat += "fixme gevonden in attribuut \"{}\" van klasse \"{}\"   ".format(
                    attribuut, list(entiteit.keys())[0])
                resultaat += "\n"
            cel = attributen[1]
            try:
                if "fixme" in cel[list(cel.keys())[0]]:
                    geenfixme += 1
    
                    resultaat += "fixme gevonden in attribuut \"{}\" van klasse \"{}\"  ".format(
                        attribuut, list(entiteit.keys())[0])
                    resultaat += "\n"
            except:
                geentype = geentype + 1
                resultaat += "Geen verwacht type gevonden bij attribuut \"{}\" van klasse \"{}\"   ".format(
                    attribuut, list(entiteit.keys())[0])
                resultaat += "\n"
            cel = attributen[2]
            if cel == "":
                geenkardinaliteit = geenkardinaliteit + 1
                resultaat += "Kardinaliteit ontbreekt in attribuut \"{}\" van klasse \"{}\"  ".format(
                    attribuut, list(entiteit.keys())[0])
                resultaat += "\n"
            cel = attributen[3]
            if cel == "":
                geendefinitie = geendefinitie + 1
                
                resultaat += "Definitie ontbreekt in attribuut \"{}\" van klasse \"{}\"  ".format(
                    attribuut, list(entiteit.keys())[0])
                resultaat += "\n"

    if resultaat == "":
        resultaat += "Alles is in orde!"

    return resultaat, geenfixme, geenbeschrijving, geentype, geenkardinaliteit, geendefinitie


driver = webdriver.Chrome()

links = ['https://data.vlaanderen.be/doc/applicatieprofiel/verkeersmetingen']
create_empty_file(outputfile)
create_empty_file(controle_app)
write_to_file(outputfile, "## OSLO standaardenregister validatie")
write_to_file(outputfile, '\n')


# using now() to get current time
current_time = datetime.now()

# Printing value of now.
print(current_time)

write_to_file(
    outputfile,
"""```diff
! Dit document is automatisch gegenereerd op : """ + str(current_time) + """
```""")
write_to_file(outputfile, '\n')

write_to_file(
    controle_app,
    """```diff
! Dit document is automatisch gegenereerd op : """ + str(current_time) + """
```""")
write_to_file(controle_app, '\n')

text = ''

for link in links:
    data = getData(link, driver)
    resultaat, geenfixme, geenbeschrijving, geentype, geenkardinaliteit, geendefinitie = analyse(data, geenfixme, geenbeschrijving, geentype, geenkardinaliteit, geendefinitie)
    if (resultaat == """Alles is in orde!"""):
        """
        write_to_file(outputfile, '\n')
        write_to_file(outputfile, "["+link+"]("+link+")")
        write_to_file(outputfile, '\\')
        write_to_file(outputfile, '\n')
        print(resultaat)
        write_to_file(outputfile, resultaat)
        write_to_file(outputfile, '\\')
        """
    else:
        
        text +='\n'
        text += "["+link+"]("+link+")"
        text += '\\'
        text += '\n'
        text += resultaat
        text += '\n'
        