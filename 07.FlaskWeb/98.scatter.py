from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import numpy as np
import os

app = Flask(__name__)

@app.route('/')
def index():
    return '''<h2>산점도 그래프</h2>
            <button onclick="location.href='/scatter'">실행</button>'''

@app.route('/scatter', methods=['GET', 'POST'])
def scatter():
    if request.method == 'GET':
        return render_template('98.scatter_form.html')
    else:
        # std, min, max 함수가 있기 때문에 변수 이름 짓기 지양
        num_ = int(request.form['num'])
        avg_ = float(request.form['avg'])
        std_ = float(request.form['std'])
        min_ = float(request.form['min'])
        max_ = float(request.form['max'])
        xs = np.random.normal(avg_, std_, num_)     # 평균, 표준편차, 갯수
        ys = np.random.uniform(min_, max_, num_)    # 최소, 최대, 갯수
        plt.figure()
        plt.scatter(xs, ys)
        filename = os.path.join(app.static_folder, 'img/scatter1.png')
        plt.savefig(filename)           #'../static/img/scatter1.png'
        # return render_template('98.scatter_res.html', avg_=avg_, std_=std_, min_=min_, max_=max_)
        params = {'avg_':avg_, 'std_':std_, 'min_':min_, 'max_':max_}
        return render_template('98.scatter_res.html', params=params)

if __name__ == '__main__':
    app.run(debug=True)