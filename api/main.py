import numpy as np
from model import predict_price
from flask import Flask, request, jsonify, render_template, json


app = Flask(__name__)

# transmission
# fuel_type
# previous_owners
# year
# car_price


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
    
    print(car_price)
    print(user_input)
    

    return render_template("index.html", 
                            transmission=user_input['transmission'],
                            fuel_type=user_input['fuel_type'],
                            previous_owners=user_input['previous_owners'],
                            year=2020,
                            mileage=user_input['mileage'],
                            price=car_price)

if __name__ == "__main__":
    app.run(debug=True)