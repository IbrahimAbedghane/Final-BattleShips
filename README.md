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

