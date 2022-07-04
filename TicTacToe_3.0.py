import random
import copy

print("Welcome to Tic-Tac-Toe!")
print("The board is enumerate like this:")

board_matrix = [[j+(i*3)+1 for j in range(3)] for i in range(3)]
board_values = [[int(0) for j in range(3)] for i in range(3)]
start_game = True

def show_board():
    for i in range(3):
        print(f'{board_matrix[i][0] if board_matrix[i][0] else " "} | {board_matrix[i][1] if board_matrix[i][1] else " "} | {board_matrix[i][2] if board_matrix[i][2] else " "}')
    print("")
    
    
show_board()

print("How you want to play?","", "1)- Player 1 vs Player 2", "2)- Player 1 vs PC", sep="\n", end="\n")

selection = 0       
position_avaible = [1,2,3,4,5,6,7,8,9]
position_taked = []

def take(num, play):
    for i in range(3):
        for j in range(3):
            if num == board_matrix[i][j]:
                board_matrix[i][j] = play
                del position_avaible[position_avaible.index(num)]
                
                if play == "O":
                    board_values[i][j] = int(-1)
                else:
                    board_values[i][j] = int(1)
                break
            
def best_choise():
    position = check_x_victory()
        
    print(position_avaible, end="\n\n")
        
    if start_game == True:
        return random.choice(position_avaible)
    else:
        best = [0,0,0]
        
        for n in range(len(position_avaible)):            
            for i in range(3):
                for j in range(3):                    
                    
                    if position_avaible[n] == board_matrix[i][j]:
                        board_values_aux = copy.deepcopy(board_values)
                        board_values_aux[i][j] = int(-1)

                        for k in range(3):
                            sum_ve = sum_v(k, board_values_aux)
                            if sum_ve < best[0]:
                                best[0] = sum_ve
                                best[1], best[2] = i, j

                            sum_ho = sum_h(k, board_values_aux)
                            if sum_ho < best[0]:
                                best[0] = sum_ho
                                best[1], best[2] = i, j

                            sum_d1 = sum_d(1, board_values_aux)
                            if sum_d1 < best[0]:
                                best[0] = sum_d1
                                best[1], best[2] = i, j

                            sum_d2 = sum_d(-1, board_values_aux)
                            if sum_d2 < best[0]:
                                best[0] = sum_d2
                                best[1], best[2] = i, j
        
        if best[0] == -3 or position == False:    
            return board_matrix[best[1]][best[2]]
        else:
            return board_matrix[position[0]][position[1]]
        
def check_x_victory():
    for i in range(3):
        count_ones = 0
        position = 0
        for j in range(3):
            if board_values[i][j] == 1:
                count_ones += 1
            elif board_values[i][j] == 0:
                position = j
            elif board_matrix[i][j] == "O":
                count_ones = 0
                break

        if count_ones == 2:
            print(f"X can win! H ({i, position})" )
            return [i, position]
        
    for j in range(3):
        count_ones = 0
        position = 0
        for i in range(3):
            if board_values[i][j] == 1:
                count_ones += 1
            elif board_values[i][j] == 0:
                position = i
            elif board_matrix[i][j] == "O":
                count_ones = 0
                break
        
        if count_ones == 2:
            print(f"X can win! V ({position, j})" )
            return [position, j] 
    

    count_ones1 = 0
    position1 = [0,0]
    count_ones2 = 0
    position2 = [0,0]
    
    for j in range(3):
        if board_values[j][j] == 1:
            count_ones1 += 1
        elif board_values[j][j] == 0:
            position1 = [j, j]
        elif board_matrix[j][j] == "O":
            count_ones1 = 0
            break
        
    for j in range(3):
        if board_values[j][2-j] == 1:
            count_ones2 += 1
        elif board_values[j][2-j] == 0:
            position2 = [j, 2-j]
        elif board_matrix[j][2-j] == "O":
            count_ones2 = 0
            break
        
    if count_ones1 == 2:
        print(f"X can win! D1 ({position1})" )
        return position1  
    
    if count_ones2 == 2:
        print(f"X can win! D2 ({position2})" )
        return position2  
    
    return False

def sum_v(col,values):
    sum_ve = 0
    
    for i in range(3):
        sum_ve += values[i][col]
    
    return sum_ve

def sum_h(row, values):
    sum_ho = 0
    
    for i in range(3):
        sum_ho += values[row][i]  
        
    return sum_ho

def sum_d(dia, values):
    sum_di = 0
        
    if dia == 1:
        for i in range(3):
            sum_di += values[i][i * dia]
    elif dia == -1:
        for i in range(3):
            sum_di += values[i][(2-i)]
    
    return sum_di

def check(num):
    if num not in position_avaible:
        return True
    else:
        return False
    
def there_is_winner():
    for i in range(3):
        sum_ve = sum_v(i, board_values)
        if abs(sum_ve) == 3:
            return sum_ve
        
        sum_ho = sum_h(i, board_values)
        if abs(sum_ho) == 3:
            return sum_ho

    sum_di1 = sum_d(1, board_values)
    if abs(sum_di1) == 3:
        return sum_di1
    
    sum_di2 = sum_d(-1, board_values)
    if abs(sum_di2) == 3:
        return sum_di2
    
win = False

def playerVsPc():
    print("\n", "I'm first! I play with O's, you play with  X's.")
    
    while not win:
        take(best_choise(), "O")
        show_board()
        global start_game
        start_game = False
        
        if there_is_winner() == -3:
            print("I WIN!")
            print(board_values)
            break
        
        if len(position_avaible) == 0:
            print("Empate!")
            break
        
        player_choice = int(input("Your turn:"))
        
        while check(player_choice):
            player_choice = int(input("Choice an avaible number of the board:"))
        
        take(player_choice, "X")
        show_board()
        
        if there_is_winner() == 3:
            print("You WIN!")
            break

def playerVsPlayer():
    player = "O"
    while not win:
        player_choice = int(input(f"{player}'s turn:"))
        
        while check(player_choice):
            player_choice = int(input("Choice an avaible number of the board:"))
            
        take(player_choice, player)       
        show_board()
        
        if there_is_winner() == -3:
            print("Player with O WIN!")
            break
        elif there_is_winner() == 3:
            print("Player with X WIN!")
            break
        
        if player == "O":
            player = "X"
        else:
            player = "O"

while selection == 0:
    selection = int(input(""))
    
    if selection == 1:
        playerVsPlayer()
    elif selection == 2:
        playerVsPc()
    else:
        print("You can chose only 1 or 2.")
        selection = 0