import media
import fresh_tomatoes


# Movies objects

into_the_wild = media.Movie(
    "Into The Wild",
    "When a man leaves his possessions to explore the world as a hitchhiker "
    "but gets trapped in the wild",
    "https://upload.wikimedia.org/wikipedia/en/thumb/8/8a/Into-the-wild."
    "jpg/220px-Into-the-wild.jpg",
    "https://www.youtube.com/watch?v=2LAuzT_x8Ek", "2008")

the_dark_knight = media.Movie(
    "The Dark Knight",
    "Batman meets his arch enemy",
    "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
    "https://www.youtube.com/watch?v=_PZpmTj1Q8Q", "2008")

black_panther = media.Movie(
    "Black Panther",
    "The king of Wakanda defends his thrown from his long lost cousin",
    "https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_po"
    "ster.jpg",
    "https://www.youtube.com/watch?v=xjDjIWPwcPU", "2018")

dunkirk = media.Movie(
    "Dunkirk",
    "British and French army stuck on a beach rescued from the German army",
    "https://upload.wikimedia.org/wikipedia/en/1/15/Dunkirk_Film_poster.jpg",
    "https://www.youtube.com/watch?v=F-eMt3SrfFU", "2017")

the_bourne_identity = media.Movie(
    "The Bourne Identity",
    "Thriller action movie based on Robert Ludlum's novel",
    "https://upload.wikimedia.org/wikipedia/en/a/ae/BourneIdentityfilm.jpg",
    "https://www.youtube.com/watch?v=AfkNq0CDx6w", "2002")

wonder_woman = media.Movie(
    "Wonder Woman",
    "Diana, an Amazonian warrior in training, leaves home to fight a war, "
    "discovering her full powers and true destiny.",
    "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282"
    "017_film%29.jpg",
    "https://www.youtube.com/watch?v=VSB4wGIdDwo", "2017")

interstellar = media.Movie(
    "Interstellar",
    "A team of explorers travel through a wormhole in space in an atte"
    "mpt to ensure humanity's survival.",
    "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_fil"
    "m_poster.jpg",
    "https://www.youtube.com/watch?v=0vxOhd4qlnA", "2014")

inglorious_bastards = media.Movie(
    "The Inglorious Basterds",
    "In Nazi-occupied France during World War II, a plan to "
    "assassinate Nazi leaders "
    "by a group of Jewish U.S. soldiers coincides with a theatre "
    "owner's vengeful plans for the same",
    "https://upload.wikimedia.org/wikipedia/en/c/c3/Inglourious_"
    "Basterds_poster.jpg",
    "https://www.youtube.com/watch?v=KnrRy6kSFF0", "2009")

django_unchained = media.Movie(
    "Django Unchained",
    "With the help of a German bounty hunter, a freed slave sets out "
    "to rescue his wife "
    "from a brutal Mississippi plantation owner.",
    "https://upload.wikimedia.org/wikipedia/en/8/8b/Django_Unc"
    "hained_Poster.jpg",
    "https://www.youtube.com/watch?v=eUdM9vrCbow", "2012")

movies = [into_the_wild, the_dark_knight, black_panther, dunkirk,
          the_bourne_identity, wonder_woman, interstellar, inglorious_bastards,
          django_unchained]

# Calling the html file generator and passing in the movies object
fresh_tomatoes.open_movies_page(movies)

