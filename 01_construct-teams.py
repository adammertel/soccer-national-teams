'''
'''
import pandas as pd

teams = [
    {"name": "Belgium", "group": "", 	"url_nft": "https://www.national-football-teams.com/country/20/<year>/Belgium.html"   },
    {"name": "Italy", "group": "", 	"url_nft": "https://www.national-football-teams.com/country/92/<year>/Italy.html"   },
    {"name": "Russia", "group": "", 	"url_nft": "https://www.national-football-teams.com/country/152/<year>/Russia.html"   },
    {"name": "Poland", "group": "", 	"url_nft": "https://www.national-football-teams.com/country/147/<year>/Poland.html"   },
    {"name": "Ukraine", "group": "", 	"url_nft": "https://www.national-football-teams.com/country/196/<year>/Ukraine.html"   },
    {"name": "Spain", "group": "", 	"url_nft": "https://www.national-football-teams.com/country/174/<year>/Spain.html"   },
    {"name": "France", "group": "", 	"url_nft": "https://www.national-football-teams.com/country/67/<year>/France.html"   },
    {"name": "Turkey", "group": "", 	"url_nft": "https://www.national-football-teams.com/country/192/<year>/Turkey.html"   },
    {"name": "England", "group": "", 	"url_nft": "https://www.national-football-teams.com/country/59/<year>/England.html"   },
    {"name": "Czech Republic", "group": "", "url_nft": "https://www.national-football-teams.com/country/50/<year>/Czech_Republic.html"   },
    {"name": "Finland", "group": "", 	"url_nft": "https://www.national-football-teams.com/country/66/<year>/Finland.html"   },
    {"name": "Sweden", "group": "", 	"url_nft": "https://www.national-football-teams.com/country/179/<year>/Sweden.html"   },
    {"name": "Croatia", "group": "", 	"url_nft": "https://www.national-football-teams.com/country/47/<year>/Croatia.html"   },
    {"name": "Austria", "group": "", 	"url_nft": "https://www.national-football-teams.com/country/13/<year>/Austria.html"   },
    {"name": "Netherlands", "group": "", "url_nft": "https://www.national-football-teams.com/country/129/<year>/Netherlands.html"   },
    {"name": "Germany", "group": "", 	"url_nft": "https://www.national-football-teams.com/country/71/<year>/Germany.html"   },
    {"name": "Portugal", "group": "", 	"url_nft": "https://www.national-football-teams.com/country/148/<year>/Portugal.html"   },
    {"name": "Switzerland", "group": "", "url_nft": "https://www.national-football-teams.com/country/180/<year>/Switzerland.html"   },
    {"name": "Denmark", "group": "", 	"url_nft": "https://www.national-football-teams.com/country/51/<year>/Denmark.html"   },
    {"name": "Wales", "group": "", 	"url_nft": "https://www.national-football-teams.com/country/205/<year>/Wales.html"   },
    {"name": "North Macedonia", "group": "", "url_nft": "https://www.national-football-teams.com/country/111/<year>/North_Macedonia.html"   },
    {"name": "Hungary", "group": "", 	"url_nft": "https://www.national-football-teams.com/country/84/<year>/Hungary.html"   },
    {"name": "Slovakia", "group": "", 	"url_nft": "https://www.national-football-teams.com/country/168/<year>/Slovakia.html"   },
    {"name": "Scotland", "group": "", "url_nft": "https://www.national-football-teams.com/country/162/<year>/Scotland.html"   },
]

teams_df = pd.DataFrame(teams)
teams_df.to_csv('teams.csv')