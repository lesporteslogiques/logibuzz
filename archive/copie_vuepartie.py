import pygame
import os
import random
import annexe

class VuePartie:
    def __init__(self, controleur):
        self.controleur = controleur
        print("VuePartie")

        self.timer = pygame.time.Clock()
        delai = 1.5
        self.temps = 0
        self.decompte = ""

        self.buzzer = pygame.joystick.Joystick(0)
        self.policeQuestion = pygame.font.SysFont('lucidasans', 44)
        self.policeReponse = pygame.font.SysFont('lucidasans', 24)
        self.posJoueur = [
            pygame.Vector2(self.controleur.ecran.get_width() * 0.2, self.controleur.ecran.get_height() * 0.85),
            pygame.Vector2(self.controleur.ecran.get_width() * 0.4, self.controleur.ecran.get_height() * 0.85),
            pygame.Vector2(self.controleur.ecran.get_width() * 0.6, self.controleur.ecran.get_height() * 0.85),
            pygame.Vector2(self.controleur.ecran.get_width() * 0.8, self.controleur.ecran.get_height() * 0.85)
        ]
        self.chxJoueur = []
        self.valChoixJoueur = [False,False,False,False]
        self.ligne = ["","","","","",""]
        self.question = ["","","","","",""]
        self.ligneQuestion = []
        self.reponse = ["","","",""]
        self.bonneReponse = 0

        self.couleurQuestion = (255,255,255)
        self.couleurDecompte = (255,255,255)
        self.couleurReponse = []
        self.couleurJoueur = []
        for i in range(0,4):
            self.couleurReponse.append((255,255,255))
            self.couleurJoueur.append("black")
            self.chxJoueur.append(0)

        self.controleur.ecran.fill("black")
        self.chxQuestion = ""
        self.chxReponse = ["","","",""]

        while self.temps < delai:
            self.temps += self.timer.tick(60) / 1000

        self.setQuestion()
    

    def delaiTemps(self, delai):
        # Méthode réutilisable pour délayer certaines parties de code
        temps = 0
        while temps < delai:
            temps += self.timer.tick(60) / 1000
    

    def setCouleur(self, couleur):
        self.controleur.ecran.fill(couleur)
    

    def setQuestion(self):
        for i in range(0,4):
            self.couleurJoueur[i] = "black"
            self.valChoixJoueur[i] = False
            self.chxJoueur[i] = 0

        element = []
        for i in range(0, len(os.listdir('questions'))):
            element.append(i)
        print(f"Éléments : {element}")
        #choix = random.sample(element, 2)  <-- Version qui limite le nombre de quetions sélectionnées
        choix = random.choice(element)
        
        with open('questions/'+str(choix)+'.txt', 'r', encoding='UTF-8') as file:
            for i in range(0,6):
                self.ligne[i] = file.readline()
                if i == 0:
                    if len(self.ligne[0].rstrip()) > 50:
                        #self.ligneQuestion = self.ligne[0].split("\\n")
                        self.ligneQuestion = annexe.scinderTexte(self.ligne[0].rstrip(), 50)
                    else:
                        self.ligneQuestion = [self.ligne[0].rstrip()]
                print(self.ligne[i].rstrip())
                
            self.bonneReponse = int(self.ligne[5]) - 1
        print(f"Sélection de {choix}.txt")
        print(f"Bonne réponse : {self.bonneReponse}")
        self.temps = 20


    def selReponse(self):
        # Si tout le monde a validé ou si le temps est écoulé:
        if (self.valChoixJoueur[0] and self.valChoixJoueur[1] and self.valChoixJoueur[2] and self.valChoixJoueur[3]) or self.temps <= 0:
            self.vraieReponse()
        
        # Si le joueur 1 appuye sur le buzzer, qu'il n'a pa déjà validé et qu'il a fait un choix:
        if self.buzzer.get_button(0) and not self.valChoixJoueur[0] and self.chxJoueur[0] != 0:
            self.couleurJoueur[0] = "yellow"
            self.valChoixJoueur[0] = True
        # Si le joueur 1 appuye sur un des 4 boutons et qu'il n'a pas déjà validé:
        for i1 in range(1,5):
            if self.buzzer.get_button(i1) and not self.valChoixJoueur[0]:
                self.couleurJoueur[0] = "blue"
                match i1:
                    case 1:
                        self.chxJoueur[0] = 4
                    case 2:
                        self.chxJoueur[0] = 3
                    case 3:
                        self.chxJoueur[0] = 2
                    case 4:
                        self.chxJoueur[0] = 1
                        
        # Rebelote pour les autres joueurs
        if self.buzzer.get_button(5) and not self.valChoixJoueur[1] and self.chxJoueur[1] != 0:
            self.couleurJoueur[1] = "yellow"
            self.valChoixJoueur[1] = True
        for i2 in range(6,10):
            if self.buzzer.get_button(i2) and not self.valChoixJoueur[1]:
                self.couleurJoueur[1] = "blue"
                match i2:
                    case 6:
                        self.chxJoueur[1] = 4
                    case 7:
                        self.chxJoueur[1] = 3
                    case 8:
                        self.chxJoueur[1] = 2
                    case 9:
                        self.chxJoueur[1] = 1

        if self.buzzer.get_button(10) and not self.valChoixJoueur[2] and self.chxJoueur[2] != 0:
            self.couleurJoueur[2] = "yellow"
            self.valChoixJoueur[2] = True
        for i3 in range(11,15):
            if self.buzzer.get_button(i3) and not self.valChoixJoueur[2]:
                self.couleurJoueur[2] = "blue"
                match i3:
                    case 11:
                        self.chxJoueur[2] = 4
                    case 12:
                        self.chxJoueur[2] = 3
                    case 13:
                        self.chxJoueur[2] = 2
                    case 14:
                        self.chxJoueur[2] = 1

        if self.buzzer.get_button(15) and not self.valChoixJoueur[3] and self.chxJoueur[3] != 0:
            self.couleurJoueur[3] = "yellow"
            self.valChoixJoueur[3] = True
        for i4 in range(16,20):
            if self.buzzer.get_button(i4) and not self.valChoixJoueur[3]:
                self.couleurJoueur[3] = "blue"
                match i4:
                    case 16:
                        self.chxJoueur[3] = 4
                    case 17:
                        self.chxJoueur[3] = 3
                    case 18:
                        self.chxJoueur[3] = 2
                    case 19:
                        self.chxJoueur[3] = 1
            
        # Pour revenir au menu
        touche = pygame.key.get_pressed()
        if touche[pygame.K_ESCAPE]:
            print("Retour au menu...")
            self.controleur.setVue(0, self.controleur)


    def vraieReponse(self):
        if self.temps <= 0:
            self.couleurDecompte = "red"
        self.majTimer()
        pygame.display.flip()
        self.delaiTemps(1)
        self.couleurReponse[self.bonneReponse] = "green"
        self.majReponses()
        self.delaiTemps(1.5)
        pygame.display.flip()
        # Indication de la bonne réponse et des joueurs ayant correctement répondu
        for i in range(0,4):
            if self.chxJoueur[i] == (self.bonneReponse + 1):
                self.couleurJoueur[i] = "green"
            else:
                self.couleurJoueur[i] = "red"
            pygame.draw.circle(self.controleur.ecran, self.couleurJoueur[i], self.posJoueur[i], 40)

        pygame.display.flip()
        self.delaiTemps(1.5)
        self.couleurDecompte = "white"
        self.couleurReponse[self.bonneReponse] = "white"
        self.setQuestion()


    def majReponses(self):
        hauteurListe = self.hauteur * 0.5
        largeurReponse = [0, 0, 0, 0]

        for i in range(0,4):
            # Liste des réponses
            self.reponse[i] = self.policeReponse.render(self.ligne[i+1].rstrip(), True, self.couleurReponse[i])
            largeurReponse[i] = (self.largeur // 2) - (self.reponse[i].get_width() // 2)
            self.controleur.ecran.blit(self.reponse[i], (largeurReponse[i], hauteurListe))
            hauteurListe += self.reponse[i].get_height()
            # Indicateurs des joueurs
            pygame.draw.circle(self.controleur.ecran, self.couleurJoueur[i], self.posJoueur[i], 40)


    def majTimer(self):
        self.temps -= self.timer.tick(60)/1000
        self.decompte = self.policeReponse.render(str(int(self.temps)), True, self.couleurDecompte)
        self.controleur.ecran.blit(self.decompte, (10,10))


    def bouclePrincipale(self, largeur, hauteur, events):
        self.question = []
        iQ = len(self.ligneQuestion)
        
        self.setCouleur("black")
        self.largeur = largeur
        self.hauteur = hauteur
        hauteurQuestion = (self.hauteur * 0.3) - ((iQ - 1) * 44)
        for i in range(0, iQ):
            rendu = self.policeQuestion.render(self.ligneQuestion[i].rstrip(), True, self.couleurQuestion)
            self.question.append(rendu)
            largeurQuestion = (self.largeur // 2) - (self.question[i].get_width() // 2)
            self.controleur.ecran.blit(self.question[i], (largeurQuestion, hauteurQuestion))
            
            hauteurQuestion += 44

        self.majTimer()
        self.majReponses()
        self.selReponse()