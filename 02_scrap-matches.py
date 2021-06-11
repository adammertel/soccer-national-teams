'''

'''

import numpy as np
import pandas as pd
from pyquery import PyQuery as pq
import requests

teams = pd.read_csv('teams.csv')
#print(teams)

matches = []

country_names = teams['name'].values
print(country_names)

years = [i for i in range(2000, 2022, 1)]

for (_, name, url_nft) in teams[['name', 'url_nft']].itertuples():
    for year in years:
        print('scrapping {} {}'.format(name, year))
        url = url_nft.replace('<year>', str(year))
        r = requests.get(url)
        c = pq(r.content)

        match_trs = [pq(tr) for tr in c('#matches table tbody tr').items()]
        for match_tr in match_trs:
            team_home = match_tr('td.teams.home span').text()
            team_away = match_tr('td.teams.away span').text()
            match_date = match_tr('td.date').text()
            match_type = match_tr('td.event').text()
            result = match_tr('td.result a').text()

            if team_home == name:
                if team_away in country_names:
                    matches.append(
                        {
                            'date': match_date,
                            'team_home': team_home,
                            'team_away': team_away,
                            'score':  result,
                            'friendly': match_type == 'Friendly',
                            'score_home': result.split(':')[0][0],
                            'score_away': result.split(':')[1][0],
                            'penalties': '' if "(" not in result else result[result.find("(")+1:result.find(")")]
                        }
                    )


pd.DataFrame(matches).to_csv('all_matches.csv')



    
