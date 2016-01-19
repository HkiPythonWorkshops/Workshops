from flask import Flask, render_template
from services.finnkino import FinnKinoXML
from services.leffatykki import LeffaTykkiRSS

app = Flask(__name__)
fk = FinnKinoXML()
lt = LeffaTykkiRSS()


def get_movies_with_reviews(area_code):
    movie_container = {}
    movies = fk.get_movies_from_area(area_code)
    reviews = lt.get_movie_reviews()
    for id, movie in movies.items():
        review_link = ""
        movie_title = movie['normalized_title']
        if movie_title in reviews:
            review_link = reviews[movie['normalized_title']]
        movie_container[id] = {
            'title': movie['title'],
            'normalized_title': movie['normalized_title'],
            'rating': movie['rating'],
            'image': movie['image'],
            'genres': ", ".join(movie['genres']),
            'review': review_link
        }
    return movie_container


@app.route('/')
def index():
    areas = fk.get_area_codes()
    data = {
        'areas': areas
    }
    return render_template('index.html', data=data)


@app.route('/movies/<area>')
def get_movies(area):
    movies = get_movies_with_reviews(area)
    data = {
        'movies': movies
    }
    return render_template('_movies.html', data=data)


if __name__ == "__main__":
    app.run(port=5001, debug=True)
