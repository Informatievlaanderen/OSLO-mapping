import requests
import json


token = "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"
username = "samuvack"

path_url = "https://raw.githubusercontent.com/Informatievlaanderen"

url = "https://api.github.com/repos/Informatievlaanderen/git/trees"
r = requests.get(url, auth=(username, token))
res = r.json()
print(res)

paths = []
for file in res["tree"]:
    path = file["path"]
    print(path)
    url2 = file["url"]
    print(url2)
    r = requests.get(url2, auth=(username, token))
    l = r.json()
    try:
        for p in l["tree"]:
            if (p["path"] == "context"):
                print(p["path"])
                print(p["url"])
                try:
                    print("reeds gebeurd")
                    """
                    r = requests.get(p["url"], auth=(username, token))
                    t = r.json()
                    for json_names in t["tree"]:
                        print(json_names["path"])
                        file_path = str(path_url) + "/" + str(path) + \
                            "/" + p["path"] + "/" + json_names["path"]
                        download = requests.get(
                            file_path, auth=(username, token))
                        print(file_path)
                        downloaded_file = download.json()
                        json_object = json.dumps(downloaded_file, indent=4)
                        f = open("../oslo/" + str(json_names["path"]), "w+")
                        f.write(json_object)
                        f.close()       
                    """
                except:
                    print("error1")
            else:

                def func(_p, longh_path):
                    if (_p["path"] == "context"):
                        print(_p["path"])
                        return _p["path"]
                    else:
                        print("else :", _p["path"])
                        print("else :", _p["url"])
                        r = requests.get(_p["url"], auth=(username, token))
                        t = r.json()                      
                        tree = t["tree"][url]
                        return func(tree, longh_path)
                q = p
                test = func(q, "")

    except:
        print('error2')
