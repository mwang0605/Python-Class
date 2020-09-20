def playingboard():
    print('          |          |')
    print('          |          |')
    print('----------------------------------')
    print('          |          |')
    print('          |          |')
    print('----------------------------------')
    print('          |          |')
    print('          |          |')
playingboard()

player1_moves = []


def placing_pieces_player1():
    player_input = input('Player One where do you want to go? (ex. middle middle, top middle, bottom middle): ')
    if player_input == 'top left':
        player1_moves.append('top left')
        print('    XX    |          |')
        print('    XX    |          |')
        print('----------------------------------')
        print('          |          |')
        print('          |          |')
        print('----------------------------------')
        print('          |          |')
        print('          |          |')
    elif player_input == 'top middle':
        player1_moves.append('top middle')
        print('          |    XX    |')
        print('          |    XX    |')
        print('----------------------------------')
        print('          |          |')
        print('          |          |')
        print('----------------------------------')
        print('          |          |')
        print('          |          |')
    elif player_input == 'top right':
        player1_moves.append('top right')
        print('          |          |     XX     ')
        print('          |          |     XX     ')
        print('----------------------------------')
        print('          |          |')
        print('          |          |')
        print('----------------------------------')
        print('          |          |')
        print('          |          |')
    elif player_input == 'middle left':
        player1_moves.append('middle left')
        print('          |          |')
        print('          |          |')
        print('----------------------------------')
        print('   XX     |          |')
        print('   XX     |          |')
        print('----------------------------------')
        print('          |          |')
        print('          |          |')
    elif player_input == 'middle middle':
        player1_moves.append('middle middle')
        print('          |          |')
        print('          |          |')
        print('----------------------------------')
        print('          |    XX    |')
        print('          |    XX    |')
        print('----------------------------------')
        print('          |          |')
        print('          |          |')
    elif player_input == 'middle right':
        player1_moves.append('middle right')
        print('          |          |')
        print('          |          |')
        print('----------------------------------')
        print('          |          |      XX    ')
        print('          |          |      XX    ')
        print('----------------------------------')
        print('          |          |')
        print('          |          |')
    elif player_input == 'bottom left':
        player1_moves.append('bottom left')
        print('          |          |')
        print('          |          |')
        print('----------------------------------')
        print('          |          |')
        print('          |          |')
        print('----------------------------------')
        print('   XX     |          |')
        print('   XX     |          |')
    elif player_input == 'bottom middle':
        player1_moves.append('bottom middle')
        print('          |          |')
        print('          |          |')
        print('----------------------------------')
        print('          |          |')
        print('          |          |')
        print('----------------------------------')
        print('          |    XX    |')
        print('          |    XX    |')
    elif player_input == 'bottom right':
        player1_moves.append('bottom right')
        print('          |          |')
        print('          |          |')
        print('----------------------------------')
        print('          |          |')
        print('          |          |')
        print('----------------------------------')
        print('          |          |     XX     ')
        print('          |          |     XX     ')
    return
placing_pieces_player1()

player2_moves = []

