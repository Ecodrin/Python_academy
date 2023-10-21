class Checkers:

    def __init__(self):
        self.p = 'ABCDEFGH'
        self.q = '12345678'
        self.board = [['' for _ in range(8)] for _ in range(8)]
        for i in range(8):
            for j in range(8):
                if i > 4 and (i % 2 == 0 and j % 2 == 0 or i % 2 == 1 and j % 2 == 1):
                    self.board[i][j] = 'B'
                elif i < 3 and (i % 2 == 0 and j % 2 == 0 or i % 2 == 1 and j % 2 == 1):
                    self.board[i][j] = 'W'
                else:
                    self.board[i][j] = 'X'
                    
    def move(self, f, t):
        self.board[self.q.index(f[1])][self.p.index(f[0])], self.board[self.q.index(t[1])][self.p.index(t[0])] =\
            self.board[self.q.index(t[1])][self.p.index(t[0])], self.board[self.q.index(f[1])][self.p.index(f[0])]

    def get_cell(self, pr):
        return Cell(self.board[self.q.index(pr[1])][self.p.index(pr[0])])


class Cell:

    def __init__(self, symbol):
        self.symbol = symbol

    def status(self):
        return self.symbol


checkers = Checkers()
checkers.move('C3', 'D4')
checkers.move('H6', 'G5')
for row in '87654321':
    for col in 'ABCDEFGH':
        print(checkers.get_cell(col + row).status(), end='')
    print()