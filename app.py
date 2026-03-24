from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def mission():
    return "Миссия Колонизация Марса"


@app.route('/index')
def deviz():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return '''Человечество вырастает из детства.<br>
<br>
Человечеству мала одна планета.<br>
<br>
Мы сделаем обитаемыми безжизненные пока планеты.<br>
<br>
И начнем с Марса!<br>
<br>
Присоединяйся!'''


@app.route('/image_mars')
def image_mars():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <figure>
                        <img src="https://avatars.mds.yandex.net/i?id=0a53a585cd88bfe67c90a24b86c41382_l-5658205-images-thumbs&n=13" alt="картинка марса">
                        <figcaption>Вот она какая, красная планета</figcaption>
                  </body>
                </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
                      </head>
                      <body>
                        <h1><b>Жди нас, Марс!</b></h1>
                        <figure>
                            <img src="{url_for('static', filename='img/mars.avif')}" alt="картинка марса" width="25%" height="25%">
                        </figure>
                        <br>
                        <a><b>Человечество вырастает из детства.</b></a><br>
                        <a><b>Человечеству мала одна планета.</b></a><br>
                        <a><b>Мы сделаем обитаемыми безжизненные пока планеты.</b></a><br>
                        <a><b>И начнем с Марса!</b></a><br>
                        <a><b>Присоединяйся!</b></a><br>
                      </body>
                    </html>"""


@app.route('/astronaut_selection')
def astronaut_selection():
    return '''
<!doctype html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <title>Отбор астронавтов</title>
</head>
<body>
    <h1>Анкета кандидата в астронавты</h1>
    <form>
        <p>
            <label for="surname">Фамилия</label><br>
            <input type="text" id="surname" name="surname">
        </p>

        <p>
            <label for="name">Имя</label><br>
            <input type="text" id="name" name="name">
        </p>

        <p>
            <label for="email">Email</label><br>
            <input type="email" id="email" name="email">
        </p>

        <p>
            <label for="education">Образование</label><br>
            <select id="education" name="education">
                <option value="">Выберите уровень образования</option>
                <option value="high_school">Среднее образование</option>
                <option value="bachelor">Бакалавр</option>
                <option value="master">Магистр</option>
                <option value="phd">Кандидат наук</option>
                <option value="doctor">Доктор наук</option>
            </select>
        </p>

        <p>
            <label for="profession">Основная профессия</label><br>
            <select id="profession" name="profession">
                <option value="">Выберите профессию</option>
                <option value="engineer_researcher">Инженер-исследователь</option>
                <option value="pilot">Пилот</option>
                <option value="builder">Строитель</option>
                <option value="exobiologist">Экзобиолог</option>
                <option value="doctor">Врач</option>
                <option value="terraforming_engineer">Инженер по терраформированию</option>
                <option value="climatologist">Климатолог</option>
                <option value="radiation_specialist">Специалист по радиационной защите</option>
                <option value="astrogeologist">Астрогеолог</option>
                <option value="glaciologist">Гляциолог</option>
                <option value="life_support_engineer">Инженер жизнеобеспечения</option>
                <option value="meteorologist">Метеоролог</option>
                <option value="rover_operator">Оператор марсохода</option>
                <option value="cyber_engineer">Киберинженер</option>
                <option value="navigator">Штурман</option>
                <option value="drone_pilot">Пилот дронов</option>
            </select>
        </p>

        <p>
            <label>Пол</label><br>
            <input type="radio" id="male" name="gender" value="male">
            <label for="male">Мужской</label><br>
            <input type="radio" id="female" name="gender" value="female">
            <label for="female">Женский</label><br>
            <input type="radio" id="other" name="gender" value="other">
            <label for="other">Другой</label>
        </p>

        <p>
            <label for="motivation">Мотивация *</label><br>
            <textarea id="motivation" name="motivation" rows="5" cols="50" placeholder="Почему вы хотите стать астронавтом и отправиться на Марс?"></textarea>
        </p>

        <p>
            <label>Готовы ли остаться на Марсе?</label><br>
            <input type="radio" id="stay_yes" name="stay_on_mars" value="yes">
            <label for="stay_yes">Да, готов(а)</label><br>
            <input type="radio" id="stay_no" name="stay_on_mars" value="no">
            <label for="stay_no">Нет, хочу вернуться</label><br>
            <input type="radio" id="stay_unsure" name="stay_on_mars" value="unsure">
            <label for="stay_unsure">Пока не уверен(а)</label>
        </p>
        
        <p>
            <label>Приложите фотографию</label><br>
            <input type="file" id="photo">
        </p>

        <hr>

        <button type="submit">Отправить заявку</button>
    </form>
</body>
</html>'''


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f"""<!doctype html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css">
    <title>Варианты выбора</title>