def placing_pieces_player2():
    player_input = input('Player Two where do you want to go? (ex. middle middle, top middle, bottom middle): ')
    if player1_moves == ['top left']:
        print('    XX    |          |')
        print('    XX    |          |')
        print('----------------------------------')
        print('          |          |')
        print('          |          |')
        print('----------------------------------')
        print('          |          |')
        print('          |          |')
    elif player1_moves == ['top middle']:
        print('          |    XX    |')
        print('          |    XX    |')
        print('----------------------------------')
        print('          |          |')
        print('          |          |')
        print('----------------------------------')
        print('          |          |')
        print('          |          |')
    elif player1_moves == ['top right']:
        print('          |          |     XX     ')
        print('          |          |     XX     ')
        print('----------------------------------')
        print('          |          |')
        print('          |          |')
        print('----------------------------------')
        print('          |          |')
        print('          |          |')
    elif player1_moves == ['middle left']:
        print('          |          |')
        print('          |          |')
        print('----------------------------------')
        print('   XX     |          |')
        print('   XX     |          |')
        print('----------------------------------')
        print('          |          |')
        print('          |          |')
    elif player1_moves == ['middle middle']:
        print('          |          |')
        print('          |          |')
        print('----------------------------------')
        print('          |    XX    |')
        print('          |    XX    |')
        print('----------------------------------')
        print('          |          |')
        print('          |          |')
    elif player1_moves == ['middle right']:
        print('          |          |')
        print('          |          |')
        print('----------------------------------')
        print('          |          |      XX    ')
        print('          |          |      XX    ')
        print('----------------------------------')
        print('          |          |')
        print('          |          |')
    elif player1_moves == ['bottom left']:
        print('          |          |')
        print('          |          |')
        print('----------------------------------')
        print('          |          |')
        print('          |          |')
        print('----------------------------------')
        print('   XX     |          |')
        print('   XX     |          |')
    elif player1_moves == ['bottom middle']:
        print('          |          |')
        print('          |          |')
        print('----------------------------------')
        print('          |          |')
        print('          |          |')
        print('----------------------------------')
        print('          |    XX    |')
        print('          |    XX    |')
    elif player1_moves == ['bottom right']:
        print('          |          |')
        print('          |          |')
        print('----------------------------------')
        print('          |          |')
        print('          |          |')
        print('----------------------------------')
        print('          |          |     XX     ')
        print('          |          |     XX     ')

#part two

    if player_input == 'top left':
        player2_moves.append('top left')
        print('    OO    |          |')
        print('    OO    |          |')
        print('----------------------------------')
        print('          |          |')
        print('          |          |')
        print('----------------------------------')
        print('          |          |')
        print('          |          |')
    elif player_input == 'top middle':
        player2_moves.append('top middle')
        print('          |    OO    |')
        print('          |    OO    |')
        print('----------------------------------')
        print('          |          |')
        print('          |          |')
        print('----------------------------------')
        print('          |          |')
        print('          |          |')
    elif player_input == 'top right':
        player2_moves.append('top right')
        print('          |          |     OO     ')
        print('          |          |     OO     ')
        print('----------------------------------')
        print('          |          |')
        print('          |          |')
        print('----------------------------------')
        print('          |          |')
        print('          |          |')
    elif player_input == 'middle left':
        player2_moves.append('middle left')
        print('          |          |')
        print('          |          |')
        print('----------------------------------')
        print('   OO     |          |')
        print('   OO     |          |')
        print('----------------------------------')
        print('          |          |')
        print('          |          |')
    elif player_input == 'middle middle':
        player2_moves.append('middle middle')
        print('          |          |')
        print('          |          |')
        print('----------------------------------')
        print('          |    OO    |')
        print('          |    OO    |')
        print('----------------------------------')
        print('          |          |')
        print('          |          |')
    elif player_input == 'middle right':
        player2_moves.append('middle right')
        print('          |          |')
        print('          |          |')
        print('----------------------------------')
        print('          |          |      OO    ')
        print('          |          |      OO    ')
        print('----------------------------------')
        print('          |          |')
        print('          |          |')
    elif player_input == 'bottom left':
        player2_moves.append('bottom left')
        print('          |          |')
        print('          |          |')
        print('----------------------------------')
        print('          |          |')
        print('          |          |')
        print('----------------------------------')
        print('   OO     |          |')
        print('   OO     |          |')
    elif player_input == 'bottom middle':
        player2_moves.append('bottom middle')
        print('          |          |')
        print('          |          |')
        print('----------------------------------')
        print('          |          |')
        print('          |          |')
        print('----------------------------------')
        print('          |    OO    |')
        print('          |    OO    |')
    elif player_input == 'bottom right':
        player2_moves.append('bottom right')
        print('          |          |')
        print('          |          |')
        print('----------------------------------')
        print('          |          |')
        print('          |          |')
        print('----------------------------------')
        print('          |          |     OO     ')
        print('          |          |     OO     ')
    return
placing_pieces_player2()
print(player2_moves)