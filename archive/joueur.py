class Joueur:
    nom = "Joueur"
    numero = 0
    buzzer = False
    bouton = 0

    def __init__(self, pseudo, num):
        self.nom = pseudo
        self.numero = num
    
    def getNom(self):
        return self.nom
    
    def setNom(self, nvNom):
        self.nom = nvNom
    
    def getNumero(self):
        return (self.numero)
    
    def setNumero(self, nvNumero):
        self.numero = nvNumero

    def getBuzzer(self):
        return self.buzzer
    
    def setBuzzer(self, etatBuzzer):
        self.buzzer = etatBuzzer

    def getBouton(self):
        return self.bouton
    
    def setBouton(self, nbBouton):
        self.bouton = nbBouton