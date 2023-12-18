from flask import Flask, render_template, request, jsonify
import requests
import logging
import os

app = Flask(__name__)

CAT_API_URL = os.environ.get('CAT_API_URL', 'https://api.thecatapi.com/v1/images/search?limit=10')

logging.basicConfig(level=logging.ERROR)

def get_random_cat_url():
    try:
        response = requests.get(CAT_API_URL)
        response.raise_for_status()
        cat_data = response.json()
        return cat_data[0]['url']
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching cat image: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ajax', methods=['POST'])
def ajax():
    data = request.json
    name = data.get('name', 'Guest')
    
    cat_url = get_random_cat_url()
    message = f"Hello, {name}! Meow! 🐱"
    
    return jsonify({'message': message, 'cat_url': cat_url})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
