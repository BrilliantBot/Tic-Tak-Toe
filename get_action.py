import numpy as np
import random

class Player():
    def __init__(self, name, start = False):
        self.values = {0:0}
        self.name = name
        self.turn = start
        self.epsilon = 1
        
        
def get_action(player1, player2):
    global spot_placeholders
    
    """Find out which players turn it is, and set thier marker and epsilon."""
    if player1.turn == True:
        marker = 1
        epsilon = player1.epsilon
    else:
        marker = 2
        epsilon = player2.epsilon
    
    players = [player1,player2]
    possible_next_states = {}
    top_value = -1
    
    """loop through every spot and, if it's empty, record the state that
    would come from the player moving in that spot"""    
    for i in range(len(spot_placeholders)):
        if spot_placeholders[i] == 0:
            copy = np.copy(spot_placeholders)
            copy[i] = marker
            s_p = state_to_num(copy)
            possible_next_states[i] = s_p
    
    """Epsilon greedy"""
    if np.random.rand() < epsilon:
        if players[marker-1].epsilon > .05:
            players[marker-1].epsilon -= .001
        return random.sample(possible_next_states.keys(),1)[0]
    
    else:
        i = 0
        for state in possible_next_states.values():
            try:
                """if the current players value for this state is higher than the 
                top recorded value, set the top value to the value of this state 
                and set action = the spot that will lead to this state"""
                if players[marker-1].values(state) > top_value:
                    top_value = players[marker-1].values(state)
                    action = list(possible_next_states.keys())[i]
            except:
                pass
            i +=1
            
        if players[marker-1].epsilon > .05:
            players[marker-1].epsilon -= .001
        
        """if there was no action set, return a random action"""
        try:
            return action
        except:
            return random.sample(possible_next_states.keys(),1)[0]


