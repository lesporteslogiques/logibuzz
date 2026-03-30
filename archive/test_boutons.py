import pygame
from joueur import *

pygame.init()
ecran = pygame.display.set_mode((1200,600))
horloge = pygame.time.Clock()
j1 = Joueur("Jean", 1)
enCours = True
delta = 0
temps = 0
boutonJ2 = False
boutonJ3 = False
boutonJ4 = False
reponse = 0

# Position du joueur au centre de la fenêtre
joueurPos = pygame.Vector2(ecran.get_width() / 2, ecran.get_height() / 2)

# Initialisation du module Joystick pour être sûr de la prise en charge des buzzers
pygame.joystick.init()
if pygame.joystick.get_init():
    print("Module Joystick initialisé")
print(f"Nombre de controleurs détectés : {str(pygame.joystick.get_count())}")


# Instanciation du buzzer
buzzer = pygame.joystick.Joystick(0)
# Le buzzer a (normalement) l'id 0
print(f"Buzzer : {buzzer.get_id()}")

# Boucle principale du programme
while enCours:
    # Sortie de la boucle principale du programme en cas de fermeture
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            enCours = False

    ecran.fill("purple")
    # Cercle dans l'écran à la position de joueurPos avec un rayon de 40
    pygame.draw.circle(ecran, "orange", joueurPos, 40)

# Test des boutons rouges de chaque buzzer, avec un drapeau pour ne faire le print qu'une seule fois

    # Bouton rouge Buzzer 1
    if buzzer.get_button(0):
        if not j1.getBuzzer():
            print(f"{j1.getNom()} a appuyé sur son buzzer")
            j1.setBuzzer(True)
        joueurPos.y -= 300 * delta
    else:
        if j1.getBuzzer():
            print(f"{j1.getNom()} a relâché son buzzer")
            j1.setBuzzer(False)
    # Bouton rouge Buzzer 2
    if buzzer.get_button(5):
        if not boutonJ2:
            print("Buzzer joueur 2 pressé")
            boutonJ2 = True
        joueurPos.y += 300 * delta
    else:
        if boutonJ2:
            print("Buzzer joueur 2 relâché")
            boutonJ2 = False
    # Bouton rouge Buzzer 3
    if buzzer.get_button(10):
        if not boutonJ3:
            print("Buzzer joueur 3 pressé")
            boutonJ3 = True
        joueurPos.x -= 300 * delta
    else:
        if boutonJ3:
            print("Buzzer joueur 3 relâché")
            boutonJ3 = False
    # Bouton rouge Buzzer 4
    if buzzer.get_button(15):
        if not boutonJ4:
            print("Buzzer joueur 4 pressé")
            boutonJ4 = True
        joueurPos.x += 300 * delta
    else:
        if boutonJ4:
            print("Buzzer joueur 4 relâché")
            boutonJ4 = False

    # Rendu à l'écran
    pygame.display.flip()

    # Limitation de la fréquence d'image à 60 par seconde
    delta = horloge.tick(60) / 1000
    temps += delta
    #print(temps)




# Fermeture du programme
pygame.quit()