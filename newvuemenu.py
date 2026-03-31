import pygame, annexe
from indicjoueur import IndicJoueur
from textemenu import TexteMenu

class VueMenu:
    def __init__(self, controleur):
        self.controleur = controleur
        self.controleur.ecran.fill("black")
        print("Menu principal")
        self.modes = [
            TexteMenu(self.controleur.ecran, 0.5, 0.35, "Quizz", 24, pygame.K_1, 1),
            TexteMenu(self.controleur.ecran, 0.5, 0.45, "Vrai ou Faux", 24, pygame.K_2, 2),
            TexteMenu(self.controleur.ecran, 0.5, 0.55, "Track & Buzz", 24, pygame.K_3, 3),
            # TexteMenu(self.controleur.ecran, 0.5, 0.65, "?", 24, pygame.K_4, 4),
            TexteMenu(self.controleur.ecran, 0.5, 0.75, "Quitter", 24, pygame.K_5, 5)
        ]
        self.indicateur = [
            IndicJoueur(1, self.controleur.ecran, 0.2, 0.7),
            IndicJoueur(2, self.controleur.ecran, 0.4, 0.7),
            IndicJoueur(3, self.controleur.ecran, 0.6, 0.7),
            IndicJoueur(4, self.controleur.ecran, 0.8, 0.7),
        ]
        self.choix = 0
        self.nbJoueurs = 0
        self.fondEcran = pygame.image.load("placeholder-fond.png")
        
        

    
    def resetCouleursModes(self):
        for i in range(0, len(self.modes)):
            self.modes[i].setCouleur("white")


    def bouclePrincipale(self, largeur, hauteur, events):
        self.controleur.ecran.fill("black")
        self.controleur.ecran.blit(self.fondEcran, (0,0))
        annexe.texteStatique(self.controleur.ecran, "LogiBuzz", 44, "white", self.controleur.ecran.get_width() * 0.5, self.controleur.ecran.get_height() * 0.2)
        for i in range(0, len(self.modes)):
            self.modes[i].majTexte()

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
                        if buzzer.get_button(0+(5*i)) and not self.indicateur[i].getBuzzer():
                            self.indicateur[i].setBuzzer(True)
                            self.indicateur[i].setValider(not self.indicateur[i].getValider())
                            if self.indicateur[i].getValider():
                                self.indicateur[i].setCouleurCercleJoueur()
                                self.indicateur[i].setTexte("J" + str(self.indicateur[i].getNumero()))
                            else:
                                self.indicateur[i].setCouleurCercle("black")
                                self.indicateur[i].setTexte("")
                        if not buzzer.get_button(0+(5*i)) and self.indicateur[i].getBuzzer():
                            self.indicateur[i].setBuzzer(False)
                        self.indicateur[i].majCercle()
                        self.indicateur[i].majTexte(0, 40)

                        bAvatSuiv = buzzer.get_button(4 + (5*i))
                        bAvatPrec = buzzer.get_button(3 + (5*i))

                        if self.indicateur[i].getValider():
                            # Avatar suivant
                            if bAvatSuiv and not self.indicateur[i].getAvatarSuiv():
                                self.indicateur[i].setAvatarSuiv(True)
                                self.indicateur[i].changerAvatar(+1)
                            if not bAvatSuiv and self.indicateur[i].getAvatarSuiv():
                                self.indicateur[i].setAvatarSuiv(False)
                            # Avatar précédent
                            if bAvatPrec and not self.indicateur[i].getAvatarPrec():
                                self.indicateur[i].setAvatarPrec(True)
                                self.indicateur[i].changerAvatar(+1)
                            if not bAvatPrec and self.indicateur[i].getAvatarPrec():
                                self.indicateur[i].setAvatarPrec(False)
                            # MaJ de l'avatar
                            self.indicateur[i].majAvatar()

                    decompte -= timer.tick(60) / 1000
                    pygame.display.flip()
                    # Fin de la boucle
                numero = []
                for i in range(0,4):
                    if self.indicateur[i].getValider():
                        numero.append(self.indicateur[i].getNumero())
                        # Il faudra adapter les autres vues pour prendre en compte le numéro des joueurs présents

                        
                match self.choix:
                    case 1:
                        self.modes[0].changerVue(self.controleur, numero)
                    case 2:
                        self.modes[1].changerVue(self.controleur, numero)
                    case 3:
                        self.modes[2].changerVue(self.controleur, numero)
        