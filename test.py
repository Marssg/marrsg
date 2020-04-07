import os, sys, pickle
from mesClasses import *


ficheUtilisateur = open("utilisateurs.txt","r") #j'ouvre le fichier qui contient les noms des utilisateurs
listeUtilisateur = ficheUtilisateur.read()

print(listeUtilisateur) #check pour moi même

ficheUtilisateur = open("utilisateurs.txt","a") #j'ouvre le fichier en permettant l'ajout de texte

userName = input("please enter user name : ") #je demande à l'utilisateur de s'authentifier


#On vérifie si l'utilisateur existe. en fonction on envoie un message adapté
if userName in listeUtilisateur :
    userName = User()
    print("Rebonjour ",userName)
else :
    userName = User()
    print("Bienvenue ", userName)
    ficheUtilisateur.write("\n" + userName)
    ficheUtilisateur = open("utilisateurs.txt","r") #j'ouvre le fichier qui contient les noms des utilisateurs
    listeUtilisateur = ficheUtilisateur.read()
    print(listeUtilisateur)
   


ficheUtilisateur.close()
