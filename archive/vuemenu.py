import pygame
from indicjoueur import IndicJoueur

class VueMenu:
    def __init__(self, controleur):
        self.controleur = controleur
        print("VueMenu !")
        self.buzzer = pygame.joystick.Joystick(0)
        self.joueur = IndicJoueur(1, self.controleur.ecran, 0, 0)
        # Définition de la poilce de caractère
        self.policeTitre = pygame.font.SysFont('lucidasans', 64, True)
        self.policeCorps = pygame.font.SysFont('lucidasans', 26)
        # Définition des couleurs
        BLANC = (255,255,255)
        self.couleurTitre = BLANC
        self.couleurCorps = []
        self.couleurCorps.append(BLANC)
        self.couleurCorps.append(BLANC)
        self.couleurCorps.append(BLANC)
        self.couleurCorps.append(BLANC)
        

    def setCouleur(self, couleur):
        self.controleur.ecran.fill(couleur)


    def checkBoutons(self):
        if self.buzzer.get_button(0):
            if not self.joueur.getBuzzer():
                print("Aïe")
                self.joueur.setBuzzer(True)
                match self.joueur.getValeur():
                    case 4:
                        self.controleur.setVue(1, self.controleur)
                    case 3:
                        self.controleur.setVue(2, self.controleur)
                    case 2:
                        self.controleur.setVue(3, self.controleur)
                    case 1:
                        self.controleur.setVue(4, self.controleur)
        else:
            if self.joueur.getBuzzer():
                self.joueur.setBuzzer(False)
        
        # Détermine le bouton sélectionné
        for i in range(1,5):
            if self.buzzer.get_button(i):
                for j in range(0,4):
                    self.couleurCorps[j] = (255,255,255)
                self.couleurCorps[i-1] = (255,120,128)
                self.joueur.setValeur(i)


    def bouclePrincipale(self, largeur, hauteur, events):
        # Titre
        self.titre = self.policeTitre.render('LogiBuzz', True, self.couleurTitre)
        largeurTitre = (largeur // 2) - (self.titre.get_width() // 2)
        self.controleur.ecran.blit(self.titre, (largeurTitre, hauteur * 0.2))
        
        # Bouton bleu
        self.boutonPartie = self.policeCorps.render('Quizz', False, self.couleurCorps[3])
        largeurBPartie = (largeur // 2) - (self.boutonPartie.get_width() // 2)
        hauteurListe = hauteur * 0.45
        self.controleur.ecran.blit(self.boutonPartie, (largeurBPartie, hauteurListe))
        hauteurListe += self.boutonPartie.get_height()
        # Bouton orange
        self.boutonCreation = self.policeCorps.render('Vrai ou Faux', False, self.couleurCorps[2])
        largeurBCreation = (largeur // 2) - (self.boutonCreation.get_width() // 2)
        self.controleur.ecran.blit(self.boutonCreation, (largeurBCreation, hauteurListe))
        hauteurListe += self.boutonCreation.get_height()
        # Bouton vert
        self.boutonOptions = self.policeCorps.render('Track & Buzz', False, self.couleurCorps[1])
        largeurBOptions = (largeur // 2) - (self.boutonOptions.get_width() // 2)
        self.controleur.ecran.blit(self.boutonOptions, (largeurBOptions, hauteurListe))
        hauteurListe += self.boutonCreation.get_height()
        # Bouton jaune
        self.boutonQuitter = self.policeCorps.render('Quitter', False, self.couleurCorps[0])
        largeurBQuitter = (largeur // 2) - (self.boutonQuitter.get_width() // 2)
        self.controleur.ecran.blit(self.boutonQuitter, (largeurBQuitter, hauteurListe))

        self.checkBoutons()