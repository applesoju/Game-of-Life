import pygame as pg


class button:
    __COLOR = (192, 192, 192)
    __BORDER_COLOR = (0, 0, 0)
    __BORDER_WIDTH = 4

    def __init__(self, coords, size) -> None:
        self.coords = coords
        self.size = size
        self.box = pg.Rect(self.coords + self.size)

    def draw(self, window) -> None:
        pg.draw.rect(window, self.__COLOR, self.box)
        for i in range(-self.__BORDER_WIDTH // 2, self.__BORDER_WIDTH // 2):
            border_coords = (
                self.coords[0] + i,
                self.coords[1] + i,
                self.size[0],
                self.size[1]
            )
            pg.draw.rect(window, self.__BORDER_COLOR, border_coords, 1)
