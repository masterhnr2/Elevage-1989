#---------------------------------------------------------------------------
#  TEST D'AFFICHAGE D'UNE IMAGE DU MANUSCRIT d'APRES UN URL DANS STREAMLIT
#----------------------------------------------------------------------------


import streamlit as st

image = "http://www.collections.musee-bretagne.fr/flora_rennes/ark:/83011/0031651661/doc/2662790"

widh_media = 2500
height_media = 1878

st.image(image)