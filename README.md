# Tic Tac Bot
A simple [tic-tac-toe](https://en.wikipedia.org/wiki/Tic-tac-toe) game with a bot that uses the [Minimax Algorithm](https://en.wikipedia.org/wiki/Minimax#Combinatorial_game_theory), _hopefully_ making it unbeatable.

![tied game against the bot](/docs/game_against_bot.gif)

## How to play

### Prerequisites
- [Pyton 3 installed](https://www.python.org/)
- Tkinter:
    * May need to be installed separately, depending on your system
    * I used my package manager to install it. Search for instructions for yours

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

#### 3. Configure the game and start to play
- It will ask for one/two player mode.
- If one player mode selected it will ask if the bot should use 'X' or 'O'
- It may take a few seconds to start, that's normal, it's building the minmax tree

## About the project (and me)
![multiple games played against the bot](/docs/multiple_games.gif)


I was always curious about how chess engines work. So to understand them better I started for something simpler: Tic-Tac-Toe.
Tic-Tac-Toe is another [Zero-sum game](https://en.wikipedia.org/wiki/Zero-sum_game), like chess.
This kind of games we can model using a [Game Tree](https://en.wikipedia.org/wiki/Game_tree), which is a graph that represents all possible game states starting from a given state.

![game tree example for tic-tac-toe](/docs/game_tree.webp)

For Tic-Tac-Toe we can build the full game tree in a reasonable time (in a few seconds), and that is what we do in this project.
**The only performance improvement we make** is to generate the full tree on startup _(that's why the game takes a couple of second to start)_, but then we use that same tree for every move and game played. That way you can reset the game instantly, but the complexity of the project does not scale above the scope.
The full tree has 549945 nodes _(internal and leafs)_ and the _root_ node. And takes approximately 350-380MB of ram.
I consider this _acceptable_ for the scope of the project, but it can **certainly** be improved. For example implementing a [Transposition Table](https://en.wikipedia.org/wiki/Transposition_table) as a first step.
Lastly, I had fun, and it was a nice introduction to IA for games and helped me to understand better _(or at least start to understand)_ how chess engine work, and I will take that as a win.

