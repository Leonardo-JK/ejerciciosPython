import math
import time

from traitlets import ValidateHandler


class Board:
        
    def __init__(self,matrix, on_seting=False):
        self.values = matrix    # Contain the correct values for each box.
        self.valid_numbers = [[[1,2,3,4,5,6,7,8,9] for i in range(9)] for j in range(9)]  # Contain all posible numbers for each box.
        self.verified_values = [[False for i in range(9)] for j in range(9)]  # Contain which box has all ready with a correct number.
        self.on_seting = on_seting # State that prevent run the test if there are numbers setted. 
    
    # This method print the board on screen.
    def show_board(self):
        def index_x():
            j = 0
            for i in range(21):                
                if i < 2 or i == 3 or i == 4 or i == 8 or i == 10 or i == 14 or i == 16 or i == 20:
                    print(" ", end="")
                elif i == 2:
                    print("h", end="")
                elif i == 9 or i == 15:
                    print("| ", end="")
                else:
                    print(j, end=" ")
                    j += 1
            print("")
            
            for i in range(20):                
                if i < 5 or i == 8 or i == 10 or i == 14 or i == 16 or i == 20:
                    print(" ", end="")
                elif i == 9 or i == 15:
                    print("| ", end="")
                else:
                    print("|", end=" ")
                    
            print("")
            
            for i in range(20):
                if i == 0:
                    print("v", end="")
                elif (i > 0 and i < 5) or i == 8 or i == 10 or i == 14 or i == 16 or i == 20:
                    print(" ", end="")
                elif i == 9 or i == 15:
                    print("| ", end="")
                else:
                    print("▼", end=" ")
                    j += 1
            print("")                
        
        def line_blanck():
            for i in range(20):
                if i < 5:
                    print(" ", end="")
                elif i == 8 or  i == 13:
                    print(" |", end="")
                else:
                    print(" ", end=" ")
            
        def line():
            for i in range(15):
                print("--", end="")
        
        
        def line_solved(l):
            j = 0
            for i in range(16):                
                if i == 0:
                    print(l, end="")
                elif i == 1:
                    print("-", end="")
                elif i == 2:
                    print("►", end="")
                elif i == 3 or i == 4:
                    print(" ", end="")               
                elif (i == 8 or i == 12):
                    print(" | ", end=" ")
                else:
                    print(self.values[l][j], end=" ")
                    j += 1
                    
        j = 0
        for i in range(18):            
            if i == 0:
                index_x()
            elif (i == 1 or i == 5 or i == 7 or i == 11 or i == 13 or i == 17):
                line_blanck()
                print("")
            elif (i == 6 or i == 12):
                line()
                print("")
            else:
                line_solved(j)
                print("")
                j += 1
                
    # This method set a correct number on a box which was given to it.            
    def set_values(self, v, h, val, send, k=None, l=None):
        if self.verified_values[v][h] == True:
            print("This position have a number settled already.")
            return
        
        print("")
        print("Linea: ", v, " - Columna: ", h, " - Numero: ", val, " - Enviado por: ", send, " (", k, ", ", l, ")", end=" ->")
                
        self.values[v][h] = val
        self.verified_values[v][h] = True
        self.valid_numbers[v][h].clear()
        self.valid_numbers[v][h].append(val)
        
        # Eliminate the correct number from the list of posible number on all the others box on the same line.
        for r in range(9):
            if r == h:
                continue
            
            if val not in self.valid_numbers[v][r]:
                continue
            else:
                self.valid_numbers[v][r].remove(val)        

        # Eliminate the correct number from the list of posible number on all the others box on the same column.
        for c in range(9):
            if c  == v:
                continue
            
            if val not in self.valid_numbers[c][h]:
                continue
            else:
                self.valid_numbers[c][h].remove(val)
        
        # Eliminate the correct number from the list of posible number on all the others box on the same square.
        hs = math.ceil((h + 1) / 3) - 1 # Auxiliar coordinate to select the rigth square
        vs = math.ceil((v + 1) / 3) - 1 #
            
        for i in range(3):
            for j in range(3):
                if (hs * 3) + i == h and (vs * 3) + j == v:
                    continue
                
                if val not in self.valid_numbers[(vs * 3) + j][(hs * 3) + i]:
                    continue
                else:
                    self.valid_numbers[(vs * 3) + j][(hs * 3) + i].remove(val)
        
        game.show_board()
        
    # This method solve the puzzle.
    def solve(self):
        changes = False # State that verify if a modification on the board was made.
        
        for i in range(9):
            not_valid_numb_row = [] # Save repeat numbers to skip when are found again on the list of posible numbers on the same row.
            not_valid_numb_col = [] # Save repeat numbers to skip when are found again on the list of posible numbers on the same column.
            for j in range(9):
                if self.verified_values[i][j] == True:
                    continue

                # Verify if each box only have one posible number and set it.
                if len(self.valid_numbers[i][j]) == 1 and self.verified_values[i][j] == False:
                    self.set_values(i, j, self.valid_numbers[i][j][0], "Unico DISPONIBLE", i, j)
                    changes = True

                # For each posible number on the list of posible numbers, verify if only can be in that box for each line.
                for num in self.valid_numbers[i][j]:
                    if num in not_valid_numb_row:
                            continue
                        
                    for k in range(9):
                        if self.verified_values[i][k] == True or k == j:
                            continue
                                                
                        if num in self.valid_numbers[i][k]:
                            not_valid_numb_row.append(num)
                            break
                    
                    if num not in not_valid_numb_row:    
                        self.set_values(i, j, num, "Unico en la LINEA", i)
                        changes = True

                # For each posible number on the list of posible numbers, verify if only can be in that box for each column.
                for num in self.valid_numbers[j][i]:     
                    if num in not_valid_numb_col:
                            continue
                    
                    for k in range(9):
                        if self.verified_values[k][i] == True or k == j:
                            continue
                                                    
                        if num in self.valid_numbers[k][i]:
                            not_valid_numb_col.append(num)
                            break
                    
                    if num not in not_valid_numb_col:
                        self.set_values(j, i, num, "Unico en la COLUMNA", j)
                        changes = True

        # Iterate for each on of the nine squares.
        for i in range(3):
            for j in range(3):
                not_valid_numb_sqr =[] # Save repeat numbers to skip when are found again on the list of posible numbers on the same square.
                for k in range(9):
                    I = (math.ceil((k + 1) / 3) - 1) + i*3  # Transform the inner coordinate to real coordinate.
                    J = (math.ceil((k + 1)) - 1) % 3 + j*3
                    
                    if self.verified_values[I][J] == True:
                        continue
                    
                    # For each posible number on the list of posible numbers, verify if only can be in that box for each square.
                    for num in self.valid_numbers[I][J]:
                        if num in not_valid_numb_sqr:
                            break
                        
                        for l in range(9):
                            y = (math.ceil((l + 1) / 3) - 1) + i*3
                            x = (math.ceil((l + 1)) - 1) % 3 + j*3
                            
                            if y == I and x == J:
                                continue
                            
                            if num in self.valid_numbers[y][x]:
                                not_valid_numb_sqr.append(num)
                                break
                        
                        if num not in not_valid_numb_sqr:
                            self.set_values(I, J, num, "Unico en el CUADRADO", i, j)
                            changes = True

        # If the board has a change then ejecute the verification again. 
        # Other wise verify if all boxes were solved and determinate if the puzzle was solved or not          
        if changes == True:
            self.solve()
        else:
            for i in range(9):
                for j in range(9):
                    if self.verified_values[i][j] == False:
                        print("It's unsolveble")
                        self.show_board()
                        exit()

            print("PUZZLE SOLVED!")
            self.show_board()
            return
                            
        
                    
