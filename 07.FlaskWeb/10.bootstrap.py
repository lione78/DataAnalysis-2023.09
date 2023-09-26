from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>부트스트랩</h2>'

@app.route('/list')
def list():
    return render_template('10.list.html')

@app.route('/form')
def form():
    return render_template('10.form.html')

@app.route('/modal')
def modal():
    return render_template('10.modal.html')

if __name__ == '__main__':
    app.run(debug=True)