</head>
<body>
    <div class="container mt-5">
        <h1>Варианты выбора</h1>

        <div class="row mt-4">
            <div class="col-md-6">
                <div class="form-check">
                    <input class="form-check-input" type="radio" name="planet" id="mars">
                    <label class="form-check-label" for="mars">
                        Марс
                    </label>
                </div>
            </div>
            <div class="col-md-6">
                <div class="form-check">
                    <input class="form-check-input" type="radio" name="planet" id="earth">
                    <label class="form-check-label" for="earth">
                        Земля
                    </label>
                </div>
            </div>
        </div>

        <hr class="my-4">

        <h2>Мое предложение: {planet_name}</h2>
        <p>Эта планета близка к Земле;</p>

        <ul>
            <li>На ней много необходимых ресурсов;</li>
            <li>На ней есть вода и атмосфера;</li>
            <li>На ней есть небольшое магнитное поле;</li>
            <li>Наконец, она просто красива!</li>
        </ul>
    </div>
</body>
</html>"""


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f"""<!doctype html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css">
    <title>Результаты отбора</title>
</head>
<body>
    <div class="container mt-5">
        <h1>Результаты отбора</h1>

        <h2 class="mt-4">Претендента на участие в миссии {nickname}:</h2>

        <h3>Поздравляем! Ваш рейтинг после {level} этапа отбора</h3>

        <h3>составляет {rating}!</h3>

        <h4 class="mt-4">Желаем удачи!</h4>
    </div>
</body>
</html>"""


@app.route('/carousel')
def carousel():
    return f"""<!doctype html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css">
    <title>Пейзажи Марса</title>
</head>
<body>
    <div class="carousel-container">
        <h1>Пейзажи Марса</h1>

        <div id="marsCarousel" class="carousel slide" data-bs-ride="carousel">
            <div class="carousel-indicators">
                <button type="button" data-bs-target="#marsCarousel" data-bs-slide-to="0" class="active"></button>
                <button type="button" data-bs-target="#marsCarousel" data-bs-slide-to="1"></button>
                <button type="button" data-bs-target="#marsCarousel" data-bs-slide-to="2"></button>
                <button type="button" data-bs-target="#marsCarousel" data-bs-slide-to="3"></button>
            </div>

            <div class="carousel-inner">
                <div class="carousel-item active">
                    <img src="{url_for('static', filename='img/mars1.jpg')}" class="d-block w-100" alt="Марс пейзаж 1">
                    <div class="carousel-caption d-none d-md-block">
                        <h5>Кратер Гейла</h5>
                        <p>Место посадки марсохода Curiosity</p>
                    </div>
                </div>

                <div class="carousel-item">
                    <img src="{url_for('static', filename='img/mars2.jpg')}" class="d-block w-100" alt="Марс пейзаж 2">
                    <div class="carousel-caption d-none d-md-block">
                        <h5>Олимп</h5>
                        <p>Высочайшая гора в Солнечной системе</p>
                    </div>
                </div>

                <div class="carousel-item">
                    <img src="{url_for('static', filename='img/mars3.jpg')}" class="d-block w-100" alt="Марс пейзаж 3">
                    <div class="carousel-caption d-none d-md-block">
                        <h5>Долины Маринер</h5>
                        <p>Гигантская система каньонов</p>
                    </div>
                </div>

                <div class="carousel-item">
                    <img src="{url_for('static', filename='img/mars4.jpg')}" class="d-block w-100" alt="Марс пейзаж 4">
                    <div class="carousel-caption d-none d-md-block">
                        <h5>Северная полярная шапка</h5>
                        <p>Ледяные шапки из водяного льда и углекислого газа</p>
                    </div>
                </div>
            </div>

            <button class="carousel-control-prev" type="button" data-bs-target="#marsCarousel" data-bs-slide="prev">
                <span class="carousel-control-prev-icon"></span>
                <span class="visually-hidden">Предыдущий</span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#marsCarousel" data-bs-slide="next">
                <span class="carousel-control-next-icon"></span>
                <span class="visually-hidden">Следующий</span>
            </button>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>"""
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')