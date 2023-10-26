import numpy as np
import pandas as pd



# Créer le tableau avec des 0,1,2 aléatoire dans 10 colonnes et 10 lignes
df = pd.DataFrame( {  'A' : [0,0,0,0,0,0,0,0,0,0],
                      'B' : [0,0,0,0,0,0,0,0,0,0],
                      'C' : [0,0,0,0,0,0,0,0,0,0],
                      'D' : [0,0,0,0,0,0,0,0,0,0],
                      'E' : [0,0,0,0,0,0,0,0,0,0]})
print(df)