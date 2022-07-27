########### PY4E 2주차 연습문제 #############
'''
 📌Q1. 컴퓨터와 함께하는 가위바위보 게임을 만들어봅시다!
 
조건1 : 함수의 인자로는 나의 가위바위보 선택이 들어감
조건2 : 누가 무엇을 냈고, 누가 승리 했는지 출력이 되어야 함
'''

import random


def trans_yours(yours):
    if (yours == ('가위' or '0')):
        yours = 0
    elif (yours == ('바위' or '1')):
        yours = 1
    elif (yours == ('보' or '2')):
        yours = 2
    else:
        print('가위, 바위, 보 중에 입력해주세요!')
        yours = 3
    return yours


def judgment(yours, coms):
    rsp_list = ['가위', '바위', '보']
    coms_trans = rsp_list[coms]
    yours_trans = rsp_list[yours]
    
    if (yours == coms):
        print(f'당신은 {yours_trans}, 컴퓨터는 {coms_trans}를 내서 이번판은 비겼습니다.')
    elif (yours == 0 and coms == 2) or (yours == 1 and coms == 0) or (yours == 2 and coms == 1):
        print(f'당신은 {yours_trans}, 컴퓨터는 {coms_trans}를 내서 이번판은당신이 이겼습니다 ^0^~!')
    else:
        print(f'당신은 {yours_trans}, 컴퓨터는 {coms_trans}를 내서 이번판은당신이 졌습니다 ㅠ_ㅠ')
    

def main_print():
    print('''
                컴퓨터와 함께하는 가위바위보 게임!
    입력은 가위(또는 0), 바위(또는 1), 보(또는 2)로 할 수 있습니다.
                    컴퓨터를 이겨보세요!
                   ~~~ Game Start ! ~~~~
                    ''')

def main():
    main_print()
    while(1):
        yours = input('가위, 바위, 보를 입력해주세요 : ')
        yours = trans_yours(yours)
        if yours == 3:
            continue
        coms = random.randrange(0,3)
        judgment(yours, coms)

        print('\n계속 하시겠습니까?')
        choice = input('Y/N 로 입력해주세요')
        choice = choice.upper()
        if (choice == 'Y'):
            continue
        else:
            print('게임을 종료합니다:)')
            break


if __name__ == "__main__":
	main()
