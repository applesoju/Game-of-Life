import copy
import random

import pygame as pg

from cell import Cell
from const import CELL_COUNT


class Board:
    """Class that represents a board
    """

    cells = []      # list of cells which are on a board
    buttons = {}    # dictionary of buttons
    texts = {}      # dictionary of texts
    fields = {}     # dictionary of fields

    def __init__(self, window, size, buttons, texts, fields) -> None:
        """Constructor of 'Board' class

        Args:
            window (pygame.Surface): Defines a surface where a board with it's elements should be drawn
            size ((int, int)): Number of cells in width and height of a board
            buttons (dict of str: Button): Dictionary with Buttons that should be placed in the menu section
            texts (dict of str: Text): Dictionary with Texts that should be placed in the menu section
            fields (dict of str: InputField): Dictionary with InputFields that should be placed in the menu section
        """

        self.run = False        # The board is not progressing by default
        self.window = window
        self.tickrate = 1       # Default tickrate is 1 tick per second

        for i in range(size[0]):        # Creating a 2D list (grid) of Cell objects
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
        """Draws the board with it's elements on a given surface (window)
        """

        for i in self.cells:        # Draw all cells
            for j in i:
                j.draw(self.window)

        for b in self.buttons:      # Draw all buttons
            self.buttons[b].draw(self.window)

        for t in self.texts:        # Draw all texts
            self.texts[t].draw(self.window)

        for f in self.fields:       # Draw all fields
            self.fields[f].draw(self.window)

    def randomize_cells(self) -> None:
        """Randomizes states of all cells
        """

        for col in self.cells:
            for cell in col:

                random_bit = random.getrandbits(1)
                cell.active = True if random_bit else False

    def clear_board(self) -> None:
        """Clear the board (changes states of all cells to not active)
        """

        for col in self.cells:
            for cell in col:
                cell.active = False

    def next_step(self) -> None:
        """Progresses the board to the next state based on the Conway's Game of Life ruleset
        """

        # Deep copy of the 2D cell list
        new_board = copy.deepcopy(self.cells)

        # list of relative coordinates of neighbours of a given cell
        neighbourhood = [
            (-1, -1), (0, -1), (1, -1),
            (-1, 0),           (1, 0),
            (-1, 1),  (0, 1),  (1, 1)
        ]

        for col in self.cells:
            for cell in col:
                active_neighbour_count = 0      # Counter of active neighbours

                for n in neighbourhood:         # For every neighbour compute it's coordinates
                    x = (cell.coords[0] + n[0]) % CELL_COUNT[0]
                    y = (cell.coords[1] + n[1]) % CELL_COUNT[1]
                    neighbour = self.cells[x][y]

                    if neighbour.active:        # If it's active increment the count
                        active_neighbour_count += 1

                # If the cell is active and has 3 neighbours it stays active
                # If the cell is inactive and has 3 neighbours it becomes active
                if active_neighbour_count == 3:
                    new_board[cell.coords[0]][cell.coords[1]].active = True

                # If the cell is active and has 2 neighbours it stays active
                elif cell.active and active_neighbour_count == 2:
                    new_board[cell.coords[0]][cell.coords[1]].active = True

                # In every other case the cell stays or becomes inactive
                else:
                    new_board[cell.coords[0]][cell.coords[1]].active = False

        # update the state of the 2D list
        self.cells = copy.deepcopy(new_board)

    def event_handler(self, event) -> bool:
        """Handles all relevant events

        Args:
            event (Event): Relevant event that needs to be processed

        Returns:
            bool: False if the event should cause the window to close. True if not.
        """
        match event.type:

            # Window is closed by clicking the 'X' button
            case pg.QUIT:
                return False

            # Key is pressed
            case pg.KEYDOWN:
                
                # If the field is active
                if self.fields['tickrate'].active:

                    # The 'Enter' key is pressed
                    if event.key == pg.K_RETURN:
                        new_tickrate = self.fields['tickrate'].process_input()

                        if new_tickrate is not None:
                            self.tickrate = new_tickrate

                    # The 'Backspace' key is pressed
                    elif event.key == pg.K_BACKSPACE:
                        self.fields['tickrate'].delete_last_char()

                    # Any other key is pressed
                    else:
                        self.fields['tickrate'].add_char(event.unicode)

            # Left Mouse Button is pressed
            case pg.MOUSEBUTTONDOWN:
                
                # Cursor position collides with the 'exit' button
                if self.buttons['exit'].box.collidepoint(event.pos):
                    return False

                # Cursor position collides with the 'start' button
                elif self.buttons['start'].box.collidepoint(event.pos):
                    self.run = True

                # Cursor position collides with the 'stop' button
                elif self.buttons['stop'].box.collidepoint(event.pos):
                    self.run = False

                # Cursor position collides with the 'clear' button
                elif self.buttons['clear'].box.collidepoint(event.pos):
                    self.clear_board()

                # Cursor position collides with the 'randomize' button
                elif self.buttons['randomize'].box.collidepoint(event.pos):
                    self.randomize_cells()

                # Cursor position collides with the 'next_step' button
                elif self.buttons['next_step'].box.collidepoint(event.pos):
                    self.next_step()

                # Cursor position collides with the 'tickrate' field
                if self.fields['tickrate'].box.collidepoint(event.pos):
                    self.fields['tickrate'].active = True

                else:
                    self.fields['tickrate'].active = False

                # Check if cursor collides with any cell
                for cols in self.cells:
                    for cell in cols:
                        if cell.box.collidepoint(event.pos):
                            cell.switch()

            # The mouse is moved
            case pg.MOUSEMOTION:
                on_button = False

                # If the cursor is on any button change it to a hand
                for key, item in self.buttons.items():
                    if item.box.collidepoint(event.pos):
                        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
                        on_button = True

                # If the cursor is on any field change it to an ibeam
                for key, item in self.fields.items():
                    if item.box.collidepoint(event.pos):
                        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_IBEAM)
                        on_button = True

                # If the cursor is not on any button then change it to an arrow
                if not on_button:
                    pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)

        return True
