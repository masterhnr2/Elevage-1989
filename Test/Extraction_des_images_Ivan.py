#-----------------------------------------------------------------------
#  DECOUPAGE DES IMAGES A PARTIR DE CORRDONNEES D'ANNOTATION 
#-----------------------------------------------------------------------

# Necessite d'avoir un dossier avec les images du manuscrit

import pandas as pd
import os
import re
from PIL import Image

# Extraction données tableau

tableau = pd.read_csv("./Elevage 2_annotation-list.csv")
coord = list(tableau["dims"])
noms = list(tableau["target"])
titre = list(tableau["label"])

#Extraction numero page

liste_canvas = []

for i in noms :
    end = len(i)
    canvas = i[end-3:end-1]
    cible = canvas.find("/")
    nop = canvas[cible:cible+1]
    canvas = int(canvas.replace(nop,""))
    liste_canvas.append(canvas)



# Extraction coordonnées    
    
liste_koord = []

for i in coord :
    kord = (i).split("), (")
    liste_koord.append(kord)


# Extraction et nettoyage des labels

liste_label = []

for i in titre :
    yaya = str(i)
    cible1 = yaya[0:3]
    yayo = yaya.replace(cible1, "")
    end = len(yayo)
    cible2 = yayo[end-4:end]
    yoyo = yayo.replace(cible2, "")
    liste_label.append(yoyo)


# Compilation

coordo = []
count = 0

for i in liste_koord : 
    yl = i[7]
    hx = i[9]
    hx_cut = hx.split(",")
    yl_cut = yl.split(",")
    dic = {
        "canvas" : liste_canvas[count],
        "label" : liste_label[count],
        "x" : hx_cut[1],
        "y" : yl_cut[0],
        "h" : hx_cut[0],
        "l" : yl_cut[1]
        }
    count += 1
    print(dic)
    coordo.append(dic)
    

# LISTE DES IMAGES : 

BOITE_IMG = os.path.join(os.getcwd(),'documents')
racine = os.path.join(os.getcwd())
print("-----------")

nbr_dir = os.listdir(BOITE_IMG)

compte = 0

for i in nbr_dir :
    enda = len(i)
    jaja = i[enda-7:enda-4]
    numer = int(re.sub(r'[^0-9]', '', jaja))

    for dic in coordo :
        if dic["canvas"] == numer :
                    
            im = Image.open(rf"{racine}\documents\{i}")

            # Size of the image in pixels (size of original image)
            # (This is not mandatory)
            width, height = im.size

            #print(f"largeur : {width}")
            #print(f"hauteur : {height}")

            # Setting the points for cropped image
            x = float(re.sub(r'[^0-9.]', '', dic["x"]))
            y = float(re.sub(r'[^0-9.]', '', dic["y"]))
            l = float(re.sub(r'[^0-9.]', '', dic["l"]))
            h = float(re.sub(r'[^0-9.]', '', dic["h"]))

            left = x
            top = y
            right = l
            bottom = h
            if right > left and top < bottom: 
                    

                print(f"canvas {numer}, left : {left}, top : {top}, right {right}, bottom {bottom}")

                # Cropped image of above dimension
                im1 = im.crop((left, top, right, bottom))

                # Shows the image in image viewer

                #im1.show()
                im1.save((rf"{racine}\cut\{compte}_{dic["label"]}.jpg"))

            else :
                print(f"canvas {numer} {dic["label"]}: erreur")

            compte += 1


    
    