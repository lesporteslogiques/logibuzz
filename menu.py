import pygame, annexe
from indicjoueur import IndicJoueur
from textemenu import TexteMenu

class VueMenu:
    def __init__(self, controleur, numJoueur: list[int] = [], teteJoueur: list[int] = [], scoreJoueur: list[int] = [], finPartie: bool = False):
        self.controleur = controleur
        self.controleur.ecran.fill("black")
        print("Menu principal")
        self.finPartie = finPartie
        self.modes = [
            TexteMenu(self.controleur.ecran, 0.5, 0.25, "Quizz", 24, pygame.K_1, 1),
            TexteMenu(self.controleur.ecran, 0.5, 0.35, "Vrai ou Faux", 24, pygame.K_2, 2),
            TexteMenu(self.controleur.ecran, 0.5, 0.45, "Track & Buzz", 24, pygame.K_3, 3),
            # TexteMenu(self.controleur.ecran, 0.5, 0.65, "?", 24, pygame.K_4, 4),
            TexteMenu(self.controleur.ecran, 0.5, 0.55, "Quitter", 24, pygame.K_5, 5)
        ]
        
        self.ancienJoueur = []
        if self.finPartie:
            for i in range(0,len(numJoueur)):
                self.ancienJoueur.append(
                    IndicJoueur(
                        numJoueur[i],
                        self.controleur.ecran,
                        (1 / (len(numJoueur) + 1)) * (i + 1),
                        0.80,
                        teteJoueur[i],
                        scoreJoueur[i],
                        True
                    )
                )
                self.ancienJoueur[i].setCouleurCercleJoueur()

        self.choix = 0
        self.fondEcran = pygame.image.load("images/lb-fond.png")
        
        

    
    def resetCouleursModes(self):
        for i in range(0, len(self.modes)):
            self.modes[i].setCouleur("white")


    def bouclePrincipale(self, largeur, hauteur, events):
        self.controleur.ecran.fill("black")
        self.controleur.ecran.blit(self.fondEcran, (0,0))
        annexe.texteStatique(self.controleur.ecran, "LogiBuzz", 54, "white", largeur * 0.5, hauteur * 0.15)
        if self.finPartie:
            annexe.texteStatique(self.controleur.ecran, "Résultats :", 30, "yellow", largeur * 0.5, hauteur * 0.70)
        for i in range(0, len(self.modes)):
            self.modes[i].majTexte()

        for j in range(0,len(self.ancienJoueur)):
            self.ancienJoueur[j].majCercle()
            self.ancienJoueur[j].majAvatar()
            self.ancienJoueur[j].majScore(0,40)

        touche = pygame.key.get_pressed()
        if touche[pygame.K_1]:
            self.resetCouleursModes()
            self.modes[0].setCouleur("red")
            self.choix = 1
        elif touche[pygame.K_2]:
            self.resetCouleursModes()
            self.modes[1].setCouleur("red")
            self.choix = 2
        elif touche[pygame.K_3]:
            self.resetCouleursModes()
            self.modes[2].setCouleur("red")
            self.choix = 3
        elif touche[pygame.K_4]:
            self.resetCouleursModes()
            self.modes[3].setCouleur("red")
            self.choix = 4
        # elif touche[pygame.K_5]:
        #     self.resetCouleursModes()
        #     self.modes[4].setCouleur("red")
        #     self.choix = 5
        
        if touche[pygame.K_RETURN]:
            if self.choix == 4:
                self.modes[3].changerVue(self.controleur)
            # if self.choix == 5:
            #     self.modes[4].changerVue(self.controleur)
            if pygame.joystick.get_count() == 0 and self.choix != 4:
                annexe.texteStatique(self.controleur.ecran, "Buzzer non détecté, veuillez le brancher", 34, "orange", self.controleur.ecran.get_width() * 0.5, self.controleur.ecran.get_height() * 0.92)
                pygame.display.flip()
                annexe.delaiTemps(3)
            elif pygame.joystick.get_count() > 0 and self.choix != 4:
                buzzer = pygame.joystick.Joystick(0)
                timer = pygame.time.Clock()
                decompte = 8
                indicateur = [
                    IndicJoueur(1, self.controleur.ecran, 0.2, 0.82, 0),
                    IndicJoueur(2, self.controleur.ecran, 0.4, 0.82, 1),
                    IndicJoueur(3, self.controleur.ecran, 0.6, 0.82, 2),
                    IndicJoueur(4, self.controleur.ecran, 0.8, 0.82, 3),
                ]
                while decompte >= 0:
                    pygame.event.pump()
                    self.controleur.ecran.fill("black")
                    annexe.texteStatique(
                        self.controleur.ecran,
                        "Appuyez sur le buzzer si vous voulez jouer ! Départ dans " + str(int(decompte)) + "...",
                        34,
                        "purple",
                        self.controleur.ecran.get_width() // 2,
                        self.controleur.ecran.get_height() // 2
                        )
                    for i in range(0,4):
                        if buzzer.get_button(0+(5*i)) and not indicateur[i].getBuzzer():
                            indicateur[i].setBuzzer(True)
                            indicateur[i].setValider(not indicateur[i].getValider())
                            if indicateur[i].getValider():
                                indicateur[i].setCouleurCercleJoueur()
                                indicateur[i].setTexte("J" + str(indicateur[i].getNumero()))
                            else:
                                indicateur[i].setCouleurCercle("black")
                                indicateur[i].setTexte("")
                        if not buzzer.get_button(0+(5*i)) and indicateur[i].getBuzzer():
                            indicateur[i].setBuzzer(False)
                        indicateur[i].majCercle()
                        indicateur[i].majTexte(0, 40)

                        bAvatSuiv = buzzer.get_button(4 + (5*i))
                        bAvatPrec = buzzer.get_button(3 + (5*i))

                        if indicateur[i].getValider():
                            # Avatar suivant
                            if bAvatSuiv and not indicateur[i].getAvatarSuiv():
                                indicateur[i].setAvatarSuiv(True)
                                indicateur[i].changerAvatar(+1)
                            if not bAvatSuiv and indicateur[i].getAvatarSuiv():
                                indicateur[i].setAvatarSuiv(False)
                            # Avatar précédent
                            if bAvatPrec and not indicateur[i].getAvatarPrec():
                                indicateur[i].setAvatarPrec(True)
                                indicateur[i].changerAvatar(-1)
                            if not bAvatPrec and indicateur[i].getAvatarPrec():
                                indicateur[i].setAvatarPrec(False)
                            # MaJ de l'avatar
                            indicateur[i].majAvatar()

                    decompte -= timer.tick(60) / 1000
                    pygame.display.flip()
                    # Fin de la boucle
                numero = []
                numeroAvatar = []
                joueurPresent = False
                for i in range(0,4):
                    if indicateur[i].getValider():
                        numero.append(indicateur[i].getNumero())
                        numeroAvatar.append(indicateur[i].getNumAvatar())
                        joueurPresent = True
                
                if not joueurPresent:
                    self.choix = 0
                        
                match self.choix:
                    # case 0:
                    #     self.controleur.setVue(0, self.controleur)
                    case 1:
                        self.modes[0].changerVue(self.controleur, numero, numeroAvatar)
                    case 2:
                        self.modes[1].changerVue(self.controleur, numero, numeroAvatar)
                    case 3:
                        self.modes[2].changerVue(self.controleur, numero, numeroAvatar)
        