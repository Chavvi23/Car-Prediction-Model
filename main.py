import pickle
import numpy as np
from flask import Flask, render_template, request
app = Flask(__name__)
model = pickle.load(open('grb.pkl', 'rb'))
@app.route('/',methods=["GET"])
def Home():
    return render_template('index.html')

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        y = int(request.form['year'])
        y=2022-y
        price = float(request.form['present_price'])
        km = float(request.form['km_driven'])
        km=np.log(km)
        owners = float(request.form['owners'])
        fuel = (request.form['fuel'])
        if fuel=='Petrol':
            Fuel_Type_Petrol=1
            Fuel_Type_Diesel=0
        else:
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=1
        person = (request.form['person'])
        if person=='Individual':
            Seller_Type_Individual=1
        else:
            Seller_Type_Individual=0
        trans = (request.form['trans'])
        if trans=='Manual':
            Transmission_Mannual=1
        else:
            Transmission_Mannual=0
        prediction = model.predict([[price, km, owners,y, Fuel_Type_Diesel,
                                     Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Mannual]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You Can Sell The Car at {}".format(output))
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
