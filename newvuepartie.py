import pygame, random, annexe, json
from indicjoueur import IndicJoueur

class VuePartie:
    def __init__(self, controleur, questions, nbJoueurs, avatarChoisi):
        self.controleur = controleur
        self.questions = questions
        print("Vue Partie, mk2")
        self.buzzer = pygame.joystick.Joystick(0)
        self.timer = pygame.time.Clock()
        delai = 1
        self.temps = 0
        self.decompte = ""
        self.policeQuestion = pygame.font.SysFont('lucidasans', 44)
        self.policeReponse = pygame.font.SysFont('lucidasans', 24)
        self.joueur = []
        for i in range(0,len(nbJoueurs)):
            self.joueur.append(
                IndicJoueur(nbJoueurs[i], self.controleur.ecran, (1 / (len(nbJoueurs) + 1)) + ((1/ (len(nbJoueurs) + 1)) * i), 0.85)
            )
            self.joueur[i].setCouleurCercleJoueur()
            self.joueur[i].setAvatar(avatarChoisi[i])
        # self.joueur = [
        #     IndicJoueur(1, self.controleur.ecran, 0.2, 0.85),
        #     IndicJoueur(2, self.controleur.ecran, 0.4, 0.85),
        #     IndicJoueur(3, self.controleur.ecran, 0.6, 0.85),
        #     IndicJoueur(4, self.controleur.ecran, 0.8, 0.85)
        # ]

        self.controleur.ecran.fill("black")

        with open(self.questions, "r", encoding="UTF-8") as fichier:
            self.listeQuestion = json.load(fichier)
        
        print(f"Il y a {len(self.listeQuestion)} questions.")
        while self.temps < delai:
            self.temps += self.timer.tick(60) / 1000
        
        self.setQuestion()
    

    def delaiTemps(self, delai):
        temps = 0
        while temps < delai:
            temps += self.timer.tick(60) / 1000
    

    def majTimer(self):
        self.temps -= self.timer.tick(60) / 1000
        if self.temps < 0:
            self.temps = 0.00
        self.decompte = self.policeReponse.render(str(int(self.temps)) + ":" + str(int((self.temps - int(self.temps)) * 1000)), True, self.couleurDecompte)
        self.controleur.ecran.blit(self.decompte, (10,10))
    

    def setQuestion(self):
        self.couleurDecompte = "white"
        self.couleurReponse = ["white", "white", "white", "white"]
        for i in range(0,len(self.joueur)):
            self.joueur[i].setCouleurCercleJoueur()
            self.joueur[i].setValider(False)
            self.joueur[i].setValeur(0)
            self.joueur[i].setCouleurTexte("white")
            self.joueur[i].setTexte("")
        
        element = []
        for num in self.listeQuestion:
            element.append(num)
        self.choix = random.choice(element)
        if len(self.listeQuestion[self.choix]["question"]) > 50:
            self.ligneQuestion = annexe.scinderTexte(self.listeQuestion[self.choix]["question"], 50)
        else:
            self.ligneQuestion = [self.listeQuestion[self.choix]["question"]]
        self.bonneReponse = self.listeQuestion[self.choix]["reponse"] - 1
        self.temps = 20
    

    def setReponse(self):
        toutValide = True
        for i in range(0, len(self.joueur)):
            for j in range(1,5):
                if self.buzzer.get_button(j + (5 * (self.joueur[i].getNumero() - 1))) and not self.joueur[i].getValider():
                    match j:
                        case 4:
                            self.joueur[i].setValeur(1)
                            self.joueur[i].setTexte("?")
                            self.joueur[i].setValider(True)
                        case 3:
                            self.joueur[i].setValeur(2)
                            self.joueur[i].setTexte("?")
                            self.joueur[i].setValider(True)
                        case 2:
                            if self.listeQuestion[self.choix]["3"] != None:
                                self.joueur[i].setValeur(3)
                                self.joueur[i].setTexte("?")
                                self.joueur[i].setValider(True)
                        case 1:
                            if self.listeQuestion[self.choix]["4"] != None:
                                self.joueur[i].setValeur(4)
                                self.joueur[i].setTexte("?")
                                self.joueur[i].setValider(True)
            self.joueur[i].majTexte(0,40)

        for i in range(0, len(self.joueur)):
            if not self.joueur[i].getValider():
                toutValide = False
        if toutValide or self.temps <= 0:
            self.vraieReponse()
        
        touche = pygame.key.get_pressed()
        if touche[pygame.K_ESCAPE]:
            print("Retour au menu !")
            self.controleur.setVue(0, self.controleur)
    

    def majReponse(self):
        hauteur = self.hauteur * 0.5
        for i in range(0,4):
            if self.listeQuestion[self.choix][str(i+1)] != None:
                reponse = self.policeReponse.render(self.listeQuestion[self.choix][str(i+1)], True, self.couleurReponse[i])
                largeur = (self.largeur // 2) - (reponse.get_width() // 2)
                self.controleur.ecran.blit(reponse, (largeur, hauteur))
                hauteur += reponse.get_height()
    

    def vraieReponse(self):
        if self.temps <= 0:
            self.couleurDecompte = "red"
        self.majTimer()
        pygame.display.flip()
        self.delaiTemps(1)
        self.couleurReponse[self.bonneReponse] = "green"
        self.majReponse()
        self.delaiTemps(1.5)
        pygame.display.flip()
        for i in range(0,len(self.joueur)):
            if self.joueur[i].getValeur() == (self.bonneReponse + 1):
                self.joueur[i].setValeur("Correct")
                self.joueur[i].setCouleurTexte("green")
            else:
                self.joueur[i].setValeur("Incorrect")
                self.joueur[i].setCouleurTexte("red")
            self.joueur[i].majTexte(0,40)
                
            # if self.joueur[i].getCouleurCercle() != "black":
            #     if self.joueur[i].getValeur == (self.bonneReponse + 1):
            #         self.joueur[i].setCouleurCercle("green")
            #     else:
            #         self.joueur[i].setCouleurCercle("red")
            #     self.joueur[i].majCercle()
        
        pygame.display.flip()
        self.delaiTemps(1.5)
        self.setQuestion()
    

    def bouclePrincipale(self, largeur, hauteur, events):
        self.controleur.ecran.fill("black")
        taille = len(self.ligneQuestion)
        self.largeur = largeur
        self.hauteur = hauteur
        hauteurQuestion = (self.hauteur * 0.3) - ((taille - 1) * 44)
        for i in range(0,taille):
            rendu = self.policeQuestion.render(self.ligneQuestion[i], True, "white")
            largeurQuestion = (self.largeur // 2) - (rendu.get_width() // 2)
            self.controleur.ecran.blit(rendu, (largeurQuestion, hauteurQuestion))
            hauteurQuestion += 44
        
        for j in range(0, len(self.joueur)):
            self.joueur[j].majCercle()
            self.joueur[j].majAvatar()
        self.majTimer()
        self.majReponse()
        self.setReponse()