from flask import Flask, request, jsonify
from flask_cors import CORS
from scrape.scraper import scraper
from scrape.scrapey_multi import get_data

app = Flask(__name__)
CORS(app)

@app.route('/api/selling', methods=['POST'])
def selling():
    user_input = request.json.get('user_input')
    
    total = get_data(user_input.split(' '), 3)
    
    return jsonify({'result': total})

@app.route('/api/buying', methods=['POST'])
def buying():
    user_input = request.json.get('user_input')

    scrape = scraper(user_input)
    output = ""
        
    for i in scrape[0]:
        output = output + "| " + i[1] + " "
    output = output + "  |||  " + scrape[1]
    
    return jsonify({'result': scrape})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)