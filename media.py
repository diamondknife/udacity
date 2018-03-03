import webbrowser
import fresh_tomatoes

class Movie():
    def __init__(self, title, storyline, image, trailer):
        self.title = title
        self.storyline = storyline
        self.image = image
        self.trailer = trailer


    def show_trailer(self):
        webbrowser.open(self.trailer)


    def show_image(self):
        webbrowser.open(self.image)

