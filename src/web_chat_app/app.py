
from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

@app.route('/aks', methods = ['POST'])
def ask_question():
    try:
        question = request.json['question']
    except Exception as e:
        return jsonify({'message': 'Error Occured', 'status' : f'error{e}'})
    
@app.route('/add_document')
def add_document():
    document = request.json['document']
    return jsonify({'messsage': 'Document Added Successfully',  'status' : 'succes'})

@app.route('/')
def home():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)