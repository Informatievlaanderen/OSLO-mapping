from github import Github

# Vervang <TOEGANGSTOKEN> door uw persoonlijke toegangstoken
g = Github("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")

repo = g.get_repo(
    "https://github.com/Informatievlaanderen/data.vlaanderen.be-generated")
context_dir = repo.get_contents("doc/applicatieprofiel/context")

folders = []
for content_file in context_dir:
    if content_file.type == "dir":
        folders.append(content_file.name)
        
print(folders)
