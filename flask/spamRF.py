#import numpy
#import scipy
#import sklearn
import pandas as pd

from flask import Flask, render_template, request, session
app = Flask(__name__)

msgLog = []
logLen = -1

def prediction(someMsg):
    mobList = "0123456789"
    urlList = [".com", ".in", ".org"]
    emojiList = [":)",":(",":P",":-*","XD"]
    keywordList = ["money","call","offer"]
    specialSymList = "!@#$%^&*(){}[]:;\"'"
    mathSymList = "+-/*%^."

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
    forest = RandomForestClassifier(n_estimators=100, oob_score=True)
    X = df.values[:, 0:9]
    Y = df.values[:, 9]
    trainX, testX, trainY, testY = train_test_split( X, Y, test_size = 0.3)
    forest.fit(trainX, trainY)
    #print('Accuracy: \n', forest.score(testX, testY))
    #pred = forest.predict(testX)

    #print("Feature importance\n")
    #print(forest.feature_importances_)

    #print("INITIALIZATION COMPLETE")
 
    msg = someMsg
    length = len(msg)

    #checkUppCase(msg)
    for i in msg:
        if (i.isupper()) == True:
            uppCase += 1
    uppCase = uppCase/length * 100
        
    for i in msg:
        if (i.islower()) == True:
            lowCase += 1
    lowCase = lowCase/length * 100

    for i in msg:
        if i == ".":
            dot += 1
    dot = dot/length * 100

    for i in msg:
        if i in mobList:
            mob += 1
    mob = mob/length * 100

    for i in urlList:
        if i in msg:
            url += 1
    url = url/length * 100

    for i in emojiList:
        if i in msg:
            emoji += 1
    emoji = emoji/length * 100

    for i in keywordList:
        if i in msg:
            keyword += 1
    keyword = keyword/length * 100

    for i in msg:
        if i in specialSymList:
            specialSym += 1
    specialSym = specialSym/length * 100

    for i in msg:
        if i in mathSymList:
            mathSym += 1
    mathSym = mathSym/length * 100

    result = forest.predict([[uppCase,lowCase,dot,mob,url,emoji,keyword,specialSym,mathSym]])

    if result == 0:
        print("hammm")
        global msgLog
        msgLog.append(msg)
        msgLog.append(' ')
        return 'HAM'

    if result == 1:
        print("spammmmmm")
        #global msgLog
        msgLog.append(msg)
        msgLog.append('SPAM')
        return 'SPAM'




user = 0
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if 'name' not in session:
        global user
        user += 1
        session['name'] = 'user' + str(user)

    if request.method == 'POST':
        global msgLog
        global logLen
        msgLog.append(session['name'])
        prediction(request.form['message'])

        logLen = len(msgLog)    
    return render_template('index.html', msgLog = msgLog, logLen = logLen)


app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'



