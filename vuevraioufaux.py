import pygame, random, annexe, json
from indicjoueur import IndicJoueur

class VueVraiOuFaux:
    def __init__(self, controleur, phrases, vousEtesCombien):
        self.controleur = controleur
        self.phrases = phrases
        self.combienDeJ = len(vousEtesCombien)
        print("VueVraiOuFaux")

        self.timer = pygame.time.Clock()

        self.temps = 0
        self.couleurDecompte = "white"
        self.decompte = ""

        self.buzzer = pygame.joystick.Joystick(0)
        self.policePhrase = pygame.font.SysFont('lucidasans', 44)
        self.policeReponse = pygame.font.SysFont('lucidasans', 24)
        self.joueur = []
        for j in range(0, self.combienDeJ):
            self.joueur.append(
                IndicJoueur(vousEtesCombien[j], self.controleur.ecran, (1 / (self.combienDeJ + 1)) + ((1 / (self.combienDeJ + 1)) * j), 0.85)
            )
            self.joueur[j].setCouleurCercleJoueur()
        self.phrase = ""
        self.bonneReponse = ""
        

        self.controleur.ecran.fill("black")

        with open(self.phrases, "r", encoding="UTF-8") as fichier:
            self.listePhrase = json.load(fichier)
        print(f"Il y a {len(self.listePhrase)} phrases/citations.")

        delai = 1
        while self.temps < delai:
            self.temps += self.timer.tick(60) / 1000
        
        self.setPhrase()


    def delaiTemps(self, delai):
        temps = 0
        while temps < delai:
            temps += self.timer.tick(60) / 1000
    

    def majTimer(self):
        self.temps -= self.timer.tick(60) / 1000
        self.decompte = self.policeReponse.render(str(int(self.temps)), True, self.couleurDecompte)
        self.controleur.ecran.blit(self.decompte, (10,10))


    def setPhrase(self):
        for i in range(0,self.combienDeJ):
            self.joueur[i].setCouleurTexte(pygame.Color("white"))
            self.joueur[i].setValider(False)
            self.joueur[i].setTexte("?")
        
        element = []
        for num in self.listePhrase:
            element.append(num)
        
        self.choix = random.choice(element)
        laPhrase = self.listePhrase[self.choix]["phrase"]
        if len(laPhrase) > 50:
            self.phrase = annexe.scinderTexte(laPhrase, 50)
        else:
            self.phrase = [laPhrase]

        self.bonneReponse = self.listePhrase[self.choix]["reponse"]
        self.temps = 10


    def choixReponse(self):
        aChoisi = True
        for k in range(0, self.combienDeJ):
            if not self.joueur[k].getValider():
                aChoisi = False

        for j in range(0, self.combienDeJ):
            for i in range(3,5):
                if self.buzzer.get_button(4 + (5 * (self.joueur[j].getNumero() - 1))) and not self.joueur[j].getValider():
                    self.joueur[j].setValider(True)
                    self.joueur[j].setValeur(True)
                    self.joueur[j].setTexte("Vrai")
                elif self.buzzer.get_button( 3 + (5 * (self.joueur[j].getNumero() - 1))) and not self.joueur[j].getValider():
                    self.joueur[j].setValider(True)
                    self.joueur[j].setValeur(False)
                    self.joueur[j].setTexte("Faux")
            self.joueur[j].majTexte(0,40)

        if aChoisi or self.temps <= 0:
            self.vraieReponse()
        
        touche = pygame.key.get_pressed()
        if touche[pygame.K_ESCAPE]:
            print("Retour au menu")
            self.controleur.setVue(0, self.controleur)


    def vraieReponse(self):
        if self.temps <= 0:
            self.couleurDecompte = "red"
        self.majTimer()
        pygame.display.flip()
        self.delaiTemps(1)
        if self.bonneReponse:
            reponse = self.policeReponse.render("Vrai", True, pygame.Color("white"))
        else:
            reponse = self.policeReponse.render("Faux", True, pygame.Color("white"))

        largeurReponse = (self.controleur.ecran.get_width() // 2) - (reponse.get_width() // 2)
        self.controleur.ecran.blit(reponse, (largeurReponse, self.controleur.ecran.get_height() * 0.5))
        for i in range(0,self.combienDeJ):
            if self.joueur[i].getValeur() == self.bonneReponse :
                self.joueur[i].setCouleurTexte(pygame.Color("green"))
            else:
                self.joueur[i].setCouleurTexte(pygame.Color("red"))
        
            self.joueur[i].majTexte(0,40)
        pygame.display.flip()
        self.delaiTemps(1.5)
        self.couleurDecompte = "white"
        self.setPhrase()



    def bouclePrincipale(self, largeur, hauteur, events):
        self.controleur.ecran.fill("black")
        for j in range(0, self.combienDeJ):
            self.joueur[j].majCercle()
        ligne = []
        taille = len(self.phrase)
        hauteurPhrase = (hauteur * 0.3) - ((taille - 1) * 44)
        for i in range(0,taille):
            rendu = self.policePhrase.render(self.phrase[i], True, "white")
            ligne.append(rendu)
            largeurPhrase = (largeur // 2) - (ligne[i].get_width() // 2)
            self.controleur.ecran.blit(ligne[i], (largeurPhrase, hauteurPhrase))
            hauteurPhrase += 44
        
        self.majTimer()
        self.choixReponse()