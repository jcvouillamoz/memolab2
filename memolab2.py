# -*- coding: utf-8 -*-
""" MEMOLAB EST UN LABORATOIRE DE MEMORISATION HUMAINE

L'idée est de concevoir un laboratoire doté de fonctions de mesures de
la mémorisation humaine. La mémorisation est conmprise ici comme la 
faculté d'acquérir des souvenirs en vue de leur restitution dans un 
contexte similaire et inversé de celui de l'apprentissage.
Il convient donc de se doter d'outils de correction de la restitution
qui opèrent avec une certaine variété d'exigences, de sorte de permettre
l'approche graduelle de la parfaite mémorisation souhaitée. L'effort 
d'apprendre est ainsi adaptable aux capacités particulières de l'apprenant.
Les séances de laboratoire sont également indexées sur les durées de
sorte de mesurer l'évolution de l'aptitude en terme de cadence, ceci en
corrélation avec le contexte général de vie de l'apprenant. 
Il devient loisible ensuite de planifier les durées nécessaires de préparation
en vue de l'échéance d'un examen ou autre situation de restitution 
efficace.

Ce laboratoire devrait donc constituer un outil à l'usage des apprenants,
des recruteurs de talents et de psychologues pédagogues ou thérapeutes.

Ce projet est un chantier de longue halène et ce qui m'importe n'est
pas de le terminer rapidement, mais d'en accompagner les pas sur une piste
de progression dans les méandres hésitant de la recherche et des avancées
rapides en science cognitive humaine.

C'est aussi un projet ouvert au monde, c'est pourquoi il est entreposé sur
github et accessible au public intéressé. C'est mon premier projet de cette
sorte mené dans cet environnement, il me revient de demander l'indulgence des
nombreux développeurs puls avancés qui trouveront certainement tant de 
matière perfectible, voire à proscrire et remplacer. Je souhaite accueillir
avec reconnaissance et attention les conseils constructifs que mes travaux
pourront appeler.

210303 - Jean-Claude Vouillamoz
"""
# ressources modules python
import tkinter


""" BASE DE REGISTRE PRIIVEE paraGen[]
Création de la base de registre privée de Memolab2 contenue dans le fichier
excel params_generaux présent sur le même répertoire que ce script, et chargée
dans le dictionnaire paramGen qui sera rendu accessible partout dans les
classes, méthodes et fonctions.
"""
import noyau_module1 as biblio1

nomFichierParametres = "params_generaux.xlsx"
paraGen = biblio1.chargeParametresGeneraux(nomFichierParametres)

""" LISTE DES MESSAGES listMessages[] - Chargement
Afin d'alléger le code et permettre par la suite de proposer un environnement
multilingue, tous les messages générés par Memolab2 sont enregistrés dans un
fichier excel séparé messages.xls. Par défaut il est stocké sur /data de
Memolab2 (voir paraGen["cheminMessages"]).
""" # -------------------
# chargement d'un fichier contenu dans /data
listMessages = []
listMessages = biblio1.xlsx2List("messages.xlsx", listMessages, paraGen)
# print(listMessages)
# print(listMessages)
# Instanciation de biblio2 pour avoir accès à toutes ses méthodes
# et attributs à portée de ce script (objet de portée de ce script)
import noyau_module2 as biblio2
xBiblio2 = biblio2.ClassModule2(paraGen, listMessages)

# Instanciation de biblio3 pour avoir accès à toutes ses méthodes
# et attributs à portée de ce script (objet de portée de ce script)
import noyau_module3 as biblio3
xBiblio3 = biblio3.ClassModule3(paraGen)

# Assignation optionnelle de variables accessible dans ce script
imprimeOK = paraGen["imprimeOK"]    # Flag d'impression optionnelle vers la console

# test mise au point imprime message
testMessage = biblio1.message("Salut", listMessages)
print(testMessage)


""" SELECTION UTILISATEUR 
L'idée est de permettre la mémorisation d'un historique d'évolution de 
chaque utilisateur. Pour cela un registre des utilisateurs : utilisateurs.xlsx
est situé dans le sous-répertoire /utilisateurs (paraGen["cheminUtilisateurs"]).
Il contient les données d'identification ainsi que le nom d'un fichier personnel
de journalisation des performances et résultats.
"""
xBiblio2.selectionUtilisateur()





