# Name: Melba Nuzen
# CMS cluster login name: mnuzen

'''
The CS 1 final exam, Fall 2018, part 1.

Functions on locations and sets of locations.
'''

import string
from utils import *

def is_adjacent(loc1, loc2):
    '''
    Arguments:
      loc1, loc2 -- (row, column) locations

    Return value: 
      True if two locations are orthogonally adjacent, otherwise False.
    '''

    assert is_loc(loc1)
    assert is_loc(loc2)
    
    (l1x, l1y) = loc1
    (l2x, l2y) = loc2
    
    boo = False
    
    if l1x == l2x:
        if abs(l1y - l2y) == 1:
            boo = True
            
    if l1y == l2y:
        if abs(l1x - l2x) == 1:
            boo = True
        
    return boo

def adjacent_to_any(loc, locset):
    '''
    Arguments:
      loc -- a (row, column) location
      locset -- a set of locations

    Return value:
      True if `loc` is not in `locset` and at least one location 
      in `locset` is adjacent to `loc`, otherwise False.

    The set `locset` is not altered.
    '''

    assert is_loc(loc)
    assert is_locset(locset)
    
    (lx, ly) = loc
    
    boo = False
    adj = False
    
    for l in locset:
        if is_adjacent(loc, l):
            adj = True
    
    if (loc not in locset) and (adj):
        boo = True
    
    return boo

def collect_adjacent(locset, target_set):
    '''
    Arguments:
      locset -- a set of (row, column) locations
      target_set -- another set of (row, column) locations

    Return value: 
      A set of all the locations in `locset` that are adjacent 
      to any location in `target_set`.

    The sets `locset` and `target_set` are not altered.
    '''

    assert is_locset(locset)
    assert is_locset(target_set)
    
    retset = set()
    
    for ls in locset:
        if adjacent_to_any(ls, target_set):
            retset.add(ls)
    
    return retset

def collect_connected(loc, locset):
    '''
    Arguments:
      loc -- a (row, column) location
      locset -- a set of locations

    Return value: 
      A set of all the locations in `locset` which are connected to `loc` 
      via a chain of adjacent locations. Include `loc` in the resulting set.

    The set `locset` is not altered.
    '''

    assert is_loc(loc)
    assert is_locset(locset)
    
    retset = set()
    retset.add(loc)
    clocset = locset.copy()
    current = loc
    
    for l in locset:
        if is_adjacent(current, l):
            retset.add(l)
            clocset.remove(l)
 
    ca = collect_adjacent(clocset, retset)
        
    for c in ca:
        retset.add(c)

    return retset

def partition_connected(locset):
    '''
    Partition a set of locations based on being connected via a chain of
    adjacent locations.  The original locset is not altered.
    Return a list of subsets.  The subsets must all be disjoint i.e.
    the intersection of any two subsets must be the empty set.

    Arguments:
      locset -- a set of (row, column) locations

    Return value: 
      The list of partitioned subsets.

    The set `locset` is not altered.
    '''

    assert is_locset(locset)
    
    clocset = locset.copy()
    
    retlst = []     
    
    while len(clocset) != 0:
        a = clocset.pop()
        cc = collect_connected(a, locset)
        retlst.append(cc)
        for c in cc:
            if c in clocset:
                clocset.remove(c)
    
    assert disjoint_subsets(retlst)
    
    return retlst


def filter_locset(locset):
    '''
    Given a locset, partition it into subsets which are connected via a
    chain of adjacent locations.  Compute two sets:
      -- the union of all partitions whose length is < 3 
      -- the union of all partitions whose length is >= 3 
    and return them as a tuple of two sets (in that order).  

    Arguments:
      locset -- a set of (row, column) locations

    Return value:
      The two sets as described above.

    The set `locset` is not altered.
    '''

    assert is_locset(locset)
    
    retlst = partition_connected(locset)
    
    big = set()
    small = set()    
    
    for r in retlst:
        if len(r) >= 3:
            big.update(r)
        else:
            small.update(r)
    
    ret = (big, small)
    
    return ret



