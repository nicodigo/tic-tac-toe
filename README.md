# Tic Tac Bot
A simple [tic-tac-toe](https://en.wikipedia.org/wiki/Tic-tac-toe) game with a bot that uses the [Minimax Algorithm](https://en.wikipedia.org/wiki/Minimax#Combinatorial_game_theory), making it _hopefully_ unbeatable.

![tied game against the bot](/docs/game_against_bot.gif)

## How to play

### Prerequisites
- [Pyton3](https://www.python.org/) installed
- Tkinter:
    * I had to install it separately, because didn't come by default.
    * I used my package manager to install it. Search for instrutions for yours

#### 1. Clone this repository and cd to it
**With HTTPS:**
```shell
git clone https://github.com/nicodigo/tic-tac-toe.git
cd tic-tac-toe
```
**With SSH:**
```shell
git clone git@github.com:nicodigo/tic-tac-toe.git
cd tic-tac-toe
```

#### 2. Execute main.sh to launch the game
```shell
./main.sh
```

#### 3. Configure the game and start to plya
- It will ask for one/two player mode.
- If one player mode selected it will ask if the bot should use 'X' or 'O'
- It may take a few seconds to start, thats normal, it's building the minmax tree
