import pygame

class TexteMenu:
    def __init__(self, ecran, x, y, texteBase, taillePolice, touche, vue: int):
        self.ecran = ecran
        self.pos = pygame.Vector2(ecran.get_width() * x, ecran.get_height() * y)
        self.police = pygame.font.SysFont('lucidasans', taillePolice)
        self.couleur = pygame.Color("white")
        self.texte = texteBase
        self.touche = touche
        self.vue = vue


    def setCouleur(self, couleur):
        self.couleur = couleur
    

    def setTexte(self, texte):
        self.texte = texte
    

    def changerVue(self, controleur, combienDeJoueurs: int = 4, numAvatar: int = 0):
            controleur.setVue(self.vue, controleur, combienDeJoueurs, numAvatar)
    

    def majTexte(self):
        rendu = self.police.render(self.texte, True, self.couleur)
        largeur = self.pos.x - (rendu.get_width() // 2)
        self.ecran.blit(rendu, (largeur, self.pos.y))