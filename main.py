from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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