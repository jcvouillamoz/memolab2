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
biblio2.ClassModule2(paraGen, listMessages)

# Instanciation de biblio3 pour avoir accès à toutes ses méthodes
# et attributs à portée de ce script (objet de portée de ce script)
import noyau_module3 as biblio3
biblio3.ClassModule3(paraGen)

# Assignation optionnelle de variables accessible dans ce script
imprimeOK = paraGen["imprimeOK"]    # Flag d'impression optionnelle vers la console

# test mise au point imprime message
testMessage = biblio1.message("Salut", listMessages)
print(testMessage)

# test lancement activité d'une classe de biblio2

"""
Un dictionnaire "dicoScenario" est créé qui contient la structure suivante:
    Clé <str> : désignation de la grandeur d'état 
    Valeur : la variable ou l'objet concerné
les clés des utilisateurs sont les suivantes:
    listUtilisateurs : la list des utilisateur enregistrés possédant un 
                        fichier personnel
    listUtilisateur : list contenant les lecons en cours d'étude et leurs états
    nomUtilisateur : prénom nom de l'utilisateur
    pseudoUtilisateur : pseudo de l'utilisateur
    nomFichierUtilisateur : nom complet du fichier personnel de l'utilisateur
Les clés des sessions labo sont les suivantes:
1) historique leçon en cours :
    nomFichierLecon : nom du fichier de la lecon en cours d'étude
    nbQuestions : nombre de questions de dito
    modeDerNiveau : mode correction dernier niveau
    derNiveau : note obtenue sur 6 (rapport nbPremRepJustes / nbQuestions)
    derDuree : Durée dernière session
    dureeCum : durée cumulée de toutes les sessions de cette leçon
    dateDerSession : Date de la dernière session
    derSessionTerminee : Vrai si toutes les questions dernière session
                            ont été traitées
2) Session labo en cours :
    dateSessionEnCours : date du jour
    dureeSessionEnCours : durée depuis la première question posée
    SessionTerminee : Flag d'indication si session terminée
    nbQuestionsRestantes : nombre de questions qu'il reste à poser
    nbPremRepJustes : Nombre de premières réponses justes
    nbRepJustes : Nombre total des réponses justes
    nbRepFausses : Nombre de réponses fausses
    auMoinsUnMotJuste : mode correction A : au moins un mot contenu dans 
                    la réponses
    tousLesMotsJustes : mode correstion B : tous les mots contenus dans 
                    la réponse
    tousLesMotsEnBonOrdre : mode correstion C : tous les mots dans le bon ordre
    copieExacte : mode correction D : copie exacte, nb espaces entre les mots 
                    non compris
    noteExamen : rapport du nb de premières réponses justes au nombre de 
                    questions de la leçon
    noteTravail : rapport du nombre de questions justes aux questions totales 
                    posées
"""
# Création du dictionnaire d'état du scenario en cours
makeDicoScenario = biblio2.Scenario()   # instanciation classe Scenario
dicoScenario = makeDicoScenario.CreationDicoScenario()  # application méthode 
                                                        # de création
# print(dicoScenario)



# ========================== G U I de MEMOLAB ==========================

# Création fenêtre principale
window = tkinter.Tk()
# Configuration fenêtre principale
window.title("Memolab2021a")
window.geometry("1000x600")
# window.minsize(640,480)
window['bg'] = '#d6ffd9'	    # Couleur du fond


################## Configuration des fonctions appelées par le menu #######

"""
Structure des menus :

    Utilisateur:
        Sélectionner
        Créer
        Editer
        Supprimer
        Statistiques
        Partager

    Fichiers:
        Créer Leçon
        Ouvrir Lecon
        Supprimer lecon
        Partager

    Laboratoire:
        Selectionner lecon
        Questions-Réponses courtes
        Questions choix multiples

    Options:
        Préférences
        Aide
        A propos

"""

def utilisateurSelectionner():
    """ SELECTION UTILISATEUR 
    L'idée est de permettre la mémorisation d'un historique d'évolution de 
    chaque utilisateur. Pour cela un registre des utilisateurs : utilisateurs.xlsx
    est situé dans le sous-répertoire /utilisateurs (paraGen["cheminUtilisateurs"]).
    Il contient les données d'identification ainsi que le nom d'un fichier personnel
    de journalisation des performances et résultats.
    """
    # Connexion de l'utilisateur à Memolab
    user = biblio2.Utilisateur()     # création objet de class utilisateur
    listUtilisateur = user.fenetreSelectionUtilisateur()
    print("Finalement : ",listUtilisateur)
    nomUtilisateurActif = listUtilisateur[2]
    # Mise en liste du fichier personnel de l'utilisateur, avec sa liste de 
    # leçons en cours. Si le fichier n'existe pas il est recréé par copie du 
    # modele présent dans le même répertoire.
    listFichierUtilisateur = user.miseEnListFichierUtilisateur(listUtilisateur[3])
    # affiche liste des lecons en cours
    biblio1.afficheListEnTable(listFichierUtilisateur)

    # Bienvenue <Nom utilisateur>
    messageTitre = "Sélection utilisateur actif..."
    messageContenu = ""
    messageContenu += "Bienvenue " + nomUtilisateurActif + " !" + "\n"
    biblio1.annonce(messageTitre, messageContenu)
    

    return nomUtilisateurActif

