# Name: Melba Nuzen
# CMS cluster login name: mnuzen

# include docstrings for all functions, comment out non-code answers


# Part 1: Pitfalls

# 1.1:
# 1) i % j = 0 is an assertion, and the boolean statement should read i % j == 0
# 2) takes in a string 'n' always; the function should take in a variable n 
# 3) 

# Part 2: Simple Functions 

import random, sys
import random, sys, time

# 2.1:
def draw_tictactoe(n):
    '''Takes in integer n that represents the  height and width of each square
    within the tic-tac toe board.'''
    assert n > 0
    ret = ""

    base = " "*n + "|" + " "*n + "|" + " "*n + "\n"
    divide = "-"*n + "+" + "-"*n + "+" + "-"*n + "\n"

    ret = base*n + divide + base*n + divide + base*n
    
    return ret
    

def test_draw_tictactoe():
    
    print(draw_tictactoe(1))
    print(draw_tictactoe(2))
    print(draw_tictactoe(3))
    print(draw_tictactoe(4))
    print(draw_tictactoe(5))

# 2.2:

def rps(player1, player2):
    '''Returns 0 if there is a tie, 1 if 1 is the winner, and 2 if 2 is the
    winner.'''
    assert (player1 == "R") or (player1 == "P") or (player1 == "S")
    assert (player2 == "R") or (player2 == "P") or (player2 == "S")
    
    w = int()
    
    dic = {"R":"S", "P":"R", "S":"P"}
    
    if player1 == player2:
        w = 0  
    if dic[player1] == player2:
        w = 1    
    if dic[player2] == player1:
        w = 2
        
    return w

def rpslk(player1, player2):
    ''' Returns 0 if there is a tie, 1 is 1 is the winner, and 2 if 2 is the 
    winner.'''
    assert (player1 == "R") or (player1 == "P") or (player1 == "S") or \
           (player1 == "L") or (player1 == "K")
    assert (player2 == "R") or (player2 == "P") or (player2 == "S") or \
           (player2 == "L") or (player2 == "K")
    
    dic = {"R":"LS", "P":"RK", "S":"PL", "L":"KP", "K":"SR"}
    
    if player1 == player2:
        w = 0  
    if player2 in dic[player1]:
        w = 1
    if player1 in dic[player2]:
        w = 2
        
    return w   

def rpslk2(player1, player2):
    '''  '''

# 2.3: 

### Supplied to students.

ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
suits = ['S', 'H', 'D', 'C']

def validate_hand(hand):
    '''
    Validate a Poker hand.  If the hand is invalid, an assertion violation occurs.
    '''

    assert type(hand) is list
    assert len(hand) == 5
    for card in hand:
        assert type(card) is tuple
        assert len(card) == 2
        assert card[0] in ranks
        assert card[1] in suits

def random_hand():
    '''
    Return a randomly-generated Poker hand.

    Cards are represented as (rank, suit) tuples.
    Ranks are 2-10, or 'J', 'Q', 'K', 'A'
    Suits are one of 'S', 'H', 'D', 'C'
    '''

    # This uses a "list comprehension", which we haven't seen yet.
    deck = [(r, s) for r in ranks for s in suits]
    random.shuffle(deck)
    hand = deck[:5]
    # This uses "lambda", which we haven't seen yet.
    hand.sort(key=lambda c: ranks.index(c[0]))
    validate_hand(hand)
    return hand

def test_random_hand():
    '''
    Create a random hand, print it, and print its Poker rank.
    '''
    hand = random_hand()
    print(hand, poker_rank(hand))

def find_hand(p_rank):
    '''
    Print the first random hand that has a particular poker rank.
    Argument:
      p_rank: a poker rank
    '''
    count = 0
    while True:
        count += 1
        hand = random_hand()
        pr = poker_rank(hand)
        if pr == p_rank:
            print()
            break
        else:
            print('.', end='')
            sys.stdout.flush()
    print(hand, pr, count)

### End supplied to students.

# Helper functions for 'poker_rank' function go here.

def poker_rank(hand):
    '''
    DOCSTRING TODO
    '''

    pass  # TODO


# Part 3: Miniproject - Conway's Game of "Life"

def make_empty_board(nrows, ncols):
    '''
    DOCSTRING TODO
    '''

    pass  # TODO

def make_random_board(nrows, ncols, p):
    '''
    DOCSTRING TODO
    '''

    pass  # TODO

def display_board(board):
    '''
    DOCSTRING TODO
    '''

    pass  # TODO

def board_sums(board):
    '''
    DOCSTRING TODO
    '''

    pass  # TODO

def display_board_sums(board):
    '''
    DOCSTRING TODO
    '''

    pass  # TODO

def board_update(board):
    '''
    DOCSTRING TODO
    '''

    pass  # TODO

def board_to_num(board):
    '''
    DOCSTRING TODO
    '''

    pass  # TODO

### Supplied to students:

def interact(nrows, ncols, p):
    '''
    Print the board and update it interactively until the user doesn't want
    to continue any more.  The user presses <return> to print the next
    generation to the terminal and enters "." to end the simulation.

    Arguments:
      nrows: number of rows (an integer > 0)
      ncols: number of columns (an integer > 0)
      p: a float in the range [0.0, 1.0]

    Return value: nothing
    '''

    answer = ''

    b = make_random_board(nrows, ncols, p)
    while True:
        print(display_board(b))
        answer = input()
        if answer == ".":
            break
        b = board_update(b)

def run_to_end(nrows, ncols, p, delay = 0.1):
    '''
    Print the board and update it non-interactively until the display repeats an
    earlier configuration, at which point the simulation stops.

    Arguments:
      nrows: number of rows (an integer > 0)
      ncols: number of columns (an integer > 0)
      p: a float in the range [0.0, 1.0]
      delay: time delay between printing of generations, in seconds

    Return value: nothing
    '''

    answer = ''
    seen = {}

    b = make_random_board(nrows, ncols, p)
    while True:
        print(display_board(b))
        time.sleep(delay)
        b = board_update(b)
        n = board_to_num(b)
        if n in seen:
            break
        seen[n] = 1

### End supplied to students.

