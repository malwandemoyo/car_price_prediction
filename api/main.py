import numpy as np
from model import predict_price
from flask import Flask, request, jsonify, render_template, json

app = Flask(__name__)

car_brand_mapping = {
    'Toyota': 1.1,
    'Isuzu': 1.2,
    'Honda': 0.92,
    'Hyundai': 0.95,
    'Mazda': 0.95,
    'BMW': 1.66,
    'Audi': 2.0,
    'Mercedez-Benz': 1.9,
    'Ford': 1.8,
    'Datsun': 1.4,    
}

@app.route('/', methods=['GET'])
def home():
        return render_template("index.html",)

@app.route('/predict',methods=['POST'])
def predict():    
    user_input = {
        "transmission": request.form.get('transmission'),
        "fuel_type": request.form.get('fuel-type'),
        "previous_owners": int(request.form.get('previous-owners')),
        "year": int(request.form.get('year')),
        "mileage": int(request.form.get('mileage')),
        }
        
   
    car_price = predict_price(user_input['transmission'], user_input['fuel_type'], user_input['previous_owners'], user_input['year'], user_input['mileage'])
    
    return render_template("index.html", 
                            transmission=user_input['transmission'],
                            fuel_type=user_input['fuel_type'],
                            previous_owners=user_input['previous_owners'],
                            year=2020,
                            mileage=user_input['mileage'],
                            price=car_price)

if __name__ == "__main__":
    app.run(debug=True)