from abc import ABC, abstractmethod

board: list = [
    ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"],
    ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"],
    ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6"],
    ["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5"],
    ["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4"],
    ["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3"],
    ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"],
    ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"],
]


class Figure(ABC):
    index_row: int = 0
    index_column: int = 0

    def __init__(self, field: str) -> None:
        self.field: str = field

    @abstractmethod
    def list_available_moves(self, **version: str) -> list:
        pass

    def validate_move(self, dest_field: str, **version: str) -> bool:
        available_moves: list = self.list_available_moves()

        if dest_field in available_moves:
            return True
        else:
            return False

    def get_position(self) -> None:
        self.index_row: int = \
            [board.index(row) for row in board if self.field in row][0]

        self.index_column: int = \
            [row.index(self.field) for row in board if self.field in row][0]

    def first_diagonal(self, moves: list) -> None:
        temp_row: int = self.index_row
        temp_column: int = self.index_column

        # wyznaczanie punktu gdzie zaczyna sie przekątna
        # od lewego, górnego rogu do prawego, dolnego
        if temp_row > temp_column:
            temp_row -= temp_column
            temp_column = 0

        else:
            temp_column -= temp_row
            temp_row = 0

        while True:
            try:
                if board[temp_row][temp_column] != self.field:
                    moves.append(board[temp_row][temp_column])

                temp_row += 1
                temp_column += 1

            except IndexError:
                break

    def second_diagonal(self, moves: list) -> None:
        temp_row: int = self.index_row
        temp_column: int = self.index_column

        # print(str(temp_row) + ' - ' + str(temp_column))

        # jesli liczba wierszy jest wieksza od kolumn,
        # poruszamy się po przękatnej od lewego, dolnego rogu,
        # do prawego górnego
        if temp_row > temp_column:
            while temp_row != 7 and temp_column != 0:
                temp_row += 1
                temp_column -= 1

            while temp_row != -1:
                try:
                    if board[temp_row][temp_column] != self.field:
                        moves.append(board[temp_row][temp_column])

                    temp_row -= 1
                    temp_column += 1

                except IndexError:
                    break

        # jesli liczba kolumn jest wieksza od wierszy,
        # poruszamy się po przękatnej od prawego, górnego rogu
        # do lewego, dolnego
        else:
            while temp_column != 7 and temp_row != 0:
                temp_column += 1
                temp_row -= 1

            while True:
                try:
                    if board[temp_row][temp_column] != self.field:
                        moves.append(board[temp_row][temp_column])

                    temp_row += 1
                    temp_column -= 1

                except IndexError:
                    break

    def vertical_and_horizontal(self, moves: list):
        for x in range(len(board)):
            if board[x][self.index_column] != self.field:
                moves.append(board[x][self.index_column])

        for x in range(len(board[self.index_row])):
            if board[self.index_row][x] != self.field:
                moves.append(board[self.index_row][x])


class King(Figure):
    def list_available_moves(self) -> list:
        self.get_position()

        moves: list = []

        for x in range(self.index_row - 1, self.index_row + 2):
            for y in range(self.index_column - 1, self.index_column + 2):
                if x == -1 or y == -1:
                    continue

                try:
                    if board[x][y] != self.field:
                        moves.append(board[x][y])

                except IndexError:
                    continue

        return moves


class Queen(Figure):
    def list_available_moves(self) -> list:
        moves: list = []

        self.get_position()

        self.first_diagonal(moves)

        self.second_diagonal(moves)

        self.vertical_and_horizontal(moves)

        return moves


class Rook(Figure):
    def list_available_moves(self) -> list:
        moves: list = []

        self.get_position()

        self.vertical_and_horizontal(moves)

        return moves


class Bishop(Figure):
    def list_available_moves(self) -> list:
        moves: list = []

        self.get_position()

        self.first_diagonal(moves)

        self.second_diagonal(moves)

        return moves


class Knight(Figure):
    def list_available_moves(self) -> list:
        moves: list = []

        self.get_position()

        values_1: list = [2, 1, -1, -2, -2, -1, 1, 2]
        values_2: list = [1, 2, 2, 1, -1, -2, -2, -1]

        for i in range(8):
            x = self.index_row + values_1[i]
            y = self.index_column + values_2[i]

            if x >= 0 and y >= 0 and x < 8 and y < 8:
                moves.append(board[x][y])

        return moves


class Pawn(Figure):
    def list_available_moves(self, **version: str) -> list:
        moves: list = []

        self.get_position()

        # argument "version" okresla w która strone moze przesuwac sie pionek
        # jeśli v1, pionek moze przesuwać się tylko do dołu
        # jeśli v2, pionek moze przesuwać sie tylko do góry
        # na dodatek, pionek nie moze znajdować się w ostatnim rzędzie,

        # jeśli pionek znajduje się w rzędzie 2 lub 7 (w zależności od wersji)
        # możliwy ruch o dwa pola
        if version["key"] == "v1" and self.index_row != 0:
            if self.index_row == 1:
                moves.append(board[self.index_row + 2][self.index_column])

            elif self.index_row + 1 < 7:
                moves.append(board[self.index_row + 1][self.index_column])

        elif version["key"] == "v2" and self.index_row != 7:
            if self.index_row == 6:
                moves.append(board[self.index_row - 2][self.index_column])

            elif self.index_row - 1 > -1:
                moves.append(board[self.index_row - 1][self.index_column])

        return moves

    def validate_move(self, dest_field: str, **version: str) -> bool:
        available_moves: list = self.list_available_moves(key=version["key"])

        if dest_field in available_moves:
            return True
        else:
            return False


# obj_1: King = King('d4')
# print(obj_1.field)
# print(obj_1.list_available_moves())

# obj_2: Queen = Queen('b3')
# print(obj_2.field)
# print(obj_2.list_available_moves())

# obj_3: Rook = Rook('c5')
# print(obj_3.field)
# print(obj_3.list_available_moves())

# obj_4: Knight = Knight('a8')
# print(obj_4.field)
# print(obj_4.list_available_moves())

# obj_5: Pawn = Pawn('f7')
# print(obj_5.field)
# print(obj_5.list_available_moves(key='v2'))
