import fresh_tomatoes
import media

breakfast_tiffany = media.Movie("Breakfast at Tiffany's", "A young New York socialite becomes interested in a young man who has moved into her apartment building,but her past threatens to get in the way.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/a/a9/Breakfast_at_Tiffanys.jpg/215px-Breakfast_at_Tiffanys.jpg",
                        "https://www.youtube.com/watch?v=urQVzgEO_w8")
#print(breakfast_tiffany.storyline)

moana = media.Movie("Moana", "In Ancient Polynesia, when a terrible curse incurred by the Demigod Maui reaches an impetuous Chieftain's daughter's island, she answers the Ocean's call to seek out the Demigod to set things right.",
                    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRW0np6nT-CAi9wq3bqxR9rAr16SBLzfZPZ66D1wHZ69jUpcj4CuA",
                    "https://www.youtube.com/watch?v=LKFuXETZUsI")
#print(moana.storyline)

bride_wars = media.Movie("Bride Wars", "Two best friends become rivals when they schedule their respective weddings on the same day.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BMTUyNTg2OTUwN15BMl5BanBnXkFtZTgwNzEzMzg5MTI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                         "https://www.youtube.com/watch?v=KBDE4uznmIw")
#bride_wars.show_trailer()

all_eyez = media.Movie("All Eyez on Me", "Tells the true and untold story of prolific rapper, actor, poet and activist Tupac Shakur.",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc5NzQ4NzU4OF5BMl5BanBnXkFtZTgwNTkxMzE0MjI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                       "https://www.youtube.com/watch?v=njnwYSybwko")

baywatch = media.Movie("Baywatch", "Devoted lifeguard Mitch Buchannon butts heads with a brash new recruit, as they uncover a criminal plot that threatens the future of the bay.",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BNTA4MjQ0ODQzNF5BMl5BanBnXkFtZTgwNzA5NjYzMjI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                       "https://www.youtube.com/watch?v=nZ5tqzw841s")

three_steps = media.Movie("Three Steps Above Heaven", "Story of two young people who belong to different worlds.",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BNjQwM2Y3ODQtYjExMi00OGIwLWFhZWYtNDY0ZDM4ZTk1MzU1XkEyXkFqcGdeQXVyNjE5NTc2OTQ@._V1_UY268_CR5,0,182,268_AL_.jpg",
                          "https://www.youtube.com/watch?v=TVBIQrg0dJc")

movies = [breakfast_tiffany, moana, bride_wars, all_eyez, baywatch, three_steps]
fresh_tomatoes.open_movies_page(movies)
