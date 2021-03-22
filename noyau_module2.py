# -*- coding: utf-8 -*-
""" Considérations techniques
Created on Sun Feb 28 21:14:07 2021

Ce module concentre le traitement des utilisateurs

@author: JCV
"""
class ClassModule2():
    
    # ressources requises
    import tkinter.filedialog as fd
    import tkinter
    import noyau_module1 as biblio1      
    
    # Variables de classe 
    """ accessibles par self.<nomvariable> depuis la classe et 
                    par ClassModule2.<nomvariable> depuis ce module,
                    ceci grace au constructeur ci-dessous
    """
    imprimeOK = None
    paraGen = []
    listMessages = []

    # Constructeur recevant en paramètre paraGen
    def __init__(self,paraGen, listMessages):                # Constructeur
        # ceci est exécuté à l'instanciation d'une leçon (style autoexec)
        self.paraGen = paraGen
        ClassModule2.paraGen = self.paraGen
        
        self.listMessages = listMessages
        ClassModule2.listMessages = self.listMessages
        
        ClassModule2.imprimeOK = paraGen["imprimeOK"]
       
        # Annonce ClassModule2 active !
        # self.biblio1.annonce("Annonce:", "ClassModule2 active !")

class Scenario():
    def __init__(self):
        pass
    
    def CreationDicoScenario(self):
        dicoScenario = {}
        ###########################  UTILISATEURS
        
        # la list des utilisateur enregistrés possédant un fichier personnel
        dicoScenario["listUtilisateurs"] = None
        # list contenant les lecons en cours d'étude et leurs états
        dicoScenario["listUtilisateur"] = None
        # prénom nom de l'utilisateur
        dicoScenario["nomUtilisateur"] = None  
        # pseudo de l'utilisateur
        dicoScenario["pseudoUtilisateur"] = None  
        # nom complet du fichier personnel de l'utilisateur
        dicoScenario["nomFichierUtilisateur"] = None 
        
        ############################ LECONS
        
        # 1) Historiques
        # nom du fichier de la lecon en cours d'étude
        dicoScenario["nomFichierLecon"] = None 
        # nombre de questions de dito
        dicoScenario["nbQuestions"] = None 
        # mode correction dernier niveau
        dicoScenario["modeDerNiveau"] = None 
        # note obtenue sur 6 (rapport nbPremRepJustes / nbQuestions)
        dicoScenario["derNiveau"] = None 
        # Durée dernière session
        dicoScenario["derDuree"] = None 
        # durée cumulée de toutes les sessions de cette leçon
        dicoScenario["dureeCum"] = None 
        # Date de la dernière session
        dicoScenario["dateDerSession"] = None 
        # Vrai si toutes les questions dernière session ont été traitées
        dicoScenario["derSessionTerminee"] = None 
        
        # 2) Session en cours
        # date du jour
        dicoScenario["dateSessionEnCours"] = None 
        # durée depuis la première question posée
        dicoScenario["dureeSessionEnCours"] = None 
        # Flag d'indication si session terminée
        dicoScenario["SessionTerminee"] = None 
        # nombre de questions qu'il reste à poser
        dicoScenario["nbQuestionsRestantes"] = None 
        # Nombre de premières réponses justes
        dicoScenario["nbPremRepJustes"] = None 
        # Nombre total des réponses justes
        dicoScenario["nbRepJustes"] = None 
        # Nombre de réponses fausses
        dicoScenario["nbRepFausses"] = None 
        # mode correction A : au moins un mot contenu dans la réponses
        dicoScenario["auMoinsUnMotJuste"] = None 
        # mode correstion B : tous les mots contenus dans la réponse
        dicoScenario["tousLesMotsJustes"] = None 
        # mode correstion C : tous les mots dans le bon ordre
        dicoScenario["tousLesMotsEnBonOrdre"] = None 
        # mode correction D : copie exacte, nb espaces entre les mots non compris
        dicoScenario["copieExacte"] = None 
        # rapport du nb de premières réponses justes au nombre de questions de la leçon
        dicoScenario["noteExamen"] = None 
        # rapport du nombre de questions justes aux questions totales posées
        dicoScenario["noteTravail"] = None 

        return dicoScenario
        
          
