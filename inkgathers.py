import re
from graphviz import Digraph
import toml

# initialisation du graph
graph = Digraph(format="pdf")

# ouverture du fichier
print("Quel est le nom du fichier que vous voulez ouvrir ?")
# nom_fichier = input("> ")
nom_fichier = "egouts"
# nom_fichier = "test"
# ouverture du code source ink
code_ink = open(nom_fichier + ".ink", "r", encoding="utf8").read()
code_ink = code_ink.split("\n")

histoire_ink = []


def nettoyer_code(code_ink):
    nouveau_code = []
    for ligne in code_ink:
        nouveau_code.append(re.sub("\t", "", ligne).lstrip())
    return nouveau_code


def trier_histoire(histoire):
    nouvelle_histoire = []
    for ligne in histoire:
        if ligne not in nouvelle_histoire:
            nouvelle_histoire.append(ligne)

    # permet de trier l’ordre des éléments de l’histoire en fonction des éléments de début
    nouvelle_histoire = sorted(nouvelle_histoire, key=lambda k: k['debut'])

    # ajoute 1 à tous les débuts et toutes les fins pour correspondre aux n° de ligne du texte source
    for ligne in nouvelle_histoire:
        ligne["debut"] += 1
        if ligne.get("fin"):
            ligne["fin"] +=1

    return nouvelle_histoire


def trouver_noeuds(code_ink):
    for ligne in code_ink:
        if re.search("\A===", ligne):

            # détermination du titre du noeud
            titre_noeud = re.sub("=", "", ligne)
            titre_noeud = re.sub("_", " ", titre_noeud)

            # recherche du prochain noeud pour déterminer la portée du précédent
            index = code_ink.index(ligne) + 1

            while True:
                if index >= len(code_ink):
                    fin_noeud = index - 1
                    break
                if re.search("\A===", code_ink[index]):
                    fin_noeud = index - 1
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
            titre_point = re.sub("=", "", ligne)
            titre_point = re.sub("_", " ", titre_point)
            titre_point = titre_point.lstrip()

            # recherche du prochain point pour déterminer la portée du précédent
            index = code_ink.index(ligne) + 1

            while True:
                if index >= len(code_ink):
                    fin_point = index - 1
                    break
                if re.search("\A===", code_ink[index]) or re.search("\A= ", code_ink[index]):
                    fin_point = index - 1
                    break
                else:
                    index += 1

            debut_point = code_ink.index(ligne)
            histoire_ink.append({"genre": "point",
                                 "nom": titre_point,
                                 "debut": debut_point,
                                 "fin": fin_point})


def trouver_derivation(ligne):

    if re.search("->", ligne):
        derivation_position = code_ink.index(ligne)
        pointe_vers = re.sub("_", " ", ligne.split("->")[1])
        pointe_vers = pointe_vers.lstrip()

        return pointe_vers


def trouver_choix(code_ink):
    for ligne in code_ink:

        etiquette = False
        derive = False

        if re.search("\A\*", ligne) or re.search("\A\+", ligne):
            # position du début du choix
            debut_choix = code_ink.index(ligne)

            # niveau du choix
            if re.search("\A\*", ligne):
                niveau_choix = ligne.count("*")
            else:
                niveau_choix = ligne.count("+")

            # recherche de la porté du choix
            index = code_ink.index(ligne) + 1
            while True:
                if index >= len(code_ink):
                    fin_choix = index - 1
                    break
                if re.search("\A-", code_ink[index]) and not \
                        re.search("\A->", code_ink[index]) and not \
                        re.search("else:", code_ink[index]) or \
                        re.search("\A\*", code_ink[index]) or \
                        re.search("\A\+", code_ink[index]) or \
                        re.search("\A=", code_ink[index]):
                    fin_choix = index - 1
                    break
                else:
                    index += 1

            # recherche du type de choix & de l’étiquette

            for ligne in code_ink:

                if code_ink.index(ligne) >= debut_choix and code_ink.index(ligne) <= fin_choix:

                    # rechercher d’étiquette
                    if re.search("\(", code_ink[debut_choix]) and re.search("\)", code_ink[debut_choix]):
                        etiquette_choix = code_ink[debut_choix].split("(")[1]
                        etiquette_choix = etiquette_choix.split(")")[0]
                        etiquette_choix = re.sub("_", " ", etiquette_choix)
                        etiquette = True

                    if re.search("->", ligne):
                        derive = True

            if derive:
                genre_choix = "choix dérivé"

            else:
                genre_choix = "choix simple"

            if etiquette:
                histoire_ink.append(
                    {"genre": genre_choix, "nom": etiquette_choix, "debut": debut_choix, "fin": fin_choix,
                     "niveau": niveau_choix})
            else:
                histoire_ink.append(
                    {"genre": genre_choix, "debut": debut_choix, "fin": fin_choix, "niveau": niveau_choix})


