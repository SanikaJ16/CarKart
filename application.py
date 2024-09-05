from flask import Flask, jsonify,render_template,request,redirect
from flask_cors import CORS,cross_origin
import pickle
import pandas as pd
import numpy as np

app=Flask(__name__)
cors=CORS(app)
model1=pickle.load(open('D:\CPP\LinearRegressionModel.pkl','rb'))
model2=pickle.load(open('D:\CPP\LassoRegressioModel.pkl','rb'))
model3=pickle.load(open('D:\CPP\DecisionTreeRegression.pkl','rb'))
model4=pickle.load(open('D:\CPP\RandomForestRegressionModel.pkl','rb'))
model5=pickle.load(open('D:\CPP\KNNModel.pkl','rb'))
car=pd.read_csv('D:\CPP\Cleaned.csv')

@app.route('/',methods=['GET','POST'])
def index():
    companies=sorted(car['company'].unique())
    car_models=sorted(car['name'].unique())
    year=sorted(car['year'].unique(),reverse=True)
    fuel_type=car['fuel_type'].unique()
    companies.insert(0,'Select Company')
    return render_template('index.html',companies=companies, car_models=car_models, years=year,fuel_types=fuel_type)


@app.route('/buy')
def buy():
    return render_template('buy.html')
@app.route('/predict', methods=['POST', 'GET'])
@cross_origin()
def predict():
    if request.method == 'POST':
        # Handle the form submission
        company = request.form.get('company')
        car_model = request.form.get('car_models')
        year = request.form.get('year')
        fuel_type = request.form.get('fuel_type')
        driven = request.form.get('kilo_driven')

        # Make predictions using the models
        prediction1 = model1.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                                                 data=np.array([car_model, company, year, driven, fuel_type]).reshape(1, 5)))
        prediction2 = model2.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                                                 data=np.array([car_model, company, year, driven, fuel_type]).reshape(1, 5)))
        prediction3 = model3.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                                                 data=np.array([car_model, company, year, driven, fuel_type]).reshape(1, 5)))
        prediction4 = model4.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                                                 data=np.array([car_model, company, year, driven, fuel_type]).reshape(1, 5)))
        prediction5 = model5.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                                                 data=np.array([car_model, company, year, driven, fuel_type]).reshape(1, 5)))

        predictions_dict = {
            "Linear": int(prediction1[0]),
            "Lasso": int(prediction2[0]),
            "Decision": int(prediction3[0]),
            "Random": int(prediction4[0]),
            "KNN": int(prediction5[0])
        }
        # Return the dictionary as JSON
        return jsonify(predictions_dict)
    # For GET requests, render the form
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    year = sorted(car['year'].unique(), reverse=True)
    fuel_type = car['fuel_type'].unique()
    companies.insert(0, 'Select Company')
    return render_template('predict.html', companies=companies, car_models=car_models, years=year, fuel_types=fuel_type)
    # return render_template('predict.html')

if __name__=='__main__':
    app.run(debug=True, use_reloader=True)
    
