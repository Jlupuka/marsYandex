from flask import Flask
from flask import url_for

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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
