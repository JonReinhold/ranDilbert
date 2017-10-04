import random 
import webbrowser

baseURL = "http://dilbert.com/strip/"
#pythonic..
hyphen = "-"

#rounded for ease of use and lack of interest in the 1980s
firstYear = 1990
firstMonth = 1
firstDay = 1

lastYear = 2016
#december just isn't funny
lastMonth = 11
lastDay = 28

randYear = str(random.randint(firstYear, lastYear)) + hyphen
randMonth = str(random.randint(firstMonth, lastMonth)) + hyphen
randDay = str(random.randint(firstDay, lastDay))

fullURL = baseURL + randYear + randMonth + randDay

webbrowser.open_new(fullURL)
