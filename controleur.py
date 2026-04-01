#from vuemenu import VueMenu
from newvuepartie import VuePartie
from vuecreation import VueCreation
from vuevraioufaux import VueVraiOuFaux
from tracknbuzz import TrackNBuzz
from newvuemenu import VueMenu
from inertie import Inertie
import pygame

class Controleur:
    def __init__(self, ecran, questions, phrases):
        self.ecran = ecran
        self.vue = VueMenu(self)
        self.enCours = True
        self.questions = questions
        self.phrases = phrases

    def getVue(self):
        return self.vue

    def setVue(self, nvVue, controleur, nombreJoueurs: int = 4, quelAvatar: int = 0):
        controleur.ecran.fill("black")
        match nvVue:
            case 0:
                self.vue = VueMenu(controleur)
            case 1:
                self.vue = VuePartie(controleur, self.questions, nombreJoueurs, quelAvatar)
            case 2:
                self.vue = VueVraiOuFaux(controleur, self.phrases, nombreJoueurs, quelAvatar)
            case 3:
                self.vue = TrackNBuzz(controleur, nombreJoueurs, quelAvatar)
            case 4:
                self.vue = Inertie(controleur)
            case 5:
                self.enCours = False

    def evenement(self, largeur, hauteur, events):
        self.vue.bouclePrincipale(largeur, hauteur, events)