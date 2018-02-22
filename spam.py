# variables




mobList = "0123456789"
urlList = [".com", ".in", ".org"]
emojiList = [":)",":(",":P",":-*","XD"]
keywordList = ["money","call","offer"]
specialSymList = "!@#$%^&*(){}[]:;\"'"
mathSymList = "+-/*%^."

#msg = ""

def checkUppCase(msg):
    #count uppercase letters percentage
    global uppCase
    for i in msg:
        if (i.isupper()) == True:
            uppCase += 1
    uppCase = uppCase/length * 100
    #return uppCase



def checkLowCase(msg):
    #count lowercase letters percentage
    global lowCase
    for i in msg:
        if (i.islower()) == True:
            lowCase += 1
    lowCase = lowCase/length * 100

def checkDot(msg):
    #count number of dots percentage
    global dot
    for i in msg:
        if i == ".":
            dot += 1
    dot = dot/length * 100

def checkMob(msg):
    #count numbers percentage
    global mob
    for i in msg:
        if i in mobList:
            mob += 1
    mob = mob/length * 100

def checkUrl(msg):
    #count patterns like "*a.b*" percentge wise.... use regEx
    global url
    for i in urlList:
        if i in msg:
            url += 1
    url = url/length * 100

def checkEmoji(msg):
    #count emoji percentage
    global emoji
    for i in emojiList:
        if i in msg:
            emoji += 1
    emoji = emoji/length * 100

def checkKeyword(msg):
    #count percentage of keywords
    global keyword
    for i in keywordList:
        if i in msg:
            keyword += 1
    keyword = keyword/length * 100

def checkSpecialSym(msg):
    #count percentage of special symbol
    global specialSym
    for i in msg:
        if i in specialSymList:
            specialSym += 1
    specialSym = specialSym/length * 100

def checkMathSym(msg):
    global mathSym
    for i in msg:
        if i in mathSymList:
            mathSym += 1
    mathSym = mathSym/length * 100

spamWrite = open("spam.csv","a+")
spamRead = open("english_big.txt", "r")
lines = spamRead.readlines()


for i in lines:
    line = i
    #print(input)
    uppCase = 0
    lowCase = 0
    dot = 0
    mob = 0
    url = 0
    emoji = 0
    keyword = 0
    specialSym = 0
    mathSym = 0

    result = 0
    length = 0
#
#
    if(line[-5] == ","):
        result = 0  #for ham
        msg = line[:-5]
#
    if(line[-6] == ","):
        result = 1  #for spam
        msg = line[:-6]
#
    print(result)
    print(msg)
#
    length = len(msg)
#
#call functions here
    checkUppCase(msg)
    checkLowCase(msg)
    checkDot(msg)
    checkMob(msg)
    checkUrl(msg)
    checkEmoji(msg)
    checkKeyword(msg)
    checkSpecialSym(msg)
    checkMathSym(msg)
#
#
    output = str(uppCase) + "," + str(lowCase) + "," + str(dot) + "," + str(mob) + "," + str(url) + "," + str(emoji) + "," + str(keyword) + "," + str(specialSym) + "," + str(mathSym) + "," + str(result) + "\n"
#
#
    spamWrite.write(output)


spamRead.close()
spamWrite.close()






























