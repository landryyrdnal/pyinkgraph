import re



from graphviz import Digraph


# initialisation du graph
graph = Digraph(format="pdf"  )

# ouverture du fichier
print("Quel est le nom du fichier que vous voulez ouvrir ?")
# nom_fichier = input("> ")
nom_fichier = "egouts"
nom_fichier = "test1"
# ouverture du code source ink
code_ink = open(nom_fichier + ".ink", "r", encoding="utf8").read()
code_ink = code_ink.split("\n")

histoire_ink = []


def definir_contenu_element(histoire_ink):
    for element in histoire_ink:
        contenu = []

        for individu in histoire_ink:
            dict = {}
            if est_dans(individu, element):
                dict["genre"] = individu.get("genre")
                if individu.get("niveau"):
                    dict["niveau"] = individu.get("niveau")
                if individu.get("nom"):
                    dict["nom"] = individu.get("nom")
                else:
                    dict["nom"] = individu.get("debut")
                contenu.append(dict)

        if len(contenu) > 0:
            element["contenu"] = contenu


def est_dans(element, dans_element):
    position = element.get("debut")
    if position > dans_element.get("debut") and position <= dans_element.get("fin"):
        return True
    else:
        return False


def genre_est(genre, element):
    if element.get("genre") == genre:
        return True
    else:
        return False


def niveau_est(niveau, element):
    if element.get("niveau") == niveau:
        return True
    else:
        return False


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
            titre_noeud = titre_noeud.lstrip()

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
                        cible = trouver_derivation(ligne)


            if derive:
                genre_choix = "choix dérivé"

            else:
                genre_choix = "choix simple"

            dict_choix = {"genre": genre_choix, "debut": debut_choix, "fin": fin_choix, "niveau": niveau_choix}

            if derive:
                dict_choix["cible"] = cible

            if etiquette:
                dict_choix["nom"] = etiquette_choix


            histoire_ink.append(dict_choix)


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
                        cible = trouver_derivation(ligne)



            if derive:
                genre_collecteur = "collecteur dérivé"

            else:
                genre_collecteur = "collecteur simple"

            dict_collecteur = {"genre": genre_collecteur, "debut": debut_collecteur, "fin": fin_collecteur,
                           "niveau": niveau_collecteur}

            if derive:
                dict_collecteur["cible"] = cible

            if etiquette:
                dict_collecteur["nom"] = etiquette_collecteur

            histoire_ink.append(dict_collecteur)


def imprimer_liens_explicites(histoire_ink):
    for element in histoire_ink:
        if element.get("cible"):
            cible = element.get("cible")
            if element.get("nom"):
                nom = element.get("nom")
                graph.edge(nom, cible)
            else:
                nom = str(element.get("debut"))
                graph.edge(nom, cible)


def imprimer_liens_implicites(histoire_ink):

    # imprime tous les liens implicites entre les noeuds/points -> choix
    for element in histoire_ink:

        if genre_est("noeud", element) or genre_est("point", element):
            index = histoire_ink.index(element) + 1

            while index < len(histoire_ink)-1:

                if genre_est("choix simple", histoire_ink[index]) or genre_est("choix dérivé", histoire_ink[index]):

                    if histoire_ink[index].get("niveau") == 1:
                        graph.edge(element.get("nom"),str(histoire_ink[index].get("nom",histoire_ink[index].get("debut"))), style = "dotted")

                    index += 1

                elif genre_est("collecteur simple", histoire_ink[index]) and histoire_ink[index].get("niveau") == 1:
                    break

                elif genre_est("collecteur dérivé", histoire_ink[index]) and histoire_ink[index].get("niveau") == 1:
                    break

                elif genre_est("point", histoire_ink[index]):
                    break

                elif genre_est("noeud", histoire_ink[index]):
                    break

                else:
                    index += 1

    # imprime tous les liens entre choix/point/noeud -> collecteurs

    for element in histoire_ink:
        index = histoire_ink.index(element)-1
        choix_trouve = False
        collecteur_inferieur = False
        if genre_est("collecteur simple", element) or genre_est("collecteur dérivé", element):
            while index > 1 :
                if genre_est("choix simple", histoire_ink[index]):

                    if histoire_ink[index].get("niveau") == element.get("niveau"):
                        graph.edge(str(histoire_ink[index].get("nom",histoire_ink[index].get("debut"))), str(element.get("nom",element.get("debut"))), style = "dashed")
                        choix_trouve = True

                    elif histoire_ink[index].get("niveau") > element.get("niveau") and collecteur_inferieur == False:
                        graph.edge(str(histoire_ink[index].get("nom",histoire_ink[index].get("debut"))), str(element.get("nom",element.get("debut"))), style = "dashed")
                        choix_trouve = True
                    index -= 1

                elif genre_est("point", histoire_ink[index]) and choix_trouve == False:
                    graph.edge(str(histoire_ink[index].get("nom")), str(element.get("nom",element.get("debut"))), style = "dashed")
                    break
                elif genre_est("noeud", histoire_ink[index]) and choix_trouve == False:
                    graph.edge(str(histoire_ink[index].get("nom")), str(element.get("nom",element.get("debut"))), style = "dashed")
                    break
                elif genre_est("collecteur simple", histoire_ink[index]) and histoire_ink[index].get("niveau") <= element.get("niveau"):
                    break
                elif genre_est("collecteur dérivé", histoire_ink[index]) and histoire_ink[index].get("niveau") <= element.get("niveau"):
                    break
                elif genre_est("noeud", histoire_ink[index]) and choix_trouve == True:
                    break
                elif genre_est("point", histoire_ink[index]) and choix_trouve == True:
                    break
                elif genre_est("collecteur simple", histoire_ink[index]) and histoire_ink[index].get("niveau") > element.get("niveau"):
                    collecteur_inferieur = True
                    index -= 1
                elif genre_est("collecteur dérivé", histoire_ink[index]) and histoire_ink[index].get("niveau") > element.get("niveau"):
                    collecteur_inferieur = True
                    index -= 1
                else:
                    index -= 1

#graph.edge("test","test1", style = "dotted")


code_ink = nettoyer_code(code_ink)
trouver_choix(code_ink)
trouver_noeuds(code_ink)
trouver_points(code_ink)
trouver_collecteur(code_ink)
definir_contenu_element(histoire_ink)

histoire_ink = trier_histoire(histoire_ink)
imprimer_liens_explicites(histoire_ink)
imprimer_liens_implicites(histoire_ink)

for i in histoire_ink:
    print(i.get("genre"),"\t\t =\t ",str(i.get("nom",i.get("debut"))), " \t", i.get("niveau",""))


# affichage du graph
graph.render(view=True)

#