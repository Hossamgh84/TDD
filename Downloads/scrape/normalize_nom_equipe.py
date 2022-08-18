
# dictionnaire contenant tous les noms possibles de chaque equipe
import pandas as pd
"""
Liste de toutes les equipes dand F2.csv
'Dijon'
'Bordeaux'
'Nice'
'Monaco'
'Strasbourg'
'Nantes'
'Rennes'
'Montpellier'
'Angers'
'Brest'
'Reims'
'Lens'
'Lille'
'Paris SG'
'Marseille'
'Nimes'
'Metz'
'St Etienne'
'Lorient'
'Lyon'

liste de toutes les equipes dans merging.csv
FC LORIENT
FC NANTES
OLYMPIQUE DE MARSEILLE
AS MONACO
ESTAC TROYES
OLYMPIQUE LYONNAIS
STADE RENNAIS FC
CLERMONT FOOT 63
AJ AUXERRE
MONTPELLIER HÉRAULT SC
OGC NICE
STADE DE REIMS
AC AJACCIO
LOSC LILLE
TOULOUSE FC
RC STRASBOURG ALSACE
ANGERS SCO
STADE BRESTOIS 29
RC LENS
PARIS SAINT-GERMAIN
"""

"""
### un code pour extraire les valeurs uniques d'un colonne
df_merge = pd.read_csv('merging.csv')
equip_unique_scrape = open('equip_unique_scrape.txt','a')
equip_unique_scrape.write(str(set(df_merge['Equipe_Home'])))
"""

def nom_normalizer(equipe_a_normaliser):
    teams = {
        'OLYMPIQUE LYONNAIS': ['LYON', 'OL', 'O.L.'], 
        'AC AJACCIO': ['AJACCIO', 'ACA', 'A.C.A', 'ATHLETIC CLUB AJACCIEN','A-C AJACCIO','A.C AJACCIO'],
        'RC STRASBOURG ALSACE' : ['STRASBOURG','RACING CLUB DE STRASBOURG ALSACE', 'RC STRASBOURG','R.C. STRASBOURG','R.C.S.','RCS', 'R.C.S.A.', 'RC STRASBOURG ALSACE', 'R.C. STRASBOURG ALSACE'], 
        'AS MONACO': ['MONACO', 'ASSOCIATION SPORTIVE DE MONACO FOOTBALL CLUB', 'AS MONACO FC', 'A.S MONACO F.C', 'ASM'], 
        'CLERMONT FOOT 63': ['CLERMONT-FERRAND', 'CF63', 'C.F.63', 'C-F 63', 'CLERMONT FOOT','CLERMONT'], 
        'PARIS SAINT GERMAIN': ['PARIS', 'PARIS-SAINT-GERMAIN FOOTBALL CLUB', 'PSG', 'P.S.G.', 'PARIS SG', 'PARIS-SG', 'PARIS SAINT-GERMAIN', 'PARIS SAINT-GERMAIN FOOTBALL CLUB', 'PARIS SAINT-GERMAIN FC'], 
        'TOULOUSE FC' : ['TOULOUSE', 'TOULOUSE FOOTBALL CLUB', 'TFC', 'T.F.C.', 'TOULOUSE FC', 'TOULOUSE F.C.'], 
        'OGC NICE': ['NICE', "OLYMPIQUE GYMNASTE CLUB NICE COTE D'AZUR", 'OGC NICE', 'O.G.C. NICE', "OGC NICE COTE D'AZUR", "O.G.C. NICE COTE D'AZUR", 'OLYMPIQUE GYMNASTE CLUB NICE'], 
        'ANGERS SCO': ['ANGERS', "SCO D'ANGERS", 'SCOA', "ANGERS SPORTING CLUB DE L'OUEST", 'SCO ANGERS', 'ANGERS-SCO', 'ANGERS S.C.O.', 'S.C.O. ANGERS'], 
        'FC NANTES' : ['NANTES', 'FOOTBALL CLUB DE NANTES', 'F.C. NANTES', 'FCN', 'F.C.N.'], 
        'RC LENS': ['LENS', 'RACING CLUB DE LENS', 'RCL', 'R.C.L.', 'R.C. LENS'], 
        'STADE BRESTOIS': ['BREST', 'STADE BRESTOIS 29', 'SB29', 'S.B.29', 'S.B. 29'], 
        'LOSC LILLE': ['LILLE', 'LOSC', 'LILLE OLYMPIQUE SPORTING CLUB', 'L.O.S.C.', 'L.O.S.C. LILLE'], 
        'AJ AUXERRE': ['AUXERRE', 'AJA', 'ASSOCIATION DE LA JEUNESSE AUXERROISE', 'A.J.AUXERRE', 'A.J AUXERRE'], 
        'MONTPELLIER HÉRAULT SC': ['MONTPELLIER', 'MONTPELLIER-HERAULT SPORT CLUB', 'MONTPELLIER HERAULT SPORT CLUB', 'MONTPELLIER HSC', 'MHSC', 'MONTPELLIER-HERAULT SC', 'MONTPELLIER-HERAULT S.C.', 'M.H.S.C.', 'MONTPELLIER HERAULT SC', 'MONTPELLIER HERAULT S.C.'], 
        'ESTAC TROYES': ['TROYES', 'ESPERANCE SPORTIVE TROYES AUBE CHAMPAGNE', 'ESTAC', 'E.S.T.A.C.', 'ESTAC TROYES', 'E.S.T.A.C. TROYES'], 
        'STADE RENNAIS FC': ['RENNES', 'STADE RENNAIS FOOTBALL CLUB', 'STADE RENNAIS FC', 'S.R.F.C.', 'STADE RENNAIS F.C.'], 
        'FC LORIENT': ['LORIENT', 'FOOTBALL CLUB LORIENT BRETAGNE SUD', 'FCL', 'F.C.L.', 'F.C. LORIENT', 'FC LORIENT BRETAGNE SUD', 'FOOTBALL CLUB LORIENTAIS'], 
        'OLYMPIQUE DE MARSEILLE': ['MARSEILLE', 'OM', 'O.M.'],
        'STADE DE REIMS': ['REIMS', 'STADE REIMS'],
        'DIJON': ['DIJON'],
        'SAINT ETIENNE': ['ST ETIENNE'],
        'BORDEAUX': ['BORDEAUX'],
        'METZ': ['METZ']}
    resultat = equipe_a_normaliser
    for equipe_name in teams:
        if equipe_a_normaliser in teams[equipe_name]:
            return equipe_name
    return resultat 
    