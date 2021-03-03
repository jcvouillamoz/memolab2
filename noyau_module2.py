# -*- coding: utf-8 -*-
""" Considérations techniques
Created on Sun Feb 28 21:14:07 2021
Noyau - Module 2
Au service de noyau seulement
fait appel aux services de biblio3
Ce module présente le partage de données du main vers module 2
via paraGen passé en paramètre au constructeur de classe
et les données générée dans ce module et restituées au main par le 
retour de méthode à l'appelant
@author: JCV
"""
class ClassModule2():
    
    # ressources requises
    import tkinter.filedialog as fd
    import tkinter
    import noyau_module1 as biblio1      
    
    # Variables de classe accessibles de tous les objets de cette classe
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

          


# ------------------------------------------
        # Instanciation d'un objet biblio3 basé sur module3
        # if ClassModule2.imprimeOK==True:
        #     print("Instanciation d'un objet de module3")
        
        # import noyau_module3 as biblio3
        # xBiblio3 = biblio3.ClassModule3(paraGen)        
        
    def selectionUtilisateur(self):
        # Répertoire hôte du registre des utilisateurs
        cheminUtilisateurs = ClassModule2.paraGen["cheminUtilisateurs"]
        fenTemp = self.tkinter.Tk()
        f_utilisateurEnCours = self.fd.askopenfilename(parent=fenTemp,
                                            title="Selection leçon en cours...",
                                            initialdir=cheminUtilisateurs,
                                            defaultextension=".xls",
                                            multiple=False)
        fenTemp.destroy()
        # Extraction nomDeFIchier
        f_utilisateurEnCours = ClassModule2.biblio1.extraitNomFichier(f_utilisateurEnCours)
        
        print(f_utilisateurEnCours)