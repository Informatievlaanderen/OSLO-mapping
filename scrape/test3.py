import requests

# Constants
BASE_URL = 'https://api.github.com'
REPO_OWNER = 'Informatievlaanderen'
SEARCH_TERM = 'Oslothema'

token = "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"
username = "samuvack"


# Constants
BASE_URL = 'https://api.github.com'
REPO_OWNER = 'Informatievlaanderen'
REPO_NAME = 'your-repo-name'  # Replace with the actual repository name
FILE_EXTENSION = '.eap'


def get_matching_documents(url):
    # Create the URL for the repository contents

    # Send GET request to the GitHub API
    response = requests.get(url,  auth=(username, token))

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response as JSON
        data = response.json()

        # Filter and print the document names with the specified file extension
        for item in data:
            print(item)
            if item['type'] == 'file' and item['name'].endswith(FILE_EXTENSION):
                print(item['name'])
    else:
        print(
            f"Failed to fetch documents: {response.status_code} - {response.text}")




def get_matching_repositories():
    # Create the URL for the repository search
    url = f'{BASE_URL}/search/repositories?q={SEARCH_TERM}+user:{REPO_OWNER}'

    # Send GET request to the GitHub API
    response = requests.get(url,  auth=(username, token))

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response as JSON
        data = response.json()

        # Extract the list of repositories
        repositories = data['items']

        # Print the repository names
        for repo in repositories:
            print(repo['name'])
            url = 'http://github.com/InformatieVlaanderen/' + str(repo['name'])
            get_matching_documents(url)
    else:
        print(
            f"Failed to fetch repositories: {response.status_code} - {response.text}")


# Call the function to retrieve matching repositories
get_matching_repositories()
