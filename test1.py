from flask import Flask, request, jsonify
import werkzeug
import predictor

app = Flask(__name__)

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

# @app.route('/uploadimage', methods=["POST"])
# def uploadImage():
#     if(request.method == "POST"):
#         imageFile = request.files['image']
#         headerData = request.headers["data"]
#         filename = werkzeug.utils.secure_filename(imageFile.filename)
#         imageFile.save("./uploadedImages/" + filename)

#         # Preprocessing the header data
#         cordListOfBbox = preProcessHeader(headerData)
#         print(cordListOfBbox)

#         #Predict the count using model
#         inputImagePath = "./uploadedImages/" + filename
#         predictedCount = predictor.predictorModel(inputImagePath, cordListOfBbox)

#         return jsonify({
#             "message":"Image Uploaded Successfully"
#         })

def uploadTest():
    filename = 'ipl.jpg'
    headerData = "Rect.fromLTRB(231.0, 254.9, 304.4, 406.9),Rect.fromLTRB(85.3, 306.3, 131.0, 389.5)"



    # Preprocessing the header data
    cordListOfBbox = preProcessHeader(headerData)
    print(cordListOfBbox)

    # Predict the count using model
    inputImagePath = "./uploadedImages/" + filename
    predictedCount = predictor.predictorModel(inputImagePath, cordListOfBbox)

    print(predictedCount)



if __name__ == "__main__":
    app.run(debug=True, port=4000)