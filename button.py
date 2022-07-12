import pygame as pg


class Button:
    """Class that represents a button
    """
    __COLOR = (192, 192, 192)       # Color of a button
    __BORDER_COLOR = (0, 0, 0)      # Border color of a button
    __BORDER_WIDTH = 4              # Width of button's border

    def __init__(self, coords, size) -> None:
        """Constructor of 'Button' class

        Args:
            coords ((int, int)): Coordinates on the surface where a button should be drawn
            size ((int, int)): Width and height of a button
        """
        self.coords = coords
        self.size = size
        self.box = pg.Rect(self.coords + self.size)

    def draw(self, window) -> None:
        """Draws the button on a given surface (window)

        Args:
            window (pygame.Surface): Defines where the cell should be drawn
        """
        pg.draw.rect(window, self.__COLOR, self.box)
        for i in range(-self.__BORDER_WIDTH // 2, self.__BORDER_WIDTH // 2):
            border_coords = (
                self.coords[0] + i,
                self.coords[1] + i,
                self.size[0],
                self.size[1]
            )
            pg.draw.rect(window, self.__BORDER_COLOR, border_coords, 1)