def utilisateurCreer():
    # Saisie nom d'utilisateur

    # formation du nom correspondant pour le fichier

    # recherche du fichier

    # création du fichier au nom de l'utilisateur

    # enregistrement du nouvel utilisateur dans le registre utilisateurs.xlsx

    # informations d'accès
    messageTitre = "Menu-Création d'un nouvel utilisateur"
    messageContenu = biblio1.message(messageTitre, listMessages)
    biblio1.annonce(messageTitre, messageContenu)

def utilisateurEditer():
    messageTitre = "Menu - Editer les données d'un utilisateur"
    messageContenu = biblio1.message(messageTitre, listMessages)
    biblio1.annonce(messageTitre, messageContenu, aspect=100)

def utilisateurSupprimer():
    # Saisie nom d'utilisateur

    # formation du nom correspondant pour le fichier

    # recherche du fichier

    # demande de confirmation du fichier trouvé

    # suppression du fichier

    # information fichier supprimé
    messageTitre = "Suppression d'un fichier utilisateur..."
    messageContenu = ""
    messageContenu += "Le fichier de l'utilisateur confirmé" + "\n"
    messageContenu += "a été supprimé." + "\n"
    biblio1.annonce(messageTitre, messageContenu)

def utilisateurStatistiques():
    messageTitre = "Menu - Utilisateur statistiques"
    messageContenu = biblio1.message(messageTitre, listMessages)
    biblio1.annonce(messageTitre, messageContenu)


def utilisateurPartager():
    messageTitre = "Menu - Utilisateur partager"
    messageContenu = biblio1.message(messageTitre, listMessages)
    biblio1.annonce(messageTitre, messageContenu)


#-----------------------

def fichiersCreerLecon():
    messageTitre = "Menu - Création fichier de lecon"
    messageContenu = biblio1.message(messageTitre, listMessages)
    biblio1.annonce(messageTitre, messageContenu)


def fichiersOuvrirLecon():
    messageTitre = "Menu - Ouvrir lecon"
    messageContenu = biblio1.message(messageTitre, listMessages)
    biblio1.annonce(messageTitre, messageContenu)


def fichiersSupprimerLecon():
    messageTitre = "Menu - Supprimer une lecon"
    messageContenu = biblio1.message(messageTitre, listMessages)
    biblio1.annonce(messageTitre, messageContenu)


def fichiersPartagerLecon():
    messageTitre = "Menu - Partager une lecon"
    messageContenu = biblio1.message(messageTitre, listMessages)
    biblio1.annonce(messageTitre, messageContenu)


#-------------

def laboratoireSelectionnerLecon():
    print("Sélection Leçons de l'utilisateur")

    
    ##################################################################

def laboratoireQuestionsReponsesCourtes():
    messageTitre = "Questions réponses courtes..."
    messageContenu = ""
    messageContenu += "En cours de développement..."
    biblio1.annonce(messageTitre, messageContenu)

def laboratoireQuestionsChoixMultiples():
    messageTitre = "Questions à choix multiples..."
    messageContenu = ""
    messageContenu += "En cours de développement..."
    biblio1.annonce(messageTitre, messageContenu)
    
def laboraoireFermerLecon():
    print("Fermeture leçon en cours")


#-------------

def optionsPreferences():
    messageTitre = "Menu - Options préférences"
    messageContenu = biblio1.message(messageTitre, listMessages)
    biblio1.annonce(messageTitre, messageContenu, couleur="#b2744b")

def optionsAide():
    messageTitre = "Aide..."
    messageContenu = ""
    messageContenu += "En cours de développement...                         "
    biblio1.annonce(messageTitre, messageContenu, aspect=300, couleur="#b2744b")

def optionsAProposDe():
    messageTitre = "Menu - A propos de"
    messageContenu = biblio1.message(messageTitre, listMessages)
    biblio1.annonce(messageTitre, messageContenu, aspect=100, couleur="#b2744b")



####################### Programme principal ################################







############### Configuration des structures de la barre de menu #############
# Instanciation d'un objet Menu appelé menu
# La fenêtre parent est la fenêtre window
menu = tkinter.Menu(window)

menu["foreground"] = "#cce4ff"

########## Sous-menu Utilisateur ##############
# Instanciation d'un sous-menu de menu appelé new_item
menu_utilisateur = tkinter.Menu(menu, tearoff=0, font = ("", 10))

