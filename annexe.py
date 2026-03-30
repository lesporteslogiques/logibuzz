import pygame

# Fonction pour scinder un texte en plusieurs lignes
# On considère que la fonction est appelée uniquement si nécessaire
def scinderTexte(texte, taille) -> str:
    # Séparation de chaque mot de la question
    mots = texte.split(" ")

    lignes = []
    ligneActuelle = ""

    # Pour chaque mot :
    for mot in mots:
        # Si la ligne actuelle avec le prochain mot ne dépasse pas la taille indiquée:
        if len(ligneActuelle + " " + mot) <= taille:
            # Si la ligne actuelle n'est pas vide:
            if ligneActuelle:
                ligneActuelle += " " + mot
            else:
                ligneActuelle = mot
        else:
            # On ajoute la ligne actuelle dans la liste lignes
            lignes.append(ligneActuelle)
            # puis on définit la ligne actuelle comme étant simplement le mot (qui n'était pas ajouté ici)
            ligneActuelle = mot
        
    # Dernière ligne
    if ligneActuelle:
        lignes.append(ligneActuelle)
    
    return lignes


# Fonction pour délayer le code (faire une pause avant de continuer)
def delaiTemps(delai):
    temps = 0
    timer = pygame.time.Clock()
    while temps < delai:
        temps += timer.tick(60) / 1000
    
# Affichage simple d'un ligne de texte à une position donnée au préalable, avec le choix de la taille
def texteStatique(affichage, contenu: str, grandeur: int, teinte, centreX, centreY):
    police = pygame.font.SysFont('lucidasans', grandeur)
    ligne = police.render(contenu, True, teinte)
    centreX -= ligne.get_width() // 2
    centreY -= ligne.get_height() // 2
    affichage.blit(ligne, (centreX, centreY))