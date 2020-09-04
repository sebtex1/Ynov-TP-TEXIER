import requests
import json

def getRepositories():
    repositories = requests.get("https://api.github.com/repositories") 
    repositoriesJSON = json.loads(repositories.text)
    for doc in repositoriesJSON:
        open('./projet_GitHub/repositories.txt', "a").write("Title: " + doc["name"] + "\n" + "Description: " + (doc["description"] is not None and doc["description"] or "no description") + "\n")
    
def getTopRepositories():
    repositories=requests.get("https://api.github.com/search/repositories?sort=stars&q=created:2020-01-01&per_page=100")
    repositoriesJSON = json.loads(repositories.text)["items"]
    for doc in repositoriesJSON:
        open('./projet_GitHub/topRepositories.txt', "a", encoding="utf8").write("Title: " + doc["name"] + "\n" + "Description: " + (doc["description"] is not None and doc["description"] or "no description") + "\n" + "Number of stars: " + str(doc["stargazers_count"]) + "\n")

getTopRepositories()