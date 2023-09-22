import sys
from flask import Flask, request

from model import sample


app = Flask(__name__)

@app.route('/generate_dsl', methods=['POST'])
def create_dsl():
    if request.method == 'POST':
        file = request.files['file']
        return sample(file)
    return 'success'
    
