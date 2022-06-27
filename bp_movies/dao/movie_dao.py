import sqlite3

from bp_movies.dao.Movie import Movie


def create_query_by_title(film_name):
    """Creates query: task 1"""
    sql_query = (f"""
            SELECT title, country, release_year, listed_in as genre, description
            FROM netflix
            WHERE title LIKE '{film_name}' 
            ORDER BY  release_year DESC 
            """)
    return sql_query


def create_query_by_years(year_from, year_to):
    """Creates query: task 2"""
    sql_query = (f"""
                SELECT title, release_year
                FROM netflix
                WHERE release_year BETWEEN {year_from} AND {year_to}
                ORDER BY  release_year DESC 
                LIMIT 100
                """)
    return sql_query


def create_query_by_rating(rating_1="", rating_2="", rating_3="", rating_4="", rating_5=""):
    """Creates query: task 3"""
    sql_query = (f"""
                    SELECT title, rating, description
                    FROM netflix
                    WHERE rating = '{rating_1}' OR rating = '{rating_2}' 
                    OR rating = '{rating_3}' OR rating = '{rating_4}' 
                    OR rating = '{rating_5}'
                    """)
    return sql_query


def create_query_by_genre(genre=""):
    """Creates query: task 4"""
    sql_query = (f"""
                        SELECT title, description, listed_in as genre, date_added
                        FROM netflix
                        WHERE genre LIKE '%{genre}%'
                        ORDER BY date_added DESC
                        LIMIT 10
                        """)
    return sql_query


def create_query_by_actors(actor_1="", actor_2=""):
    """Creates query: task 5"""
    sql_query = (f"""
                SELECT "cast"
                FROM netflix
                WHERE "cast" LIKE '%{actor_1}%' AND "cast" LIKE '%{actor_2}%'
                """)
    return sql_query


def get_duplicates(actor_1, actor_2):
    """Returns list of actors which are co-playing with actor_1 and actor_2 more than twice"""
    query = create_query_by_actors(actor_1, actor_2)
    movies_instance = Movie_DAO(query)
    movies = movies_instance._load_movies()
    actors_list = []
    for movie in movies:
        actors = movie.cast.split(", ")
        for actor in actors:
            actors_list.append(actor)
    duplicates_actors = [actor_i for actor_i in actors_list if actors_list.count(actor_i) > 2]
    unique_duplicates = list(set(duplicates_actors))
    unique_duplicates.remove(actor_1)
    unique_duplicates.remove(actor_2)
    return unique_duplicates


def create_query_by_type(type_movie, release_year, genre):
    """Creates query: task 6"""
    sql_query = (f"""
                SELECT "type" as type_movie, release_year, listed_in as genre
                FROM netflix
                WHERE type_movie = '{type_movie}' AND release_year = '{release_year}' AND genre LIKE '%{genre}%'¶
                """)
    return sql_query


class Movie_DAO:
    def __init__(self, sql_query):
        self.sql_query = sql_query

    def get_sql_request_result(self):
        """ Gets query results by searching query"""
        with sqlite3.connect("netflix.db") as connection:
            cursor = connection.cursor()
            cursor.execute(self.sql_query)
            executed_query = cursor.fetchall()
            fields = [description[0] for description in cursor.description]
            return executed_query, fields

    def gets_list_of_dicts(self):
        """ Returns list dict with movie """
        executed_query, fields = self.get_sql_request_result()

        result = []
        movie = {}
        i = 0
        for iteration in executed_query:
            for field in fields:
                movie[field] = iteration[i]
                i += 1
            x = movie
            movie = {}
            result.append(x)
            i = 0
        return result

    def _load_movies(self):
        """Return list of objects Movie"""
        movies_data = self.gets_list_of_dicts()
        list_of_movie_instances = []
        for movie_data in movies_data:
            instance = Movie(**movie_data)
            list_of_movie_instances.append(instance)
        return list_of_movie_instances
