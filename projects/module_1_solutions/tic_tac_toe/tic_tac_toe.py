"""
Консольная игра 'Крестики-нолики' с базовой логикой против компьютера
"""

import random


def print_board(board):
    """Выводит игровое поле в консоль"""
    print("\n   |   |   ")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("   |   |   \n")


def check_winner(board, player):
    """Проверяет, выиграл ли указанный игрок"""
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False


def is_board_full(board):
    """Проверяет, заполнено ли игровое поле"""
    return " " not in board


def get_player_move(board):
    """Получает ход от игрока"""
    while True:
        try:
            move = int(input("Введите номер клетки (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Пожалуйста, введите число от 1 до 9.")
            elif board[move] != " ":
                print("Эта клетка уже занята. Выберите другую.")
            else:
                return move
        except ValueError:
            print("Пожалуйста, введите число от 1 до 9.")


def get_computer_move(board, computer_symbol, player_symbol):
    """Определяет ход компьютера"""
    for i in range(9):
        if board[i] == " ":
            board_copy = board.copy()
            board_copy[i] = computer_symbol
            if check_winner(board_copy, computer_symbol):
                return i

    for i in range(9):
        if board[i] == " ":
            board_copy = board.copy()
            board_copy[i] = player_symbol
            if check_winner(board_copy, player_symbol):
                return i

    if board[4] == " ":
        return 4

    corners = [0, 2, 6, 8]
    available_corners = [i for i in corners if board[i] == " "]
    if available_corners:
        return random.choice(available_corners)

    available_moves = [i for i in range(9) if board[i] == " "]
    return random.choice(available_moves)


def choose_symbol():
    """Позволяет игроку выбрать символ (X или O)"""
    while True:
        symbol = input("Выберите символ (X или O): ").upper()
        if symbol in ["X", "O"]:
            return symbol
        print("Пожалуйста, введите X или O.")


def main():
    """Основная функция игры"""
    print("Добро пожаловать в игру 'Крестики-нолики'!")
    print("Клетки пронумерованы от 1 до 9, как на клавиатуре:")
    print("\n 1 | 2 | 3 ")
    print("___|___|___")
    print(" 4 | 5 | 6 ")
    print("___|___|___")
    print(" 7 | 8 | 9 ")
    print("   |   |   \n")

    player_symbol = choose_symbol()
    computer_symbol = "O" if player_symbol == "X" else "X"

    if random.choice([True, False]):
        print("Вы ходите первым!")
        current_player = player_symbol
    else:
        print("Компьютер ходит первым!")
        current_player = computer_symbol

    board = [" "] * 9

    while True:
        if current_player == player_symbol:
            print_board(board)
            move = get_player_move(board)
            board[move] = player_symbol
        else:
            print("Ход компьютера...")
            move = get_computer_move(board, computer_symbol, player_symbol)
            board[move] = computer_symbol
            print(f"Компьютер выбрал клетку {move + 1}")

        if check_winner(board, current_player):
            print_board(board)
            if current_player == player_symbol:
                print("Поздравляю! Вы выиграли!")
            else:
                print("Компьютер выиграл. Попробуйте еще раз!")
            break
        elif is_board_full(board):
            print_board(board)
            print("Ничья! Игра окончена.")
            break

        current_player = computer_symbol if current_player == player_symbol else player_symbol

    play_again = input("\nХотите сыграть еще раз? (да/нет): ").lower()
    if play_again in ['да', 'д', 'yes', 'y']:
        main()
    else:
        print("Спасибо за игру! До свидания!")


if __name__ == "__main__":
    main()