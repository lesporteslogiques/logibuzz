#from vuemenu import VueMenu
from partie import VuePartie
from vraioufaux import VueVraiOuFaux
from tracknbuzz import TrackNBuzz
from menu import VueMenu
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

    def setVue(self, nvVue, controleur, nombreJoueurs: list[int] = [], quelAvatar: list[int] = [], quelScore: list[int] = [], partieFinie: bool = False):
        controleur.ecran.fill("black")
        match nvVue:
            case 0:
                self.vue = VueMenu(controleur, nombreJoueurs, quelAvatar, quelScore, partieFinie)
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