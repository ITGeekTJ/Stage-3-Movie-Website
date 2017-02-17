import media
import fresh_tomatoes

# Variable & Data for Toy Story instance.
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# Variable & Data for Avatar instance.
avatar = media.Movie("Avatar",
                     "A marine on an alien planet.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

# Variable & Data for Tombstone instance.
tombstone = media.Movie("Tombstone",
                        "The film is based on events in Tombstone, Arizona, including the Gunfight at the O.K. Corral and the Earp Vendetta Ride, during the 1880s. It depicts a number of western outlaws and lawmen, such as Wyatt Earp, William Brocius, Johnny Ringo, and Doc Holliday.",
                        "https://upload.wikimedia.org/wikipedia/en/7/71/Tombstoneposter.jpeg",
                        "https://www.youtube.com/watch?v=XTWYKf5hXIg")

# Variable & Data for Christmas Vacation instance.
christmas_vacation = media.Movie("Christmas Vacation",
                                 "The Griswolds are preparing for a family seasonal celebration, but things never run smoothly for Clark, his wife Ellen and their two kids.",
                                 "https://upload.wikimedia.org/wikipedia/en/5/53/NationalLampoonsChristmasVacationPoster.JPG",
                                 "https://www.youtube.com/watch?v=tLVd4ipC5Lc")

# Variable & Data for Wedding Crashers instance.
wedding_crashers = media.Movie("Wedding Crashers",
                               "A pair of womanizers sneak into weddings and take advantage of the romantic tinge in the air.",
                               "https://upload.wikimedia.org/wikipedia/en/3/3e/Wedding_crashers_poster.jpg",
                               "https://www.youtube.com/watch?v=omI8i1a7rlQ")

# Variable & Data for The Social Network instance.
the_social_network = media.Movie("The Social Network",
                                 "The story of a college student that creates a website that millions now use.",
                                 "https://upload.wikimedia.org/wikipedia/en/7/7a/Social_network_film_poster.jpg",
                                 "https://www.youtube.com/watch?v=lB95KLmpLR4")

# Variable & Data for Dumb & Dumber instance.
dumb_and_dumber = media.Movie("Dumb & Dumber",
                              "The cross-country adventures of two good-hearted but incredibly stupid friends.",
                              "http://t0.gstatic.com/images?q=tbn:ANd9GcRfKxcLRaftGDJ-q6WataYprMWOROBAhNPxuqjCUL8vaCA6ZaW1",
                              "https://www.youtube.com/watch?v=MSu25pQ4iFw")

# Variable & Data for National Treasure.
national_treasure = media.Movie("National Treasure",
                                "A historian races to find the legendary Templar Treasure before a team of mercenaries.",
                                "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY3NTc4OTYxMF5BMl5BanBnXkFtZTcwMjk5NzUyMw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                                "https://www.youtube.com/watch?v=mcf4tXYjaxo")

# Variable & Data for Super Troopers.
super_troopers = media.Movie("Super Troopers",
                             "Five Vermont state troopers, avid pranksters with a knack for screwing up, try to save their jobs and out-do the local police department by solving a crime.",
                             "https://images-na.ssl-images-amazon.com/images/M/MV5BYzAyOTZjZDItZjNiYy00YTA3LWEyYWMtZTA0NmUzYjZhNjg0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                             "https://www.youtube.com/watch?v=MPhWl_S8ies")

# List of instances
movies = [toy_story, avatar, tombstone, christmas_vacation, wedding_crashers, the_social_network, dumb_and_dumber, national_treasure, super_troopers]

# Calls the program to open the movies web page.
fresh_tomatoes.open_movies_page(movies)


