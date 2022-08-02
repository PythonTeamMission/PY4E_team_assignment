# -*- coding: utf-8 -*-
# 모두를 위한 파이썬 PY4E 
# 3주차 팀 과제
# 팀: 턴태코치_2팀 / 작성자: jm / 기여자: chabbo, jm, Noas / 작성일: 220729
# 👍👍3주차 미션 목적 - 반복문, 조건문 함수 익히기


"""

📌Q1. 숫자를 입력 받고 그 숫자의 구구단을 출력하는 함수를 만들어 봅시다. 다만 아래의 조건을 만족해 주세요.

조건 1: 홀 수 번째만 출력하기

조건 2: 값이 50이하인 것만 출력하기

🔽 출력 예시

# 입력
number = int(input("몇 단? : "))
gugudan(number)

# 출력
몇 단? : 8
8 단
8 X 1 = 8
8 X 3 = 24
8 X 5 = 40

"""

#########################################################
#                        chabbo                         #
#########################################################

# 조건문 수정, while문으로 바꿔보기
def multiplication(number):
    print(f'====={number}단=====')
    for i in range(50):
        odd_num = 2*i + 1
        mul_num = number * odd_num
        if (mul_num <= 50):
            print(f'{number} X {odd_num} = {mul_num}')
        else:
            print('50이 넘어 종료합니다.')
            break

try:
    number = int(input('몇 단을 계산할까요?'))
    if (number > 0): 
        multiplication(number)
    else:
        print('계산을 위해 양수를 입력해주세요.')
except:
    print('숫자로 입력해주세요!')



#########################################################
#                        Noas                           #
#########################################################



number = input("몇 단? : ")
if number.isnumeric():
    print(number, '단')
    for i in range(1, 50):
        if i % 2 == 1 and int(number) * i < 50:
            print(number, "x", i, " = ", int(number) * i)

else:
    print("잘못된 값을 입력하셨습니다.")
    quit()



#########################################################
#                          jm                           #
#########################################################

#사용자가 프로그램의 시작/종료 선택을 할 수 있도록 구조를 나누었습니다.
#강의에서 배운 lower을 통해 y,n이 대/소문자에 관계없이 작동하도록 함수를 만들었습니다.
#처음에는 1~9까지만 정해두었다가 구구단의 범위를 늘렸습니다.

def printGugu(dan):
    print(f"----- {dan} 단 ----- ")
    i = 1
    result = 1

    while result <= 50:
        result = dan * i
        if result > 50:
          break
        print(f"{dan} X {i} = {result}")

        i += 2

    print("구구단 출력이 완료되었습니다.")
    print("----------------------------")
    runAgain()


# 사용자 입력값을 받는 함수
def getInput():
    print("\n******************************************************")
    print("  홀수를 곱하여 50보다 작은 수를 출력하는 구구단 프로그램입니다.")
    print("******************************************************")

    dan = input("몇단을 출력할까요? :")

    try :
        dan = int(dan)
        if int(dan) > 0 and int(dan) < 51 :
            printGugu(dan)
        else:
            raise Exception()
        
    except:
        print("잘못된 값을 입력하셨습니다. 1~50 사이의 정수를 입력해주세요.")
        runAgain()

    return dan


# 프로그램 시작/종료 함수
def runAgain():
    again = input("프로그램을 다시 시작하시겠습니까? (Y/N)")
    if (again.lower()) == "y":
        getInput()
    elif (again.lower()) == "n":
        print("프로그램을 종료합니다.")
    else:
        print("잘못된 값을 입력하셨습니다.")
        runAgain()


getInput()


"""
📌Q2. 가위바위보 업그레이드 버젼을 함수로 만들어 봅시다. 아래와 같은 조건을 만족해 주세요.

조건 1: 게임을 몇 판을 진행할 것인지 입력을 받아주기
조건 2: 0, 1, 2, "가위", "바위", "보" 이외에 다른 입력을 받으면 재입력 받기
조건 3: 게임종료 후 나와 컴퓨터의 총 전적 출력하기

🔽 출력 예시

# 입력
games = int(input("몇 판을 진행하시겠습니까? : "))
rsp_advanced(games)

# 출력
가위 바위 보 : 0
나: 가위
컴퓨터: 보
1 번째 판 나의 승리!

가위 바위 보 : 1
나: 바위
컴퓨터: 가위
2 번째 판 나의 승리!

나의 전적: 2승 0무 0패
컴퓨터의 전적: 0승 0무 2패

"""

import random

#########################################################
#                        chabbo                         #
#########################################################


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


#########################################################
#                        Noas                           #
#########################################################

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



#########################################################
#                          jm                           #
#########################################################


