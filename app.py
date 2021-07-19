from flask import Flask, render_template
import data
app: Flask = Flask(__name__)

stars_length = '★★★★★'
def my_tours(obj, val):
    my_dict = dict()
    for key in obj.keys():
        if obj[key]['departure'] == val:
            my_dict.update({key: obj[key]})

    return my_dict

@app.route('/')
def render_main():
    return render_template('index.html', title=data.title, subtitle=data.subtitle, description=data.description, departures=data.departures, tours=data.tours)


@app.route('/departures/<departure>/')
def render_departure(departure):
    return render_template('departure.html', title=data.title, departures=data.departures, tours=my_tours(data.tours, departure), departure=departure)


@app.route('/tours/<int:id>/')
def render_tour(id):
    return render_template('tour.html', title=data.title, departures=data.departures, tour=data.tours[id], stars_length=stars_length)


if __name__ == '__main__':
    app.run()
