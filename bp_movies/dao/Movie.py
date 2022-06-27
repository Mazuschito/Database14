class Movie:
    def __init__(self, title="", country="", release_year=0, genre="", description="", rating="", date_added="",
                 cast="", type_movie=""):
        self.title = title
        self.country = country
        self.release_year = release_year
        self.genre = genre
        self.description = description
        self.rating = rating
        self.date_added = date_added
        self.cast = cast
        self.type_movie = type_movie

    def __repr__(self):
        return f"title: {self.title} \
                country: {self.country} \
                release_year: {self.release_year} \
                genre: {self.genre} \
                rating: {self.rating} \
                description: {self.description}"
