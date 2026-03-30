import pygame, tkinter, json, sys
from controleur import *

if len(sys.argv) != 3:
    print("Erreur - veuillez indiquer les fichiers JSON")
    sys.exit()

fichierQuestions = str(sys.argv[1])
fichierPhrases = str(sys.argv[2])

# Résolution de l'écran
largeur = tkinter.Tk().winfo_screenwidth()
print(largeur)
hauteur = tkinter.Tk().winfo_screenheight()
print(hauteur)

delta = 0
enCours = True
# Initialisation de pygame
pygame.init()

ecran = pygame.display.set_mode((largeur,hauteur), pygame.FULLSCREEN)
horloge = pygame.time.Clock()
pygame.joystick.init()
pygame.font.init()
controleur = Controleur(ecran, fichierQuestions, fichierPhrases)
pygame.mouse.set_visible(False)

# Boucle principale
while controleur.enCours:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            controleur.enCours = False

    controleur.evenement(largeur, hauteur, events)

    pygame.display.flip()
    delta = horloge.tick(60) / 1000

pygame.quit()