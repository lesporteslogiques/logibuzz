import pygame

class IndicJoueur:
    def __init__(self, numero, ecran, x, y):
        self.ecran = ecran
        self.numero = numero
        self.buzzer = False
        self.pos = pygame.Vector2(ecran.get_width() * x, ecran.get_height() * y)
        self.police = pygame.font.SysFont('lucidasans', 28)
        self.texte = ""
        self.couleurTexte = "white"
        self.couleurCercle = "black"
        match self.numero:
            case 1:
                self.couleurJoueur = "blue"
            case 2:
                self.couleurJoueur = "orange"
            case 3:
                self.couleurJoueur = "green"
            case 4:
                self.couleurJoueur = "yellow"
        self.valider = False
        self.valeur = ""
        self.vecteurX = 0
        self.vecteurY = 0
        self.timer = pygame.time.Clock()
        self.listeAvatar = [
            pygame.image.load("placeholder-avatar1.webp"),
            pygame.image.load("placeholder-avatar2.webp"),
            pygame.image.load("placeholder-avatar3.webp"),
            pygame.image.load("placeholder-avatar4.webp")
        ]
        self.numAvatar = 0
        self.avatar = self.listeAvatar[self.numero - 1]
        self.avatarSuivant = False
        self.avatarPrecedent = False
    

    def getNumero(self):
        return self.numero


    def getValeur(self):
        return self.valeur


    def setValeur(self, valeur):
        self.valeur = valeur
    

    def getTexte(self):
        return self.texte
    

    def setTexte(self, texte):
        self.texte = texte


    def setCouleurTexte(self, couleur):
        self.couleurTexte = couleur
    

    def getCouleurCercle(self):
        return self.couleurCercle


    def setCouleurCercle(self, couleur):
        self.couleurCercle = couleur
    

    def setCouleurCercleJoueur(self):
        self.couleurCercle = self.couleurJoueur
    

    def getValider(self):
        return self.valider


    def setValider(self, valide):
        self.valider = valide
    

    def getBuzzer(self):
        return self.buzzer
    

    def setBuzzer(self, buzzer):
        self.buzzer = buzzer
    

    def majTexteGauche(self):
        texte = self.police.render(self.valeur, True, self.couleurTexte)
        largeur = self.pos.x - (texte.get_width() + 40)
        self.ecran.blit(texte, (largeur, self.pos.y))


    def majTexte(self, decalX: int = 0, decalY: int = 0):
        rendu = self.police.render(self.texte, True, self.couleurTexte)
        largeurTexte = self.pos.x - (rendu.get_width() // 2)
        self.ecran.blit(rendu, (largeurTexte + decalX, self.pos.y + decalY))


    def majCercle(self, decalX: int = 0, decalY: int = 0):
        pygame.draw.circle(self.ecran, self.couleurCercle, (self.pos.x + decalX, self.pos.y + decalY), 40)
    

    def getPosX(self):
        return self.pos.x


    def getPosY(self):
        return self.pos.y


    def ajoutInertie(self, inertX: int = 0, inertY: int = 0):
        self.vecteurX += inertX
        self.vecteurY += inertY


    def majPosition(self):
        delta = self.timer.tick(60) / 400
        self.vecteurX -= delta
        self.vecteurY -= delta
        if self.vecteurX < 0:
            self.vecteurX = 0
        if self.vecteurY < 0:
            self.vecteurY = 0

        self.pos.x += self.vecteurX
        self.pos.y += self.vecteurY
    

    def resetPosition(self, resetX, resetY):
        self.vecteurX = 0
        self.vecteurY = 0
        self.pos = pygame.Vector2(self.ecran.get_width() * resetX, self.ecran.get_height() * resetY)
    

    def getAvatar(self):
        return self.avatar
    

    def getNumAvatar(self):
        return self.numAvatar
    

    def setAvatar(self, avatarChoisi):
        self.avatar = self.listeAvatar[avatarChoisi]
    

    def changerAvatar(self, nvAvatar):
        self.numAvatar += nvAvatar
        if self.numAvatar >= len(self.listeAvatar):
            self.numAvatar = 0
        elif self.numAvatar < 0:
            self.numAvatar = len(self.listeAvatar) - 1
        self.avatar = self.listeAvatar[self.numAvatar]
    

    def getAvatarSuiv(self) -> bool:
        return self.avatarSuivant
    

    def getAvatarPrec(self) -> bool:
        return self.avatarPrecedent
    

    def setAvatarSuiv(self, valeur: bool):
        self.avatarSuivant = valeur
    

    def setAvatarPrec(self, valeur: bool):
        self.avatarPrecedent = valeur
    

    def majAvatar(self, avatX: int = 0, avatY: int = 0):
        centreX = self.pos.x - (self.avatar.get_width() // 2)
        centreY = self.pos.y - (self.avatar.get_height() // 2)
        self.ecran.blit(self.avatar, (centreX + avatX, centreY + avatY))