from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def main_page():
    return render_template('home.html')

@main.route("/about")
def about_page():
    return render_template('about.html', title='About')

@main.route("/recent_movies")
def recent_movies_page():
    return render_template('recent_movies.html', title='Recent Movies')

@main.route("/genres")
def genres_page():
    return render_template('genres.html', title='Genres')