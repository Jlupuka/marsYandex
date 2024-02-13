from flask import Flask
from flask import url_for
from flask import request

app = Flask(__name__)

text = '''Человечество вырастает из детства. 
Человечеству мала одна планета. 
Мы сделаем обитаемыми безжизненные пока планеты. 
И начнем с Марса!
Присоединяйся!'''.split('\n')
alerts = ["alert alert-primary",
          "alert alert-secondary",
          "alert alert-success",
          "alert alert-danger",
          "alert alert-warning",
          "alert alert-info",
          "alert alert-light",
          "alert alert-dark"]
professions = ('инженер-исследователь, '
               'пилот, строитель, '
               'экзобиолог, '
               'врач, инженер по'
               ' терраформированию, '
               'климатолог, специалист '
               'по радиационной защите, '
               'астрогеолог, гляциолог, '
               'инженер жизнеобеспечения, '
               'метеоролог, оператор марсохода,'
               ' киберинженер, штурман, пилот дронов').split(', ')
choiceText = [
    'Эта планета близка к Земле;',
    'На ней много необходимых ресурсов;',
    'На ней есть вода и атмосфера;',
    'На ней есть небольшое магнитное поле;',
    'Наконец, она просто красива!']


@app.route('/')
def default():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    return '</br>'.join(text)


@app.route('/image_mars')
def image_mars():
    title = f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}"
                     alt="Марс">
                    <p>Вот она какая, красная планета</p>
                  </body>
                </html>"""
    return title


@app.route('/promotion_image')
def promotion_image():
    promotion_text = [f'<div class="{alert}" role="alert">\n{line}\n</div>'
                      for line, alert in zip(text, alerts)]
    title = f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                    <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}"
                     alt="Марс">
                    <p>Вот она какая, красная планета</p>
                    {'\n'.join(promotion_text)}
                  </body>
                </html>"""
    return title


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        checkBox = [(f'<div class="form-group form-check">\n  '
                     f'<input type="checkbox" class="form-check-input" id="acceptRules{index}" '
                     f'name="profession{index}">\n'
                     f'<label class="form-check-label" for="acceptRules{index}">{name}</label>\n'
                     f'</div>')
                    for index, name in enumerate(professions)]
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Анкета на участие в миссии/title>
                          </head>
                          <body>
                            <h1>Анекта претендента на участие в миссии</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="surname" class="form-control" id="surname" aria-describedby="emailHelp" placeholder="Введите фамилию" name="surname">
                                    <input type="name" class="form-control" id="name" aria-describedby="emailHelp" placeholder="Введите имя" name="name">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите email" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Общее среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                    <label for="form-group">Какие у Вас есть профессии?</label>
                                    {'\n'.join(checkBox)}
                                    <label for="form-group">Укажите пол</label>
                                    <div class="form-group">
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group form-check">
                                         <input type="checkbox" class="form-check-input" id="acceptRules" 
                                         name="accept">
                                         <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                     </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.json)
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def choice(planet_name: str):
    choice_text = [f'<div class="{alert}" role="alert">\n{line}\n</div>'
                   for line, alert in zip(choiceText, alerts)]
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Мое предложение: {planet_name}</h1>
                    {'\n'.join(choice_text)}
                  </body>
                </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname: str, level: int, rating: float):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h2>Претендента на участие в миссии {nickname}</h2>
                    <div class="{alerts[2]}" role="alert">
                        Поздравляем! Ваш рейтинг после {level} этапа отбора составляет {rating}!
                    </div>
                    <div class="{alerts[4]}" role="alert">
                        Желаем удачи!
                    </div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
