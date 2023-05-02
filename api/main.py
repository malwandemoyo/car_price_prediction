import numpy as np
from model import predict_price
from flask import Flask, request, jsonify, render_template, json
# import pickle

app = Flask(__name__)
# model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST', 'GET'])
def predict():
   
    car_trans = ['Manual', 'Automatic'] 
    car_fuel_type = ['Diesel', 'Petrol']
    previous_owners = ['1', '2', '3', 'more']
    
    my_data = ['mileage', 'fuel-type', 'previous-owners', 'transmission', 'year']
    user_input = []
    
    for data in my_data:
        user_input.append(request.form.get(data))

    print(user_input)

    
    
    return 'Success'

    
    # for dta in mydata:
    #     print(type(dta))
        
    # data2 = json.loads(request.form)
    # print(data2)
    # print(f'Thiis the output: {request}')



    # print(request)   

#     int_features = [int(x) for x in request.form.values()]
#     final_features = [np.array(int_features)]
#     prediction = model.predict(final_features)

#     output = round(prediction[0], 2)

#     return render_template('index.html', prediction_text='Sales should be $ {}'.format(output))

# @app.route('/results',methods=['POST'])
# def results():

#     data = request.get_json(force=True)
#     prediction = model.predict([np.array(list(data.values()))])

#     output = prediction[0]
#     return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)