# Name: Melba Nuzen
# CMS cluster login name: mnuzen

# include docstrings for all functions, comment out non-code answers


# Part 1: Pitfalls

# 1.1:
# 1) i % j = 0 is an assertion, and the boolean statement should read i % j == 0
# 2) takes in a string 'n' always; the function should take in a variable n 
# 3) the function docstring must have triple quotations: ''' or """
# 4) there must be a colon behind the while. while True: to indicate the 
# beginning of the code that runs. 
# 5) 

# 1.2:
# 1) the final print should print out num and count within one brace
# print('{num : count}')
# 2) variable count is not defined before printing
# 3) hist[n] == 1 is a boolean expression and should be just hist[n] = 1
# 4) the for loop only needs num as a key parameter to loop. with the key
# you can find the count of the num by saying print('{num : hist[num]}')
# 5) to loop through a dictionary keys, you need to use .keys() to extract
# the keys and convert them to a list that you can iterate through.

# 1.3:
# 1) the function must have a function name that accurately describes its 
# purpose.
# 2) there should spaces between each operator: for example, tt = 0 
# instead of tt=0.
# 3) indenting should be four spaces.
# 4) variable names should have something to do with what the variable
# represents.
# 5) comments should have a space after the #. like # 4, instead of #4. 
# comments should also explain code clearly.

# Part 2: Simple Functions 

import random, sys
import random, sys, time

# 2.1:
def draw_tictactoe(n):
    '''Takes in integer n that represents the  height and width of each square
    within the tic-tac toe board.'''
    assert n > 0
    ret = ""

    base = " "*n + "|" + " "*n + "|\n"
    divide = "-"*n + "+" + "-"*n + "+" + "-"*n + "\n"

    ret = "\n" + base*n + divide + base*n + divide + base*n + "\n"
    
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
    
def histogram_rank(hand):
    '''Takes in a hand and returns a dictionary of the number of times a value
    appears within the hand.'''
    lst_v = []
    dic_v = {}
    for card in list(hand):
        (val, suit) = card
        dic_v.update({val:suit})
        lst_v.append(val)
   
    dic_r = {}    
    key = list(dic_v.keys())
    for k in key:
        dic_r[k] = lst_v.count(k)  
          
    return dic_r

def histogram_suit(hand):
    '''Takes in a hand and returns a dictionary of the number of times a suit
    appears within the hand.'''
    lst_v = []
    dic_v = {}
    for card in list(hand):
        (val, suit) = card
        dic_v.update({suit:val})
        lst_v.append(suit)
   
    dic_r = {}    
    key = list(dic_v.keys())
    for k in key:
        dic_r[k] = lst_v.count(k)  
          
    return dic_r

def value(hand):
    '''Returns the numerical ranking of each card in the hand.'''
    ranks = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, \
             'J':11, 'Q':12, 'K':13, 'A':1}
    lst = []
    for card in hand:
        (val, suit) = card
        lst.append(ranks[val])
    return lst

def flush(vals):
    '''Checks if values are in a straight flush'''
    boo = False
    count = 0
    high = max(vals)
    s = high
    #need to check for royal flush bc now cards are not in order
    for i in range(1, len(vals)):
        if (high - i) in vals:
            count += 1
            s += (high - i)
            
    if count >= len(vals)-1:
        boo = True
    elif count == 3 and s == 46 and (1 in vals):
        boo = True
    return boo

def poker_rank(hand):
    '''Returns the rank of a poker hand.'''
    validate_hand(hand)
    rank = ""
       
    h_rank = histogram_rank(hand)
    h_suit = histogram_suit(hand)
    h_vals = value(hand)
    
    # check for no pair
    if len(h_rank) == 5 and len(h_suit) != 1:
        rank = "NP" 
    
    # check for flush
    if len(h_suit) == 1:
        rank = "FL"
        if flush(h_vals):
            rank = "SF"
              
    # check for straight
    else:
        if flush(h_vals) and len(h_suit) != 1:
            rank = "ST"       
    
    # check for pairs  
    vals = list(h_rank.values())
    largest = max(vals)
    length = len(vals)
    
    if largest == 4:
        rank = "4K"
    elif largest == 3:
        if length == 2:
            rank = "FH"
        if length == 3:
            rank = "3K"
    elif largest == 2:
        if length == 3:
            rank = "2P"
        if length == 4:
            rank = "1P"
            
    return rank
   



# Part 3: Miniproject - Conway's Game of "Life"

def make_empty_board(nrows, ncols):
    '''Takes in the number of columns and rows and creates an empty board.'''
    board = []
    for i in range(0, nrows):
        col = []        
        for j in range(0, ncols):
            col.append(0)
        board.append(col)
    return board

def make_random_board(nrows, ncols, p):
    '''Returns a new board that is randomly filled with cells. '''
    board = []
    for i in range(0, nrows):
        col = []        
        for j in range(0, ncols):
            rand = random.random()
            if rand > p:
                col.append(0)
            else:
                col.append(1)
        board.append(col)
    return board    

def display_board(board):
    '''Takes in a Life board and returns Life board in graphic format.'''
    rows = len(board)
    cols = len(board[0])
    ends = "+" + "-"*cols + "+\n"
    l_board = ends
    
    for i in range(0, rows):
        l_board += "|"
        for j in range(0, cols):
            if board[i][j] == 1:
                l_board += "*"
            else:
                l_board += " "
        l_board += "|\n"
        
    l_board += ends
    return l_board


def board_sums(board):
    '''Takes in a Life board and returns the neighbor sums.'''
    rows = len(board)
    cols = len(board[0])
    s_board = make_empty_board(rows, cols)
    
    for i in list(range(0, rows)):
        for j in list(range(0, cols)):
            
            for r in list(range(i-1, i+2)):
                for c in list(range(j-1, j+2)):
                    if r != i or c != j:
                        if c >= 0 or r >= 0:
                            if board[r%rows][c%cols] == 1:
                                s_board[i][j] += 1
                        elif c >= 0:
                            if board[r][c%cols] == 1:
                                s_board[i][j] += 1
                        elif r >= 0:
                            if board[r%rows][c] == 1:
                                s_board[i][j] += 1
                        else:
                            if board[r][c] == 1:
                                s_board[i][j] += 1
                             
    return s_board    
    


def display_board_sums(board):
    '''Takes in a Life board and returns the sum board in graphic format.'''
    board = board_sums(board)
    rows = len(board)
    cols = len(board[0])
    ends = "+" + "-"*cols + "+\n"
    l_board = ends
    
    for i in range(0, rows):
        l_board += "|"
        for j in range(0, cols):
                l_board += str(board[i][j])
        l_board += "|\n"
        
    l_board += ends
    return l_board

def board_update(board):
    '''Takes in a Life board and returns the next generation.'''
    #cannot copy because refers to same items
    n_board = [x[:] for x in board]
    rows = len(board)
    cols = len(board[0])
    s_board = board_sums(board)
    
    for i in range(0, rows):
        for j in range(0, cols):
            if s_board[i][j] == 3:
                n_board[i][j] = 1
            if s_board[i][j] < 2 or s_board[i][j] > 3:
                n_board[i][j] = 0
   
    return n_board


def board_to_num(board):
    '''Computes a unique integer that represents the Life board.'''
    rows = len(board)
    cols = len(board[0])
    ret = 0
    n = 0
    
    for i in range(0, rows):
        for j in range(0, cols):
            ret += board[i][j]*(2**n)
            n += 1
    
    return ret
    
    
    
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

