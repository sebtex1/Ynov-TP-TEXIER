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

def wordFilter(words):
    filter = ["-", "", " ", "*"]
    if (words in filter):
        return False
    else:
        return True

def getAllWorldOccurrences():
    dictionnary={}
    for file in os.listdir():
        allWords=[]
        testwords={}
        current_file = open(file, encoding="utf8")
        words = current_file.read().replace("\n", " ").split(" ")
        filtered = filter(wordFilter, words)
        for s in filtered:    
            allWords.append(s)
        for word in allWords:
            if word in allWords:
                testwords[word] = allWords.count(word)
                dictionnary[file.replace(".txt", "")] = testwords
    return dictionnary    
        
print(getAllWorldOccurrences())