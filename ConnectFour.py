import numpy as np


class ConnectFour:
    NUMBER_OF_ROWS = 6
    NUMBER_OF_COLUMNS = 6
    CHOICES = set(range(NUMBER_OF_COLUMNS))

    def __init__(self):
        self.matrix = np.zeros((ConnectFour.NUMBER_OF_ROWS, ConnectFour.NUMBER_OF_COLUMNS), np.int8)

    def start(self):
        cur_player = 1
        end = False
        number_of_moves = 0
        total_moves = self.NUMBER_OF_ROWS * self.NUMBER_OF_COLUMNS
        while not end:
            valid = False
            print(self.matrix)
            print(f'Player{cur_player} move. Choose a column by typing its number:')
            while not valid:
                choice = int(input())
                valid = self.check_choice(choice)
            row = self.drop(cur_player, choice)
            number_of_moves += 1
            if self.check_win(cur_player, choice, row):
                print(f'Player{cur_player} has won!')
                print(self.matrix)
                end = True
            if number_of_moves == total_moves:
                print('Game is over!')
                end = True
            # Switch players
            if cur_player == 1:
                cur_player = 2
            else:
                cur_player = 1

    def column_is_full(self, column):
        for i in range(self.NUMBER_OF_ROWS):
            if self.matrix[i][column] == 0:
                return False
        return True

    def check_choice(self, choice):
        if choice not in self.CHOICES:
            print('Wrong choice. Choose columns from 0 to 5')
            return False
        if self.column_is_full(choice):
            print('The column is full. Choose another one')
            return False
        return True

    def drop(self, cur_player, column):
        for i in reversed(range(self.NUMBER_OF_ROWS)):
            if self.matrix[i][column] == 0:
                self.matrix[i][column] = cur_player
                break
        return i

    def check_win(self, cur_player, column, row):
        # horizontal
        count = 0
        for i in range(self.NUMBER_OF_COLUMNS):
            if self.matrix[row][i] == cur_player:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

        # vertical
        count = 0
        for i in range(self.NUMBER_OF_ROWS):
            if self.matrix[i][column] == cur_player:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

        # left diagonal
        count = 0
        diag = np.diag(self.matrix, column - row)
        for i in diag:
            if i == cur_player:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

        # right diagonal
        count = 0
        diag = np.diag(np.fliplr(self.matrix), (ConnectFour.NUMBER_OF_COLUMNS - 1- column)-row)
        for i in diag:
            if i == cur_player:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0


if __name__ == '__main__':
    connectFour = ConnectFour()
    connectFour.start()
