import pickle
from flask import Flask, render_template, request
from sklearn.datasets import load_iris
data = load_iris()

# Initialize the Flask app
app = Flask(__name__)

# Load the pre-trained Random Forest model
with open('random_forest_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Define a route for the home page
@app.route('/')
def home():
    return render_template("index.html")

# Define a route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get input values from the HTML form
    sepal_length = float(request.form['sepal_length'])
    sepal_width = float(request.form['sepal_width'])
    petal_length = float(request.form['petal_length'])
    petal_width = float(request.form['petal_width'])

    # Make a prediction using the loaded model
    prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]

    # Get the class label (Iris species name) from the dataset
    species = data.target_names[prediction]

    return render_template('index.html', prediction_text=f'Predicted Species: {species}')

if __name__ == '__main__':
    app.run(debug=True)



