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
    
    # Variables de classe accessibles de tous les objets de cette classe
    imprimeOK = None

    # Constructeur recevant en paramètre paraGen
    def __init__(self,paraGen):                # Constructeur
        # ceci est exécuté à l'instanciation d'une leçon (style autoexec)
        self.paraGen = paraGen
        ClassModule2.imprimeOK = paraGen["imprimeOK"]

        # ------------------------------------------
        # Instanciation d'un objet biblio3 basé sur module3
        if ClassModule2.imprimeOK==True:
            print("Instanciation d'un objet de module3")
        
        import noyau_module3 as biblio3
        xBiblio3 = biblio3.ClassModule3(paraGen)        
        
        """ Code de mise au point
        
        # Appel d'une méthode de xBiblio3 (module3)
        # Ceci peut être fait de partout dans la classe
        quittance3 = xBiblio3.imprimeBonjour()
        if ClassModule2.imprimeOK==True:
            print(quittance3)

        if ClassModule2.imprimeOK==True:
            print("De module2 : Instanciation d'un objet ClassModule2")
        """ # --------------------------------------------        
    def imprimeHelloWorld(self):
        if ClassModule2.imprimeOK==True:    # exemple accès d'un paramètre
            print("De module2 : Hello World !")    # depuis cette classe
            return "C'est fait !"
        else:
            return "Ce n'est pas fait car imprimeOK = False !"
        