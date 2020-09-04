import requests
import json
import math
import os

repo={}
topRepo={}
user="sebtex1"

def getRepositories():
    dictionnary={}
    repositories = requests.get("https://api.github.com/repositories") 
    repositoriesJSON = json.loads(repositories.text)
    i = 0
    for doc in repositoriesJSON:
        # open('./projet_GitHub/repositories.txt', "a").write("Title: " + doc["name"] + "\n" + "Description: " + (doc["description"] is not None and doc["description"] or "no description") + "\n")
        dictionnary[i]={}
        dictionnary[i]["title"]=doc["name"]
        dictionnary[i]["description"]=doc["description"]
        i+=1
    repoJson= json.dumps(dictionnary)
    open('./repositories.json', "w", encoding="utf8").write(repoJson)
        
    
def getTopRepositories():
    dictionnary={}
    repositories=requests.get("https://api.github.com/search/repositories?sort=stars&q=created:2020-01-01&per_page=100")
    repositoriesJSON = json.loads(repositories.text)["items"]
    i=0
    for doc in repositoriesJSON:
        # open('./projet_GitHub/topRepositories.txt', "a", encoding="utf8").write("Title: " + doc["name"] + "\n" + "Description: " + (doc["description"] is not None and doc["description"] or "no description") + "\n" + "Number of stars: " + str(doc["stargazers_count"]) + "\n")
        dictionnary[i]={}
        dictionnary[i]["title"]=doc["name"]
        dictionnary[i]["description"]=doc["description"]
        dictionnary[i]["stars"]=doc["stargazers_count"]
        i+=1
    repoJson= json.dumps(dictionnary)
    open('./topRepositories.json', "w", encoding="utf8").write(repoJson)

def initRepo():
    repoFile = "./Repositories.json"
    topRepoFile = "./topRepositories.json"

    repoFile_content = open(repoFile, "r", encoding="utf8").read()
    topRepoFile_content = open(topRepoFile, "r", encoding="utf8").read()
    
    repo = json.loads(repoFile_content)
    topRepo = json.loads(topRepoFile_content)

def pageRepoUser():
    user_url = requests.get("https://api.github.com/users/"+user)
    url_json = json.loads(user_url.text)
    # savoir le nombre de page potentiel du User
    count = url_json["public_repos"]/100
    count = math.ceil(count)
    return count

def ReposUser():
    dictionnary={}
    url=requests.get("https://api.github.com/users/"+user+"/repos?per_page=100")
    url_json = json.loads(url.text)
    i=0
    for repo in  url_json:
        dictionnary[i]={}
        dictionnary[i]["title"]=repo["name"]
        dictionnary[i]["description"]=repo["description"]
        dictionnary[i]["stars"]=repo["stargazers_count"]
        i+=1
    repoJson = json.dumps(dictionnary)
    open('./users/'+user+".json", "w", encoding="utf8").write(repoJson)

def getReposUserStars():
    file="./users/"+user+".json"
    if os.access(file, os.R_OK):
        last_dictionnary={}
        last_dictionnary = json.loads(open(file, "r", encoding="utf8").read())
        new_dictionnary={}
        ReposUser()
        new_dictionnary = json.loads(open(file, "r", encoding="utf8").read())
        i=0
        for i in new_dictionnary:
            print(new_dictionnary[i]["title"])

def spyUser():
    nbOfPage = pageRepoUser()
    if nbOfPage == 1:
        repo_url = requests.get("https://api.github.com/users/"+user+"/repos?per_page=100")
        repo_url_json = json.loads(repo_url.text)
        print(repo_url_json)
    

# spyUser()
# initRepo()
# getRepositories()
# getTopRepositories()
getReposUserStars()