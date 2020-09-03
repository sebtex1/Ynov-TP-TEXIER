import os
import requests
from bs4 import BeautifulSoup
import re

os.chdir('./books')

def getBooksTitleAndAuthor():
    titles=[]
    authors=[]
    dictionnary={}
    for file in os.listdir():
        current_file = open(file, encoding="utf8")
        for line in current_file.readlines():
            if line.startswith("Title:"):
                titles.append(line.split(": ")[1].replace("\n", ""))
            elif line.startswith("Author:"):
                authors.append(line.split(": ")[1].replace("\n", ""))
                break
    dictionnary["titles"] = titles
    dictionnary["authors"] = authors
    return dictionnary

def renameAllBooks():
    dictionnary=getBooksTitleAndAuthor()
    i = 0
    for file in os.listdir():
        os.rename(file, dictionnary["titles"][i].upper().replace(" ", "_") + "-" + dictionnary["authors"][i].upper().replace(" ", "_") + ".txt")
        i += 1

def wordsInBooks():
    dictionnary={}
    for file in os.listdir():
        current_file = open(file, encoding="utf8")
        filtre = filter(wordFilter, current_file.read().replace("\n", " ").split(" "))
        dictionnary[file.replace(".txt", "")] = len(' '.join(list(filtre)).split())
    return dictionnary

def wordFilter(words):
    filter = ["-", "", " ", "*"]
    if (words in filter):
        return False
    else:
        return True

# getAllWordOccurenceInBooks()["nom du livre"]["mot rechercher"]
def getAllWordOccurenceInBooks():
    dictionnary = {}
    for file in os.listdir():
        current_file = open(file, encoding="utf8")
        words = filter(wordFilter, current_file.read().replace("\n", " ").split(" "))
        all_words = (' '.join(list(words)).split())
        book_dictionnary = {}
        for word in all_words:
            if word.lower() not in book_dictionnary:
                book_dictionnary[word.lower()] = 1
            else:
                book_dictionnary[word.lower()] = book_dictionnary[word.lower()] + 1
        dictionnary[file.replace(".txt", "")] = book_dictionnary
    return dictionnary
        
def getAllWordOccurrence():
    newdictionary = {} 
    dictionary = getAllWordOccurenceInBooks() 
    for dicKey in dictionary: # boucle qui parcours toutes les clées "nom des livres" dans le dictionnaire
        for word in dictionary[dicKey]: # boucle qui parcours toutes les clées "mots" dans le dictionnaire dictionary[**dicKey**] (dicKey qui est la clé au dessus)
            if word not in newdictionary: 
                newdictionary[word] = dictionary[dicKey][word] # On ajoute donc le mot et ça valeur dans le dictionnaire des livres
            else: 
                newdictionary[word] = newdictionary[word] + dictionary[dicKey][word] # on récupère la valeur dans le nouveau dictionnaire et on fait la somme avec la valeur du dictionnaire des livres
    return newdictionary 
        
def getTop10Occurrence():
    top10=[]
    dictionnary=getAllWordOccurrence()
    sort = sorted(dictionnary.items(), key=lambda x: x[1]) 
    for loop in range(len(sort)-1, len(sort)-11, -1):
        top10+=sort[loop]
    print(top10)

def getBooksLinks():
    os.chdir('../dl_books')
    results = requests.get('http://www.gutenberg.org/robot/harvest')
    parser = BeautifulSoup(results.text)
    print(parser)
    # for link in parser.find_all('a'):
    #     # url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', link)
    #     print(link.find('https:'))
        
    
# myString = "This is my tweet check it out http://example.com/blah"

# print(re.search("(?P<url>https?://[^\s]+)", myString).group("url"))

getBooksLinks()