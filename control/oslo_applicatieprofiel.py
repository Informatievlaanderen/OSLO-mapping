from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re
from datetime import datetime, timedelta


outputfile = '../output/dead_links.md'
readme = '../README.md'
vocabularium_output = 'vocabularium.txt'

try:
    with open('dead_link_urls.txt', 'r', encoding='latin-1') as file1:
        lines = file1.readlines()
except IOError as e:
    print(f'Error: Failed to read file. {e}')
# finally:
#    file1.close()


def create_empty_file(filename):
    """
    Create an empty file.

    Args:
        filename (str): The name of the file to be created.

    Returns:
        None
    """
    try:
        with open(filename, 'r+', encoding='latin-1') as file:
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
    # finally:
    #    output.close()


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
    # finally:
    #    output.close()

# haal data uit AP


global number_of_deadlinks
number_of_deadlinks = 0
create_empty_file(outputfile)
create_empty_file('../log/checked.md')

# using now() to get current time
current_time = datetime.now()

write_to_file(
    outputfile,
    """```diff
! Dit document is automatisch gegenereerd op : """ + str(current_time) + """
```""")
write_to_file(outputfile, '\n')


write_to_file(
    'log/checked.md',
    """```diff
! Dit document is automatisch gegenereerd op : """ + str(current_time) + """
```""")
write_to_file('../log/checked.md', '\n')

lines = ['https://data.vlaanderen.be/doc/applicatieprofiel/verkeersmetingen']

for line in lines:
        # 'https://data.vlaanderen.be/standaarden/erkende-standaard/openbaar-domein---uitbreiding-begraafplaats-(vocabularium).html'
        link = str(line)
        # print(link)
        # write_to_file(outputfile, '\n')
        # write_to_file(outputfile, '\n')
        # write_to_file(outputfile, '\n')
        # write_to_file(outputfile, link)
        # write_to_file(outputfile, '\n')

        def substring_after(s, delim):
                return s.partition(delim)[1]

        def validate_url(url):
            try:
                r = requests.head(url)
                if str(r.status_code) == '404':
                    return True
            except IOError as e:
                return True

        def check_voc(url):
            if 'https://data.vlaanderen.be/ns/' in url:
                write_to_file(vocabularium_output, url)

        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        urls = []
        url_names = []

        for link in soup.find_all('a'):
            print(link.get('href'))
            if 'http' in link.get('href'):
                urls.append(link.get('href'))

        print(urls)

        text = ''

        for i in range(0, len(urls)):
            if ("https://data.vlaanderen.be/ns/" in str(urls[i])):
                write_to_file('../log/vocabularium.txt', urls[i])
                write_to_file('../log/vocabularium.txt', '\n')

            if ("https://data.vlaanderen.be/doc/applicatieprofiel/" in str(urls[i])):
                write_to_file('../log/applicatieprofiel.txt', urls[i])
                write_to_file('../log/applicatieprofiel.txt', '\n')

            check_voc(urls[i])

            if validate_url(urls[i]):
                number_of_deadlinks = number_of_deadlinks+1
                if text == '':
                    text += '\n'
                    text += '\n'
                    text += '\n'
                    text += '['+str(line)+']('+str(line)+')'
                    text += '\n'
                    text += '\n'

                text += 'url is broken [' + \
                    str(urls[i]) + '](<'+str(urls[i])+'>) \n'
                text += '\n'
                #write_to_file(outputfile, 'url is broken [' + urls[i] + ')')
                #write_to_file(outputfile, '\n')
            if (text != '') & (i == len(urls)-1):
                text += '\n'
                text += '--------------------------------------------------'
        write_to_file(outputfile, str(text))

        write_to_file('log/checked.md', str(line))

write_to_file(readme, '\n')
write_to_file(readme, '\n')
write_to_file(readme, "## Controle deadlinks OSLO standaarden")
write_to_file(readme, '\n')

write_to_file(readme, '\n')
write_to_file(readme, str(number_of_deadlinks) +
              ' dode linken gevonden in het standaarden')

write_to_file(
    readme, '\n')
write_to_file(
    readme, 'Voor meer informatie, ga naar [dit overzicht](output/dead_links.md)')
