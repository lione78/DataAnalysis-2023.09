from flask import Flask, render_template, request, flash, session
from bp.crawling import crawl_bp
from bp.map import map_bp
from bp.user import user_bp
import os, random
import util.map_util as mu
import util.weather_util as wu

app = Flask(__name__)
app.secret_key = 'qwert12345'       # flash와 session을 사용하려면 반드시 설정해야 함.
app.config['SESSION_COOKIE_PATH'] = '/'     # 형식적인 문장

app.register_blueprint(crawl_bp, url_prefix='/crawling')    # localhost:5000/crawling/* 는 crawl bp가 처리
app.register_blueprint(map_bp, url_prefix='/map')
app.register_blueprint(user_bp, url_prefix='/user')

@app.before_first_request
def before_first_request():     # 최초 1회 실행
    global quotes, quote
    # global addr : session으로 써서 안 줘도 됨.
    filename = os.path.join(app.static_folder, 'data/todayQuote.txt')
    with open(filename, encoding='UTF-8') as file:
        quotes = file.readlines()       # list 형태로 읽음.
    quote = random.sample(quotes, 1)[0]
    session['quote'] = quote
    session['addr'] = '서울시 영등포구'

# for AJAX ######################################
@app.route('/change_quote')
def change_quote():
    global quote        # 위에 것과 같음.
    quote = random.sample(quotes, 1)[0]
    session['quote'] = quote
    return quote

@app.route('/change_addr')
def change_addr():
    addr = request.args.get('addr')     # ajax의 value값 받음.
    session['addr'] = addr
    return addr

@app.route('/weather')
def weather():
    # 서울시 영등포구 + '청' -> 도로명 주소 -> 카카오 로컬 -> 위도, 경도 좌표 획득
    addr = request.args.get('addr')
    lat, lng = mu.get_coord(app.static_folder, addr + '청')
    html = wu.get_weather(app.static_folder, lat, lng)
    return html


##################################################

@app.route('/')
def home():
    menu = {'ho':1, 'us':0, 'cr':0, 'ma':0, 'sc':0}     # menubar에 class active 할 수 있는 dict 하나만 1이 되야 함.
    # flash('Welcome to my Web!!')
    return render_template('home.html', menu=menu)  # 항상 menu 보내줘야함.

@app.route('/schedule')
def schedule():
    menu = {'ho':0, 'us':0, 'cr':0, 'ma':0, 'sc':1}
    return render_template('schedule.html', menu=menu)

if __name__ == '__main__':
    app.run(debug=True)