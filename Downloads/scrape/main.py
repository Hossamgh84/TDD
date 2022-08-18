
from lxml import html
import requests
import pandas as pd
from normalize_nom_equipe import nom_normalizer

# journée à scrapper
for journee in range(1,39): # journée de 1 à 23 (index final = 24-1)
    # url de la site à scrapper
    url_a_scrapper = f"https://www.ligue1.fr/calendrier-resultats?seasonId=2022-2023&matchDay={journee}"
    # url principale de la site
    url_base = "https://www.ligue1.fr"
    # request pour avoir le corps de code de la page à scrapper
    resp = requests.get(url_a_scrapper)
    # trier la contnue du code de la page comme un arbre de html
    tree = html.fromstring(resp.content)

    # scrape toutes les id des matchs dans la page
    match_id = []
    match_id_code = tree.xpath('/html/body/main/div[3]/div[2]/div/div[2]/ul[*]/li/a/div[2]')
    for each_id in match_id_code:
        # if va chercher dans chaque balise a id son contenu 
        # et l'ajouter dans la liste de match_id
        match_id.append(each_id.attrib["id"])

    # recuperer les elements à chercher par leurs xpath
    equipe_home = []
    equipe_away = []
    match_href = []
    match_url = []
    i=0
    for each_id in match_id:
        # le resultat de tree.xpath sera en forme de liste 
        # il faut index[0] et .text pour recuperer le contenu
        equipe_home.append(nom_normalizer(tree.xpath(f'//*[@id="{each_id}_match-result"]/a/div[1]/div/span[1]')[0].text))
        equipe_away.append(nom_normalizer(tree.xpath(f'//*[@id="{each_id}_match-result"]/a/div[3]/div/span[1]')[0].text))
        # Afin d'avoir acceder à la page de detailles de match
        # on scrape le lien de chaque match et on l'ajout à la url_base
        # afin de deviner un lien complet
        # ici le resultat de tree.xpath a plusieurs attributes
        # donc on choisis l'attribue concerné par [0].attrib["href"]
        # href c'est l'attribue nous interesse
        match_href.append(tree.xpath(f'//*[@id="{each_id}_match-result"]/a'))
        match_url.append(url_base + match_href[i][0].attrib["href"])
        i+=1
    for i in range(10):
        print(i+1," - ",equipe_home[i],"\t", equipe_away[i],"\n url: ", match_url[i],"\n")

    # zipper les informations des listes dans un dataframe
    # avec 3 columns correspondant à chaque liste
    # et les sauvegarder dans un fichier CSV
    df_journee_1 = pd.DataFrame(list(zip(equipe_home, equipe_away, match_url)), 
                        columns =['Equipe HOME', 'Equipe AWAY', 'URL']) 
    df_journee_1.to_csv(f'journee_{journee}.csv', index=False)
