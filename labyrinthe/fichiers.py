import os
repcour =os.getcwd()

#Création de fichier

def niveau_text(matrice,nom):
    os.chdir(repcour+"/Niveaux")
    niveau=open(nom,'w')
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            niveau.write(str(matrice[i][j]))
        niveau.write('\n')
    niveau.close()
    os.chdir(repcour)

#Ouverture

def niveau_matrice(texte):
    os.chdir(repcour+"/Niveaux")
    niveau=open(texte,'r')
    matrice = []
    for ligne in niveau:
        ligne_niveau=[]
        for valeur in ligne:
            if valeur!='\n':
                ligne_niveau.append(int(valeur))
        matrice.append(ligne_niveau)
    niveau.close()
    os.chdir(repcour)
    return (matrice)
