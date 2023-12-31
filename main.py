from flask import Flask, render_template, request, jsonify
from src.scraper import scraper
from src.scrapey_multi import get_data
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_input', methods=['POST'])
def process_input():
    user_input = request.json.get('user_input')
    additional_data = request.json.get('additional_data')
    print(user_input)
    print(additional_data)

    if (additional_data == "selling"):
        # Process the user input as needed
        result = f"You entered: {user_input}"
        total = get_data(user_input.split(' '), 3)
        return jsonify({'result': total})
    elif(additional_data == "buying"):
        scrape = scraper(user_input)
        output = ""
        for i in scrape[0]:
            output = output + "| " + i[1] + " "
        output = output + "  |||  " + scrape[1]
        return jsonify({'result': scrape})


@app.route('/about')
def about():
    return render_template('pages/about.html')

@app.route('/buying')
def buying():
    return render_template('pages/buying.html')

@app.route('/selling')
def selling():
    return render_template('pages/selling.html')

@app.route('/contact')
def contact():
    return render_template('pages/contact.html')

if __name__ == '__main__':
    app.run(debug=True)