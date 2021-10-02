from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'name': 'Peter',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date': 'September 29, 2021'
    }
]

@app.route("/")
@app.route("/home")
def main_page():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about_page():
    return render_template('about.html', title='About')

@app.route("/recent_movies")
def recent_movies_page():
    return render_template('recent_movies.html', title='Recent Movies')

@app.route("/genres")
def genres_page():
    return render_template('genres.html', title='Genres')