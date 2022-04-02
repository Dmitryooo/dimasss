from flask import Flask, render_template
import data

app = Flask(__name__)


@app.errorhandler(404)
@app.errorhandler(KeyError)
def render_not_found(_):
    return 'Ошибка 404</br> Можете вернуться на гравную страницу</br>  <a href="/" class="btn btn-sm btn-primary">Главная</a>', 404


@app.route('/')
def index():
    return render_template('index.html', tours=data.tours,
                           title=data.title,
                           subtitle=data.subtitle,
                           description=data.description,
                           departures=data.departures)


@app.route('/departures/<departure>/')
def departures(departure):
    return render_template('departures.html', departure=departure, title=data.title, tours=data.tours,
                           departures=data.departures)


@app.route('/tours/<int:id>/')
def tours(id):
    return render_template('tours.html', tours=data.tours[id])


@app.route('/data/departures/<departure>')
def data_departures(departure):
    return render_template('departures.html')


if __name__ == '__main__':
    app.run(debug=True)
