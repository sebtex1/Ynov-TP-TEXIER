#focntion max()
def max(nb1, nb2):
    if (nb1 >= nb2):
        return nb1
    else:
        return nb2

#fonction max_of_three()
def max_of_three(nb1, nb2, nb3):
    if (nb1 >= nb2 and nb3):
        return nb1
    elif (nb2 >= nb1 and nb3):
        return nb2
    else:
        return nb3

#len()
def len(text):
    x=0
    for i in text:
        x += 1
    return x

#fonction pour vérifier si le caractère est une voyelle
def match_voyelle(char):
    voyelle = ["a", "e", "i", "o", "u", "y"]
    return char in voyelle 

#translate()
def translate(text):
    textTranslated = []
    for i in text:
       textTranslated.append(i)
       if not match_voyelle(i) and i != " ":
           textTranslated.append("o" + i)
    return "".join(textTranslated)

#sum()
def sum(array):
    sum = 0
    for i in array:
        sum += 1
    return sum

#multiply()
def multiply(array):
    sum = 1
    for i in array:
        sum *= i
    return sum

#reverse()
def reverse(text):
    txt = str()
    for i in range(len(text)-1, -1, -1):
        txt += text[i]
    return txt

#is_palindrome()
def is_palindrome(text):
    return text == reverse(text)

#is_member()
def is_member(arg, array):
    i=0
    while i != len(array):
        if arg == array[i]:
            return True
        i +=1
    return False

#overlapping()
def overlapping(array1, array2):
    for char1 in range(len(array1)):
        for char2 in range(len(array2)):
            if char1 == char2:
                return True
    return False

#generate_n_chars()
def generate_n_chars(nb, arg):
    generation= []
    for i in range(nb):
        generation.append(arg)
    return "".join(generation)

#histogram()
def histogram(array):
    for i in array:
        print(generate_n_chars(i, "*"))

#max_in_list()
def max_in_list(array):
    max=0
    for i in array:
        for y in array:
            if max < y:
                max = y
    return max

