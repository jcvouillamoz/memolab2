# -*- coding: utf-8 -*-
"""
Fichier Noyau du projet

Programme principal bootstrap du projet

Fait appel aux services de module 2 et module 3 (et module n)
chaque module n peut faire appel aux services du module n + ...
seulement.

Le module 1 est spécialement attaché au main et ne contient que
quelques fonctions d'initialisation dont le chargement des
paramètres généraux du fichier excel param_generaux.xlsx

jcv-210228
"""
#%% Importation des paramètres généraux issus du fichier
#   params_generaux.xlsx situé sur le même dossier que ce script et
#   sa bibliothèque memolab_biblio_1
import noyau_module1 as biblio1
nomFichierParametres = "params_generaux.xlsx"
paraGen = biblio1.chargeParametresGeneraux(nomFichierParametres)

# Instanciation de biblio2 pour avoir accès à toutes ses méthodes
# et attributs à portée de ce script (objet de portée de ce script)
import noyau_module2 as biblio2
xBiblio2 = biblio2.ClassModule2(paraGen)

# Instanciation de biblio3 pour avoir accès à toutes ses méthodes
# et attributs à portée de ce script (objet de portée de ce script)
import noyau_module3 as biblio3
xBiblio3 = biblio3.ClassModule3(paraGen)

# Assignation optionnelle de paramètres accessible dans ce script
imprimeOK = paraGen["imprimeOK"]
print("Main : imprimeOK =",imprimeOK )

# Impression optionnelle dans ce script
if imprimeOK==True:
    print("De noyau : Initialisation noyau")

# Exemple appel d'une méthode de module 2
DonneeRetournee = xBiblio2.imprimeHelloWorld()
if imprimeOK==True:
    print("De noyau :",DonneeRetournee)

# Exemple appel d'une méthode de module 3
DonneeRetournee = xBiblio3.imprimeBonjour()
if imprimeOK==True:
    print("De noyau :",DonneeRetournee)

