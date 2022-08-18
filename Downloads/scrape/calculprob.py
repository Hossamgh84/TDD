
import numpy as np
#import matplotlib.pyplot as plt
import math
import pandas as pd
import csv
from normalize_nom_equipe import nom_normalizer

df = pd.read_csv('merging_F.csv', sep=';')
### normalizer tous les noms des equipes dans le dataframe
# Home 
df['HomeTeam'] = df['HomeTeam'].str.strip().str.upper()
df['HomeTeam'] = df['HomeTeam'].apply(nom_normalizer)
# Away
df['AwayTeam'] = df['AwayTeam'].str.strip().str.upper()
df['AwayTeam'] = df['AwayTeam'].apply(nom_normalizer)

home_total = df[['FTHG']].sum()[0]
home_average = df[['FTHG']].mean()[0]
nb_of_matches = df[['HomeTeam']].count()[0]
#print(home_total)
#print(home_average)
#print(nb_of_matches)

away_total = df[['FTAG']].sum()[0]
away_average = df[['FTAG']].mean()[0]
#print(away_total)
#print(away_average)

with open('merging.csv') as calendrier:
    csv_reader = csv.reader(calendrier)
    with open('final-results.csv', 'w') as new_file:
        # on ouvre un csv pour sauvegarder les resultats
        csv_writer = csv.writer(new_file)                

        for line in calendrier: # line est un chaine des caracs
            data_line = line.split(sep=',') # separer les donnée
            domicile = nom_normalizer(data_line[1].strip().upper()) # recuperer l'equipe domicile
            visiteur = nom_normalizer(data_line[2].strip().upper()) # recuperer l'equipe visiteur

            team_home_df = df[df['HomeTeam']==domicile]
            team_home_total = team_home_df[['FTHG']].sum()[0]
            team_home_average = team_home_df[['FTHG']].mean()[0]
            home_conceed_total = team_home_df[['FTAG']].sum()[0]
            home_conceed_average = team_home_df[['FTAG']].mean()[0]
            nb_matches_home = team_home_df[['FTAG']].count()[0]
            home_attack_str = (team_home_average / home_average)
            home_defence_str = (home_conceed_average / away_average)

            team_away_df = df[df['AwayTeam']==visiteur]
            away_score_total = team_away_df[['FTAG']].sum()[0]
            away_score_average = team_away_df[['FTAG']].mean()[0]
            away_conceed_total = team_away_df[['FTHG']].sum()[0]
            away_conceed_average = team_away_df[['FTHG']].mean()[0]
            nb_matches_away = team_away_df[['FTHG']].count()[0]
            away_attack_str = (away_score_average / away_average)
            away_defence_str = (away_conceed_average / home_average)

            #csv_writer.writerow(str(away_attack_str)+','+str(away_defence_str)+'\n')
            new_file.write(str(domicile)+','+str(visiteur)+','+str(away_attack_str).strip()+','+str(away_defence_str).strip()+','+str(home_attack_str).strip()+','+str(home_defence_str).strip()+'\n')

