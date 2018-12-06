'''
This program allows the user to interactively play the game of Sudoku.
'''


class SudokuError(Exception):
    pass

class SudokuLoadError(SudokuError):
    pass

class SudokuMoveError(SudokuError):
    pass

class SudokuCommandError(SudokuError):
    pass

class Sudoku:
    '''Interactively play the game of Sudoku.'''

    def __init__(self):
        '''Initalizes the Sudoku board.'''
        self = []
        for r in range(0,9):
            for c in range(0,9):
                self[r][c] = None
        self.moves = []

    def load(self, filename):
        '''Loads the contents of a file into a board representation.'''
        f = open(filename,'r')
        lines = f.readlines()
        lstlines = lines.split('\n')
        
        if len(lstlines) != 9:
            raise SudokuLoadError("File must have exactly 9 lines")
        
        for line in lstlines:
            if len(line) != 9:
                raise SudokuLoadError("Lines must have exactly 9 characters")
                      
        for r in range(0,9):
            for line in lstlines:
                for c in range(0,9):
                    self[r][c] = line[c] 
                    
        f.close()   
        del moves[:]
        

    def save(self, filename):
        file = open('filename','w')
        for r in range(0,9):
            for c in range(0,9):
                file.write(self[r][c])
            file.write('\n')
        file.close()

    def show(self):
        '''Pretty-print the current board representation.'''
        print()
        print('   1 2 3 4 5 6 7 8 9 ')
        for i in range(9):
            if i % 3 == 0:
                print('  +-----+-----+-----+')
            print(f'{i + 1} |', end='')
            for j in range(9):
                if self.board[i][j] == 0:
                    print(end=' ')
                else:
                    print(f'{self.board[i][j]}', end='')
                if j % 3 != 2 :
                    print(end=' ')
                else:
                    print('|', end='')
            print() 
        print('  +-----+-----+-----+')
        print()

    def move(self, row, col, val):
        '''Takes in the row, column, and number to place at a location. It also
        checks that the inputs are valid coordinates, the move is valid, and 
        makes the move.'''
        
        # checks if the numbers are integers
        if type(row) != int:
            raise SudokuMoveError("The row number must be an integer.")
        if type(col) != int:
            raise SudokuMoveError("The column number must be an integer.")
        if type(val) != int:
            raise SudokuMoveError("The value must be be an integer.")
        
        # checks if the numbers are from 1 to 9
        if 0 < row < 9:
            raise SudokuMoveError("The row number must be from 1 to 9.")
        if 0 < col < 9:
            raise SudokuMoveError("The column number must be from 1 to 9.")
        if 0 < val < 9:
            raise SudokuMoveError("The value number must be from 1 to 9.")
        
        # checks if the move is valid
        
        # checks if box is empty
        if self[row][col] == 0:
            raise SudokuMoveError("You must choose an empty box.")
    
        # checks if row has that value
        for r in range(0,9):
            if self[r][col] == val:
                raise SudokuMoveError("There is already a number" + val + \
                                      "in that row.")
    
        # checks if column has that value
        for c in range(0,9):
            if self[row][c] == val:
                raise SudokuMoveError("There is already a number" \
                                      + val + "in that column.")
        
        # checks the surrounding box
        for r in range(row-1, row+2):
            for c in range(col-1, col+2):
                if r != row and c != col:
                    if self[r][c] == val:
                        raise SudokuMoveError("There is already a number" + \
                                              val + "in that box.")
        
        self[row][col] = val
        self.moves.append((row, col, val))

    def undo(self):
        (row, col, val) = self.moves.pop()
        self[row][col] = 0
        

    def solve(self):
        while True:
            try:
                cmd = input('Enter a command.')
            
                if cmd == 'q':
                    quit(0)
            
                elif type(cmd) == int:
                    lst = [int(i) for i in str(cmd)]
                    self.move(lst[0], lst[1], lst[2])
            
                elif cmd == 'u':
                    self.undo()
                
                elif cmd[:2] == 's ':
                    self.save(cmd[2:])
                    
                else:
                    raise SudokuCommandError("You must enter a valid command.")
                    
                except SudokuMoveError:
                    raise SudokuMoveError("Invalid move.") 

if __name__ == '__main__':
    s = Sudoku()

    while True:
        filename = input('Enter the sudoku filename: ')
        try:
            s.load(filename)
            break
        except FileNotFoundError as e:
            print(e)
        except SudokuLoadError as e:
            print(e)

    s.show()
    s.solve()

