import pygame as pg

from const import TEXT_FONT


class text:
    def __init__(self, coords, color, content, text_size) -> None:
        self.coords = coords
        self.color = color
        self.content = content
        self.text_size = text_size
        self.font = pg.font.SysFont(TEXT_FONT, self.text_size)

    def draw(self, window) -> None:
        text = self.font.render(self.content, True, self.color)
        text_box = text.get_rect()
        text_box.center = self.coords
        window.blit(text, text_box)
