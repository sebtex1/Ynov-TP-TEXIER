import requests
import json
from bs4 import BeautifulSoup

def getRepositories():
    repositories = requests.get("https://api.github.com/repositories") 
    parse = BeautifulSoup(repositories.text)
    repositoriesJSON = json.loads(str(parse))
    for doc in repositoriesJSON:
        print(doc["name"])
        print(doc["description"] is not None and doc["description"] or "no description") 
        open('./projet_GitHub/repositories.txt', "a").write("Title: " + doc["name"] + "\n" + "Description: " + (doc["description"] is not None and doc["description"] or "no description") + "\n")
    # return 

getRepositories()