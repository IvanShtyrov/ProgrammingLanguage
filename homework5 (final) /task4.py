class Cell:
    def __init__(self, number):
        self.number = number
        self.value = " "  # Инициализируем клетку пустым значением " "


class Board:
    def __init__(self):
        self.cells = [Cell(i) for i in range(1, 10)]  # Создаем список клеток для игровой доски

    def display(self):
        for i in range(0, 9, 3):
            print(f"{self.cells[i].value} | {self.cells[i + 1].value} | {self.cells[i + 2].value}")  # Отображаем доску
            if i < 6:
                print("---------")

    def make_move(self, cell_number, player):
        cell = self.cells[cell_number - 1]
        if cell.value == " ":  # Проверяем, что клетка пуста
            cell.value = player.symbol  # Устанавливаем значение клетки, связанное с символом игрока
            return True
        else:
            return False


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol  # Символ игрока (X или O)


def main():
    board = Board()
    player1 = Player("Player 1", "X")
    player2 = Player("Player 2", "O")

    current_player = player1
    while True:
        board.display()
        print(f"{current_player.name}'s turn ({current_player.symbol})")
        cell_number = int(input("Enter the number of the cell to make a move (1-9): "))

        if cell_number < 1 or cell_number > 9:
            print("Invalid input. Please choose a number between 1 and 9.")
            continue

        if board.make_move(cell_number, current_player):
            if check_winner(board, current_player):
                board.display()
                print(f"{current_player.name} wins! Congratulations!")
                break
            elif is_board_full(board):
                board.display()
                print("It's a draw! The game is a tie.")
                break
            else:
                current_player = player2 if current_player == player1 else player1
        else:
            print("Cell already occupied. Try again.")


def check_winner(board, player):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combo in winning_combinations:
        if all(board.cells[i].value == player.symbol for i in combo):  # Проверяем, есть ли победитель
            return True
    return False


def is_board_full(board):
    return all(cell.value != " " for cell in board.cells)  # Проверяем, заполнена ли доска


if __name__ == "__main__":
    main()
