import tkinter as tk
import turtle
import othelo
# Constants
SCREEN_SIZE = 50
DISK_SIZE = 20
BOARD_BG_COLOR = "grey"
SEP_COLOR = "black"
DISK_COLORS = ["black", "white"]
BOARD_WIDTH = 8
BOARD_HEIGHT = 8
class GameBoard:
    def __init__(self):
        self.board = [[0] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]
        self.screen_size = SCREEN_SIZE
        self.board_color = BOARD_BG_COLOR
        self.line_color = SEP_COLOR
        self.disk_size = DISK_SIZE
        self.disk_color = DISK_COLORS
        self.move = ()
        self.possible_moves = []
    def draw_board(self):
        turtle.setup(self.screen_size * 8 + self.screen_size, self.screen_size * 8 + self.screen_size)
        turtle.screensize(self.screen_size, self.screen_size)
        turtle.bgcolor('white')
        turtle.title('Othello Game')
        game = turtle.Turtle(visible=False)
        game.penup()
        game.speed(0)
        game.hideturtle()
        game.color(self.line_color, self.board_color)
        game.begin_fill()
        corner = -8 * self.screen_size / 2
        game.setposition(corner, corner)
        game.begin_fill()
        for _ in range(4):
            game.pendown()
            game.forward(self.screen_size*8)
            game.left(90)
        game.end_fill()
        for i in range(8 + 1):
            game.setposition(corner, corner + i * self.screen_size)
            self.draw_lines(game)
        game.left(90)
        for i in range(8 + 1):
            game.setposition(corner + i * self.screen_size, corner)
            self.draw_lines(game)
    def draw_lines(self, game):
        game.pendown()
        game.forward(self.screen_size * 8)
        game.penup()
    def is_point_on_board(self, x, y):
        return -4 * self.screen_size < x < 4 * self.screen_size and -4 * self.screen_size < y < 4 * self.screen_size
    def is_point_on_line(self, x, y):
        return x % self.screen_size == 0 or y % self.screen_size == 0
    def convert_coordinates(self, x, y):
        if self.is_point_on_board(x, y):
            row = 4 - 1 - y // self.screen_size
            col = x // self.screen_size + 4
            return (int(row), int(col))
        return ()
    def get_coordinates(self, r, c):
        if self.is_point_on_board(r, c) and not self.is_point_on_line(r, c):
           self.move = self.convert_coordinates(r, c)
        else:
            self.move = ()
    def get_disk_SPos(self,sq):
        if sq == ():
            return ()
        for i in range(2): 
            if sq[i] not in range(8):
                return ()
        r, c = sq[0], sq[1] 
        y = ((8- 1) / 2 - r) * self.screen_size 
        if c < 4: 
            x = (c - (8 - 1) / 2) * self.screen_size - self.disk_size 
            p = - self.disk_size 
        else:
            x = (c - (8 - 1) / 2) * self.screen_size + self.disk_size 
            p = self.disk_size 

        return ((x, y), p)  
    def draw_disk(self, sq, color):
        position = self.get_disk_SPos(sq)
        if position:
            coordinate = position[0]
            r = position[1]
        else:
            print('Invalid square.')
            return
        disk = turtle.Turtle(visible = False)
        disk.penup()
        disk.speed(0)
        disk.hideturtle()
        disk.color(self.disk_color[color])
        disk.setposition(coordinate)
        disk.setheading(90)
        disk.begin_fill()
        disk.pendown()
        disk.circle(r)
        disk.end_fill()
    def clear_possible_moves(self):
        for move in self.possible_moves:
            position = self.get_disk_SPos(move)
            coordinate = position[0] 
            rad = position[1] 
            disk = turtle.Turtle(visible=False)
            disk.penup()
            disk.speed(0)
            disk.hideturtle()
            disk.color(self.board_color)
            disk.setposition(coordinate)
            disk.setheading(90)
            disk.pendown()
            disk.circle(rad)    
    def draw_possible_moves(self, moves):
        self.clear_possible_moves()
        self.possible_moves = moves
        for move in moves:
            position = self.get_disk_SPos(move) 
            coordinate = position[0] 
            rad = position[1] 
            disk = turtle.Turtle(visible=False)
            disk.penup()
            disk.speed(0)
            disk.hideturtle()
            disk.color('black')
            disk.setposition(coordinate)
            disk.setheading(90)
            disk.pendown()
            disk.circle(rad)
    def show_result(self, black_score, white_score):
        if black_score > white_score:
            result = tk.messagebox.showinfo('Game Over', 'You win!')
        elif black_score < white_score:
            result = tk.messagebox.showinfo('Game Over', 'You lose!')
        else:
            result = tk.messagebox.showinfo('Game Over', 'Draw!')
        if(result == 'ok'):
            turtle.bye()
    def choose_difficulty():
        root = tk.Tk()
        root.title("Difficulty Level")
        difficulty_var = tk.StringVar()
        difficulty_var.set("Easy")
        welcome_label = tk.Label(root, text="Welcome to Othello Game!")
        welcome_label.pack()
        difficulty_label = tk.Label(root, text="Choose difficulty level:")
        difficulty_label.pack()
        difficulty_option_menu = tk.OptionMenu(root, difficulty_var, "Easy", "Medium", "Hard")
        difficulty_option_menu.pack()
        confirm_button = tk.Button(root, text="Confirm", command= lambda: root.destroy())
        confirm_button.pack()
        selected_difficulty = difficulty_var.get()
        if(selected_difficulty == "Easy"):
            selected_difficulty = 1
        elif(selected_difficulty == "Medium"):
            selected_difficulty = 3
        else:
            selected_difficulty = 5
        root.mainloop()
        return selected_difficulty


