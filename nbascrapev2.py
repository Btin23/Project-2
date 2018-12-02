import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


url_source = 'https://www.basketball-reference.com/leagues/NBA_2018_final.html'

#Open Connection to page
connection = uReq(url_source)
nba_site = connection.read()
connection.close()

page_soup = soup(nba_site, "html.parser")

containers = page_soup.findAll("tr",{"class":"full_table"})

filename = "nbastats.txt"
f = open(filename, "w")

headers = "player, games, fg, threepts, totalpts\n"

f.write(headers)

for container in containers:
	playername = container.a.text


	game = container.find_all(attrs={"data-stat": "g"})
	games = game[0].text.strip()


	fg = container.find_all(attrs={"data-stat": "fg"})
	fieldgoals = fg[0].text.strip()


	threep = container.find_all(attrs={"data-stat": "fg3"})
	threepoints = threep[0].text.strip()


	pts = container.find_all(attrs={"data-stat": "pts"})
	points = pts[0].text.strip()

	# // test script // print("player_name" + player_name)
	# // test script // print("player_age" + player_age)
	
	f.write(playername + "," + games + "," + fieldgoals + "," + threepoints + "," + points + "\n") 
