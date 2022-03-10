# Import the neccesary packages
from flask import Flask,request, url_for, redirect, render_template
from werkzeug.utils import secure_filename
import pandas as pd
import keras
import pickle
import numpy as np

app = Flask(__name__)

# Import the best performing Machine Learning model
model = pickle.load(open("prediction_model.pkl", "rb"))
# Specify the column names for the features
cols = ['Gender', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate']

# Executed when the URL https://localhost:5000/ launched
@app.route('/')
def home():
    return render_template("home.html")

# Executed when /predict URL is lauched on a POST action
@app.route('/predict',methods=['POST'])
# Function to use ML model to predict calories for the inputs
def predict():
    # Obtain values from the inputs in webpage
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
    
    # Preprocess the obtained inputs to be used by the ML model
    # Assign value 0 for male and 1 for female
    if gender == 'male':
        gender_feature = int(0)
    if gender == 'female':
        gender_feature = int(1)

    # Convert age to integer type
    age_feature = int(age)

    # Convert height to centimeter and float type
    if height_unit == 'cm':
        height_feature = float(height)
    if height_unit == 'ft':
        height_feature = (float(height) / 30.48)

    # Convert weigh to kilograms and float type
    if weight_unit == 'kg':
        weight_feature = float(weight)
    if weight_unit == 'lb':
        weight_feature = (float(weight) / 2.2046)

    # Convert duration to minutes and float type
    if duration_unit == 'min':
        duration_feature = float(duration)
    if duration_unit == 'hr':
        duration_feature = (float(duration) * 60)

    # Create a feature array
    features = np.array([gender_feature, age_feature, height_feature, weight_feature, duration_feature, heart_rate])
    # Convert feature array to pandas dataframe
    data_unseen = pd.DataFrame([features], columns = cols)
    # Reassure the type of features
    data = data_unseen.astype({'Gender':'int64','Age':'int64','Height':'float64','Weight':'float64','Duration':'float64','Heart_Rate':'float64'})
    # Use the ML model to predict the calories using the features
    prediction = model.predict(data)
    # Obtain the predicted value and round the value to 0 decimal points
    result = round(prediction[0])
    # Send the input data obtained and calories predicted to the home.html file
    return render_template('home.html', gender='Gender : {}'.format(gender), age='Age : {}'.format(age), height='Height : {}'.format(height + ' ' + height_unit), weight='Weight : {}'.format(weight + ' ' + weight_unit), duration='Duration : {}'.format(duration + ' ' + duration_unit), heartrate='Heart rate : {} bpm'.format(heart_rate), pred='Calories burned: {}'.format(result))


# Added to execute the code above when app.py(this file) is launched
if __name__ == '__main__':
    app.run(debug=True)
