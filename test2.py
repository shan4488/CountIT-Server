import predictor

def preProcessHeader(headerData):
    headerDataList = headerData.split(")")
    # print(headerDataList[0] +" | " + headerDataList[1] +" | " + headerDataList[2])
    dataList = []
    for item in headerDataList:
        strippedData = item.strip(",Rect.fromLTRB(")
        # print(type(strippedData))
        cordDataList = strippedData.split(",")
        print(cordDataList)
        dataList.append(cordDataList)
    dataList.pop()
    return dataList


def uploadTest():
    filename = 'oranges.jpg'
    #headerData = "Rect.fromLTRB(208.6, 180.9, 254.4, 520.5),Rect.fromLTRB(111.4, 186.2, 159.8, 501.4),Rect.fromLTRB(44.7, 194.4, 46.8, 494.2),Rect.fromLTRB(24.0, 192.2, 80.7, 480.7)"
    #headerData = "Rect.fromLTRB(62.3, 163.5, 91.1, 463.5),Rect.fromLTRB(193.7, 161.2, 216.0, 463.5),Rect.fromLTRB(273.9, 156.9, 297.5, 463.9)"
    headerData = "Rect.fromLTRB(71.0, 49.0, 104.0, 83.0),Rect.fromLTRB(134.0, 119.0,  169.0, 151.0),Rect.fromLTRB(7.0, 200.0, 44.0, 236.0)"
    #headerData = "Rect.fromLTRB(218.5, 116.0, 302.9, 608.2)"

    # Preprocessing the header data
    cordListOfBbox = preProcessHeader(headerData)
    print(cordListOfBbox)

    # Predict the count using model
    inputImagePath = "./uploadedImages/" + filename
    predictedCount = predictor.predictorModel(inputImagePath, cordListOfBbox)

    print(predictedCount)


uploadTest()