import sklearn
from sklearn import linear_model
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import VotingRegressor 
from sklearn import tree
import pandas as pd

def createPositionModel(file, position):
    df = pd.read_csv(file)
    df = df.dropna()
    df = df[df['FantPos'] == position]

    if position == 'QB':
        X = df[['PassAtt/G','PassYds/G', 'PassTD/G', 'RushAtt/G', 'Y/A','RushYds/G',
                    'RushTD/G', 'TotTD/G','PPG','VBD']]
    elif position == 'RB':
        X = df[['RushAtt/G', 'Y/A','RushYds/G', 'RushTD/G','Rec/G','RecYds/G','Y/R',
                    'RecTD/G','TotTD/G','PPG','VBD']]
    elif position == 'WR' or 'TE':
        X = df[['Rec/G','RecYds/G','Y/R', 'RecTD/G','TotTD/G','PPG','VBD']]
    else:
        print('Invalid position entered')
        return

    y = df['Next Year PPG']

    reg1 = GradientBoostingRegressor(random_state=1)
    reg2 = RandomForestRegressor(random_state=1)
    reg3 = LinearRegression()
    
    regr = VotingRegressor(estimators=[('gb', reg1), ('rf', reg2), ('lr', reg3)])
    regr.fit(X, y)
    return regr


def testModelAccuracy(model, file, position):
    df = pd.read_csv(file)
    df = df.dropna()
    df = df[df['FantPos'] == position]

    if position == 'QB':
        XTest = df[['PassAtt/G','PassYds/G', 'PassTD/G', 'RushAtt/G', 'Y/A','RushYds/G',
                    'RushTD/G', 'TotTD/G','PPG','VBD']]
    elif position == 'RB':
        XTest = df[[ 'RushAtt/G', 'Y/A','RushYds/G', 'RushTD/G','Rec/G','RecYds/G','Y/R',
                    'RecTD/G','TotTD/G','PPG','VBD']]
    elif position == 'WR' or 'TE':
        XTest = df[['Rec/G','RecYds/G','Y/R', 'RecTD/G','TotTD/G','PPG','VBD']]
    else:
        print('Invalid position entered')
        return

    yTest = df['Next Year PPG']
    results = model.score(XTest, yTest)
    return results


def testModelDifference(model, file, position):

    df = pd.read_csv(file)
    df = df.dropna()
    df = df[df['FantPos'] == position]

  
    if position == 'QB':
        XTest = df[['PassAtt/G','PassYds/G', 'PassTD/G', 'RushAtt/G', 'Y/A','RushYds/G',
                    'RushTD/G', 'TotTD/G','PPG','VBD']]
    elif position == 'RB':
        XTest = df[['RushAtt/G', 'Y/A','RushYds/G', 'RushTD/G','Rec/G','RecYds/G','Y/R',
                    'RecTD/G','TotTD/G','PPG','VBD']]
    elif position == 'WR' or 'TE':
        XTest = df[['Rec/G','RecYds/G','Y/R', 'RecTD/G','TotTD/G','PPG','VBD']]
    else:
        print('Invalid position entered')
        return


    yPred = model.predict(XTest)
    predAndActual = {'Name': df['Player'], 'Predicted PPG': yPred,
                     'Actual PPG': df['Next Year PPG']}


    dataFrame = pd.DataFrame(predAndActual)

    dataFrame['Predicted PPG'] = dataFrame['Predicted PPG'].round(decimals=3)
    dataFrame['Difference'] = dataFrame['Predicted PPG'] - dataFrame['Actual PPG']
    dataFrame['Difference'] = dataFrame['Difference'].round(decimals=3)
    dataFrame['AbsDifference'] = dataFrame['Difference'].abs()
    meanDiff = round(dataFrame['Difference'].mean(), 3)
    medianDiff = round(dataFrame['Difference'].median(), 3)
    meanAbsDiff = round(dataFrame['AbsDifference'].mean(), 3)
    medianAbsDiff = round(dataFrame['AbsDifference'].median(), 3)

    return dataFrame, meanDiff, medianDiff, meanAbsDiff, medianAbsDiff

def testModel(model, testCSV, trainingCSV, position):
    accuracy = testModelAccuracy(model, trainingCSV, position)
    differences = testModelDifference(model, testCSV, position)
    meanDiff = differences[1]
    medDiff = differences[2]
    meanAbsDiff = differences[3]
    medAbsDiff = differences[4]

    print('The accuracy of the {0} model is {1}'.format(position, accuracy))
    print('The {0} model has an average error of {1} PPG and an average absolute error of {2} PPG'.format(position, meanDiff, meanAbsDiff))
    print('The {0} model has a median error of {1} PPG and a median absolute error of {2} PPG'.format(position, medDiff, medAbsDiff))
    print('\n')

def useModel(model, file, position):
    df = pd.read_csv(file)
    df.dropna()
    df = df[df['FantPos'] == position]

    if position == 'QB':
        X = df[['PassAtt/G','PassYds/G', 'PassTD/G', 'RushAtt/G', 'Y/A',
                'RushYds/G', 'RushTD/G', 'TotTD/G','PPG','VBD']]
    elif position == 'RB':
        X = df[['RushAtt/G', 'Y/A','RushYds/G', 'RushTD/G','Rec/G',
                'RecYds/G', 'Y/R', 'RecTD/G','TotTD/G','PPG','VBD']]
    elif position == 'WR' or 'TE':
        X = df[['Rec/G','RecYds/G','Y/R', 'RecTD/G','TotTD/G','PPG','VBD']]
    else:
        print('Invalid position entered')
        return
    yPred = model.predict(X)

    dataFrameDict = {'Name': df['Player'], 'FantPos': df['FantPos'], 'Predicted PPG': yPred}
    dataFrame = pd.DataFrame(dataFrameDict)
    dataFrame = dataFrame.sort_values(by = ['Predicted PPG'], ascending = False)
    dataFrame['Predicted PPG'] = dataFrame['Predicted PPG'].round(decimals = 3)
    dataFrame['Predicted PPR'] = 17 * dataFrame['Predicted PPG']
    dataFrame['Predicted PPR'] = dataFrame['Predicted PPR'].round(decimals = 3)

    posRank = []
    posRankNum = 1
    for index, row in df.iterrows():
        posRank.append(posRankNum)
        posRankNum += 1

    dataFrame['PosRank'] = posRank
  
    if position == 'QB':
        playersDrafted = 10 * 2
    if position == 'RB':
        playersDrafted = 10 * 4.5
    if position == 'WR':
        playersDrafted = 10 * 3.5
    if position == 'TE':
        playersDrafted = 10 * 2

    playersDrafted = playersDrafted
    newDF = dataFrame[dataFrame['PosRank'] == playersDrafted]
    baseline = newDF.iloc[0].at['Predicted PPR']
    dataFrame['VBD'] = dataFrame['Predicted PPR'] - baseline
    dataFrame['VBD'] = dataFrame['VBD'].round(decimals = 3)

    dataFrame = dataFrame.reset_index(drop = True)

    return dataFrame.to_string(max_rows=200)


file = "testing.csv"
file2 = "training.csv"
f = "test2.csv"
l = createPositionModel("testing.csv", "RB")
print(testModelAccuracy(l, file, "RB"))
testModel(l,file, file2, "RB")
print(useModel(l,file2,"RB"))