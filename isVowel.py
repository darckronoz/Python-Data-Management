vowelList = []
consonantList = []

def fillLists():
    global consonantList
    for i in range(97, 123):
        if(i == 97 or i == 101 or i == 105 or i == 111 or i == 117):
            vowelList.append(chr(i))
        else:
            consonantList.append(chr(i))

fillLists()

def verifyChar(x):
    for i in range(len(consonantList)):
        if(consonantList[i]==x.lower()):
            return True
    return False

def countVowel(phrase):
    print(phrase[0].lower() == vowelList[0])
    a = 0
    e = 0
    letteri = 0
    o = 0
    u = 0
    vow = []
    for i in range(len(phrase)):
        if(phrase[i].lower() == vowelList[0]):
            a = a+1
        elif(phrase[i].lower() == vowelList[1]):
            e = e+1
        elif(phrase[i].lower() == vowelList[2]):
            letteri = letteri+1
        elif(phrase[i].lower() == vowelList[3]):
            o = o+1
        elif(phrase[i].lower() == vowelList[4]):
            u = u+1
    vow.append(a)
    vow.append(e)
    vow.append(letteri)
    vow.append(o)
    vow.append(u)
    return vow

def printNumberOfVowels(word, list):
    print(word, ' has:', ' a->', list[0],' e->', list[1],' i->', list[2],' o->', list[3],' u->', list[4])

worddd = 'gestion de datos'

printNumberOfVowels(worddd, countVowel(worddd))
