import pygame as pg

from const import CELL_DIMS, CELL_PADDING


class cell:
    __ACTIVE_COLOR = (215, 215, 215)
    __INACTIVE_COLOR = (0, 0, 0)

    def __init__(self, coords, active=False, size=CELL_DIMS) -> None:
        self.coords = coords
        self.active = active
        self.size = size
        self.box = pg.Rect(
            self.coords[0] * CELL_DIMS[0] + CELL_PADDING,
            self.coords[1] * CELL_DIMS[1] + CELL_PADDING,
            CELL_DIMS[0] - 2 * CELL_PADDING,
            CELL_DIMS[1] - 2 * CELL_PADDING
        )

    def draw(self, window):
        color = self.__ACTIVE_COLOR if self.active else self.__INACTIVE_COLOR
        pg.draw.rect(window, color, self.box)

    def switch(self):
        self.active = not self.active
