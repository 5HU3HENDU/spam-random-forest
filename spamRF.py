#import numpy
#import scipy
#import sklearn
import pandas as pd


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


uppCase = 0
lowCase = 0
dot = 0
mob = 0
url = 0
emoji = 0
keyword = 0
specialSym = 0
mathSym = 0



from sklearn.ensemble import RandomForestClassifier
df = pd.read_csv('spam.csv')
df.columns = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'Y']
df.head()

from sklearn.cross_validation import train_test_split
forest = RandomForestClassifier(n_estimators=100, oob_score=True, random_state=123456)
X = df.values[:, 0:9]
Y = df.values[:, 9]
trainX, testX, trainY, testY = train_test_split( X, Y, test_size = 0.3)
forest.fit(trainX, trainY)
print('Accuracy: \n', forest.score(testX, testY))
pred = forest.predict(testX)

msg = input("Type a message")

length = len(msg)

checkUppCase(msg)
checkLowCase(msg)
checkDot(msg)
checkMob(msg)
checkUrl(msg)
checkEmoji(msg)
checkKeyword(msg)
checkSpecialSym(msg)
checkMathSym(msg)

result = forest.predict([[uppCase,lowCase,dot,mob,url,emoji,keyword,specialSym,mathSym]])

if result == 0:
    print("it's HAM")

if result == 1:
    print("It's SPAM")