with open('final-results.csv', 'r') as matchs:
    csv_reader = csv.reader(matchs)
    with open('match-prob.csv', 'w') as probs:
        # on ouvre un csv pour sauvegarder les resultats
        csv_writer = csv.writer(probs) 
        for line in matchs: # line est un chaine des caracs
            data_line = line.split(sep=',') # separer les donnée
            domicile = nom_normalizer(data_line[0].strip().upper()) # recuperer l'equipe domicile
            visiteur = nom_normalizer(data_line[1].strip().upper()) # recuperer l'equipe visiteur
            away_attack_str = data_line[2].strip()
            away_defence_str = data_line[3].strip()
            home_defence_str = data_line[4].strip()
            home_attack_str = data_line[5].strip()

            home_expect = float(home_attack_str) * float(away_defence_str) * float(home_average)
            away_expect = float(away_attack_str) * float(home_defence_str) * float(away_average)
            def poisson_probability(l, x):
                probability = ((l**x) * math.exp(-l)) / math.factorial(x)
                return probability*100
            home_goals_prob = []
            for i in range(8):
                expect = poisson_probability(home_expect, i)
                home_goals_prob.append(expect)
            home_goals_probs = np.round(home_goals_prob,2)
            away_goals_prob = []
            for i in range(8):
                expect = poisson_probability(away_expect, i)
                away_goals_prob.append(expect)  
            away_goals_probs = np.round(away_goals_prob,2) 
            p = {'Home0':[((home_goals_probs[0]*away_goals_probs[0])/100), ((home_goals_probs[0]*away_goals_probs[1])/100), ((home_goals_probs[0]*away_goals_probs[2])/100), ((home_goals_probs[0]*away_goals_probs[3])/100), ((home_goals_probs[0]*away_goals_probs[4])/100), ((home_goals_probs[0]*away_goals_probs[5])/100),((home_goals_probs[0]*away_goals_probs[6])/100),((home_goals_probs[0]*away_goals_probs[7])/100)], 
                'Home1':[((home_goals_probs[1]*away_goals_probs[0])/100), ((home_goals_probs[1]*away_goals_probs[1])/100), ((home_goals_probs[1]*away_goals_probs[2])/100), ((home_goals_probs[1]*away_goals_probs[3])/100), ((home_goals_probs[1]*away_goals_probs[4])/100), ((home_goals_probs[1]*away_goals_probs[5])/100),((home_goals_probs[1]*away_goals_probs[6])/100),((home_goals_probs[1]*away_goals_probs[7])/100)], 
                'Home2':[((home_goals_probs[2]*away_goals_probs[0])/100), ((home_goals_probs[2]*away_goals_probs[1])/100), ((home_goals_probs[2]*away_goals_probs[2])/100), ((home_goals_probs[2]*away_goals_probs[3])/100), ((home_goals_probs[2]*away_goals_probs[4])/100), ((home_goals_probs[2]*away_goals_probs[5])/100),((home_goals_probs[2]*away_goals_probs[6])/100),((home_goals_probs[2]*away_goals_probs[7])/100)], 
                'Home3':[((home_goals_probs[3]*away_goals_probs[0])/100), ((home_goals_probs[3]*away_goals_probs[1])/100), ((home_goals_probs[3]*away_goals_probs[2])/100), ((home_goals_probs[3]*away_goals_probs[3])/100), ((home_goals_probs[3]*away_goals_probs[4])/100), ((home_goals_probs[3]*away_goals_probs[5])/100),((home_goals_probs[3]*away_goals_probs[6])/100),((home_goals_probs[3]*away_goals_probs[7])/100)], 
                'Home4':[((home_goals_probs[4]*away_goals_probs[0])/100), ((home_goals_probs[4]*away_goals_probs[1])/100), ((home_goals_probs[4]*away_goals_probs[2])/100), ((home_goals_probs[4]*away_goals_probs[3])/100), ((home_goals_probs[4]*away_goals_probs[4])/100), ((home_goals_probs[4]*away_goals_probs[5])/100),((home_goals_probs[4]*away_goals_probs[6])/100),((home_goals_probs[4]*away_goals_probs[7])/100)], 
                'Home5':[((home_goals_probs[5]*away_goals_probs[0])/100), ((home_goals_probs[5]*away_goals_probs[1])/100), ((home_goals_probs[5]*away_goals_probs[2])/100), ((home_goals_probs[5]*away_goals_probs[3])/100), ((home_goals_probs[5]*away_goals_probs[4])/100), ((home_goals_probs[5]*away_goals_probs[5])/100),((home_goals_probs[5]*away_goals_probs[6])/100),((home_goals_probs[5]*away_goals_probs[7])/100)],
                'Home6':[((home_goals_probs[6]*away_goals_probs[0])/100), ((home_goals_probs[6]*away_goals_probs[1])/100), ((home_goals_probs[6]*away_goals_probs[2])/100), ((home_goals_probs[6]*away_goals_probs[3])/100), ((home_goals_probs[6]*away_goals_probs[4])/100), ((home_goals_probs[6]*away_goals_probs[5])/100),((home_goals_probs[6]*away_goals_probs[6])/100),((home_goals_probs[6]*away_goals_probs[7])/100)],
                'Home7':[((home_goals_probs[7]*away_goals_probs[0])/100), ((home_goals_probs[7]*away_goals_probs[1])/100), ((home_goals_probs[7]*away_goals_probs[2])/100), ((home_goals_probs[7]*away_goals_probs[3])/100), ((home_goals_probs[7]*away_goals_probs[4])/100), ((home_goals_probs[7]*away_goals_probs[5])/100),((home_goals_probs[7]*away_goals_probs[6])/100),((home_goals_probs[7]*away_goals_probs[7])/100)]}
            probability = pd.DataFrame(p, index=['away0','away1','away2', 'away3', 'away4', 'away5', 'away6', 'away7'])
            nump = probability.to_numpy()
            draw_prob = np.trace(nump)
            Home_win_prob = (np.trace(nump, offset = 1))+(np.trace(nump, offset = 2))+(np.trace(nump, offset = 3))+(np.trace(nump, offset = 4))+(np.trace(nump, offset = 5))+(np.trace(nump, offset = 6))
            away_win_prob = (np.trace(nump, offset = -1))+(np.trace(nump, offset = -2))+(np.trace(nump, offset = -3))+(np.trace(nump, offset = -4))+(np.trace(nump, offset = -5))+(np.trace(nump, offset = -6))
            probs.write(domicile+','+visiteur+','+str(draw_prob).strip()+','+str(Home_win_prob)+','+str(away_win_prob)+','+'\n')
matchs.close()
probs.close()