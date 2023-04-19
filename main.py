from flask import Flask, request, jsonify
import werkzeug
import predictor
import math

app = Flask(__name__)

def preProcessHeader(headerData):
    headerDataList = headerData.split(")")
    dataList = []
    for item in headerDataList:
        strippedData = item.strip(",Rect.fromLTRB(")
        # print(type(strippedData))
        cordDataList = strippedData.split(",")
        print(cordDataList)
        dataList.append(cordDataList)
    dataList.pop()
    return dataList

@app.route('/uploadimage', methods=["POST"])
def uploadImage():
    if(request.method == "POST"):
        imageFile = request.files['image']
        headerData = request.headers["data"]
        filename = werkzeug.utils.secure_filename(imageFile.filename)
        imageFile.save("./uploadedImages/" + filename)

        # Preprocessing the header data
        cordListOfBbox = preProcessHeader(headerData)
        print(cordListOfBbox)

        # Predict the count using model
        inputImagePath = "./uploadedImages/" + filename
        predictedCount = predictor.predictorModel(inputImagePath, cordListOfBbox)

        return jsonify({
            "message":"Image Uploaded Successfully : " + str(math.ceil(float(predictedCount)))
        })



if __name__ == "__main__":
    app.run(debug=True, port=4000)