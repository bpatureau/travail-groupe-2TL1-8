import pygame
from pygame.locals import *
import classes.Ant_hill as antHill
import classes.game as game
import classes.food as foodModule
import pygameUtils as py
import os
import running as run

pygame.init()

largeur_fenetre = 1280
hauteur_fenetre = 720
stat_font = py.pygame.font.SysFont("impact", 20)

screen = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

background = pygame.image.load("img/background.png").convert()

pygame.display.set_caption('Menu de sauvegarde de partie')

# Fonction pour afficher le menu des sauvegardes.
def afficher_menu(sauvegardes, debut_index):
    font = pygame.font.Font(None, 36)
    bouton_hauteur = 50
    boutons = []
    nb_max_boutons_affiches = 10

    rect_haut = font.render("^", True, (0, 0, 0)).get_rect(center=(largeur_fenetre // 2, bouton_hauteur // 2))
    rect_bas = font.render("v", True, (0, 0, 0)).get_rect(center=(largeur_fenetre // 2, (nb_max_boutons_affiches + 1) * bouton_hauteur))

    # Affichage des flèches vers le haut et vers le bas dans la liste des boutons
    boutons.append((font.render("^", True, (0, 0, 0)), rect_haut, "HAUT"))
    boutons.append((font.render("v", True, (0, 0, 0)), rect_bas, "BAS"))

    for i, nom_sauvegarde in enumerate(sauvegardes[debut_index:debut_index + nb_max_boutons_affiches], debut_index):
        texte = font.render(nom_sauvegarde, True, (0, 0, 0))
        rect = texte.get_rect(center=(largeur_fenetre // 2, (i - debut_index + 1) * bouton_hauteur))
        boutons.append((texte, rect, nom_sauvegarde))

    return boutons, rect_haut, rect_bas, nb_max_boutons_affiches

# Fonction principale pour gérer le menu des sauvegardes.
def menu_principal(sauvegardes):
    debut_index = 0
    running = True

    while running:
        screen.fill((0, 0, 0))

        screen.blit(background, (0, 0))


        boutons, rect_haut, rect_bas, nb_max_boutons_affiches = afficher_menu(sauvegardes, debut_index)


        for texte, rect, _ in boutons:
            screen.blit(texte, rect)


        for event in pygame.event.get():
            if event.type == QUIT:
                running = False  # Quitte si fermeture de fenêtre.
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()  # Obtient la position actuelle de la souris.
                    # Vérifie si les flèches haut et bas sont cliquées pour faire défiler le menu.
                    if rect_haut.collidepoint(mouse_pos) and debut_index > 0:
                        debut_index -= 1
                    elif rect_bas.collidepoint(mouse_pos) and debut_index + nb_max_boutons_affiches < len(sauvegardes):
                        debut_index += 1

                    # Vérifie si un bouton de sauvegarde est cliqué
                    for texte, rect, nom_sauvegarde in boutons[2:]:
                        if rect.collidepoint(mouse_pos):
                            lauch(nom_sauvegarde)

        pygame.display.flip()

    pygame.quit()


def lauch(nom_sauvegarde):
    py.pygame.display.set_caption('SIMULATION')

    save_button = py.Button((0, 160, 0), 1150, 650, 100, 50, 'Save')  # bouton save

    """définition des variables initiales """
    colony = antHill.Ant_hill()
    colony.load(f"{chemin()}{nom_sauvegarde}")

    print(colony.day)
    print(colony.food)
    print(colony.ant_list)

    day = colony.day
    ant_weight = 6
    food_stock = colony.food

    """création des instances"""

    runningGame = game.game()
    food = foodModule.foodStock()
    food._food_stock = food_stock

    """création de la colonie"""

    ant_nbr = colony.nbr_ant_alive()


    screen.fill((0, 0, 0))
    py.pygame.display.update()

    while True:
        save_button.draw(screen)

        for event in py.pygame.event.get():
            if event.type == py.pygame.QUIT:
                py.pygame.quit()
            if event.type == py.pygame.KEYDOWN:
                if event.key == py.pygame.K_SPACE:
                    screen.fill((0, 0, 0))
                    day, consumed_food = runningGame.aDay(day, food, colony, ant_nbr, ant_weight)
                    py.display_stats(screen, stat_font, day, len(colony.ant_list), food.food_stock, consumed_food)
            if event.type == py.pygame.MOUSEBUTTONDOWN:
                mouse_pos = py.pygame.mouse.get_pos()
                if save_button.isOver(py.pygame.mouse.get_pos()):
                    page_save(colony, day, food.food_stock)

        py.pygame.display.update()

######################################################@
import pygame
import sys



def afficher_texte(texte, x, y):
    texte_surface = stat_font.render(texte, True, (255, 255, 255))
    screen.blit(texte_surface, (x, y))


def page_save(colony, day, food):
    # Champ d'entrée et bouton OK
    input_rect = pygame.Rect(540, 360, 200, 40)
    input_texte = ''
    input_active = False

    bouton_ok = pygame.Rect(150, 150, 100, 40)
    pygame.draw.rect(screen, (255, 0, 0), bouton_ok)
    afficher_texte('OK', 180, 160)


    menu_text = stat_font.render("Entrez le nom de votre sauvegarde et appuyez sur entrer", True, (255, 255, 255))
    menu_rect = menu_text.get_rect(center=(640, 300))

    while True:
        screen.fill((0, 0, 0))
        screen.blit(menu_text, menu_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if bouton_ok.collidepoint(event.pos):
                    print(input_texte)
                    colony.save(f"{chemin()}{input_texte}", food, day)
                    run.main_menu()
                    return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print(input_texte)
                    colony.save(f"{chemin()}{input_texte}", food, day)
                    run.main_menu()
                    return
                if event.key == pygame.K_BACKSPACE:
                    input_texte = input_texte[:-1]
                else:
                    input_texte += event.unicode

        pygame.draw.rect(screen, (255, 255, 255), input_rect, 2)
        afficher_texte(input_texte, input_rect.x + 5, input_rect.y + 5)

        pygame.display.flip()

def liste():
    path = os.getcwd()
    path_save = path + '/save'
    liste_sauvegardes = os.listdir(path_save)
    return liste_sauvegardes
def chemin():
    path = os.getcwd()
    path_save = path + '/save/'
    return path_save

