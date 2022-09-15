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

print(verifyChar(input()))

