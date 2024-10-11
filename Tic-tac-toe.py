def games_board(board):
    print('-' * 13)
    for i in board:

        print('|', *i[0], '|', *i[1], '|', *i[2], '|')
        print('-' * 13)

board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def play_game():

    motion = 0
    while True :
        motion += 1
        print(f'Ход {motion}')
        if motion % 2 == 0:
            symbol = 'O'
            print('Ход ноликов.')
        else:
            symbol = 'X'
            print('Ход креситков.')
        try:
            wer = int(input(f'Введите номер строки (от 1 до 3): ')) - 1
            gor = int(input(f'Введите номер столбца (от 1 до 3): ')) - 1

            if 0 <= wer <= 2 and 0 <= gor <= 2:
                if board[wer][gor] == ' ':
                    board[wer][gor] = symbol
                else:
                    print('Ячейка занята 😒 Вы пропускаете ход...')
                    games_board(board)
                    continue
            else:
                print('Некорректный ввод или выход за границы поля. Вы пропускаете ход...')
                games_board(board)
                continue

            games_board(board)
            if check_winner(board, symbol):
                end_game(symbol)
                break

        except ValueError:
            print('Некорректный ввод. Вы пропускаете ход...')
            games_board(board)
            continue

def check_winner(board, symbol):
    for i in range(3):
        if all(board[i][j] == symbol for j in range(3)):
            return True
        if all(board[j][i] == symbol for j in range(3)):
            return True

    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2-i] == symbol for i in range(3)):
        return True

    return False


def end_game(winner):
    if winner == "X":
        print("Поздравляем! Выиграли крестики!")
    elif winner == "O":
        print("Поздравляем! Выиграли нолики!")
    else:
        print("Ничья!")

if __name__ == '__main__':
    print('Давай играть в Крестики-нолики! 😊')
    print('-' * 34)
    play_game()





