import webbrowser 

    """This program was made to create a web page with 6 movie posters and their trailers.""""
    
class Movie():
    #class Movie creates structure for arrays in entertainment.py
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
