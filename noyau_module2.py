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
            print(listUtilisateur, type(listUtilisateur))
            
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
            pos = len(listUtilisateurs)+1
            pseudo = xPseudo.get()
            prenomNom = xPrenomNom.get()
            nomFichier = ClassModule2.biblio1.creaNomFichier(prenomNom)
            if not __trouveUserFileInListUtilisateurs(nomFichier):
                listUtilisateurs.append([pos,pseudo,prenomNom,nomFichier])
                listEntete = ["numPos","pseudo","prenomNom","fichierUtilisateur"]
                print("updateNewUser : listEntete :", listEntete)
                listUtilisateurs3 = []
                listUtilisateurs3.append(listEntete)
                for element in listUtilisateurs:
                    listUtilisateurs3.append(element)
                print("updateNewUser : listUtilisateurs3 :", listUtilisateurs3)
                print("updateNewUser : len(listUtilisateurs3) :", len(listUtilisateurs3))
                listUtilisateur = listUtilisateurs3[len(listUtilisateurs3)-1]
                print("updateNewUser : listUtilisateur : ",listUtilisateur)
                ClassModule2.biblio1.list2Xlsx(listUtilisateurs3, 
                                                       nomFichierXlsx, 
                                                       ClassModule2.paraGen,
                                                       cheminFichierXlsx)
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
        
        self.__fenetreSelectionUtilisateur()
        
        listUtilisateur = pickle.load(open('tempUser.bin', 'rb'))
        print("Depuis fin de module2 : ", listUtilisateur)
        
        return listUtilisateur
        
        
        









# =============================== TESTS LOCAUX ========================

if __name__ == '__main__':
    pass
    