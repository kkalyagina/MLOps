import os
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import joblib
import numpy as np
import pandas as pd
import json
from json import JSONEncoder

app = Flask(__name__)
api = Api(app)

model = joblib.load('iris-model.model')

class MakePrediction(Resource):
    @staticmethod
    def post():
        posted_data = request.get_json()
        
        # data=np.array(posted_data['features']).reshape(1, -1)
        # prediction=model.predict(data)

        data=np.array(list(posted_data['features']))
        prediction=model.predict(data)

        prediction=pd.Series(prediction).to_json(orient='values')
       

        # class NumpyArrayEncoder(JSONEncoder):
        #     def default(self, obj):
        #         if isinstance(obj, np.ndarray):
        #             return obj.tolist()
        #         return JSONEncoder.default(self, obj)

        # # Serialization
        # numpyData = {"predict":prediction}
        # encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  
        


        # if first_predict == 0:
        #     predicted_class = 'Iris-setosa'
        # elif first_predict == 1:
        #     predicted_class = 'Iris-versicolor'
        # else:
        #     predicted_data = 'Iris-virginica'

        
        return jsonify({
            'Prediction': prediction
        })


api.add_resource(MakePrediction, '/predict')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)
