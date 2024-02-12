from flask import Flask, request, jsonify
from scrape.scraper import scraper
from scrape.scrapey_multi import get_data
app = Flask(__name__)

@app.route('/process_input', methods=['GET'])
def process_input():
    user_input = request.json.get('user_input')
    additional_data = request.json.get('additional_data')
    
    print(user_input)
    print(additional_data)

    if (additional_data == "selling"):
        total = get_data(user_input.split(' '), 3)
        return jsonify({'result': total})
    
    elif(additional_data == "buying"):
        scrape = scraper(user_input)
        output = ""
        
        for i in scrape[0]:
            output = output + "| " + i[1] + " "
        output = output + "  |||  " + scrape[1]
        
        return jsonify({'result': scrape})

if __name__ == '__main__':
    app.run(debug=True, port=5000)