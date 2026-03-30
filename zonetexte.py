import pygame
import annexe

class ZoneTexte:
    def __init__(self, x, y, largeur, hauteur, carMax):
        self.rect = pygame.Rect(x, y, largeur, hauteur)
        self.couleur = pygame.Color("gray")
        self.texte = ""
        self.nbLigneQuestion = 0
        self.police = pygame.font.SysFont('lucidasans', 24)
        self.actif = False
        self.carMax = carMax


    def evenement(self, events, tailleLigne):
        for event in events:
            # Clic dans le champ
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.actif = True
                    self.couleur = pygame.Color("white")
                else:
                    self.actif = False
                    self.couleur = pygame.Color("gray")
            
            if event.type == pygame.KEYDOWN and self.actif:
                if event.key == pygame.K_BACKSPACE:
                    self.texte = self.texte[:-1]
                elif len(self.texte) <= self.carMax:
                    self.texte += event.unicode
                
                
    def affichage(self, ecran):
        pygame.draw.rect(ecran, self.couleur, self.rect)
        rectTexte = self.police.render(self.texte, True, (0,0,0))
        ecran.blit(rectTexte, (self.rect.x + 5, self.rect.y + 5))