# Battleships Game in Python

## Table of Contents
- Introduction
- Features
- Prerequisites
- Installation
- How to Play
- Game Setup
- Gameplay
- Ending the Game
- Game Rules and Mechanics
- Grid Representation
- Ship Placement Rules
- Turn Mechanics 
- Code Overview
- Function Descriptions
- Possible Improvements
- License 
- Contact Information

## Introduction

Welcome to the Battleships Game in Python! This is a console-based implementation of the childhood classic Battleships game where you play again the computer. You can customise your grid size and the number of ships, place your ships strategically on the grid and try to sink all of the computer's ships before it sinks yours!

## Features

- Customisable Gride Size: Choose the size of the battleground.
- Customise Number of Ships: Decide how many ships you and the computer will play with.
- Manual Ship Placement: Place your ships on the grid manually and select your position/orientation.
- Random Computer Ship Placement: The computer will place its ships randomly on the grid.
- Turn-Based Gameplay: Alternate turns between you and the computer.
- Real-Time Updates: Grids are updated and displayed after each turn.
- Input Validation: Robust checks for user inputs to ensure valid gameplay.

## Prerequisites

- Make sure you have the latest Python installed on your system in order to run the game.

## Installation

- You can find the Battleships Game [Here](https://dashboard.heroku.com/apps/finalbattleships/deploy/github)

## Game Setup

1. Run the Game: 
Open the link above and get stuck right in!
2. Enter Grid Size:
When prompted, enter the desired grid size (e.g., 5 for a 5x5 grid).
3. Enter Number of Ships:
Input the number of ships you wish to have in the game.
4. Place Your Ships:
- For each ship, you will be prompted to:
1. Enter Orientation: H for horizontal or V for vertical.
2. Enter Ship Length: Choose between 2 or 3.
3. Enter Starting Coordinates:
- Colum (X coordinate): An integer between 0 and grid size -1.
- Row (Y coordinate): An integer between 0 and gride size -1.
- The grid will display your ships after each placement.
5. Computer Places Ships:
- The computer will automatically place its ships randomly on its grid.

## Gameplay

- Player's Turn:
1. View Opponent's Grid:
- The grid displays your previous hits and misses on the computer's grid.
2. Make a Guess:
- Enter Column (X coordinate): An integer between 0 and grid size -1.
- Enter Row (Y coordinate): An integer between 0 and grid size -1.
- The game will notify you if it's a hit (Hit!) or a miss (Miss.).
- The computer's remaining ships will be updated.
- Computer's Turn:
- The computer will make a guess on your grid.
- You will be informed whether the computer scored a hit or a miss.
- Your remaining ships will be updated.

## Ending the Game

- The game continues until either the player or the computer has no ships remaining.
- The game will announce the winner.
- Player Wins: Congratulations! You win.
- Computer Wins: Game Over! The computer wins.

## Game Rules and Mechanics

### Grid Representation

- Symbols:
1. ~: Unknown or unexplored cell.
2. S: Ship (only visible on your grid).
3. X: Hit.
4. O: Miss.

## Ship Placement Rules

- Ships can be placed either horizontally (H) or vertically (V).
- Ship lengths can be either 2 or 3.
- Ships cannot overlap with other ships.
- Ships cannot extend betond the boundaries of the grid.

## Turn Mechanics

- Valid Guesses:
1. You cannot guess a location you have already guessed.
2. Coordinates must be within the bounds of the grid.
3. Processing Guesses:
- If a guess hits a ship, the cell is marked with X.
- If a guess misses, the cell is marked with O.
4. Ship Sinking:
- Each hit reduces the opponent's remaining ships by one.
- The game tracks and displays the number of ships remaining for both players.

## Code Overview

The game is structured into several functions for modularity and clarity.

### Function Descriptions
- create_grid(size): Create and returns a size x size grid initialised with ~
- display_grid(grid, hide_ships=True): Displays the grid in the console
- If hide_ships is True it hides the ships (replaces S with ~)
- place_ships(grid, num_ships): Randomly places num_ships ships on the grid for the computer
- Ships are of a random length (2 or 3) and random orientation.
- player_place_ships(grid, num_ships): Allows the player to place their ships on their grid and validates inputs for orientation, ship length and starting coordinates.
- get_user_guess(size): Prompts the player to enter valid coordinates for their guess and ensures the coordinates are within the grid.
- process_guess(opponent_grid, display_grid, x, y): Processes the player's guess against the computer's grid and updated both the opponent's grid and the player's display grid and returns True if it's a hit, False otherwise
- computer_guess(player_grid, computer_memory): The computer makes a random guess and ensuring it doesn't guess the same location twice using computer_memory. It then proceeds to update the player's grid with the result.
- count_ships(grid): Counts and returns the number of ships (S) remaining on a grid.
- play_game(): The main function that runs the game, manages the game loop and alternates turns between the player and the computer and finally determines and announces the winner.

## Possible Improvements 

- Enhanced AI for Computer: Implement smarter guessing logic for the computer after it scores a hit.
- Different Ship Types: Introduce ships of various lengths and types (e.g., Battleship, Cruiser etc).
- Graphical User Interfact: Develop a GUI version using external libraries 
- Save and Load Game:Implement functionality to save the game state and load it later.
- Network Multiplayer: Allow two players to play against each other over a network.

## License

This project is open-source and is available on Heroku

## Contact Information

For any questions, suggestions or contributions please contact:
- Name: [Ibrahim Abedghane]
- Email: [abedghaneibrahim94@gmail.com]

Enjoy the game and happy hunting!