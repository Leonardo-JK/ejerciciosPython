import math
import time


class Board:
        
    def __init__(self,matrix, on_seting=False):
        self.values = matrix
        self.valid_numbers = [[[1,2,3,4,5,6,7,8,9] for i in range(9)] for j in range(9)]
        self.verified_values = [[False for i in range(9)] for j in range(9)]
        self.on_seting = on_seting
    
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
                
                
    def set_values(self, v, h, val, send, k=None, l=None):
        
        
            print("")
            print("Linea: ", v, " - Columna: ", h, " - Numero: ", val, " - Enviado por: ", send, " (", k, ", ", l, ")", end=" ->")
                    
            self.values[v][h] = val
            self.verified_values[v][h] = True
            self.valid_numbers[v][h].clear()
            self.valid_numbers[v][h].append(val)
            
            for r in range(9):
                if r == h:
                    continue
                
                if val not in self.valid_numbers[v][r]:
                    continue
                else:
                    self.valid_numbers[v][r].remove(val)        
            
            for c in range(9):
                if c  == v:
                    continue
                
                if val not in self.valid_numbers[c][h]:
                    continue
                else:
                    self.valid_numbers[c][h].remove(val)
            
            hs = math.ceil((h + 1) / 3) - 1 
            vs = math.ceil((v + 1) / 3) - 1  
                
            for i in range(3):
                for j in range(3):
                    if (hs * 3) + i == h and (vs * 3) + j == v:
                        continue
                    
                    if val not in self.valid_numbers[(vs * 3) + j][(hs * 3) + i]:
                        continue
                    else:
                        self.valid_numbers[(vs * 3) + j][(hs * 3) + i].remove(val)
            
    
    def solve(self):
        changes = False
        
        print("Inicio cerificacion UNICO DISPONIBLE:", end="\n\n")
        #Verifica si solo hay un numero disponible
        for i in range(9):
            for j in range(9):                
                if len(self.valid_numbers[i][j]) == 1 and self.verified_values[i][j] == False:
                    self.set_values(i, j, self.valid_numbers[i][j][0], "Unico DISPONIBLE", i, j)
                    changes = True
        print("")            
        print("Fin verificacion de unico disponible", end="\n\n")
        for i in range(9):
                for k in range(9):
                    print('%20s' % game.valid_numbers[i][k], sep=" - ", end="")
                print("")
        print("\n\n")
        
        if changes == True:
            print("REINICIO DE COMPROVACIONES")
            print("")
            self.solve()
            
        # 
        print("Inicio verificacion de LINEAS:", end="\n\n")
        #Verifica si es el unico posible en la linea
        for i in range(9):
            not_valid_numb_row = []   
            for j in range(9):
                if self.verified_values[i][j] == True:
                    continue  
                
                for num in self.valid_numbers[i][j]:
                    if num in not_valid_numb_row:
                            continue
                        
                    for k in range(9):
                        if self.verified_values[i][k] == True or k == j:
                            continue
                                                
                        if num in self.valid_numbers[i][k]:
                            not_valid_numb_row.append(num)
                            break
                    print("Linea: ", i)    
                    print(not_valid_numb_row)
                    print("")
                    
                    if num not in not_valid_numb_row:    
                        self.set_values(i, j, num, "Unico en la LINEA", i)
                        changes = True       
        print("")                    
        print("Fin verificacion de LINEAS.", end="\n\n")
        for i in range(9):
            for k in range(9):
                print('%20s' % game.valid_numbers[i][k], sep=" - ", end="")
            print("")
        print("\n\n")
                    
        if changes == True:
            print("REINICIO DE COMPROVACIONES")
            print("")
            self.solve()    
            
        print("Inicio de verificacion de COLUMNAS:", end="\n\n")               
        #Verifica si es el unico en la columna  
        for i in range(9):
            not_valid_numb_col = []   
            for j in range(9):
                if self.verified_values[j][i] == True:
                    continue
                
                for num in self.valid_numbers[j][i]: 
                    print("Columna: ", i, "Linea: ", j, " - Numero: ", num)     
                    if num in not_valid_numb_col:
                            continue
                    
                    for k in range(9):
                        if self.verified_values[k][i] == True or k == j:
                            continue
                                                    
                        if num in self.valid_numbers[k][i]:
                            not_valid_numb_col.append(num)
                            break
                    
                    print("Numeros repetidos: ", not_valid_numb_col)
                    print("") 
                    
                    if num not in not_valid_numb_col:
                        self.set_values(j, i, num, "Unico en la COLUMNA", j)
                        changes = True
        print("")                
        print("Fin verificacion de COLUMNAS.", end="\n\n")
        for i in range(9):
            for k in range(9):
                print('%20s' % game.valid_numbers[i][k], sep=" - ", end="")
            print("")
        print("\n\n")
                    
        if changes == True:
            print("REINICIO DE COMPROVACIONES")
            print("")
            self.solve()
        
        print("Inicio de verificacion de CUADRADOS:", end="\n\n")
        #Verifica si es el unico en el cuadrado
        for i in range(3):
            for j in range(3):
                not_valid_numb_sqr =[] 
                for k in range(9):
                    I = (math.ceil((k + 1) / 3) - 1) + i*3
                    J = (math.ceil((k + 1)) - 1) % 3 + j*3
                    
                    if self.verified_values[I][J] == True:
                        continue
                    
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
                        print("Cuandrado: ", i, j)
                        print(not_valid_numb_sqr)
                        print("") 
                    
                        if num not in not_valid_numb_sqr:
                            self.set_values(I, J, num, "Unico en el CUADRADO", i, j)
                            changes = True
        print("")                
        print("Fin verificacion CUADRADOS", end="\n\n")
        for i in range(9):
            for k in range(9):
                print('%20s' % game.valid_numbers[i][k], sep=" - ", end="")
            print("")
        print("\n\n")                    
                    
        if changes == True:
            self.solve()
        else:
            sum = 0
            
            for i in range(9):
                for j in range(9):
                    sum += len(self.valid_numbers[i][j])  
            
            if sum == 81:
                print("PUZZLE SOLVED!")
                self.show_board()
                exit()
            else:              
                print("It's unsolveble")
                self.show_board()
                exit()                        
        
                    
test_matrix = [['-','-','-','-','-','-','-','-','-'],['-',2,'-','-',5,'-',6,'-','-'],['-',8,'-','-',4,'-',1,'-','-'],['-','-','-','-',2,9,'-','-',1],['-','-',1,8,'-','-','-',7,'-'],['-',5,'-',3,'-','-','-',8,'-'],['-',3,'-','-','-',8,'-','-',7],['-','-','-',1,'-','-',5,6,'-'],[7,'-','-','-','-',6,'-','-',9]]
matrix = [["-" for i in range(9)] for j in range(9)]
game = Board(matrix)

game.show_board()

solved = False
print("Introduce the coordinates and the value in this format: 'v h #'")

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
    print(data)
    if data == "solve":
        game.solve()
        game.show_board()
        solved = True
    elif data == "test":
        test(test_matrix)
        game.show_board()
    else:
        values = data.split(" ")
        print(values)
        print(game.valid_numbers)
        game.set_values(int(values[0]), int(values[1]), int(values[2]), "User")
        game.show_board()
        print(game.valid_numbers)
        