def trouver_collecteur(code_ink):
    for ligne in code_ink:

        etiquette = False
        derive = False

        if re.search("\A-", ligne) and not re.search("else:", ligne) and not re.search("\A->", ligne):
            # position du début du collecteur
            debut_collecteur = code_ink.index(ligne)

            # niveau du collecteur
            niveau_collecteur = ligne.count("-")

            # recherche de la porté du collecteur
            index = code_ink.index(ligne) + 1
            while True:
                if index >= len(code_ink):
                    fin_collecteur = index - 1
                    break
                if re.search("\A-", code_ink[index]) and not \
                        re.search("\A->", code_ink[index]) and not \
                        re.search("else:", code_ink[index]) or \
                        re.search("\A\*", code_ink[index]) or \
                        re.search("\A\+", code_ink[index]) or \
                        re.search("\A=", code_ink[index]):
                    fin_collecteur = index - 1
                    break
                else:
                    index += 1
            for ligne in code_ink:

                # recherche du type de collecteur

                if code_ink.index(ligne) >= debut_collecteur and code_ink.index(ligne) <= fin_collecteur:
                    # rechercher d’étiquette
                    if re.search("\(", code_ink[debut_collecteur]) and re.search("\)", code_ink[debut_collecteur]):
                        etiquette_collecteur = code_ink[debut_collecteur].split("(")[1]
                        etiquette_collecteur = etiquette_collecteur.split(")")[0]
                        etiquette_collecteur = re.sub("_", " ", etiquette_collecteur)
                        etiquette = True

                    if re.search("->", ligne):
                        derive = True

            if derive:
                genre_collecteur = "collecteur dérivé"

            else:
                genre_collecteur = "collecteur simple"

            if etiquette:
                histoire_ink.append({"genre": genre_collecteur, "nom": etiquette_collecteur, "debut": debut_collecteur,
                                     "fin": fin_collecteur, "niveau": niveau_collecteur})
            else:
                histoire_ink.append({"genre": genre_collecteur, "debut": debut_collecteur, "fin": fin_collecteur,
                                     "niveau": niveau_collecteur})









