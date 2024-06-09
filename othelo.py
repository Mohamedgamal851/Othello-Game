import turtle  
from GameBoard import GameBoard  
import computer
MOVE_DIRECTIONS = [(0, -1), (0, +1), (-1, 0), (+1, 0)]

class GameLogic(GameBoard):

    def __init__(self):
        GameBoard.__init__(self) 
        self.c_player = 0 
        self.num_disks = [2, 2] 
        self.computerPlayer = computer.ComputerPlayer(self) 
    def initialize_Gameboard(self):
        GameBoard.draw_board(self)
        coordinate1 = int(8 / 2 - 1) 
        coordinate2 = int(8 / 2)
        first_squares = [(coordinate1, coordinate2), (coordinate1, coordinate1),
                         (coordinate2, coordinate1), (coordinate2, coordinate2)]
        for i in range(len(first_squares)):
            color = i % 2 
            row = first_squares[i][0]
            col = first_squares[i][1]
            self.board[row][col] = color + 1
            self.draw_disk(first_squares[i], color)

    def occur_move(self):
        if self.is_valid_move(self.move):  
            self.board[self.move[0]][self.move[1]] = self.c_player + 1 
            self.num_disks[self.c_player] += 1  
            self.draw_disk(self.move, self.c_player)  
            self.Update_disks() 

    def Update_disks(self):
        cur_disk = self.c_player + 1  
        for direction in MOVE_DIRECTIONS: 
            if self.check_for_outflank(self.move, direction):
                i = 1
                while True:
                    row = self.move[0] + direction[0] * i
                    col = self.move[1] + direction[1] * i
                    if self.board[row][col] == cur_disk:
                        break
                    else:
                        self.board[row][col] = cur_disk 
                        self.num_disks[self.c_player] += 1 
                        self.num_disks[(self.c_player + 1) % 2] -= 1  
                        self.draw_disk((row, col), self.c_player)  
                        i += 1

    def check_for_outflank(self, move, direction):
        i = 1 
        if self.c_player in (0, 1) and \
           self.is_valid_coord(move[0], move[1]):
            cur_disk = self.c_player + 1 
            while True: 
                row = move[0] + direction[0] * i 
                col = move[1] + direction[1] * i 
                if not self.is_valid_coord(row, col) or \
                    self.board[row][col] == 0: 
                    return False 
                elif self.board[row][col] == cur_disk: 
                    break 
                else: 
                    i += 1 
        return i > 1 

    def has_valid_move(self): 
        for row in range(8):
            for col in range(8):
                move = (row, col)
                if self.is_valid_move(move):
                    return True
        return False
    
    def get_valid_moves(self):
        moves = []
        for row in range(8):
            for col in range(8):
                move = (row, col)
                if self.is_valid_move(move):
                    moves.append(move)
        return moves
    def is_valid_move(self, move):
        if move != () and self.is_valid_coord(move[0], move[1]) \
           and self.board[move[0]][move[1]] == 0:
            for direction in MOVE_DIRECTIONS: 
                if self.check_for_outflank(move, direction):  
                    return True
        return False

    def is_valid_coord(self, row, col):
        if 0 <= row < 8 and 0 <= col < 8:
            return True
        return False

    def run(self):
        self.c_player = 0
        GameBoard.draw_possible_moves(self, self.get_valid_moves())
        turtle.onscreenclick(self.play)
        turtle.mainloop()

    def play(self, x, y):
        if self.has_valid_move():
            self.get_coordinates(x, y)
            if self.is_valid_move(self.move):
                turtle.onscreenclick(None)
                self.occur_move()
            else:
                return
        while True:
            self.c_player = 1
            if self.has_valid_move():
                self.move ,_= self.computerPlayer.computerHard(self, self.difficulty, -64, 64, 2)
                self.occur_move()
                self.c_player = 0
                if self.has_valid_move():
                    break
            else:
                break
        self.c_player = 0
        if not self.has_valid_move() or sum(self.num_disks) == 8 ** 2:
            turtle.onscreenclick(None)
            GameBoard.show_result(self, self.num_disks[0], self.num_disks[1])
        else:
            GameBoard.draw_possible_moves(self, self.get_valid_moves())
            turtle.onscreenclick(self.play)
    def evaluate_board(self, player):
        return self.num_disks[player] - self.num_disks[(player + 1) % 2]
    def getAlloutFlanksDisks(self,move):
        getAlloutFlanksDisks = []
        for direction in MOVE_DIRECTIONS:
            if self.check_for_outflank(move, direction):
                i = 1
                while True:
                    row = move[0] + direction[0] * i
                    col = move[1] + direction[1] * i
                    if self.board[row][col] == self.c_player + 1:
                        break
                    else:
                        getAlloutFlanksDisks.append((row, col))
                        i += 1
        return getAlloutFlanksDisks
    def Game_Play(self):
        self.difficulty = GameBoard.choose_difficulty()
        self.initialize_Gameboard()
        self.run()