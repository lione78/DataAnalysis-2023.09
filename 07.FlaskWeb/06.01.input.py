from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h2>계산기/언어와 음식</h2>'

@app.route('/calc', methods=['GET', 'POST'])
def calc():
    pass

if __name__ == '__main__':
    app.run(debug=True)