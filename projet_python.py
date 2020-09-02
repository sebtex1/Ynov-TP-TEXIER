import os

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
        os.rename(file, dictionnary["titles"][i] + "-" + dictionnary["authors"][i] + ".txt")
        i += 1

def wordsInBooks():
    dictionnary={}
    for file in os.listdir():
        current_file = open(file, encoding="utf8")
        filtre = filter(wordFilter, current_file.read().replace("\n", " ").split(" "))
        dictionnary[file.replace(".txt", "")] = len(' '.join(list(filtre)).split())
    return dictionnary

def getAllWorldOccurrences():
    dictionnary={}
    for file in os.listdir():
        current_file = open(file, encoding="utf8")
        words = current_file.read().replace("\n", " ").split(" ").filter()
        print(words)

def wordFilter(words):
    filter = ["-", "", " ", "*"]
    return words in filter and False or True

print(wordsInBooks())