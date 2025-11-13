# import the necessary libraries 
from flask import Flask, request, render_template
import pickle
import numpy as np

# initialize the flask application
app = Flask(__name__)

# load the model
with open("iris_model.pkl", "rb") as file:
    model = pickle.load(file)

# define the home route
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # get input features
    sepal_length = float(request.form['sepal_length'])
    sepal_width = float(request.form['sepal_width'])
    petal_length = float(request.form['petal_length'])
    petal_width = float(request.form['petal_width'])

    # prepare the feature array for prediction
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(features)

    # model already returns a species name like "Iris-virginica"
    predicted_species = prediction[0]

    return render_template('index.html', prediction=f'The predicted species is {predicted_species}')

if __name__ == "__main__":
    app.run(debug=True)
