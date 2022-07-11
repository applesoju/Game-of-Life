import pygame as pg

from text import text


class input_field:
    __INACTIVE_COLOR = (96, 96, 96)
    __ACTIVE_COLOR = (240, 240, 240)
    __BORDER_COLOR = (0, 0, 0)
    __BORDER_WIDTH = 4
    __TEXT_COLOR = (0, 0, 0)

    def __init__(self, coords, size, input_type) -> None:
        self.coords = coords
        text_coords = (
            coords[0] + size[0] / 2,
            coords[1] + size[1] / 2
        )
        self.size = size
        self.input_type = input_type
        self.text = text(
            text_coords, self.__TEXT_COLOR, '', 30
        )
        self.active = False
        self.box = pg.Rect(self.coords + self.size)

    def draw(self, window) -> None:
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
        input = None

        try:
            input = self.input_type(self.text.content)
        except:
            print('Error - Input has a wrong type')

        self.text.content = ''
        return input

    def delete_last_char(self) -> None:
        self.text.content = self.text.content[:-1]

    def add_char(self, char) -> None:
        if len(self.text.content) < 3:
            self.text.content += char

        else:
            print('Warning - Input has reached the maximum size')
