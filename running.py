import classes.Ant_hill as antHill
import classes.game as game
import classes.food as foodModule
import pygameUtils as py

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

        options_button = py.Button((0, 0, 0), 525, 400, 200, 50, 'OPTIONS')
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
                if options_button.isOver(mouse_pos):
                    options()
                if quit_button.isOver(mouse_pos):
                    py.pygame.quit()

        py.pygame.display.update()


def launch():
    py.pygame.display.set_caption('SIMULATION')

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

        for event in py.pygame.event.get():
            if event.type == py.pygame.QUIT:
                py.pygame.quit()
            if event.type == py.pygame.KEYDOWN:
                if event.key == py.pygame.K_SPACE:
                    screen.fill((0, 0, 0))
                    day, consumed_food = runningGame.aDay(day, food, colony, ant_nbr, ant_weight)
                    py.display_stats(screen, stat_font, day, len(colony.ant_list), food.food_stock, consumed_food)

        py.pygame.display.update()


def options():
    py.pygame.display.set_caption('OPTIONS')

    while True:
        screen.fill((0, 0, 0))

        for event in py.pygame.event.get():
            if event.type == py.pygame.QUIT:
                py.pygame.quit()

        py.pygame.display.update()


main_menu()
