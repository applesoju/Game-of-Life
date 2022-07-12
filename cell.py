import pygame as pg

from const import CELL_DIMS, CELL_PADDING


class cell:
    """Class that represents one cell
    """

    __ACTIVE_COLOR = (215, 215, 215)    # Color of an active cell
    __INACTIVE_COLOR = (0, 0, 0)        # Color of an inactive cell

    def __init__(self, coords, active=False, size=CELL_DIMS) -> None:
        """Constructor of 'Cell' class.

        Args:
            coords ((int, int)): The coordinates of a cell. Ranges between (0,0) and CELL_COUNT
            active (bool, optional): Defines whether the cell is active (alive) or not. Defaults to False.
            size ((int, int), optional): Defines the size of a cell. Defaults to CELL_DIMS.
        """
        
        self.coords = coords
        self.active = active
        self.size = size
        self.box = pg.Rect(         # Rectangle object that represents a cell on a board
            self.coords[0] * CELL_DIMS[0] + CELL_PADDING,
            self.coords[1] * CELL_DIMS[1] + CELL_PADDING,
            CELL_DIMS[0] - 2 * CELL_PADDING,
            CELL_DIMS[1] - 2 * CELL_PADDING
        )

    def draw(self, window) -> None:
        """Draws the cell on a given surface (window)

        Args:
            window (pygame.Surface): Defines where the cell should be drawn.
        """
        
        color = self.__ACTIVE_COLOR if self.active else self.__INACTIVE_COLOR
        pg.draw.rect(window, color, self.box)

    def switch(self) -> None:
        """Switches the state of a cell
        """
        self.active = not self.active
