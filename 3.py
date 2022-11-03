# # Создайте программу для игры в ""Крестики-нолики"".




board = list(range(1, 10))
win_board = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
def draw_board ():
    print('')
    for i in range(3):
        print (' | ', board[0 + i * 3], ' | ', board[1 + i * 3], ' | ', board[2 + i * 3])
        print('')

def player_step (step):
    while True:
        value = input('Where do you want to put ' + step + ' ? ')
        if not (value in '123456789'):
            print ('Wrong step. Continue')
            continue
        value = int(value)
        if str(board[value - 1]) in 'XO':
            print ('This cell is busy')
            continue
        board[value - 1] = step
        break

def chek_win():
    for each in win_board:
        if board[each[0] - 1] == board[each[1] - 1] == board[each[2] - 1]:
            return board[each[1] - 1]
    else: 
        return False

def main():
    counter = 0
    while True:
        draw_board()
        if counter % 2 == 0:
            player_step('X')
        else:
            player_step('O')
        if counter > 3:
            winner = chek_win()
            if winner:
                draw_board()
                print(winner, "win")
                break
        counter += 1
        if counter > 8:
            draw_board()
            print ('No one won')
            break

main()



