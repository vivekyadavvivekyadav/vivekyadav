from re import template
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from joblib import dump, load

app = Flask(__name__,template_folder='template') #Initialize the flask App
model = pickle.load(open(r'C:\Users\VIVEK\Desktop\project\rental proj\model.pkl', 'rb')) # loading the trained model
@app.route('/') # Homepage
def home():
    return render_template('index.html')

@app.route('/predict/',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    print("TEST")
    # retrieving values from form
    print(request.form.values)
    init_features = [[int(x) for x in request.form.values()]]
    print(init_features)
    
    #final_features = [np.array(init_features)]

    prediction =  model.predict((np.array(init_features)))
    print(prediction)
    # rendering the predicted result
    return render_template('index.html',Prediction_text='Predicted price : €{}'.format(prediction)) 
if __name__ == "__main__":

    app.run(debug=True)