#-----------------------------------------------------------------------
#      RECONSTITUTION DES URLS DES IMAGES DU LIVRE
#-----------------------------------------------------------------------

import os 
import json 

racine = os.getcwd()
chemin = os.path.join(racine,"page.json")

la_grosse_liste = []
base_link = "http://www.collections.musee-bretagne.fr/flora_rennes/ark:/83011/0031519888/doc/"
numb = 2272000
end = "/high"
page = 7

le_dic =  {
    "page": 1,
    "permalink": "mmm"
}

# Recuperation du debut

f = open(chemin)
data2 = f.read()
f.close()
final = json.loads(data2)

# remplissage du json

for i in range(453) : 
    la_grosse_liste.append(le_dic)

with open(chemin, 'w', encoding='utf-8') as f:
        json.dump(la_grosse_liste, f, ensure_ascii=False, indent=2)

# maj du json

f = open(chemin)
data = f.read()
f.close()
data_json = json.loads(data)

for i in data_json : 
    numb += 1
    page += 1
    i["page"] = page
    i["permalink"] = f"{base_link}{numb}{end}"

# Fusion des 7 premiers item et de la suite generée

final.extend(data_json)

print(final)

# Json dump

with open(chemin, 'w', encoding='utf-8') as f:
        json.dump(final, f, ensure_ascii=False, indent=2)


