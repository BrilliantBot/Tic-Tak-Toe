def play_game(player1,player2):
    global spot_placeholders 
    state_history = []
    
    while True:
        
        if player1.turn == True:
            a = get_action(player1,player2)
            spot_placeholders[a] = 1
            state_history.append(state_to_num(spot_placeholders))
            
            if check_for_winner() == True:
                print('Winner = ' + player1.name)
                spot_placeholders = [0,0,0,0,0,0,0,0,0]
                update_values(player1,state_history,True)
                update_values(player2,state_history)
                break
            
        if player2.turn == True:
            a = get_action(player1,player2)
            spot_placeholders[a] = 2
            state_history.append(state_to_num(spot_placeholders))
            
            if check_for_winner() == True:
                print('Winner = ' + player2.name)
                spot_placeholders = [0,0,0,0,0,0,0,0,0]
                update_values(player2,state_history,True)
                update_values(player1,state_history)
                
                break
            
        if check_for_winner() == 'CatGame':
            print('CatGame!')
            spot_placeholders = [0,0,0,0,0,0,0,0,0]
            update_values(player1,state_history)
            update_values(player2,state_history)
            break
        
        player1.turn = not player1.turn
        player2.turn = not player2.turn
      
def update_values(player,state_history,winner=False):
    player.values[state_history[-1]] = -1
    if winner == True:
        player.values[state_history[-1]] = 1
    
    for state in state_history:
        if state not in player.values:
            player.values[state] = 0
    
    for i in range(len(state_history)-1,0,-1):
        player.values[state_history[i-1]] += .1*(player.values[state_history[i]] - player.values[state_history[i-1]])
