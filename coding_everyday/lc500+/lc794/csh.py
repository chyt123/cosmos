class Solution(object):
    def validTicTacToe(self, board):
        x, o = 0, 0
        # how many
        for i in board:
            for j in i:
                if j == 'X':
                    x += 1
                if j == 'O':
                    o += 1

        if x != o and x != o + 1:
            return False

        if x == o == 0:
            return True

        win_flag = False
        # check row
        for row in board:
            if row[0] == row[1] == row[2] and row[0] != ' ':
                print "row"
                if win_flag:
                    return False
                win_flag = True
        for row in board:
            if row[0] == row[1] == row[2]:
                if row[0] == 'X':
                    return x == o + 1
                if row[0] == 'O':
                    return x == o

        # check col
        win_flag = False
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
                print "col"
                if win_flag:
                    return False
                if (board[0][i] == 'X' and x == o + 1) or (board[0][i] == 'O' and x == o):
                    win_flag = True
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i]:
                if board[0][i] == 'X':
                    return x == o + 1
                if board[0][i] == 'O':
                    return x == o

        # check diagonal
        if (board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]):
            print "dia"
            if board[1][1] == 'X':
                return x == o + 1
            if board[1][1] == 'O':
                return x == o

        return True


if __name__ == "__main__":
    sol = Solution()
    board = ["X  ","   ","   "]
    print sol.validTicTacToe(board)

