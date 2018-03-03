import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story about a boy and his real life toys",
                        "http://www.cultjer.com/toy-story-poster",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")


avatar = media.Movie("Avatar",
                     "A story about weird futuristic cartoon world",
                     "https://www.traileraddict.com/avatar/poster/6",
                     "https://www.youtube.com/watch?v=6ziBFh3V1aM"
                     )


the_rock = media.Movie("The Rock",
                        "A story an escape from Alcatraz",
                        "http://www.imdb.com/title/tt0117500/mediaviewer/rm2777683456",
                        "http://www.imdb.com/title/tt0117500/videoplayer/vi1743388953?ref_=tt_ov_vi")

movies = [toy_story, avatar, the_rock]

fresh_tomatoes.open_movies_page(movies)


