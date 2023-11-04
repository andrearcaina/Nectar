from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('get.html')

@app.route('/process_input', methods=['POST'])
def process_input():
    user_input = request.json.get('user_input')
    print(user_input)
    # Process the user input as needed
    result = f"You entered: {user_input}"
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run()