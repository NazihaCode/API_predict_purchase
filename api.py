# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 03:28:57 2023

@author: Naziha
"""



from flask import Flask, jsonify, make_response, request
#from flask_ngrok import run_with_ngrok
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

from flask import render_template



app = Flask(__name__)
model=pickle.load(open('model.pkl','rb'))
#run_with_ngrok(app)
scaler =StandardScaler()
@app.route("/")
def putStatus():
    return render_template('index.html')
 # return jsonify(data)
 


@app.route('/predict',methods=['GET','POST'])
def predict():
    #accept_json=[('Content-Type', 'application/json;')]
    data = request.form
    gender = str(data['Gender'])
    age = str(data['Age'])
    sal = str(data['Salary'])
    test = np.array([[gender,age,sal]])
    prediction = model.predict(scaler.fit_transform(test))
    output = prediction[0]
    if(output == 0):
        result = "He/She's not gonna purchase it!"
    else:
        result= "He/She's gonna purchase it!"
    return render_template('result.html',response = result) 
if __name__ == "__main__":
    app.run(debug=True)
    
