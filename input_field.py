import pygame as pg

from text import Text


class InputField:
    """Class that represents a field where a user can provide an input
    """

    __INACTIVE_COLOR = (96, 96, 96)     # Color of a field when it's inactive
    __ACTIVE_COLOR = (240, 240, 240)    # Color of a field when its' active
    __BORDER_COLOR = (0, 0, 0)          # Border color of a field
    __BORDER_WIDTH = 4                  # Width of the border of a field

    # Color of the text that will be displayed after input
    __TEXT_COLOR = (0, 0, 0)

    def __init__(self, coords, size, input_type) -> None:
        """Constructor of 'InputField' class

        Args:
            coords ((int, int)): Coordinates on the surface where a field should be drawn
            size ((int, int)): Width and height of a field
            input_type (type): Expected type of an input
        """

        self.coords = coords
        text_coords = (
            coords[0] + size[0] / 2,
            coords[1] + size[1] / 2
        )       # calculate the place where a text should be drawn
        self.size = size
        self.input_type = input_type
        self.text = Text(
            text_coords, self.__TEXT_COLOR, '', 30
        )       # Create a 'Text' object that will be used to display the input
        self.active = False

        # Rectangle object that represents a field on a board
        self.box = pg.Rect(self.coords + self.size)

    def draw(self, window) -> None:
        """Draws the field on a given surface (window)

        Args:
            window (pygame.Surface): Defines where the cell should be drawn
        """

        if not self.active:
            pg.draw.rect(window, self.__INACTIVE_COLOR, self.box)

        else:
            pg.draw.rect(window, self.__ACTIVE_COLOR, self.box)

        for i in range(-self.__BORDER_WIDTH // 2, self.__BORDER_WIDTH // 2):
            border_coords = (
                self.coords[0] + i,
                self.coords[1] + i,
                self.size[0],
                self.size[1]
            )
            pg.draw.rect(window, self.__BORDER_COLOR, border_coords, 1)

        self.text.draw(window)

    def process_input(self):
        """Processes the given input and checks it's type

        Returns:
            input_type: Given input in wanted type if conversion is successful or None if it isn't
        """

        input = None

        try:                # Try converting the input to appropriate type
            input = self.input_type(self.text.content)
        except TypeError:
            print('Error - Input has a wrong type')

        self.text.content = ''  # Reset the input
        return input

    def delete_last_char(self) -> None:
        """Deletes the last character in an input
        """
        
        self.text.content = self.text.content[:-1]

    def add_char(self, char) -> None:
        """Add a character to the input string

        Args:
            char (string): The character that should be added to already existing input string
        """
        
        if len(self.text.content) < 3:
            self.text.content += char

        else:
            print('Warning - Input has reached the maximum size')