# Configuration du sous-menu
menu_utilisateur.add_command(label="Sélectionner", command=utilisateurSelectionner)
menu_utilisateur.add_command(label="Créer", command=utilisateurCreer)
menu_utilisateur.add_command(label="Editer", command=utilisateurEditer)
menu_utilisateur.add_command(label="Supprimer", command=utilisateurSupprimer)
menu_utilisateur.add_command(label="Statistiques", command=utilisateurStatistiques)
menu_utilisateur.add_command(label="Partager", command=utilisateurPartager)

# Assignation du sous-menu en cascade à menu
menu.add_cascade(label='Utilisateur', menu=menu_utilisateur)


########## Sous-menu Fichiers ##############
# Instanciation d'un sous-menu de menu appelé new_item
menu_fichier = tkinter.Menu(menu, tearoff=0, font = ("", 10))

# Configuration du sous-menu
menu_fichier.add_command(label="Créer", command=fichiersCreerLecon)
menu_fichier.add_command(label="Ouvrir", command=fichiersOuvrirLecon)
menu_fichier.add_command(label="Supprimer", command=fichiersSupprimerLecon)
menu_fichier.add_command(label="Partager", command=fichiersPartagerLecon)

# Assignation du sous-menu en cascade à menu
menu.add_cascade(label="Leçons", menu=menu_fichier)


########## Sous-menu Laboratoire ##############
# Instanciation d'un sous-menu de menu appelé new_item
menu_laboratoire = tkinter.Menu(menu, tearoff=0, font = ("", 10))

# Configuration du sous-menu
menu_laboratoire.add_command(label="Sélectionner lecon", command=laboratoireSelectionnerLecon)
menu_laboratoire.add_command(label="Questions-Réponses courtes", command=laboratoireQuestionsReponsesCourtes)
menu_laboratoire.add_command(label="Questions-Réponses choix multiples", command=laboratoireQuestionsChoixMultiples)
menu_laboratoire.add_command(label="Quitter lecon", command=laboraoireFermerLecon)

# Assignation du sous-menu en cascade à menu
menu.add_cascade(label='Laboratoire', menu=menu_laboratoire)


########## Sous-menu Options ##############
# Instanciation d'un sous-menu de menu appelé new_item
menu_Options = tkinter.Menu(menu, tearoff=0, font = ("", 10))

# Configuration du sous-menu
menu_Options.add_command(label="Préférences", command=optionsPreferences)
menu_Options.add_command(label="Aide", command=optionsAide)
menu_Options.add_command(label="A propos de", command=optionsAProposDe)

# Assignation du sous-menu en cascade à menu
menu.add_cascade(label='Options', menu=menu_Options)

############# Quitter #################
menu.add_command(label="Quitter", command = window.destroy)

# Assignation de menu à window en barre de menu
window.config(menu=menu)

#####################################################################
###################### Mise en place des frames #####################
#####################################################################

# Entête
textTitre = "Memolab 21 a"
bgFrameColor = "#f29f66"
fgFrameColor = "black"
sizeLabelWidget = 12
titre = tkinter.Label(text = textTitre, font=("", 12))
frameEntete = tkinter.LabelFrame(window,text=textTitre, width = 1000, height = 100)
frameEntete.configure(bg=bgFrameColor, fg=fgFrameColor)
frameEntete.grid(row=0, column=0, columnspan=3)
frameEntete.grid_propagate(0)

# 
textTitre = "Niveau :"
titre = tkinter.Label(text = textTitre, font=("", 12))
frameNiveau = tkinter.LabelFrame(window,labelwidget=titre, width = 200, height = 400)
frameNiveau.configure(bg=bgFrameColor, fg=fgFrameColor)
frameNiveau.grid(row=1, column=0)
frameNiveau.grid_propagate(0)

textTitre = "Dialogues :"
titre = tkinter.Label(text = textTitre, font=("", 12))
FrameDialogue = tkinter.LabelFrame(window,labelwidget=titre, width = 600, height = 400)
FrameDialogue.grid(row=1, column=1)
FrameDialogue.grid_propagate(0)

textTitre = "Mode :"
titre = tkinter.Label(text = textTitre, font=("", 12))
frameMode = tkinter.LabelFrame(window,labelwidget=titre, width = 200, height = 400)
frameMode.configure(bg=bgFrameColor, fg=fgFrameColor)
frameMode.grid(row=1, column=2)
frameMode.grid_propagate(0)

textTitre = "Etat leçon en cours :"
titre = tkinter.Label(text = textTitre, font=("", 12))
frameEtat = tkinter.LabelFrame(window,labelwidget=titre, width = 1000, height = 100)
frameEtat.configure(bg=bgFrameColor, fg=fgFrameColor)
frameEtat.grid(row=2, column=0, columnspan=3)
frameEtat.grid_propagate(0)

# bouclage de la fenêtre window
window.mainloop()