# def tri_par_critere(critere, interval, histoire_ink):
#     if type(critere) == str:
#         critere = list(critere)
#     resultat = []
#     for ligne in histoire_ink:
#         if ligne.get("genre") in critere \
#                 and histoire_ink.index(ligne) >= interval.get("debut") + 1 \
#                 and histoire_ink.index(igne) <= interval.get("fin"):
#             resultat.append(ligne)
#     return resultat
#
#
# def imprimer(histoire_ink):
#     # impression des noeuds et des points en subgraph respectifs
#
#     for noeud in histoire_ink:
#
#         # recherche chaque nœud
#         if noeud.get("genre") == "noeud":
#
#             # recherche tous les points dans chaque nœud
#             liste_points_dans_noeud = tri_par_critere("point", noeud, histoire_ink)
#
#                 for point in liste_points_dans_noeud:
#
#                     # recherche tous les choix & collecteurs dans chaque point
#                     liste_choix_collecteurs_dans_point = tri_par_critere(["choix simple",
#                                                                           "choix dérivé",
#                                                                           "collecteur simple",
#                                                                           "collecteur dérivé"], point, histoire_ink)
#
#
#
#                 # recherche tous les choix & collecteurs dans le noeud qui n’appartiennent pas à un point du noeud
#
#             # déterminer la portée du noeud avant le premier point
#             if len(liste_points_dans_noeud) >= 1:
#                 # tri la liste des points dans le noeud par ordre d’apparition
#                 liste_points_dans_noeud = sorted(liste_points_dans_noeud, key=lambda k: k['debut'])
#                 limite = liste_points_dans_noeud[0].get("debut") - 1
#
#                 liste_choix_collecteurs_dans_noeud = []
#                 for choix_collecteur in histoire_ink:
#                     liste_points_collecteurs_a_chercher = ["choix simple",
#                                                            "choix dérivé",
#                                                            "collecteur simple",
#                                                            "collecteur dérivé"]
#
#                     if choix_collecteur.get("genre") in liste_points_collecteurs_a_chercher and \
#                             choix_collecteur.get("debut") in range(noeud.get("debut"), limite):
#                         liste_choix_collecteurs_dans_noeud.append(choix_collecteur)
#                         print(range(noeud.get("debut"), limite))
#
#                 # IMPRESSION DES NOMS DES NŒUDS, POINTS, CHOIX & COLLECTEURS
#
#                 # impression points en subgraph
#                 with graph.subgraph(name=str("cluster_" + str(noeud.get("nom")))) as sub:
#                     # ajout du nœud au graph
#                     sub.node(noeud.get("nom"), shape="box")
#                     # style de la boîte du noeud
#                     sub.attr(style="filled", color="lightgrey")
#
#                     # ajout des points du nœud au subgraph
#                     for point in liste_points_dans_noeud:
#                         sub.node(point.get("nom"))
#
#                     # ajout des choix & collecteurs du nœud au subgraph
#                     for choix_collecteur in liste_choix_collecteurs_dans_noeud:
#                         sub.node(str(choix_collecteur.get("nom", choix_collecteur.get("debut"))), shape="plaintext",
#                                  color="blue")
#
#                     if len(liste_choix_collecteurs_dans_point) >= 1:
#
#                         # impression points & choix_collecteurs en subsubgraph
#                         with sub.subgraph(name=str("cluster_" + str(point.get("nom")))) as subsub:
#
#                             # style de la boîte du point
#                             subsub.attr(color="white")
#
#                             # ajout des choix_collecteurs du point au subsubgraph
#                             for choix_collecteur in liste_choix_collecteurs_dans_point:
#                                 subsub.node(str(choix_collecteur.get("nom", choix_collecteur.get("debut"))),
#                                             shape="plaintext")
#                             subsub.node(str(point.get("nom")))
#
#     # IMPRESSION DES CHOIX SIMPLES
#
#     # relie tous les choix simple au collecteur du même niveau le plus proche
#     for choix_simple in histoire_ink:
#
#         # filtre les choix simples
#         if choix_simple.get("genre") == "choix simple":
#             # recherche du collecteur le plus proche
#             collecteur = ["collecteur simple", "collecteur dérivé"]
#             index = histoire_ink.index(choix_simple) + 1
#             while True:
#                 # si la ligne est un collecteur
#                 if index >= len(histoire_ink) - 1:
#                     break
#
#
#                 elif histoire_ink[index].get("genre") in collecteur:
#                     # si le niveau du choix est égale ou inférieur à celui du collecteur
#                     if choix_simple.get("niveau") <= histoire_ink[index].get("niveau"):
#                         graph.edge(str(choix_simple.get("nom", choix_simple.get("debut"))),
#                                    str(histoire_ink[index].get("nom", histoire_ink[index].get("debut"))))
#
#                     break
#
#                 else:
#                     index += 1


code_ink = nettoyer_code(code_ink)
trouver_choix(code_ink)
trouver_noeuds(code_ink)
trouver_points(code_ink)
trouver_collecteur(code_ink)

histoire_ink = trier_histoire(histoire_ink)


for i in histoire_ink:
    print(i)


# affichage du graph
#graph.render(view=True)
