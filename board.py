import copy
import random
from tkinter.tix import CELL

import pygame as pg

from cell import Cell
from const import CELL_COUNT


class Board:
    cells = []
    buttons = {}
    texts = {}
    fields = {}

    def __init__(self, window, size, buttons, texts, fields) -> None:
        self.run = False
        self.window = window
        self.tickrate = 1

        for i in range(size[0]):
            temp_list = []

            for j in range(size[1]):
                temp_list.append(Cell((i, j)))

            self.cells.append(temp_list)

        self.number_of_cells = size[0] * size[1]

        for b in buttons:
            self.buttons[b] = buttons[b]

        for t in texts:
            self.texts[t] = texts[t]

        for f in fields:
            self.fields[f] = fields[f]

    def draw(self) -> None:
        for i in self.cells:
            for j in i:
                j.draw(self.window)

        for b in self.buttons:
            self.buttons[b].draw(self.window)

        for t in self.texts:
            self.texts[t].draw(self.window)

        for f in self.fields:
            self.fields[f].draw(self.window)

    def randomize_cells(self) -> None:
        for col in self.cells:
            for cell in col:

                random_bit = random.getrandbits(1)
                cell.active = True if random_bit else False

    def clear_board(self) -> None:
        for col in self.cells:
            for cell in col:
                cell.active = False

    def next_step(self) -> None:
        new_board = copy.deepcopy(self.cells)
        
        neighbourhood = [
            (-1, -1), (0, -1), (1, -1),
            (-1, 0), (1, 0),
            (-1, 1), (0, 1), (1, 1)
        ]
        
        for col in self.cells:
            for cell in col:
                active_neighbour_count = 0
                
                for n in neighbourhood:
                    x = (cell.coords[0] + n[0]) % CELL_COUNT[0]
                    y = (cell.coords[1] + n[1]) % CELL_COUNT[1]
                    neighbour = self.cells[x][y]
                    
                    if neighbour.active:
                        active_neighbour_count += 1
                        
                if active_neighbour_count == 3:
                    new_board[cell.coords[0]][cell.coords[1]].active = True
                    
                elif cell.active and active_neighbour_count == 2:
                    new_board[cell.coords[0]][cell.coords[1]].active = True
                    
                else:
                    new_board[cell.coords[0]][cell.coords[1]].active = False
        
        self.cells = copy.deepcopy(new_board)
        
    def event_handler(self, event) -> bool:
        match event.type:

            case pg.QUIT:
                return False

            case pg.KEYDOWN:
                if self.fields['tickrate'].active:

                    if event.key == pg.K_RETURN:
                        new_tickrate = self.fields['tickrate'].process_input()

                        if new_tickrate is not None:
                            self.tickrate = new_tickrate

                    elif event.key == pg.K_BACKSPACE:
                        self.fields['tickrate'].delete_last_char()

                    else:
                        self.fields['tickrate'].add_char(event.unicode)

            case pg.MOUSEBUTTONDOWN:
                if self.buttons['exit'].box.collidepoint(event.pos):
                    return False

                elif self.buttons['start'].box.collidepoint(event.pos):
                    self.run = True

                elif self.buttons['stop'].box.collidepoint(event.pos):
                    self.run = False

                elif self.buttons['clear'].box.collidepoint(event.pos):
                    self.clear_board()

                elif self.buttons['randomize'].box.collidepoint(event.pos):
                    self.randomize_cells()

                elif self.buttons['next_step'].box.collidepoint(event.pos):
                    self.next_step()

                if self.fields['tickrate'].box.collidepoint(event.pos):
                    self.fields['tickrate'].active = True

                else:
                    self.fields['tickrate'].active = False

                for cols in self.cells:
                    for cell in cols:
                        if cell.box.collidepoint(event.pos):
                            cell.switch()

            case pg.MOUSEMOTION:
                on_button = False

                for key, item in self.buttons.items():
                    if item.box.collidepoint(event.pos):
                        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
                        on_button = True

                for key, item in self.fields.items():
                    if item.box.collidepoint(event.pos):
                        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_IBEAM)
                        on_button = True

                if not on_button:
                    pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)

        return True
