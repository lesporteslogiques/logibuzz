import pygame, annexe, random
from indicjoueur import IndicJoueur

class TrackNBuzz:
    def __init__(self, controleur, nbJoueurs):
        self.controleur = controleur
        self.nbJoueurs = len(nbJoueurs)
        print("Vue Track & Buzz")
        # self.timer = pygame.time.Clock()
        self.temps = 0
        self.buzzer = pygame.joystick.Joystick(0)
        self.punchline = [
            "Trop rapide pour vous !",
            "Ça va, pas trop mal aux doigts ?",
            "C'est la maîtrise !",
            "Je ne sens plus ma main mais ça valait le coup !",
            "OUI !! J'ai la meilleure technique !",
            "J'aimerais remercier ma maman sans qui je n'existerais pas !",
            "victoire.mp3",
            "JE SUIS PILOTE",
            "Gagner c'est super",
            "J'ai même eu le temps d'aller aux toilettes !",
            "Plus rapide que Flash !"
        ]
        self.joueur = []
        for i in range(0,len(nbJoueurs)):
            self.joueur.append(IndicJoueur(nbJoueurs[i], self.controleur.ecran, 0.05, 0.25 + (0.20 * i)))
            self.joueur[i].setCouleurCercleJoueur()
        self.controleur.ecran.fill("black")
        annexe.delaiTemps(1)
    

    def majJoueurs(self):
        for i in range(0,self.nbJoueurs):
            self.joueur[i].majCercle(0,0)


    def quiGagne(self, gagnant: int, phrase: str):
        numJoueur = self.joueur[gagnant].getNumero()
        texteVictoire = "Le joueur " + str(numJoueur) + " gagne la course !"
        decompte = 7
        self.joueur[gagnant].setValeur(phrase)
        while decompte >= 1:
            self.controleur.ecran.fill("black")
            annexe.texteStatique(self.controleur.ecran, texteVictoire, 44, "white", (self.controleur.ecran.get_width() // 2), (self.controleur.ecran.get_height() * 0.1))
            self.majJoueurs()
            self.joueur[gagnant].majTexteGauche()
            if decompte <= 5:
                annexe.texteStatique(self.controleur.ecran, "On repart dans " + str(decompte) + " secondes...", 34, "white", (self.controleur.ecran.get_width() // 2), (self.controleur.ecran.get_height() * 0.18))
            pygame.display.flip()
            annexe.delaiTemps(1)
            decompte -= 1
        for i in range(0,self.nbJoueurs):
            self.joueur[i].resetPosition(0.05, 0.25 + (0.2 * i))


    def quiAvance(self):
        for i in range(0,self.nbJoueurs):
            if self.joueur[i].getPosX() >= (self.controleur.ecran.get_width() - 20):
                punch = random.choice(self.punchline)
                self.quiGagne(i, punch)
                break
            if self.buzzer.get_button(0+(5 * (self.joueur[i].getNumero() - 1))) and not self.joueur[i].getBuzzer():
                self.joueur[i].setBuzzer(True)
                self.joueur[i].ajoutInertie(0.45,0)
            if not self.buzzer.get_button(0+(5 * (self.joueur[i].getNumero() - 1))) and self.joueur[i].getBuzzer():
                self.joueur[i].setBuzzer(False)
            self.joueur[i].majPosition()
            self.joueur[i].majCercle(0,0)
        
        clavier = pygame.key.get_pressed()
        if clavier[pygame.K_ESCAPE]:
            print("Retour au menu, fini de martyriser les buzzers !")
            self.controleur.setVue(0, self.controleur)
    

    def bouclePrincipale(self, largeur, hauteur, events):
        self.controleur.ecran.fill("black")
        self.quiAvance()