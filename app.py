from flask import Flask, jsonify

app=Flask(__name__)

@app.get('/')
def home():
    return "First basic structure of Flask"

@app.get('/json-home')    
def json_home():
    return jsonify({"message": "First basic structure of Flask"})
