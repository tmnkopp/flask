import json, os, re
import pandas as pd
import numpy as np 
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data_from_csv/')
def get_data_from_csv():  
    file_path = os.path.join(app.static_folder, 'titanic.csv')
    df=pd.read_csv(file_path)
    dict = str(df.to_dict(orient='records'))
    with open(app.static_folder + r'\titanic.json','w') as f:
        f.write(dict)
    return jsonify(dict)

@app.route('/get_data_from_json/')
def get_data_from_json():  
    file_path = os.path.join(app.static_folder, 'titanic.json')
    with open(file_path,'r') as f:
        data=f.read()
        return jsonify(data) 

if __name__ == "__main__":
    app.run(debug=True)