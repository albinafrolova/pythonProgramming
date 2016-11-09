import webbrowser
class Movie:
    
    def __init__(self, title, year ,genre, poster_url='', trailer_url='' ):
        
        #here write code 

    def print_movie(self):
        print(self.title, self.year, self.genre)

    def print_trailer(self):
        webbrowser.open(self.trailer_url)
