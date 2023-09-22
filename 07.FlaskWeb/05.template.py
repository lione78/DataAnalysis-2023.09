from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Template</h2>'

 # name 값을 주면 그 값이 되고, 안 주면 None이 됨. default 설정/ None없으면 에러 발생
@app.route('/hello', methods=['GET', 'POST'])
@app.route('/hello/<name>')
def hello(name=None):
    if request.method == 'GET':
        dt = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
        return render_template('05.template.html', name=name if name != None else '', dt=dt)        # Params를 html로 전달
    else:
        name_ = request.values['name']
        return f'{name_}'
    
if __name__ == '__main__':
    app.run(debug=True)