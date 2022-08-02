scp = ['가위', '바위', '보']
import random
games = int(input('몇 판을 하시겠습니까?'))
player_win = 0
player_draw = 0
player_lose = 0
com_win = 0
com_draw = 0
com_lose = 0

def game(my_choice):
    if my_choice not in scp:
        print('잘못된 입력입니다. 가위, 바위, 보 중에 하나를 고르세요. 처음부터 다시 시작해주세요.')
        quit()

    else:
        computer = random.randint(0, 2)
        com_choice = scp[computer]
        global player_win, player_draw, player_lose, com_win, com_lose, com_draw


        if my_choice == com_choice:
            print('당신은', my_choice,'를 냈습니다!')
            print('컴퓨터는', com_choice,'를 냈습니다!')
            print('무승부')
            player_draw += 1
            com_draw += 1


        elif (my_choice == '가위' and com_choice == '보') or (my_choice == '바위' and com_choice == '가위') or (my_choice == '보' and com_choice == '바위'):
            print('당신은', my_choice,'를 냈습니다!')
            print('컴퓨터는', com_choice,'를 냈습니다!')
            print('승리')
            player_win += 1
            com_lose += 1


        else:
            print('당신은', my_choice,'를 냈습니다!')
            print('컴퓨터는', com_choice,'를 냈습니다!')
            print('패배')
            player_lose+=1
            com_win += 1


for i in range(1, games + 1):
    game(input('가위, 바위, 보 중 하나를 고르세요 '))

print('나의 전적:',player_win,'승',player_draw,'무',player_lose,'패')
print('컴퓨터의 전적:',com_win,'승',com_draw,'무',com_lose,'패')







