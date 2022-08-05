# Game of Life in Python

A simple implementation of the famous 'Game of Life' cellular automaton devised by John Horton Conway.

## Description

For this project i tried to create a simple cellular automata with the Conways Game of Life ruleset. The game is "played" on a 2D grid of cells which can be in one of two states: alive or dead. When the game is moving to the next step, a couple of rules are applied to all cells:

- Any live cell with fewer than 2 live neighbours dies
- Any live cell with more than 3 live neighbours dies
- Any dead cell with exacly 3 live neighbours becomes alive
- Any other cell doesn't change it's state in the next step.

Even though those rules are quite simple they allow for many complex cell structures like oscillators, moving systems - gliders and spaceships and even structures that generate other structures like glider guns.

The program also provides a number of ways to influence the state of the game using a menu:

- you can change how fast the game proceeds to the next step
- you can start or stop the simulation
- you can proceed to the next step
- you can randomize all cells
- you can clear the whole grid

You can also manually change the state of any cell by clicking on it.

## Dependencies

Libraries used in the project:

- PyGame
- copy (for `copy.deepcopy()` method)
- random (for randomizing the state of a game)

## Usage

To start the program all you need to do is type 

```
py main.py
```

Most of the functionality is self-explanatory but it's worth noting that the grey field on top of the menu is used to input the game's tickrate. If the tickrate is equal to 5 it means the game tries to go through 5 steps in one second.

## Authors

Patryk Marciniak ( patryknmarciniak@gmail.com )

## Feedback

Any feedback is welcome, I'm a beginner trying to improve. If you have any questions or suggestions please e-mail me at patryknmarciniak@gmail.com

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

This is my first project and almost everything was implemented from scratch.

* [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
* [A simple README.md template](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)