# Name: Melba Nuzen
# CMS cluster login name: mnuzen

'''
The CS 1 final exam, Fall 2018, part 2.

The Dissembler puzzle game.
'''

from utils import *
import locset as ls

# ---------------------------------------------------------------------- 
# Functions on board representations.
# ---------------------------------------------------------------------- 

def invert_rep(rep):
    '''
    Invert the board representation which maps locations to colors.
    The inverted representation will map colors to sets of locations.

    Arguments:
      rep -- a dictionary mapping locations to one-character strings
             representing colors

    Return value:
      a dictionary mapping one-character strings (representing colors)
      to sets of locations

    The input dictionary 'rep' is not altered.
    '''

    assert is_rep(rep)
    
    ret = {}
    
    keys = rep.keys()
    
    for key in keys:
        ret[rep[key]] = key
    
    return ret


def revert_rep(inverted):
    '''
    Invert the board representation which maps colors to sets of 
    locations.  The new representation will map locations to colors.

    Arguments:
      inverted -- a dictionary mapping one-character strings 
                  (representing colors) to sets of locations

    Return value:
      a dictionary mapping locations to one-character strings
      representing colors

    The input dictionary 'inverted' is not altered.
    '''

    assert is_inverted_rep(inverted)
    
    ret = {}
    items = inverted.items()
    
    for key, value in items:
        for v in value:
            ret[v] = key

    return ret

def swap_locations(rep, loc1, loc2):
    '''
    Exchange the contents of two locations.

    Arguments:
      rep -- a dictionary mapping locations to one-character strings
             representing colors
      loc1, loc2 -- adjacent locations which are in the board rep

    Return value:
      a new dictionary with the same structure of 'rep' with the
      specified locations having each others' contents

    The input dictionary 'rep' is not altered.
    '''

    assert is_rep(rep)
    assert is_loc(loc1)
    assert is_loc(loc2)
    assert ls.is_adjacent(loc1, loc2)
    assert loc1 in rep
    assert loc2 in rep
    
    ret = {}
    
    keys = rep.keys()
    holder = rep[loc1]
    ret[loc1] = rep[loc2] 
    ret[loc2] = holder    
    
    for key in keys:
        if (key != loc1) and (key != loc2):
            ret[key] = rep[key]
    
    return ret


def remove_connected_groups(rep):
    '''
    Remove all connected color groups covering at least three squares
    from a board representation.

    Arguments: 
      rep -- a dictionary mapping locations to one-character strings
             representing colors

    Return value:
      a tuple of two dictionaries of the same kind as the input
      (i.e. a mapping between locations and color strings);
      the first contains the remaining locations only, 
      and the second contains the removed locations only 

    The input dictionary 'rep' is not altered.
    '''

    assert is_rep(rep)
    
    #remaining location/color pairs
    ret1 = {}
    #location/color pairs meant to be removed
    ret2 = {}
    
    nums = set()
    inverted = invert_rep(rep)
    
    keys = rep.keys()
    
    for key in keys:
        nums.add(key)
    
    filtered = ls.filter_locset(nums)
    
    
    
    ret = (ret1, ret2)
                  
    return ret
    


def adjacent_moves(nrows, ncols):
    '''
    Create and return a set of all moves on a board with 'nrows' rows and
    'ncols' columns.  The moves consist of two adjacent (row, column)
    locations.

    Arguments:
      nrows -- the number of rows on the board
      ncols -- the number of columns on the board

    Return value:
      the set of moves, where each move is a pair of adjacent locations
      and each location is a (row, column) pair; also the two locations
      are ordered in the tuple (the "smallest" comes first)

    Note that the moves are independent of the contents of any board
    representation; we aren't considering whether the moves would actually 
    change anything on a board or whether the locations of each move are 
    occupied by color squares.
    '''

    assert type(nrows) is int and type(ncols) is int
    assert nrows > 0 and ncols > 0
    
    ret = set()
    
    loc = set() 
    adj = {}
    
    while nrows >= 0:
        while ncols >= 0:
            location = (nrows, ncols)
            loc.add(location)
            adj[location] = ls.collect_adjacent(location, loc)
            nrows -= 1
            ncols -= 1
        
    keys = adj.keys()
        
    for key in keys:
        for l in adj[key]:
            ret.add((key, l))
            
    return ret


def possible_moves(rep, nrows, ncols):
    '''
    Compute and return a set of all the possible moves.  A "possible move"
    is a move where:
    -- both locations of the move are adjacent
    -- both locations on the board rep are occupied by colors 
    -- making the move will cause some locations to be vacated

    Arguments: 
      rep -- a dictionary mapping locations to one-character strings
             representing colors
      nrows -- the number of rows on the board
      ncols -- the number of columns on the board

    Return value: 
      the set of possible moves

    The input dictionary 'rep' is not altered.
    '''

    assert is_rep(rep)
    assert type(nrows) is int and type(ncols) is int
    assert nrows > 0 and ncols > 0
    
    ret = set()
    
    return ret