# 중간에 프로그램을 종료하기 위해 방법을 찾다가 생성자, 소멸자를 알게되어 사용해보았습니다.. 맞는 사용법인지 모르겠네요
# 파이썬은 객체지향인데 어째서 같은 클래스 내에서 아래 있는 함수를 인지하지 못하나요? 하단에 작성한 함수를 상단에서 부를 수 있는 방법이 있을까요 ㅠㅜ?


class playRPSGame:
    drawCount = 0
    loseCount = 0
    winCount = 0

    def __init__(self): #왜 실행이 안되지?
        print("\n         *** 게임 시작 ***         \n")

    def __del__(self):
        print("프로그램을 종료합니다.")

    # 게임 종료 확인 함수
    def checkGameExit():
            again = input("게임을 종료할까요?(Y/N) :")

            if (again.lower()) == "n":
                return "이어하기"
            elif (again.lower()) == "y":
                thisGame = playRPSGame()
                del thisGame
                return None
            else: 
                print("계속하려면 'Y' / 종료하려면 'N' 을 입력해주세요.")
                return playRPSGame.checkGameExit()

    
    def errorAdapter():
            print("잘못된 값을 입력하셨습니다.")
            if playRPSGame.checkGameExit() == "이어하기":
                playRPSGame.runGame()

    # 게임 값 입력 함수
    def runGame():
        comRPS = ["가위", "바위", "보"]

        com = random.randint(0, 2)
        computer = comRPS[com]
        myRPS = input("'가위', '바위', '보' 혹은 0(가위),1(바위),2(보)를 입력해주세요: ")

        #1. type오류 먼저 확인 
        #2. 범위 오류 제어
        if myRPS.isnumeric():
            if  -1 < int(myRPS) and int(myRPS) < 3: 
                mStrRPS = comRPS[int(myRPS)]

                print("\n당신은 " + mStrRPS + " 를 냈습니다!")
                print("컴퓨터는 " + computer + " 를 냈습니다!")
                playRPSGame.getRPSResult(mStrRPS, int(myRPS), com)

            else:
                playRPSGame.errorAdapter()
            
        elif comRPS.__contains__(myRPS):

            print("\n당신은 " + myRPS + " 를 냈습니다!")
            print("컴퓨터는 " + computer + " 를 냈습니다!")
            playRPSGame.getRPSResult(myRPS, comRPS.index(myRPS), com)

        else:
            playRPSGame.errorAdapter()



    # 가위바위보 게임 인트로
    def introRPS():

        print("\n***************************************************")
        print("      ✌ ✊✋   가위 바위 보 게임입니다.   ✋✊✌ ")
        print("***************************************************")

        playCounts = input("\n몇 판을 진행하시겠습니까? 숫자로 입력해주세요. :")
        print("\n         *** 게임 시작 ***         \n")


        if playCounts.isnumeric():
            curCount=0

            for i in range(0, int(playCounts)):
                playRPSGame.runGame()
                curCount += 1

                if i == int(playCounts)-1:
                    print("================ 게임종료 =================\n")
                    print(f"당신의 전적 : {playRPSGame.winCount}승 / {playRPSGame.drawCount}무 / {playRPSGame.loseCount}패")
                    print(f"컴퓨터의 전적 : {playRPSGame.loseCount}승 / {playRPSGame.drawCount}무 / {playRPSGame.winCount}패\n")

                    if playRPSGame.winCount > playRPSGame.loseCount:
                        print("==============================================")
                        print("  🎉 대결에서 승리했습니다! 축하합니다 !! 🎉")
                        print("==============================================\n")

        else:

            print("입력값이 올바르지 않습니다.")
            playRPSGame.checkGameExit() == "이어하기"
            playRPSGame.introRPS()


    #결과 출력 함수
    def getRPSResult(user, userNum, com):
        
        score = com - userNum
        if userNum == com :
            playRPSGame.drawCount += 1
            print("\n무승부 입니다!\n")

        elif score == 2 or score == -2:
            playRPSGame.loseCount += 1
            print("\n당신의 패배 입니다!\n")
        else :
            playRPSGame.winCount += 1
            print("\n 축하합니다! 당신의 승리입니다!\n")


p = playRPSGame
p.introRPS()


