import random
from time import time
from numpy import prod, product

start_time = 0
final_time = 0
class Board:
    def __init__(self, size_width, size_heigth, bombs_num):
        self.bombs_num = bombs_num
        self.size = [size_heigth, size_width]
        self.board_values = [[None for i in range(size_width)] for j in range(size_heigth)]
        self.board_show = [[False for i in range(size_width)] for j in range(size_heigth)]
        self.free_position = (size_heigth * size_width) - bombs_num
    
    
    def free(self):
        print(self.free_position)
        
    
    def put_bombs(self):
        bombs = 0
        
        while bombs < self.bombs_num:
            row = random.randint(0, self.size[0] - 1)
            col = random.randint(0, self.size[1] - 1)
            
            if self.board_values[row][col] == "*":
                continue
            else:
                self.board_values[row][col] = "*"
                bombs += 1

    
    # This function was make to test the program ############################################
    def solution(self):                                                                     #
        for i in range(self.size[1] + 1):                                                   #
            print("  |" if i == 0 else i - 1, end=" ")                                      #
        print("|")                                                                          #
                                                                                            #
        for i in range(self.size[0]):                                                       #
            for j in range(self.size[1] + 1):                                               #
                print((str(i) + " |") if j == 0 else self.board_values[i][j - 1], end="  ") #
            print("|")                                                                      #
    #########################################################################################
    
    def show_board(self):
        for i in range(self.size[1] + 1):
            print(('%6s' % ' ') if i == 0 else '%2s' % str(i - 1), end=" ")
        print("")
        
        for i in range(self.size[1] + 1):
            print(('%6s' % ' ') if i == 0 else '%2s' % "|", end=" ")
        print("")
        
        for i in range(self.size[1] + 1):
            print(('%6s' % ' ') if i == 0 else '%2s' % "▼", end=" ")
        print("")

        for i in range(self.size[0]):
            for j in range(self.size[1] + 1):
                print(('%2s' % str(i) + " -► ") if j == 0 else ('%2s' % str(self.board_values[i][j - 1]) if self.board_show[i][j - 1] == True else '%2s' % ' '), end=" ")
            print("")
    
    
    def reset(self):
        self.board_values = [[None for i in range(self.size[1])] for j in range(self.size[0])]
        self.board_show = [[False for i in range(self.size[1])] for j in range(self.size[0])]
        self.free_position = prod(self.size)
            
            
    def new_board(self):
        self.put_bombs()
        
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                
                if self.board_values[i][j] == "*":
                    continue
                else:
                    total_bombs = 0
                                        
                    for r in range(max(0, i - 1), min(self.size[0], i + 2)):
                        for c in range(max(0, j - 1), min (self.size[1], j + 2)):    
                            if self.board_values[r][c] == "*":
                                total_bombs += 1   
                                                
                    self.board_values[i][j] = total_bombs
            
        self.solution()
        print("")
        
        
    def look_at(self, row, col):
        
        if row == None:
            return True
        
        if self.board_values[row][col] == "*": 
            for i in range(self.size[0]):
                for j in range(self.size[1]):
                    if self.board_values[i][j] == "*":
                        self.board_show[i][j] = True
            self.show_board()
            print("You loose!")
            return False
            
        if self.board_values[row][col] > 0:
            self.board_show[row][col] = True
            self.free_position -= 1
            
            self.show_board()
        
        
        def clear_location(r, c):
            if self.board_values[r][c] == 0 and self.board_show[r][c] == True:
                for i in range(max(0, r - 1), min(self.size[0], r + 2)):
                    for j in range(max(0, c - 1), min(self.size[1], c + 2)):
                        if self.board_values[i][j] != "*" and self.board_values[i][j] != 0 and self.board_show[i][j] == False:
                            self.board_show[i][j] = True
                            self.free_position -= 1
                        if self.board_values[i][j] == 0 and self.board_show[i][j] == False:
                            self.board_show[i][j] = True
                            self.free_position -= 1
                            clear_location(i,j)
                                    
            
        if self.board_values[row][col] == 0:
            self.board_show[row][col] = True
            self.free_position -= 1
            clear_location(row, col)
            self.show_board()    
        
        if self.free_position > 0:    
            return True
        else:
            print("")
            print("Free postion left: ", end="")
            self.free()
            global final_time
            final_time = time.time()
            print("Congratulation! YOU WIN!")
            print("Your time: ", final_time - start_time, "seconds.")
            return False

print("Welcome  to Minesweeper!")
print("The coordinates must be have the format: row,column (with the ',' and without spaces)")
width = int(input("Choose the board's width: "))
heigth = int(input("Choose the board's heigth: "))
bombs = int(input("How many bombs do you want to plant: "))

game = Board(width, heigth, bombs)
game.new_board()
game.show_board()

on_game = True
show = [None, None]

while on_game:
    start_time = time.time()
    print("")
    print("Free postion left: ", end="")
    game.free()
    select = (input("Choose the coordinates: ")).split(",")
    print("")
    show[0], show[1] = int(select[0]), int(select[1])
    on_game = game.look_at(show[0], show[1])
    
    if not on_game:
        print("")
        
        choised = ""
        
        while choised == "":
            choised = (input("Do you want to play again? (s/n): ")).lower()
            
            if choised == "s":
                game.reset()
                game.new_board()
                game.show_board()
                on_game = True
            elif choised == "n":
                print("Good Bye!")
            else: 
                choise = ""
                print("You must to choose between 's' or 'n'.")