class Utilisateur():
    def __init__(self):
        pass
        # self.fenetreSelectionUtilisateur()


    def __fenetreSelectionUtilisateur(self):
        
        # Chargement des utilisateurs existants
        cheminFichierXlsx = ClassModule2.paraGen["cheminUtilisateurs"]
        nomFichierXlsx = ClassModule2.paraGen["nomFichierUtilisateurs"]
        listUtilisateurs = []
        listUtilisateurs = ClassModule2.biblio1.xlsx2List(nomFichierXlsx, 
                                                          listUtilisateurs, 
                                                          ClassModule2.paraGen, 
                                                          cheminFichierXlsx)
        # Création liste des utilisateurs sans la ligne d'entête ni des lignes 
        # vides. C'est une "épuration".
        listUtilisateurs2 = []
        for ligne in listUtilisateurs:
            if ligne[0] != None and ligne[0] != "numPos":
                listUtilisateurs2.append(ligne)
        listUtilisateurs = listUtilisateurs2[:]
        # print(listUtilisateurs)
        
        # Formulaire d'identification de l'utilisateur
        fenetre = ClassModule2.tkinter.Tk()
        fenetre.title("Identification utilisateur")
        fenetre.configure(padx=20, pady=20)
        
        ############################## CONNEXION ##############################
        # Labelframe connexion
        labelFrameConnexion = ClassModule2.tkinter.LabelFrame(fenetre, text="Connexion : ")
        labelFrameConnexion.grid(row=0, column=0, sticky="sw")
        
        labelTitre = ClassModule2.tkinter.Label(labelFrameConnexion,
                                                text="Sélection de ton pseudo :",
                                                height=1)
        labelTitre.grid(row=0, column=0, columnspan=2, sticky="enw")
        
        labelPseudo = ClassModule2.tkinter.Label(labelFrameConnexion,
                                                 text="Pseudo : ")
        labelPseudo.grid(row=1, column = 0)

        listBoxUtilisateur = ClassModule2.tkinter.Listbox(labelFrameConnexion, 
                                                          height=len(listUtilisateurs))
        listBoxUtilisateur.select_set(0)
        for ligne in listUtilisateurs:
            listBoxUtilisateur.insert(ligne[0]-1,ligne[1])
        listBoxUtilisateur.grid(row=1, column=1)
        
        # fonction appelée avec le bouton Connect
        def updateLabel():
            indexSelection = listBoxUtilisateur.curselection()[0]
            listUtilisateur = listUtilisateurs[indexSelection]
            # print(listUtilisateur, type(listUtilisateur))
            # Sauvegardse dans un fichier binaire persistant de la ligne
            # de données de l'utilisateur sélectionné.
            import pickle
            pickle.dump(listUtilisateur, open('tempUser.bin', 'wb'))
            
            fenetre.destroy()
            return

        # bouton
        boutonConnect = ClassModule2.tkinter.Button(labelFrameConnexion, 
                                                    text="Connexion", 
                                                    command=updateLabel)
        boutonConnect.grid(row=2, column=0, columnspan=2, sticky="ew")
        
        ##################### NOUVEL UTILISATEUR #######################
        labelFrameNewUser = ClassModule2.tkinter.LabelFrame(fenetre, 
                                                              text="Nouvel utilisateur : ")
        labelFrameNewUser.grid(row=1, column=0, sticky="sw")
        
        xPseudo = ClassModule2.tkinter.StringVar()
        xPrenomNom = ClassModule2.tkinter.StringVar()
        
        labelPseudo = ClassModule2.tkinter.Label(labelFrameNewUser,text="Pseudo : ")
        labelPseudo.grid(row=0, column=0)
        entryPseudo = ClassModule2.tkinter.Entry(labelFrameNewUser, textvariable=xPseudo)
        entryPseudo.grid(row=0,column=1)
        
        labelPrenomNom = ClassModule2.tkinter.Label(labelFrameNewUser,text="Prénom Nom : ")
        labelPrenomNom.grid(row=1, column=0)
        entryPrenomNom = ClassModule2.tkinter.Entry(labelFrameNewUser, textvariable=xPrenomNom)
        entryPrenomNom.grid(row=1,column=1)
        
        def __trouveUserFileInListUtilisateurs(nomFichier):
            for ligne in listUtilisateurs:
                if ligne[3] == nomFichier:
                    return True
            return False                
        
        def updateNewUser():
            # initialisation des 4 champs de la liste Utilisateurs
            pos = len(listUtilisateurs)+1
            pseudo = xPseudo.get()
            prenomNom = xPrenomNom.get()
            nomFichier = ClassModule2.biblio1.creaNomFichier(prenomNom)
            # ajout nouvel utilisateur si son nom de fichier est nouveau
            if not __trouveUserFileInListUtilisateurs(nomFichier):
                # reconstitution de la list au format du fichier xlsx
                listEntete = ["numPos","pseudo","prenomNom","fichierUtilisateur"]
                listUtilisateurs.append([pos,pseudo,prenomNom,nomFichier])
                listUtilisateurs3 = []
                listUtilisateurs3.append(listEntete)
                for element in listUtilisateurs:
                    listUtilisateurs3.append(element)

                # mise à jour du fichier xlsx des utilisateurs
                ClassModule2.biblio1.list2Xlsx(listUtilisateurs3, 
                                                       nomFichierXlsx, 
                                                       ClassModule2.paraGen,
                                                       cheminFichierXlsx)
                # création liste des données de l'utilisateur sélectionné
                listUtilisateur = listUtilisateurs3[len(listUtilisateurs3)-1]
                
                # sauvegarde en fichier binaire pour la persistance de 
                # cette liste une fois supprimé l'objet fenetre
                import pickle
                pickle.dump(listUtilisateur, open('tempUser.bin', 'wb'))

                fenetre.destroy()
                return
        
        boutonEnregistre = ClassModule2.tkinter.Button(labelFrameNewUser, 
                                                    text="Connexion", 
                                                    command=updateNewUser)
        boutonEnregistre.grid(row=2, column=0, columnspan=2, sticky="ew")
        
        fenetre.mainloop()
        
        
    def fenetreSelectionUtilisateur(self):
        import os
        import pickle
        
        # exécution de la méthode de sélection / création d'utilisateur
        # qui va déposer dans un fichier binaire la liste des données
        # de l'utilisateur sélectionné.
        self.__fenetreSelectionUtilisateur()
        
        # récupération de la liste des données de l'utilisateur sélectionné
        listUtilisateur = []
        try:
            listUtilisateur = pickle.load(open('tempUser.bin', 'rb'))
            # print("Depuis fin de module2 : ", listUtilisateur)
            os.remove('tempUser.bin')
        except:
            pass
        
        return listUtilisateur
        
        ###############################
        
        """ %%%%%%%%%%%%%%%%%%%%%%% ref initiale fenêtre autonome %%%%%%%%%%%%%
        # Formulaire d'identification de l'utilisateur
        fenetre = ClassModule2.tkinter.Tk()
        fenetre.title("Identification utilisateur")
        fenetre.configure(padx=20, pady=20)
        
        ############################## CONNEXION ##############################
        # Labelframe connexion
        labelFrameConnexion = ClassModule2.tkinter.LabelFrame(fenetre, text="Connexion : ")
        labelFrameConnexion.grid(row=0, column=0, sticky="sw")
        
        labelTitre = ClassModule2.tkinter.Label(labelFrameConnexion,
                                                text="Sélection de ton pseudo :",
                                                height=1)
        labelTitre.grid(row=0, column=0, columnspan=2, sticky="enw")
        
        labelPseudo = ClassModule2.tkinter.Label(labelFrameConnexion,
                                                 text="Pseudo : ")
        labelPseudo.grid(row=1, column = 0)

        listBoxUtilisateur = ClassModule2.tkinter.Listbox(labelFrameConnexion, 
                                                          height=len(listUtilisateurs))
        listBoxUtilisateur.select_set(0)
        for ligne in listUtilisateurs:
            listBoxUtilisateur.insert(ligne[0]-1,ligne[1])
        listBoxUtilisateur.grid(row=1, column=1)
        
        # fonction appelée avec le bouton Connect
        def updateLabel():
            indexSelection = listBoxUtilisateur.curselection()[0]
            listUtilisateur = listUtilisateurs[indexSelection]
            # print(listUtilisateur, type(listUtilisateur))
            # Sauvegardse dans un fichier binaire persistant de la ligne
            # de données de l'utilisateur sélectionné.
            import pickle
            pickle.dump(listUtilisateur, open('tempUser.bin', 'wb'))
            
            fenetre.destroy()
            return

        # bouton
        boutonConnect = ClassModule2.tkinter.Button(labelFrameConnexion, 
                                                    text="Connexion", 
                                                    command=updateLabel)
        boutonConnect.grid(row=2, column=0, columnspan=2, sticky="ew")
        
        ##################### NOUVEL UTILISATEUR #######################
        labelFrameNewUser = ClassModule2.tkinter.LabelFrame(fenetre, 
                                                              text="Nouvel utilisateur : ")
        labelFrameNewUser.grid(row=1, column=0, sticky="sw")
        
        xPseudo = ClassModule2.tkinter.StringVar()
        xPrenomNom = ClassModule2.tkinter.StringVar()
        
        labelPseudo = ClassModule2.tkinter.Label(labelFrameNewUser,text="Pseudo : ")
        labelPseudo.grid(row=0, column=0)
        entryPseudo = ClassModule2.tkinter.Entry(labelFrameNewUser, textvariable=xPseudo)
        entryPseudo.grid(row=0,column=1)
        
        labelPrenomNom = ClassModule2.tkinter.Label(labelFrameNewUser,text="Prénom Nom : ")
        labelPrenomNom.grid(row=1, column=0)
        entryPrenomNom = ClassModule2.tkinter.Entry(labelFrameNewUser, textvariable=xPrenomNom)
        entryPrenomNom.grid(row=1,column=1)
        
        def __trouveUserFileInListUtilisateurs(nomFichier):
            for ligne in listUtilisateurs:
                if ligne[3] == nomFichier:
                    return True
            return False                
        
        def updateNewUser():
            # initialisation des 4 champs de la liste Utilisateurs
            pos = len(listUtilisateurs)+1
            pseudo = xPseudo.get()
            prenomNom = xPrenomNom.get()
            nomFichier = ClassModule2.biblio1.creaNomFichier(prenomNom)
            # ajout nouvel utilisateur si son nom de fichier est nouveau
            if not __trouveUserFileInListUtilisateurs(nomFichier):
                # reconstitution de la list au format du fichier xlsx
                listEntete = ["numPos","pseudo","prenomNom","fichierUtilisateur"]
                listUtilisateurs.append([pos,pseudo,prenomNom,nomFichier])
                listUtilisateurs3 = []
                listUtilisateurs3.append(listEntete)
                for element in listUtilisateurs:
                    listUtilisateurs3.append(element)

                # mise à jour du fichier xlsx des utilisateurs
                ClassModule2.biblio1.list2Xlsx(listUtilisateurs3, 
                                                       nomFichierXlsx, 
                                                       ClassModule2.paraGen,
                                                       cheminFichierXlsx)
                # création liste des données de l'utilisateur sélectionné
                listUtilisateur = listUtilisateurs3[len(listUtilisateurs3)-1]
                
                # sauvegarde en fichier binaire pour la persistance de 
                # cette liste une fois supprimé l'objet fenetre
                import pickle
                pickle.dump(listUtilisateur, open('tempUser.bin', 'wb'))

                fenetre.destroy()
                return
        
        boutonEnregistre = ClassModule2.tkinter.Button(labelFrameNewUser, 
                                                    text="Connexion", 
                                                    command=updateNewUser)
        boutonEnregistre.grid(row=2, column=0, columnspan=2, sticky="ew")
        
        ###############################
        
        fenetre.mainloop()
        
       
        
        

        
    
    def fenetreSelectionUtilisateur(self):
        import os
        import pickle
        
        # exécution de la méthode de sélection / création d'utilisateur
        # qui va déposer dans un fichier binaire la liste des données
        # de l'utilisateur sélectionné.
        self.__fenetreSelectionUtilisateur()
        
        # récupération de la liste des données de l'utilisateur sélectionné
        listUtilisateur = []
        try:
            listUtilisateur = pickle.load(open('tempUser.bin', 'rb'))
            # print("Depuis fin de module2 : ", listUtilisateur)
            os.remove('tempUser.bin')
        except:
            pass
        
        return listUtilisateur
    
     """ ########## Fin référence
    
    
    
    
    def miseEnListFichierUtilisateur(self,nomFichierUtilisateur):
        """
        
        Parameters
        ----------
        nomFichierUtilisateur : str
            nom complet du fichier de l'utilisateur

        Returns
        -------
        listfichierUtilisateur

        """
        import os
        import shutil
        import time
        cheminRacine = ClassModule2.biblio1.ouSuisJe()
        print("cheminRacine=",cheminRacine)
        cheminFichierUtilisateur = ClassModule2.paraGen["cheminUtilisateurs"]
        print("cheminUtilisateur=", cheminFichierUtilisateur)
        print(nomFichierUtilisateur)
        aOuvrir = cheminRacine + cheminFichierUtilisateur + "/" + nomFichierUtilisateur
        print("aOuvrir=",aOuvrir)
        trouve = os.path.exists(aOuvrir)
        print("trouve=",trouve)
        if not trouve:
            # copie du fichier utilisateur_modele.xlsx vers aOuvrir
            source = cheminRacine + cheminFichierUtilisateur + "/utilisateur_modele.xlsx"
            cible = aOuvrir
            shutil.copy(source,cible)
            time.sleep(3)
        # mise en list du fichier trouvé
        nomFichierXlsx = nomFichierUtilisateur
        listXlsx = []
        listFichierUtilisateur = ClassModule2.biblio1.xlsx2List(nomFichierXlsx, 
                                                                listXlsx,
                                                                ClassModule2.paraGen,
                                                                cheminRelXlsx=cheminFichierUtilisateur)
        return listFichierUtilisateur
   
            
        
        
        









# =============================== TESTS LOCAUX ========================

if __name__ == '__main__':
    pass
    