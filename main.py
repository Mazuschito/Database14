from flask import Flask
from bp_movies.views import bp_movies

app = Flask(__name__)
app.register_blueprint(bp_movies)

if __name__ == "__main__":
    app.run()