"""
📌Q3. 2개의 숫자를 입력하여 그 사이에 짝수만 출력하는 함수를 만들어 봅시다. 그리고 중앙값도 함께 출력 해봅시다.(단, 중앙값이 짝수가 아닐 경우에는 중앙값은 출력을 하지 않고, 짝수인 수만 출력한다)

중앙값: 정중앙에 있는 값

특정 두 숫자 사이의 수들을 리스트로 만드는 법

n = 1
m = 10
numbers = [ i for i in range(n,m+1)] # [1,2,3,4,5,6,7,8,9,10]
# range(시작 숫자, 끝 숫자 + 1)
🔽 출력 예시

# 입력
n = int(input("첫 번째 수 입력 : "))
m = int(input("두 번째 수 입력 : "))
find_even_number(n, m)

# 출력
첫 번째 수 입력 : 1
두 번째 수 입력 : 11
2 짝수
4 짝수
6 짝수
6 중앙값
8 짝수
10 짝수

"""
#########################################################
#                        chabbo                         #
#########################################################


def find_even_number(n, m):
    if (n > m):
        temp = m
        m = n
        n = temp

    num_list = []
    for i in range(n,m+1):
        num_list.append(i)
    
    middle_num = int(len(num_list) /2)
    idx = 0
    for num in num_list:
        if ((idx == middle_num) and (num_list[middle_num] % 2 ==0)):
            print(num, '중앙값')
        elif (num % 2 == 0):
            print(num, '짝수')
        idx += 1

print('두 숫자 사이에 짝수 값만 찾아주는 마법의 컴퓨터!')
try:
    n = int(input('첫번째 수를 입력해주세요 : '))
    m = int(input('두번째 수를 입력해주세요 : '))
    find_even_number(n,m)
except:
    print('를 입력해주세요!')


#########################################################
#                          jm                           #
#########################################################


"""
# 처음 제가 구현하려고 했던 함수들입니다.. ㅠ 결국 포기하고 다른 방법으로 구현하게 되었지만
# 재귀함수를 활용하여 두개의 다른 함수들을 이용해서 값을 리턴하는 구조에 어떤 점을 수정해야하는지 질문드리고 싶습니다.

# 에러:
# 잘못된 값 입력 후 정상 값 입력시 리턴값이 이전 값(잘못된 값)으로 나옴 + 함수의 반복

#제가 구현하려고 했던 방법은:
x = input("값 입력 : ")
checkType(x)
-> 타입이 잘못되었을 경우 재귀함수를 통해 checkType(x) 반복
-> 타입이 맞았을 경우 checkMinus(x)
-> 0 이하의 값은 재귀함수를 통해 checkMinus(var) 반복
-> 타입이 int , 0 보다 큰 값은 return 

# 수정하기 위한 노력: 파이썬에서 재귀함수를 구현하기 위해서 return에서 해당 함수를 다시 불러야한다는 것을 검색을 통해 알게되었습니다. 하지만 아래 코드에서는 왜 안되는지, 오류가 나는지 모르겠습니다.. .ㅠㅠㅠ

def checkMinus(var):
    if var > 0:
        print("값리턴 ####", var)
        return int(var)
    else:
        print("0보다 작을때 #####")
        checkType(input("0보다 큰 숫자로 입력해주세요. : "))
        checkMinus(var)

def checkType(var):
    if var.isnumeric:
        print("숫자입력#####")
        checkMinus(int(var))

    else :
        print("잘못된 값을 입력하셨습니다.")
        checkType(input("반드시 정수로 입력해주세요 : "))


def checkLastNum(fir, sec):
    if sec >= fir:
        return int(sec)
    else :
        print("마지막 값은 처음 값보다 큰 수로 입력해주세요.")
        last = checkType(input("마지막 값을 다시 입력해주세요 : "))
        checkLastNum(fir, last)
"""


ERROR_MSG_type = "잘못된 값을 입력하셨습니다. 0보다 큰 숫자 정수를 입력해주세요."
ERROR_MSG_bigger = "잘못된 값을 입력하셨습니다. 처음 입력한 숫자보다 큰 숫자를 입력해주세요."


#처음 숫자의 타입이 int / 0보다 큰지 확인 후 값 리턴
def setFirNumber():
    num = input("처음 숫자를 입력해주세요 : ")
    if num.isnumeric():
        int(num)
        if int(num) > 0:
            return int(num)
        else : 
            print(ERROR_MSG_type)
            return setFirNumber()
    else:
        print(ERROR_MSG_type)
        return setFirNumber()


#두번째 숫자의 타입이 int / 처음 값보다 큰지 확인 후 값 리턴
def setSecNumber(num1):
    num2 = input("마지막 숫자를 입력해주세요 : ")
    if num2.isnumeric():
        int(num2)
        if int(num2) > num1:
            return int(num2)
        else : 
            print(ERROR_MSG_bigger)
            print("입력된 첫 숫자 : ", num1)
            return setSecNumber(num1)
    else:
        print(ERROR_MSG_type)
        return setSecNumber(num1)


