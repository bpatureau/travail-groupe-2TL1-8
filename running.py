import classes.Ant_hill as antHill
import classes.game as game
import classes.food as foodModule
import pygameUtils as py
import loader_save as save
import os


py.pygame.init()

screen = py.pygame.display.set_mode((1280, 720), )
background = py.pygame.image.load("img/background.png").convert()
get_font = py.pygame.font.SysFont("impact", 100)
stat_font = py.pygame.font.SysFont("impact", 20)


def main_menu():
    py.pygame.display.set_caption('FOURMIZ')

    while True:
        screen.blit(background, (0, 0))
        mouse_pos = py.pygame.mouse.get_pos()
        menu_text = get_font.render("FOURMIZ", True, (0, 0, 0))
        menu_rect = menu_text.get_rect(center=(640, 100))

        launch_button = py.Button((0, 0, 0), 525, 250, 200, 50, 'LAUNCH')
        launch_button.draw(screen)

        charg_button = py.Button((0, 0, 0), 525, 350, 200, 50, 'CHARGER')
        charg_button.draw(screen)

        options_button = py.Button((0, 0, 0), 525, 450, 200, 50, 'OPTIONS')
        options_button.draw(screen)

        quit_button = py.Button((0, 0, 0), 525, 550, 200, 50, 'QUIT')
        quit_button.draw(screen)



        screen.blit(menu_text, menu_rect)

        for event in py.pygame.event.get():
            if event.type == py.pygame.QUIT:
                py.pygame.quit()
            if event.type == py.pygame.MOUSEBUTTONDOWN:
                if launch_button.isOver(mouse_pos):
                    launch()
                if charg_button.isOver(mouse_pos):
                    save.menu_principal(liste())
                if options_button.isOver(mouse_pos):
                    options()
                if quit_button.isOver(mouse_pos):
                    py.pygame.quit()

        py.pygame.display.update()


def launch():
    py.pygame.display.set_caption('SIMULATION')

    save_button = py.Button((0, 160, 0), 1150, 650, 100, 50, 'Save')  # bouton save
    """définition des variables initiales """

    day = 0
    ant_weight = 6
    food_stock = 5000
    initial_ant_queen_nbr = 1
    initial_ant_nbr = 300

    """création des instances"""

    runningGame = game.game()
    colony = antHill.Ant_hill()
    food = foodModule.foodStock()
    food._food_stock = food_stock

    """création de la colonie"""

    colony.hill_constructor(initial_ant_queen_nbr, initial_ant_nbr, day)
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
                    main_menu()
                    return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print(input_texte)
                    colony.save(f"{chemin()}{input_texte}", food, day)
                    main_menu()
                    return
                if event.key == pygame.K_BACKSPACE:
                    input_texte = input_texte[:-1]
                else:
                    input_texte += event.unicode

        pygame.draw.rect(screen, (255, 255, 255), input_rect, 2)
        afficher_texte(input_texte, input_rect.x + 5, input_rect.y + 5)

        pygame.display.flip()





def options():
    py.pygame.display.set_caption('OPTIONS')

    while True:
        screen.fill((0, 0, 0))

        for event in py.pygame.event.get():
            if event.type == py.pygame.QUIT:
                py.pygame.quit()

        py.pygame.display.update()


def liste():
    path = os.getcwd()
    path_save = path + '/save'
    liste_sauvegardes = os.listdir(path_save)
    return liste_sauvegardes
def chemin():
    path = os.getcwd()
    path_save = path + '/save/'
    return path_save


main_menu()
