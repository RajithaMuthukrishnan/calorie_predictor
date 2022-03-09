from flask import Flask,request, url_for, redirect, render_template, jsonify
from werkzeug.utils import secure_filename
import os
import pandas as pd
from PIL import Image
import keras
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("prediction_model.pkl", "rb"))
cols = ['Gender', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate']

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict',methods=['POST'])
def predict():
    inputs = [x for x in request.form.values()]
    gender = inputs[0]
    age = inputs[1]
    height = inputs[2]
    height_unit = inputs[3]
    weight = inputs[4]
    weight_unit = inputs[5]
    duration = inputs[6]
    duration_unit = inputs[7]
    heart_rate = inputs[8]
    
    if gender == 'male':
        gender_feature = int(0)
    if gender == 'female':
        gender_feature = int(1)

    age_feature = int(age)

    if height_unit == 'cm':
        height_feature = float(height)
    if height_unit == 'ft':
        height_feature = (float(height) / 30.48)

    if weight_unit == 'kg':
        weight_feature = float(weight)
    if weight_unit == 'lb':
        weight_feature = (float(weight) / 2.2046)

    if duration_unit == 'min':
        duration_feature = float(duration)
    if duration_unit == 'hr':
        duration_feature = (float(duration) * 60)

    features = np.array([gender_feature, age_feature, height_feature, weight_feature, duration_feature, heart_rate])
    data_unseen = pd.DataFrame([features], columns = cols)
    data = data_unseen.astype({'Gender':'int64','Age':'int64','Height':'float64','Weight':'float64','Duration':'float64','Heart_Rate':'float64'})
    prediction = model.predict(data)
    result = round(prediction[0])
    return render_template('home.html', gender='Gender : {}'.format(gender), age='Age : {}'.format(age), height='Height : {}'.format(height + ' ' + height_unit), weight='Weight : {}'.format(weight + ' ' + weight_unit), duration='Duration : {}'.format(duration + ' ' + duration_unit), heartrate='Heart rate : {}'.format(heart_rate), pred='Calories burned: {}'.format(result))


if __name__ == '__main__':
    app.run(debug=True)
