import pygame


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


def drawText(surface, text, color, rect, font, aa=False, bkg=None):
    rect = pygame.Rect(rect)
    y = rect.top
    lineSpacing = -2

    # get the height of the font
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word
        if i < len(text):
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]

    return text


def display_stats(surface, font, day, ant_nbr, food_stock, consumed_food):

    day_text = f"Jour : {day}"
    ant_nbr_text = f"Fourmis :{ant_nbr}"
    food_stock_text = f"Nourriture :{food_stock}"
    stat_rectangle = pygame.Rect(1000, 50, 200, 300)
    day = font.render(day_text, True, (0, 0, 0))
    ant_nbr = font.render(ant_nbr_text, True, (0, 0, 0))
    food = font.render(food_stock_text, True, (0, 0, 0))
    day_rect = day.get_rect(center=(1100, 60))
    ant_nbr_rect = day.get_rect(center=(1050, 90))
    food_rect = day.get_rect(center=(1050, 120))
    pygame.draw.rect(surface, (255, 255, 255), stat_rectangle)
    surface.blit(day, day_rect)
    surface.blit(ant_nbr, ant_nbr_rect)
    surface.blit(food, food_rect)
    pygame.display.flip()
