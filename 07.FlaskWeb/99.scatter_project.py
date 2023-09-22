from flask import Flask, render_template, request
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
import seaborn as sns

app = Flask(__name__)

@app.route('/')
def index():
    return '<h2>Scatter</h2>'

@app.route('/scatter', methods=['GET', 'POST'])
# @app.route('/scatter/mean/<mean_>/std/<std_>/num/<num_>/min/<min_>/max/<max_>', methods=['GET', 'POST'])
def scatter_graph():
    if request.method == 'GET':
        return render_template('99.scatter_input.html')
    else:
        mean_ = request.values['mean_']
        std_ = request.values['std_']
        num_ = request.values['num_']
        min_ = request.values['min_']
        max_ = request.values['max_']
        noraml_list = np.random.normal(int(mean_), int(std_), int(num_))
        uniform_list = np.random.uniform(int(min_), int(max_), int(num_))
        df = pd.DataFrame(zip(noraml_list, uniform_list))
        df.columns = ['x', 'y']

        plt.rcParams['font.family'] = 'Malgun Gothic'
        plt.rcParams['axes.unicode_minus'] = False
        plt.figure(figsize=(10, 10))
        # plt.scatter(x=noraml_list, y=uniform_list)
        sns.scatterplot(data=df, x='x', y='y', marker='+', color='r', s=50)
        plt.title('Normal 분포와 Uniform 분포의 상관관계')
        plt.savefig('static/img/scatter.png')
        img_file = os.path.join(app.root_path, 'static/img/scatter.png')
        mtime = int(os.stat(img_file).st_mtime)
        return render_template('99.scatter.html', mtime=mtime)

if __name__ == '__main__':
    app.run(debug=True)