import pygame as pg

from const import TEXT_FONT


class Text:
    """Class that represents the text drawn on a surface
    """

    def __init__(self, coords, color, content, text_size) -> None:
        """Constructor of 'Text' class

        Args:
            coords ((int, int)): Coordinates on the surface where a text should be drawn
            color ((int, int, int)): Color of the text
            content (string): Defines the content of a text
            text_size (int): Font size of a text
        """

        self.coords = coords
        self.color = color
        self.content = content
        self.text_size = text_size

        # Font object that corresponds to a given dont
        self.font = pg.font.SysFont(TEXT_FONT, self.text_size)

    def draw(self, window) -> None:
        """Draws the text on a given surface (window)

        Args:
            window (pygame.Surface): Defines where the cell should be drawn.
        """
        text = self.font.render(self.content, True, self.color)
        text_box = text.get_rect()
        text_box.center = self.coords
        window.blit(text, text_box)
