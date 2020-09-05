import re
from graphviz import Digraph
import toml

# initialisation du graph
graph = Digraph(format="pdf")

# ouverture du fichier
print("Quel est le nom du fichier que vous voulez ouvrir ?")
# nom_fichier = input("> ")
nom_fichier = "egouts"
nom_fichier = "test"
# ouverture du code source ink
code_ink = open(nom_fichier + ".ink", "r", encoding="utf8").read()
code_ink = code_ink.split("\n")


histoire_ink = []


def trier_histoire(histoire):
    # permet de trier l’ordre des éléments de l’histoire en fonction des éléments de début
    nouvelle_histoire = sorted(histoire, key=lambda k: k['debut'])
    return nouvelle_histoire

def trouver_noeuds(code_ink):

    for ligne in code_ink:
        if re.search("\A===", ligne):

            # détermination du titre du noeud
            titre_noeud = re.sub("=","",ligne)
            titre_noeud = re.sub("_"," ",titre_noeud)

            # recherche du prochain noeud pour déterminer la portée du précédent
            index = code_ink.index(ligne)+1

            while True:
                if index >= len(code_ink):
                    fin_noeud = index-1
                    break
                if re.search("\A===", code_ink[index]):
                    fin_noeud = index-1
                    break
                else:
                    index += 1
            debut_noeud = code_ink.index(ligne)
            histoire_ink.append({"genre": "noeud",
                                 "nom": titre_noeud,
                                 "debut": debut_noeud,
                                 "fin": fin_noeud})

def trouver_points(code_ink):

    for ligne in code_ink:
        if re.search("\A= ", ligne):

            # détermination du titre du point
            titre_point = re.sub("=","",ligne)
            titre_point = re.sub("_"," ",titre_point)

            # recherche du prochain point pour déterminer la portée du précédent
            index = code_ink.index(ligne)+1

            while True:
                if index >= len(code_ink):
                    fin_point = index-1
                    break
                if re.search("\A===", code_ink[index]) or re.search("\A= ", code_ink[index]):
                    fin_point = index-1
                    break
                else:
                    index += 1

            debut_point = code_ink.index(ligne)
            histoire_ink.append({"genre": "point",
                                 "nom": titre_point,
                                 "debut": debut_point,
                                 "fin": fin_point})

def trouver_derivation(code_ink):

    for ligne in code_ink:
        if re.search("->",ligne):
            derivation_position = code_ink.index(ligne)
            pointe_vers = re.sub("_"," ",ligne.split("->")[1])
            histoire_ink.append({"genre": "derivation",
                                 "debut": derivation_position,
                                 "cible":pointe_vers})




trouver_derivation(code_ink)
trouver_noeuds(code_ink)
trouver_points(code_ink)

histoire_ink = trier_histoire(histoire_ink)
for i in histoire_ink:
    print(i)