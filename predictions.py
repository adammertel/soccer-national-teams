'''
'''

import pandas as pd
import numpy as np
from dateutil import parser


teams = pd.read_csv('teams.csv')
matches = pd.read_csv('all_matches.csv', dtype={'score_home': 'int64', 'score_away': 'int64'})
#matches['date'] = matches['date'].astype('datetime64[ns]')
#print(matches)
team_names = teams['name'].to_list()
predictions = pd.DataFrame(index = team_names, columns = team_names)

#print(predictions)


for (_, t1) in teams[['name']].itertuples():
    for (_, t2) in teams[['name']].itertuples():
        if t1 != t2:
            team_matches_home = \
                matches[(matches['team_home'] == t1) & (matches['team_away'] == t2)]

            team_matches_away = \
                matches[(matches['team_away'] == t1) & (matches['team_home'] == t2)]

            # team 1
            t1_team_scores = np.array(\
                team_matches_home['score_home'].values.tolist() + \
                team_matches_away['score_away'].values.tolist() \
            )

            # team 2
            t2_team_scores = np.array(\
                team_matches_home['score_away'].values.tolist() + \
                team_matches_away['score_home'].values.tolist() \
            )

            # weights
            match_dates = team_matches_home['date'].values.tolist() + \
                team_matches_away['date'].values.tolist()

            match_years = list(map(lambda x: parser.parse(x).year, match_dates))
            match_weights = list(map(lambda x: (x - 1999) / (2021 - 1999), match_years))

            #t1_df = pd.DataFrame({'score': t1_team_scores, 'ws': match_weights})
            
            t1_wavg = np.NaN if len(match_weights) == 0 else np.average(t1_team_scores, weights=match_weights)
            t2_wavg = np.NaN if len(match_weights) == 0 else np.average(t2_team_scores, weights=match_weights)
            

            predictions.at[t1, t2] = t1_wavg
            predictions.at[t2, t1] = t2_wavg
            # print(t1, t1_team_scores.mean(), t2, t2_team_scores.mean())

predictions.to_csv('predictions.csv')
