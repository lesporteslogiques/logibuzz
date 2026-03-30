import pygame, annexe
from indicjoueur import IndicJoueur

class Inertie:
    def __init__(self, controleur):
        self.controleur = controleur
        print("Inertie")
        annexe.delaiTemps(1)
        self.timer = pygame.time.Clock()
        self.controleur.ecran.fill("black")
        self.joueur = [
            IndicJoueur(1, self.controleur.ecran, 0.2, 0.5)
        ]
        self.pagaieG = 0
        self.axeX = 100
    

    def calculInertie(self):
        bouton = pygame.key.get_pressed()
        if bouton[pygame.K_f] and not self.joueur[0].getBuzzer():
            self.joueur[0].setBuzzer(True)
            self.pagaieG += 0.55
        if not bouton[pygame.K_f] and self.joueur[0].getBuzzer():
            self.joueur[0].setBuzzer(False)

        if bouton[pygame.K_q] and not self.joueur[1].getBuzzer():
            self.joueur[1].setBuzzer(True)
            self.pagaieD += 0.55
        if not bouton[pygame.K_q] and self.joueur[1].getBuzzer():
            self.joueur[1].setBuzzer(False)
        
        self.pagaieG -= self.timer.tick(60) / 500
        if self.pagaieG < 0:
            self.pagaieG = 0

    

    def majCanoe(self):
        self.axeX += self.pagaieG
        canoe = pygame.Rect(self.axeX, 360, 100, 50)
        pygame.draw.ellipse(self.controleur.ecran, "white", canoe)


    def bouclePrincipale(self, largeur, hauteur, events):
        self.controleur.ecran.fill("black")
        self.calculInertie()
        self.majCanoe()