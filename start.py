# coding=UTF-8
import fresh_tomatoes
import EntertainmentCenter
"""get the movie list and render the web page"""


moivelist = [EntertainmentCenter.american_captain,
             EntertainmentCenter.monster,
             EntertainmentCenter.turtle,
             EntertainmentCenter.xmen]
fresh_tomatoes.open_movies_page(moivelist)
