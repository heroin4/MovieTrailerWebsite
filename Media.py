# coding=UTF-8
import webbrowser
"""this class include the data structure constructor
and the method that is to open the trailer web page
"""


class movie():
    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_url = trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer_url)
