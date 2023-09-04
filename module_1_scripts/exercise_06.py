class Board:
    def __init__(self):
        self._values = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        self._def_values = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

    def set_row_col(self, row, col):
        self._values[row][col] = 1

    def reset_board(self):
        self._values = self._def_values

    def print_board(self):
        for row in self._values:
            print(row[0], " ", row[1], " ", row[2], " ", row[3], " ", row[4])


def get_row_col():
    board_obj = Board()
    row = input("Please input a row number from 1-5: ")
    col = input("Please input a col number from 1-5: ")

    try:
        row = int(row)
        col = int(col)
        if row < 1 | row > 5 | col < 1 | col > 5:
            raise ValueError("Row and Col value must be between 1 and 5")
        else:
            board_obj.set_row_col(row-1,col-1)
            board_obj.print_board()
    
    except ValueError:
        get_row_col()
    
if __name__ == "__main__":
    get_row_col()