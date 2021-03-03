# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 21:43:13 2021

Noyau - module 3

Au service de main et de module2

@author: JCV
"""
class ClassModule3():
    
    # Variables de classe accessibles de tous les objets de cette classe
    imprimeOK = None

    # Constructeur recevant en paramètre paraGen
    def __init__(self,paraGen):                # Constructeur
        # ceci est exécuté à l'instanciation d'une leçon (style autoexec)
        # Assignation de paraGen reçu en paramètre en propriété de méthode
        self.paraGen = paraGen
        ClassModule3.imprimeOK = paraGen["imprimeOK"]
        if ClassModule3.imprimeOK==True:
            print("De module3 : Instanciation d'un objet ClassModule2")
        
    def imprimeBonjour(self):
        if ClassModule3.imprimeOK==True:    # exemple accès d'un paramètre
            print("De module3 : Bonjour !")    # depuis cette classe
            return "C'est fait !"
        else:
            return "Ce n'est pas fait car imprimeOK = False !"
        
