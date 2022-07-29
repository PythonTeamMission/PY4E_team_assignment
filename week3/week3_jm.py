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

#사용자가 프로그램의 시작/종료 선택을 할 수 있도록 구조를 나누었습니다.
#강의에서 배운 lower을 통해 y,n이 대/소문자에 관계없이 작동하도록 함수를 만들었습니다.
#구구단을 처음에는 1~9까지만 정해두었다가
# 1. 3x11은 50보다 작은 값
# 2. 조건에서 1~9까지 범위를 제한하지 않음
#따라서 구구단의 범위를 늘렸습니다.

"""
    i = None
    while result<= 50:
        if i == None:
            i = 1
"""

print("???????????")

def printGugu(dan):
    print(f"----- {dan} 단 ----- ")
        result = dan * i
        if result > 50:
          break
        print(f"{dan} X {i} = {result}")

        i += 2

    print("구구단 출력이 완료되었습니다.")
    print("----------------------------")
    runAgain()


#사용자 입력값을 받는 함수
def getInput():
    print("\n***************************************************")
    print("  50보다 작은 수를 출력하는 홀수 구구단 프로그램입니다.")
    print("***************************************************")

    dan = input("몇단을 출력할까요?")

    if dan.isnumeric():
        printGugu(int(dan))
    else:
        print("잘못된 값을 입력하셨습니다.")
        runAgain()


#프로그램 시작/종료 함수
def runAgain():
    again = input("프로그램을 다시 시작하시겠습니까? (Y/N)")
    if (again.lower()) == y:
        main()
    elif (again.lower()) == n:
        print("프로그램을 종료합니다.")
    else : 
        print("잘못된 값을 입력하셨습니다.")
        runAgain()


main()


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

