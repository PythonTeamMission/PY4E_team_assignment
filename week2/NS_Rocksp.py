scp = ['가위', '바위', '보']
import random
computer = random.randint(0, 2)


def game(my_choice):
    if my_choice not in scp:
        print('잘못된 입력입니다. 가위, 바위, 보 중에 하나를 고르세요. 처음부터 다시 시작해주세요.')

    else:
        com_choice = scp[computer]
        if my_choice == com_choice:
            print('당신은', my_choice,'를 냈습니다!')
            print('컴퓨터는', com_choice,'를 냈습니다!')
            print('무승부')

        elif (my_choice == '가위' and com_choice == '보') or (my_choice == '바위' and com_choice == '가위') or (my_choice == '보' and com_choice == '바위'):
            print('당신은', my_choice,'를 냈습니다!')
            print('컴퓨터는', com_choice,'를 냈습니다!')
            print('승리')

        else:
            print('당신은', my_choice,'를 냈습니다!')
            print('컴퓨터는', com_choice,'를 냈습니다!')
            print('패배')


game(input('가위, 바위, 보 중 하나를 고르세요 '))







