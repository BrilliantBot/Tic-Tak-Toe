spot_placeholders = [0,0,0,0,0,0,0,0,0]
class Player():
    def __init__(self, name, start = False):
        self.values = {0:.5}
        self.name = name
        self.turn = start

def get_action(player):
    while True:
        action = int(input(player.name + ', Where would you like to go?\n Move: '))
        if spot_placeholders[action] == 0:
            return action
        else:
            continue

def print_board():
    board = []
    for spot in spot_placeholders:
        if spot == 0:
            board.append('_')
        if spot == 1:
            board.append('X')
        if spot == 2:
            board.append('O')
    print(board[0],board[1],board[2])
    print(board[3],board[4],board[5])
    print(board[6],board[7],board[8])

def check_for_winner():
    if spot_placeholders[0] == spot_placeholders[1] and spot_placeholders[1] == spot_placeholders[2] and spot_placeholders[2] != 0:
        return True
    if spot_placeholders[0] == spot_placeholders[3] and spot_placeholders[3] == spot_placeholders[6] and spot_placeholders[6] != 0:
        return True
    if spot_placeholders[0] == spot_placeholders[4] and spot_placeholders[4] == spot_placeholders[8] and spot_placeholders[8] != 0:
        return True
    if spot_placeholders[1] == spot_placeholders[4] and spot_placeholders[4] == spot_placeholders[7] and spot_placeholders[7] != 0:
        return True
    if spot_placeholders[2] == spot_placeholders[4] and spot_placeholders[4] == spot_placeholders[6] and spot_placeholders[6] != 0:
        return True
    if spot_placeholders[2] == spot_placeholders[5] and spot_placeholders[5] == spot_placeholders[8] and spot_placeholders[8] != 0:
        return True
    if spot_placeholders[6] == spot_placeholders[7] and spot_placeholders[7] == spot_placeholders[8] and spot_placeholders[8] != 0:
        return True
    if spot_placeholders[3] == spot_placeholders[4] and spot_placeholders[4] == spot_placeholders[5] and spot_placeholders[5] != 0:
        return True
    elif (spot_placeholders[0] != 0 and spot_placeholders[1] != 0 and
          spot_placeholders[2] != 0 and spot_placeholders[3] != 0 and
          spot_placeholders[4] != 0 and spot_placeholders[5] != 0 and
          spot_placeholders[6] != 0 and spot_placeholders[7] != 0 and
          spot_placeholders[8] != 0):
        return 'CatGame'
    else:
        return False
    
def play_game(player1,player2):
    global spot_placeholders 
    
    while True:
        print_board()
        if player1.turn == True:
            a = get_action(player1)
            spot_placeholders[a] = 1
            if check_for_winner() == True:
                print('Winner = ' + player1.name)
                spot_placeholders = [0,0,0,0,0,0,0,0,0]
                break
        if player2.turn == True:
            a = get_action(player2)
            spot_placeholders[a] = 2
            if check_for_winner() == True:
                print('Winner = ' + player2.name)
                spot_placeholders = [0,0,0,0,0,0,0,0,0]
                break
        if check_for_winner() == 'CatGame':
            print('CatGame!')
            spot_placeholders = [0,0,0,0,0,0,0,0,0]
            break
        
        player1.turn = not player1.turn
        player2.turn = not player2.turn
      
        

p1 = Player('Computer 1', True) 
p2 = Player('Computer 2')   

play_game(p1,p2)
