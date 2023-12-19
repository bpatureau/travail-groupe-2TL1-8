import pygame

pygame.init()

class Button:

    """
    code de la classe boutton :"https://www.youtube.com/watch?v=4_9twnEduFA"
    """
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, ):
        # Call this method to draw the button on the screen

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('impact', 30)
            text = font.render(self.text, 1, (255, 255, 255))
            win.blit(text,
                     (self.x + (self.width / 2 - text.get_width() / 2),
                      self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x, y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False


screen = pygame.display.set_mode((1280, 720), )
background = pygame.image.load("img/background.png").convert()
get_font = pygame.font.SysFont("impact", 100)


def main_menu():
    pygame.display.set_caption('FOURMIZ')

    while True:
        screen.blit(background, (0, 0))
        mouse_pos = pygame.mouse.get_pos()
        menu_text = get_font.render("FOURMIZ", True, (0, 0, 0))
        menu_rect = menu_text.get_rect(center=(640, 100))

        launch_button = Button((0, 0, 0), 525, 250, 200, 50, 'LAUNCH')
        launch_button.draw(screen)

        options_button = Button((0, 0, 0), 525, 400, 200, 50, 'OPTIONS')
        options_button.draw(screen)

        quit_button = Button((0, 0, 0), 525, 550, 200, 50, 'QUIT')
        quit_button.draw(screen)

        screen.blit(menu_text, menu_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if launch_button.isOver(mouse_pos):
                    launch()
                if options_button.isOver(mouse_pos):
                    option()
                if quit_button.isOver(mouse_pos):
                    pygame.quit()

        pygame.display.update()

main_menu()