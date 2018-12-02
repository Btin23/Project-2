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

filename = "nba_2017_stats.csv"
f = open(filename, "w")

headers = "Player_Name, Player_Age, Yrs_in_League, Games, Minutes_Played, Field_Goals, FG_Attemps, 3_Points, 3_Points_Attempts, Free_Throws, FT_Attempts, Offensive_Rebounds, Total_Rebounds, Assists, Steals, Blocks, Turnovers, Personal_Fouls, Total_Points\n"

f.write(headers)

for container in containers:
	player_name = container.a.text

	age = container.find_all(attrs={"data-stat": "age"})
	player_age = age[0].text.strip()

	yrs = container.find_all(attrs={"data-stat": "years"})
	yrs_in_league = yrs[0].text.strip()

	game = container.find_all(attrs={"data-stat": "g"})
	games = game[0].text.strip()

	mp = container.find_all(attrs={"data-stat": "mp"})
	minutes_played = mp[0].text.strip()

	fg = container.find_all(attrs={"data-stat": "fg"})
	field_goals = fg[0].text.strip()

	fga = container.find_all(attrs={"data-stat": "fga"})
	field_goals_attempts = fga[0].text.strip()

	threep = container.find_all(attrs={"data-stat": "fg3"})
	three_points = threep[0].text.strip()

	threepa = container.find_all(attrs={"data-stat": "fg3a"})
	three_points_attempts = threepa[0].text.strip()

	ft = container.find_all(attrs={"data-stat": "ft"})
	free_throws = ft[0].text.strip()

	fta = container.find_all(attrs={"data-stat": "fta"})
	free_throws_attempts = fta[0].text.strip()

	orb = container.find_all(attrs={"data-stat": "orb"})
	off_rebounds = orb[0].text.strip()

	trb = container.find_all(attrs={"data-stat": "trb"})
	total_rebounds = trb[0].text.strip()

	ast = container.find_all(attrs={"data-stat": "ast"})
	assists = ast[0].text.strip()

	stl = container.find_all(attrs={"data-stat": "stl"})
	steals = stl[0].text.strip()

	blk = container.find_all(attrs={"data-stat": "blk"})
	blocks = blk[0].text.strip()

	tov = container.find_all(attrs={"data-stat": "tov"})
	turnovers = tov[0].text.strip()

	pf = container.find_all(attrs={"data-stat": "pf"})
	personal_fouls = pf[0].text.strip()

	pts = container.find_all(attrs={"data-stat": "pts"})
	points = pts[0].text.strip()

	# // test script // print("player_name" + player_name)
	# // test script // print("player_age" + player_age)
	
	f.write(player_name + "," + player_age + "," + yrs_in_league + "," + games + "," + minutes_played + "," + field_goals + "," + field_goals_attempts + "," + three_points + "," + three_points_attempts + "," + free_throws + "," + free_throws_attempts + "," + off_rebounds + "," + total_rebounds + "," + assists + "," + steals + "," + blocks + "," + turnovers + "," + personal_fouls + "," + points + "\n") 
