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
        
