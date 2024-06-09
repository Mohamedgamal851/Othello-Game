# Othello-Game
Implement the strategy board game Othello for two players on an 8×8 board. Players place disks to outflank and flip the opponent's disks, aiming to have the majority of disks in their color by the end. Black moves first. If no legal move is available, the player passes. The game ends when no moves are possible or a player runs out of pieces.

## About Othello
Othello is a strategy board game for two players,
played on an 8×8 uncheckered board. Two players
compete, using 64 identical game pieces ("disks")
that are white on one side and black on the other.
Each player chooses one color to use throughout
the game. Players take turns placing one disk on an
empty square, with their assigned color facing up.
After a play is made, any disks of the opponent's
color that lie in a straight line bounded by the one
just played and another one in the current player's
color are turned over. When all playable empty
squares are filled, the player with more disks
showing in their own color wins the game.
## Game Setup
- Initially, the board is set up by placing two black disks and
two white disks at the center of the board exactly as shown
in the opposite figure. The game always begins with this setup.
- Then, the remaining 60 disks are divided between players such that each player has 30 disks.
## How the game goes
1. When it’s a player’s turn, he must look for an empty square on the board that is adjacent
to one of the opponent’s pieces. The player can add his disk there with his color facing
upwards.
2. If the newly added disk encloses a straight horizontal row or vertical column of the
opponent’s pieces between two disks of the player’s color, then it’s a legal move known
as “outflanking”.

3. Once the player outflanks the opponent's disks, they are flipped over to the player’s
color (i.e. the player captured them). The disks now count as the player’s pieces on the
board even if he didn’t originally play them.
4. After that the player passes the turn to his opponent to continue playing.
5. When it is no longer possible for either player to move, the game is over. Disks are counted and the player with the majority of their color showing is the winner.
## Game Rules
- Black always moves first.
- If a player cannot outflank and flip at least one opposing disk, they miss their turn and
their opponent moves again.
- A disk may outflank any number of disks in one or more rows in any direction (either
horizontally or vertically) at the same time.

- Players may not skip over their own color disks to outflank an opposing disk.

- Disks may only be outflanked as a direct result of a move and must fall in the direct line
of the disk placed down.

- The game may end if a player runs out of pieces.

#### Note: You can play the game online to get familiar with how it works:
https://www.eothello.com/
