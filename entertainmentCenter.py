import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story about a boy and his real life toys.",
                        "http://www.cultjer.com/toy-story-poster",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A story about weird futuristic cartoon world.",
                     "https://www.traileraddict.com/avatar/poster/6",
                     "https://www.youtube.com/watch?v=6ziBFh3V1aM")

the_rock = media.Movie("The Rock",
                        "A story an escape from Alcatraz.",
                        "http://www.imdb.com/title/tt0117500/mediaviewer/rm2777683456",
                        "http://www.imdb.com/title/tt0117500/videoplayer/vi1743388953?ref_=tt_ov_vi")

con_air = media.Movie("Con Air",
                        "A story about hijacking a plane.",
                        "http://www.imdb.com/title/tt0118880/mediaviewer/rm2913112576",
                        "http://www.imdb.com/title/tt0118880/videoplayer/vi3572407833?ref_=tt_ov_vi")

ratatouille = media.Movie("Ratatouille",
                        "A story about a mouse who wants to be chef.",
                        "http://www.imdb.com/title/tt0382932/mediaviewer/rm937921792",
                        "http://www.imdb.com/title/tt0382932/videoplayer/vi465937945?ref_=tt_ov_vi")

shawshank_redemption = media.Movie("Shawshank Redemption",
                        "A story about a prison break.",
                        "http://www.imdb.com/title/tt0111161/mediaviewer/rm10105600",
                        "http://www.imdb.com/title/tt0111161/videoplayer/vi3877612057?ref_=tt_ov_vi")

movies = [toy_story, avatar, the_rock, con_air, ratatouille, shawshank_redemption]

fresh_tomatoes.open_movies_page(movies)


