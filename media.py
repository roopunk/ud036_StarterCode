class Movie():

    def __init__(self, title, storyline, poster_url, youtube_url, year):
        """
        Initializes Movie object
        :param title: Title of the movie
        :param storyline: Brief storyline of the movie
        :param poster_url: Poster image url, mostly picked from wikipedia
        :param youtube_url: Trailer url from youtube
        :param year: Year of movie release
        """
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_url
        self.trailer_youtube_url = youtube_url
        self.year = year
