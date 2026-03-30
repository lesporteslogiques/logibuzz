import pygame
from zonetexte import ZoneTexte

class VueCreation:
    def __init__(self, controleur):
        self.controleur = controleur
        self.champs = []
        y = 50

        champ = ZoneTexte(
            50,
            y,
            self.controleur.ecran.get_width() * 0.4,
            self.controleur.ecran.get_height() * 0.15,
            140
        )
        self.champs.append(champ)
        y += (self.controleur.ecran.get_height() * 0.15) + 60

        for i in range(1,5):
            champ = ZoneTexte(
                50,
                y,
                self.controleur.ecran.get_width() * 0.35,
                self.controleur.ecran.get_height() * 0.1,
                30
            )
            self.champs.append(champ)
            y += (self.controleur.ecran.get_height() * 0.1) + 40
        

    def bouclePrincipale(self, largeur, hauteur, events):
        self.controleur.ecran.fill("black")
        for i in range(0,5):
            self.champs[i].evenement(events, 20)
            self.champs[i].affichage(self.controleur.ecran)
        
        touche = pygame.key.get_pressed()
        if touche[pygame.K_ESCAPE]:
            print("Fin de la création, retour au menu")
            self.controleur.setVue(0, self.controleur)