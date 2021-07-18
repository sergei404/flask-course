from flask import Flask, render_template

app: Flask = Flask(__name__)


@app.route('/')
def render_main():
    return render_template('index.html')


@app.route('/departures/<departure>/')
def render_departure(departure):
    print(departure)
    return render_template('departure.html')


@app.route('/tours/<id>/')
def render_tour(id):
    print(id)
    return render_template('tour.html')


if __name__ == "__main__":
    app.run(debug=True)
