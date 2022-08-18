
import csv
merged =open("merging.csv","a")    
merged.write('Journée,Equipe_Home,Equipe_Away,URL\n')  
for num in range(1,39):
    f = open("journee_"+str(num)+".csv")
    next(f) # skip the header
    for line in f:
        merged.write(f'{num},'+line)
    f.close() # not really needed
merged.close()

merged_F =open("merging_F.csv","a")    
merged_F.write('HomeTeam;AwayTeam;FTHG;FTAG\n')  
for num in range(1,3):
    ff = open("F"+str(num)+".csv")
    next(ff) # skip the header
    for line in ff:
        merged_F.write(line)
    ff.close() # not really needed
merged_F.close()