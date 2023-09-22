from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>파라메터 전달값 받기</h2>' 

# localhost:5000/area?pi=3.14&radius=10 // 옛날 방식
@app.route('/area')
def area():
    pi = request.args.get('pi', '3.141592')         # defalut값을 줄 수 있다. / 여기서는 에러 안남
    radius = request.values['radius']               # GET/POST 모두 사용할 수 있음.
    result = float(pi) * float(radius) * 2          # float 변환시 에러남.
    return f'<h1>pi={pi}, radius={radius}, area={result}</h1>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('02.login.html')
    else:
        uid = request.form['uid']
        pwd = request.values['pwd']
        return f'<h1>uid={uid}, pwd={pwd} 환영합니다.</h1>'
    
@app.route('/sample', methods=['GET', 'POST'])
def sample():
    if request.method == 'GET':
        return render_template('03.sample.html')
    else:
        a = request.values['a']
        b = request.values['b']
        c = float(a) * float(b)
        return f'<h2>{a} * {b} = {c}</h2>'
    
# localhost:5000/user/james, localhost:/user/maria
@app.route('/user/<uname>')
def user(uname):
    return f'<h1>uname = {uname}</h1>'

# localhost:5000/square/12
@app.route('/square/<int:number>')          # 보통은 str , param앞에 data type 지정
def square(number):
    return f'<h1>{number} ** 2 = {number ** 2}</h1>'

# localhost:5000/circle/3.14/and/10.0
@app.route('/circle/<float:pi>/and/<float:radius>')     # type을 정확히 기입 ex) radius : 5.0으로 기입
def circle(pi, radius):                                 # 보통은 type을 변경하지 않음.
    return f'<h1>pi={pi}, radius={radius}, area={pi*radius**2}</h1>'

if __name__ == '__main__':
    app.run(debug=True)