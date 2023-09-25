from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''<h2>입력값 받기</h2>
            <button onclick="location.href='/calc'">셀렉트(calc 사례)</button>
            <button onclick="location.href='/lang'">라디오 체크박스(lang, food 사례)</button>
    '''

@app.route('/calc', methods=['GET', 'POST'])
def calc():
    if request.method == 'GET':
        op_list = ['+', '-', '*', '/', '//', '%', '**']
        return render_template('06.calc_form.html', op_list=op_list)
    else:
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        op = request.form['op']
        result = eval(f'{num1}{op}{num2}')      # eval(2 + 3) > 5
        return f'''<h2>{num1} {op} {num2} = {result}</h2>
                <button onclick="location.href='/calc'">재실행</button>
        '''

@app.route('/lang', methods=['GET', 'POST'])
def lang():
    lang_dict = {'en' : '영어', 'fr' : '프랑스어', 'es' : '스페인어', 'jp' : '일어', 'cn' : '중국어'}
    food_list = ['삼겹살', '갈비탕', '불고기', '피자', '햄버거']
    if request.method == 'GET':
        return render_template('06.lang_food.html', lang_dict=lang_dict, food_list=food_list)
    else:
        language = request.form['language']
        foods = request.values.getlist('food')
        selected_foods = []
        for food_index in foods:
            selected_foods.append(food_list[int(food_index)])
        # selected_food = list(map(lambda x : food_list[int(x)],foods))
        return f'''
            <h2>선택한 언어 : {lang_dict[language]}</h2>
            <h2>선택한 음식 : {selected_foods}</h2>
            <button onclick="location.href='/lang'">재실행</button>
        '''

if __name__ == '__main__':
    app.run(debug=True)