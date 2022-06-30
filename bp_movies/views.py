from flask import render_template, Blueprint, jsonify
from bp_movies.dao import movie_dao

bp_movies = Blueprint("bp_movies", __name__, template_folder="templates")


@bp_movies.route("/")
def main_page():
    return f"This is the main page"


@bp_movies.route("/movie/<title>")
def movie_info(title):
    """View with list of movies matching the title"""
    query, query_var = movie_dao.create_query_by_title(title)
    movies_instance = movie_dao.Movie_DAO(query, query_var)
    movies = movies_instance._load_movies()
    return render_template("movie.html", movies=movies)


@bp_movies.route("/api/movie/<title>")
def api_movie_info(title):
    """Return JSON list of movies by title"""
    query, query_var = movie_dao.create_query_by_title(title)
    movies_instance = movie_dao.Movie_DAO(query, query_var)
    all_movies_as_dict = movies_instance.gets_list_of_dicts()
    return jsonify(all_movies_as_dict), 200


@bp_movies.route("/<int:year_from>/to/<int:year_to>")
def years_till_years(year_from, year_to):
    """View with list of movies with between two years"""
    query, query_var = movie_dao.create_query_by_years(year_from, year_to)
    movies_instance = movie_dao.Movie_DAO(query, query_var)
    movies = movies_instance._load_movies()
    qty = len(movies)
    return render_template("years.html", movies=movies, year_from=year_from, year_to=year_to, qty=qty)


@bp_movies.route("/api/<int:year_from>/to/<int:year_to>")
def api_years_till_years(year_from, year_to):
    """Return JSON list of movies from year to year"""
    query, query_var = movie_dao.create_query_by_years(year_from, year_to)
    movies_instance = movie_dao.Movie_DAO(query, query_var)
    all_movies_as_dict = movies_instance.gets_list_of_dicts()
    return jsonify(all_movies_as_dict), 200


@bp_movies.route("/rating/children")
def rating_children():
    """View with list of movies with children rating"""
    query, query_var = movie_dao.create_query_by_rating(rating_1="G")
    movies_instance = movie_dao.Movie_DAO(query, query_var)
    movies = movies_instance._load_movies()
    status = "Children"
    qty = len(movies)
    return render_template("rating.html", movies=movies, status=status, qty=qty)


@bp_movies.route("/api/rating/children")
def api_rating_children():
    """Return JSON list of movies by children rating"""
    query, query_var = movie_dao.create_query_by_rating(rating_1="G")
    movies_instance = movie_dao.Movie_DAO(query, query_var)
    all_movies_as_dict = movies_instance.gets_list_of_dicts()
    return jsonify(all_movies_as_dict), 200


@bp_movies.route("/rating/family")
def rating_family():
    """View with list of movies with family rating"""
    query, query_var = movie_dao.create_query_by_rating(rating_1="G", rating_2="PG", rating_3="PG-13")
    movies_instance = movie_dao.Movie_DAO(query, query_var)
    movies = movies_instance._load_movies()
    status = "Family"
    qty = len(movies)
    return render_template("rating.html", movies=movies, status=status, qty=qty)


@bp_movies.route("/api/rating/family")
def api_rating_family():
    """Return JSON list of movies by family rating"""
    query, query_var = movie_dao.create_query_by_rating(rating_1="G", rating_2="PG", rating_3="PG-13")
    movies_instance = movie_dao.Movie_DAO(query, query_var)
    all_movies_as_dict = movies_instance.gets_list_of_dicts()
    return jsonify(all_movies_as_dict), 200


@bp_movies.route("/rating/adult")
def rating_adult():
    """View with list of movies with adult rating (R, NC-17)"""
    query, query_var = movie_dao.create_query_by_rating(rating_1="R", rating_2="NC-17")
    movies_instance = movie_dao.Movie_DAO(query, query_var)
    movies = movies_instance._load_movies()
    status = "Adult"
    qty = len(movies)
    return render_template("rating.html", movies=movies, status=status, qty=qty)


@bp_movies.route("/api/rating/adult")
def api_rating_adult():
    """Return JSON list of movies by adult rating"""
    query, query_var = movie_dao.create_query_by_rating(rating_4="R", rating_5="NC-17")
    movies_instance = movie_dao.Movie_DAO(query, query_var)
    all_movies_as_dict = movies_instance.gets_list_of_dicts()
    return jsonify(all_movies_as_dict), 200


@bp_movies.route("/genre/<genre>")
def get_by_genre(genre):
    query, query_var = movie_dao.create_query_by_genre(genre)
    movies_instance = movie_dao.Movie_DAO(query, query_var)
    movies = movies_instance._load_movies()
    qty = len(movies)
    return render_template("genre.html", movies=movies, qty=qty, genre=genre)


@bp_movies.route("/api/genre/<genre>")
def api_get_by_genre(genre):
    """Return JSON list of movies by genre"""
    query, query_var = movie_dao.create_query_by_genre(genre)
    movies_instance = movie_dao.Movie_DAO(query, query_var)
    all_movies_as_dict = movies_instance.gets_list_of_dicts()
    return jsonify(all_movies_as_dict), 200


# Task 6 functionality
#print(movie_dao.create_query_by_actors("Rose McIver", "Ben Lamb"))
print(movie_dao.get_duplicates("Rose McIver", "Ben Lamb"))


@bp_movies.route("/<type_movie>/<int:release_year>/<genre>")
def get_movie_by_filters(type_movie, release_year, genre):
    """Return JSON list of movies by type, year and genre"""
    query, query_var = movie_dao.create_query_by_type(type_movie, release_year, genre)
    movies_instance = movie_dao.Movie_DAO(query, query_var)
    movies = movies_instance._load_movies()
    qty = len(movies)
    return render_template("filters.html", movies=movies, qty=qty, type_movie=type_movie, genre=genre, release_year=release_year)

@bp_movies.route("/api/<type_movie>/<int:release_year>/<genre>")
def api_get_movie_by_filters(type_movie, release_year, genre):
    """Return JSON list of movies by type, year and genre"""
    query, query_var = movie_dao.create_query_by_type(type_movie, release_year, genre)
    movies_instance = movie_dao.Movie_DAO(query, query_var)
    all_movies_as_dict = movies_instance.gets_list_of_dicts()
    return jsonify(all_movies_as_dict), 200