def checkPlayAgain():
        again = input(" 프로그램이 종료되었습니다.\n다시 시작하시려면 스페이스바를 입력해주세요! : ")
        again = ' '.join(again.split())
        if (again == " " or again == ""): 
            getCenterNum()
        else :
            print("\n***************************************************")
            print("             프로그램을 종료합니다.")
            print("***************************************************")


def getCenterNum():
    
        print("\n***************************************************")
        print("  중앙값이 짝수인지 확인하는 프로그램입니다.")
        print("***************************************************")

        #타입 확인
        #음수 확인
        #처음숫자 < 마지막숫자
        num1 = setFirNumber()
        num2 = setSecNumber(int(num1))

        print("입력된 첫 숫자 : ", num1)
        print("입력된 마지막 숫자 : ", num2)

        numbers = [i for i in range(num1, num2+1)]
        numbers.sort()
        
        medianIdx = len(numbers)/2

        for i, var in enumerate(numbers):

            #짝수
            if var % 2 == 0 :
                print(f"값 : {var}  = 짝수")
                #중앙값
                if numbers[int(medianIdx)] == var:
                    print(f"값 : {var}  = * 중앙값 *")
                #elif numbers[int(medianIdx)] -1 == var: #{1,2,3,4}의 리스트가 있을때 2는 중앙값인가?
                #    print(f"값 : {var}  = * 중앙값 *")
        

        checkPlayAgain()

getCenterNum()


"""
📌Q4. 2개의 숫자를 입력하여 그 사이에 소수가 몇 개인지 출력하는 함수를 만들어 봅시다.

소수: 1과 자기 자신만을 약수로 가지는 수

🔽 출력 예시 

# 입력
n = int(input("첫 번째 수 입력 : "))
m = int(input("두 번째 수 입력 : "))
count_prime_number(n, m)

# 출력
소수개수  4

"""


#########################################################
#                        Noas                           #
#########################################################

n = input("첫 번째 수 입력 : ")
m = input("두 번째 수 입력 : ")
x = 0

if n.isdigit() and m.isdigit():
    for i in range(int(n), int(m) + 1):
        y = 0
        for z in range(1, i + 1):
            if i % z == 0:
                y += 1
        if y == 2:
            x += 1
else:
    print("잘못된 값을 입력하셨습니다.")
    quit()

print('소수는',x,'개 입니다.')


#########################################################
#                          jm                           #
#########################################################

import math

ERROR_MSG_type = "잘못된 값을 입력하셨습니다. 0보다 큰 숫자 정수를 입력해주세요."
ERROR_MSG_bigger = "잘못된 값을 입력하셨습니다. 처음 입력한 숫자보다 큰 숫자를 입력해주세요."

#처음 숫자의 타입이 int / 0보다 큰지 확인 후 값 리턴
def setFirNumber():
    num = input("처음 숫자를 입력해주세요 : ")
    if num.isnumeric():
        int(num)
        if int(num) > 0:
            return int(num)
        else : 
            print(ERROR_MSG_type)
            return setFirNumber()
    else:
        print(ERROR_MSG_type)
        return setFirNumber()


#두번째 숫자의 타입이 int / 처음 값보다 큰지 확인 후 값 리턴
def setSecNumber(num1):
    num2 = input("마지막 숫자를 입력해주세요 : ")
    if num2.isnumeric():
        int(num2)
        if int(num2) > num1:
            return int(num2)
        else : 
            print(ERROR_MSG_bigger)
            print("입력된 첫 숫자 : ", num1)
            return setSecNumber(num1)
    else:
        print(ERROR_MSG_type)
        return setSecNumber(num1)


def checkPlayPrimeAgain():
        again = input(" 프로그램이 종료되었습니다.\n다시 시작하시려면 스페이스바를 입력해주세요! : ")
        again = ' '.join(again.split())
        if (again == " " or again == ""): 
            printPrimeNums()
        else :
            print("\n***************************************************")
            print("             프로그램을 종료합니다.")
            print("***************************************************")


def printPrimeNums():

    print("\n***************************************************")
    print("  두 숫자 사이의 소수가 몇 개인지 출력하는 프로그램입니다.")
    print("***************************************************")

    fir = int(setFirNumber())
    sec = int(setSecNumber(fir))

    a = [False,False] + [True]*(sec-1)
    primes=[]

    for i in range(fir,sec+1):
      if a[i]:
        primes.append(i)
        for j in range(2*i, sec+1, i):
            a[j] = False
    print("소수 리스트 : ", primes)

    print(f"\n{fir}과 {sec} 사이의 소수들은 총 {len(primes)} 개 입니다.\n")
    checkPlayAgain()


printPrimeNums()