import pickle
import numpy as np
def choix():
    print('1) saisir les enseignants')
    print('2) ajouter un enseignant')
    print('3) modifier score enseignant')
    print('4) classer les enseignants')
    print('5) liste des acceptés')
    print('6) quitter')

def verif_name(name):
    j = 0
    v = True
    while j<len(name) and v == True:
        if not("A"<=name[j].upper()<="Z" or name[j] == " "):
            v = False
        else:
            j += 1
    return v
        
def saisir_E():
    E = dict()
    E["identifiant"]=input("identifiant enseignant : ")
    while len(E["identifiant"]) != 8 :
        E["identifiant"]=input("identifiant enseignant : ")

    E["nom_prenom"]=input("nom et prenom enseignant : ")
    while not(verif_name(E["nom_prenom"])):
        E["nom_prenom"]=input("nom et prenom enseignant : ")    
    E["score"]=int(input("score enseignant : "))
    while not(E["score"]>0):
        E["score"]=int(input("score enseignant : "))
    E["date"] = dict()
    E["date"]["j"] = int(input("jour : "))
    if not(1 <= E["date"]["j"] <= 31):
        E["date"]["j"] = int(input("jour : "))
            
    E["date"]["m"] = int(input("mois : "))
    if not(1 <= E["date"]["m"] <= 12):
        E["date"]["m"] = int(input("mois : "))
            
    E["date"]["a"] = int(input("annee : "))
    if not(E["date"]["a"]<=1985):
        E["date"]["a"] = int(input("annee : "))
    return E

def saisir(path):
    file = open(path,"wb")
    rep = True
    while rep:
        E = saisir_E()
        pickle.dump(E,file)
        x = input('continuer (y,n)')
        if(x.upper() == "N"):
            rep = False
    file.close()

def add(path):
    file = open(path,"ab")
    E = saisir_E()
    pickle.dump(E,file)
    file.close()

def rechercher(x):
    
    return index

def ceateTab():
    file = open("promotion.dat","rb")
    fin_fiche = False
    T = np.array([dict()]*1000)
    size = 0
    stop = False
    i=0
    while not(fin_fiche):
        while stop == False:
            try: 
                T[i] = pickle.load(file)
                size += 1
                i += 1     
            except:
                fin_fiche = True
                stop = True
    file.close
    return T,size

def mod(path):
    x = input("saisir identifiant enseignant : ")
    while len(x) != 8 :
        x = input("saisir identifiant enseignant : ")
    if( rechercher(x) != -1):
        modifier(x)


ceateTab()
cont = True    
while(cont):
    choix()
    x = int(input('choissier une option : '))
    while not(1<=x<=6):
        x = int(input('choissier une option : '))
    if (x == 1):
        saisir("promotion.dat")
    elif (x == 2):
        add("promotion.dat")
    elif (x == 3):
        mod("promotion.dat")
    elif (x == 6):
        print('end')
        cont = False
