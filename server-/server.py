from flask import Flask, request, jsonify
app = Flask(__name__)

# util will contain all the core routines whereas the server will
# just do the routing of the request
import util
# First routine would be to return the locations in Banglore city
# we have locations in model-/columns.json file
# need to create sub directory called aritfacts in server- directory

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/predict_home_price',methods=['POST'])
def predict_home_price():
    # When we run HTML file we will get all int inputs in
    # request.form in this form
    total_sqft= float(request.form['total_sqft'])
    location= request.form['location']
    bhk= int(request.form['bhk'])
    bath= int(request.form['bath'])
    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin','*')

    return response

if __name__ == "__main__":
    print("Starting python Flask Server for House Price Prediction...")
    util.load_saved_artifacts()
    app.run()