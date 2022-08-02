'''
📌Q2. 가위바위보 업그레이드 버젼을 함수로 만들어 봅시다. 
아래와 같은 조건을 만족해 주세요.

 - 조건 1: 게임을 몇 판을 진행할 것인지 입력을 받아주기
 - 조건 2: 0, 1, 2, "가위", "바위", "보" 이외에 다른 입력을 받으면 재입력 받기
 - 조건 3: 게임종료 후 나와 컴퓨터의 총 전적 출력하기
'''
# 전적나타내는 부분 쉽게 하는 방법 (dictionary 사용할 수 있을거같은데..?)
# global 변수 사용해서 count 처리해보기


import random


def trans_yours(yours):
    if (yours == '가위' or yours == '0'):
        yours = 0
    elif (yours == '바위' or yours == '1'):
        yours = 1
    elif (yours == '보' or yours == '2'):
        yours = 2
    else:
        print('가위, 바위, 보 중에 입력해주세요!')
        yours = 3
    return yours


def judgment(yours, coms, complete):
    rsp_list = ['가위', '바위', '보']
    coms_trans = rsp_list[coms]
    yours_trans = rsp_list[yours]
    print(f'\n나 : {yours_trans}, \n컴퓨터 : {coms_trans}')
    if (yours == coms):
        print(f'{complete +1}판은 비겼습니다.\n')
        win = 'bigim'
    elif (yours == 0 and coms == 2) or (yours == 1 and coms == 0) or (yours == 2 and coms == 1):
        print(f'{complete +1}판은 내가 이겼습니다 ^0^~!\n')
        win = 'me'
    else:
        print(f'{complete +1}판은 내가 졌습니다 ㅠ_ㅠ\n')
        win = 'com'
    return win
    

def main_print():
    print('''
                컴퓨터와 함께하는 가위바위보 게임!
    입력은 가위(또는 0), 바위(또는 1), 보(또는 2)로 할 수 있습니다.
                    컴퓨터를 이겨보세요!
                   ~~~ Game Start ! ~~~~
                   ''')

def main():
    main_print()
    game_num = int(input('몇 판을 진행하시겠습니까?'))
    complete = 0
    win_list = []
    while(1):
        if (game_num == complete):
            print('게임 횟수가 끝나 게임을 종료합니다!')
            print(f'나의     전적 : {win_num_me}승 {wim_num_bigim}무 {win_num_com}패 ')
            print(f'컴퓨터의 전적 : {win_num_com}승 {wim_num_bigim}무 {win_num_me}패 ')
            break
        yours = input('가위, 바위, 보를 입력해주세요 : ')
        yours = trans_yours(yours)
        if yours == 3:
            continue
        coms = random.randrange(0,3)
        win = judgment(yours, coms, complete)
        win_list.append(win)
        win_num_me = win_list.count('me')
        win_num_com = win_list.count('com')
        wim_num_bigim = win_list.count('bigim')

        complete += 1


if __name__ == "__main__":
	main()