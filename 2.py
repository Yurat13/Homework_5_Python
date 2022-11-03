# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""


# Игра человека против человека
# from random import randint

# candies = 2021
# chel_1 = input('Ener name of the 1st player: ')
# chel_2 = input('Ener name of the 2nd player: ')
# turn = randint(0,1)
# if turn == 0:
#     print (f'First step - {chel_1}')
# else:
#     print (f'First step - {chel_2}')
# turn += 1
# while True:
#     k = int(input('Enter the candies of candies: '))
#     if k <= 28 and k > 0:
#         candies = candies - k
#         print('')
#         print (f"Left {candies} candies")
#         if candies == 0:
#             print ('Game over')
#             if turn % 2 == 0: print (f'Player {chel_2} is win')
#             else: print (f'Player {chel_1} is win')
#             break
#         if turn % 2 == 0: 
#             print (f'Player {chel_1} is going')
#         else:
#             print (f'Player {chel_2} is going')
#         turn += 1
        
        
#     else: print('Maximum candies of candies in one turn - 28')


# Игра против бота с "интеллектом"
from random import randint

def turn_bot (candies):
    n = candies % 29
    if n == 0:
        n = randint (1, 28)
    return n

def turn_player (candies):
    n = 29
    while n > 28 or n < 1:
        n = int(input('Enter the number of candies: '))
        if n > 28 or n < 1:
            print ('You took uncorrect number of candies')
        if n > candies:
            print ('You took more candies then left')
    return n



candies = 113
chel_1 = input('Enter your name: ')
chel_2 = 'computer'
turn = randint(0,1)
if turn == 0:
    print (f'First step - {chel_1}')
else:
    print (f'First step - {chel_2}')
while True:
    if turn % 2 == 0: 
        print (f'Player {chel_1} is going')
        n = turn_player(candies)
        print (f'Player {chel_1} took {n} candies')
    elif turn % 2 == 1:
        print (f'Computer is going')
        n = turn_bot(candies)
        print (f'Computer took {n} candies')
    
    candies = candies - n
    print('')
    print (f"Left {candies} candies")
    if candies == 0:
        print ('Game over')
        if turn % 2 == 0: print (f'Player {chel_1} won')
        else: print (f'The computer won')
        break
    turn += 1
       
        
       
        
 