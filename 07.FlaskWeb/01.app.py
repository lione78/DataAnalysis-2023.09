from flask import Flask, render_template

# 터미널에서도 사용 가능
app = Flask(__name__)       # Flask의 __main__을 사용

@app.route('/')         # localhost:5000/ 을 서비스하기 위한 코드 http://127.0.0.1:5000 (/)<-의미
def index():            # def 이름은 의미가 없음.
    return '<h1>Hello Flask</h1><h2>Flask 좋아요!!!</h2>'       #ajax, json으로 데이터 보낼 때.

@app.route('/hello')
def hello():
    return render_template('01.hello.html')     # templates가 default임. "이름 바뀌면 안됨.""

@app.route('/sub/hello')
def sub_hello():
    return render_template('sub/01.hello.html')     # sub밑에 있을 경우는 경로명도 같이 써줌.

# debug=True면 코드가 고쳐지면 reload됨.(개발시) // 실제 서비스시에는 꺼둠.
# Model같이 lib가 변경되면 될지 모름. 
if __name__ == '__main__':
    app.run(debug=True)