test_matrix = [['-','-','-','-','-','-','-',6,3],[2,3,'-','-','-','-',1,7,'-'],[1,'-',4,'-','-','-','-','-','-'],['-',2,'-','-','-','-',4,'-','-'],['-','-',6,8,5,3,'-','-','-'],['-','-','-','-',7,'-',9,'-','-'],['-','-','-',5,9,6,'-','-',8],['-',4,'-','-','-','-',3,'-','-'],['-',7,'-','-',8,'-','-','-','-']]
matrix = [["-" for i in range(9)] for j in range(9)]
game = Board(matrix)

game.show_board()

solved = False
print("Introduce the coordinates and the value in this format: 'vh#'.")

def test(m):
    print(game.valid_numbers)
    if not game.on_seting:
            for i in range(9):
                for j in range(9):
                    print("(",i,", ", j, ")")
                    if m[i][j] != "-":                        
                        game.set_values(i, j, m[i][j], "Test")
                        
    else:
        print("You can't test the game ones the setup is started.")
    
    print("Fin Carga del Test:", end="\n\n")    
    for i in range(9):
        for k in range(9):
            print('%20s' % game.valid_numbers[i][k], sep=" - ", end="")
        print("")
    print("\n\n")
                
while not solved:
    data = (input("Enter new value or 'solve': "))
            

            
    if data == "solve":
        start = time.time()
        game.solve()
        print(time.time() - start, " segundos.")
        solved = True
    elif data == "test":
        test(test_matrix)
        game.show_board()
    else:
        try:
            print(data)
                        
            if len(data) != 3 or int(data[0]) < 0 or int(data[0]) > 8 or int(data[1]) < 0 or int(data[1]) > 8 or int(data[2]) < 1 or int(data[2]) > 9:
                raise ValueError
            
            game.set_values(int(data[0]), int(data[1]), int(data[2]), "User")
        except ValueError:
            print("Please, enter a correct input.")     
            