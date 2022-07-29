

모두의 파이썬 팀과제 week2 파일을 제출하는 폴더입니다.

===============================================================

                    코치님의 피드백 정리
                    
===============================================================

# Q1 - jm


import random

print("\n ********************************** \n")
print("컴퓨터와 함께하는 가위바위보 게임입니다.")
print("\n **********************************")


def printWinner(winner):
    # winner == 0 : 컴퓨터의 승리 / winner == 1: 사람의 승리
    if winner == 0:
        print("\n컴퓨터의 승리입니다!\n")
    else:
        print("\n 축하합니다! 당신의 승리입니다!\n")

# 가위바위보 진행 함수


def rockPaperScissors(my, com):
    if com == my:
        print("무승부 입니다!")
    elif my == "가위":  # 사람 - 가위
        if com == "바위":
            printWinner(0)
        else:  # 컴퓨터 - 보
            printWinner(1)
    elif my == "바위":  # 사람 - 바위
        if com == "가위":
            printWinner(1)
        else:  # 컴퓨터 - 보
            printWinner(0)
    elif my == "보":  # 사람 - 보
        if com == "가위":
            printWinner(0)
        else:  # 컴퓨터 - 바위
            printWinner(1)


rcp = ["가위", "바위", "보"]
myRPC = input("\n'가위', '바위', '보' 혹은 0(가위),1(바위),2(보)를 입력해주세요: ")
computer = rcp[random.randint(0, 2)]

try:
    if myRPC.isnumeric():
        myRPC = rcp[int(myRPC)]
    elif myRPC not in rcp:
        raise Exception

    print("\n당신은 " + myRPC + " 를 냈습니다!")
    print("컴퓨터는 " + computer + " 를 냈습니다!")
    rockPaperScissors(myRPC, computer)

except:
    print("잘못된 값을 입력하셨습니다.\n프로그램을 종료합니다.")
제가 코드를 작성할 때 중요시한 부분은
자료형을 하나로 고정해서 출력할 때 용이하게 한다(문자열),
중복되는 부분은 없애도록 한다(try except에서 겹치는 부분).
이정도 였습니다.
입력이 정상적으로 되지 않을 때 except로 예외처리하고자 했고, isnumeric으로 숫자를 입력했다면, rcp 리스트에서 받아와서 값을 변경시켰고, 0, 1, 2외의 값이 등장한다면 IndexError로, 이상한 문자열일 경우에는 raise로, 예외처리를 해봤습니다.




그리고 분기를 나눌 때, 집합의 여집합을 떠올리면서 분기를 세우는 것도 좋습니다. 예를 들어 학점을 나눌 때
score = 88

if score >= 95 and score <= 100:
...
elif score >= 90 and score <= 94:
...
이러한 분기에서
score = 88

if score >= 95:
    print("A+")
elif score >= 90:
    print("A")
이렇게 바꾸는 것이죠. 그 이유는 if score >= 95 and score <= 100:이 부정이라면 어차피 score는 94 이하이기 때문에 elif score >= 90 and score <= 94: 에서 score <= 94는 제외하고 나타내도 되는 것입니다. 동일한 이유로 다음에는 elif score >= 85 로 나타내도 되는 것이겠죠? 어차피 이전 조건에서 score는 90보다 작은 것이 확인되었으니까요.




# Q3 - Noas


Q3 문제에서 Noas님의 제출에서 수정하면 좋을 것 같은 부분이 있었습니다. 먼저 grader함수의 인자로 이미 숫자형이 들어오기 때문에 int 함수는 빼도 됩니다. 그리고, 학점을 받을 변수를 설정해서 각 조건마다 학점만 저장하고, 모든 조건을 마친 후에 한꺼번에 print 하는 것입니다.
elif score < 60:
    grade = "F"
...

# 모든 조건을 거친 후

print("학생 이름 :", name)
print("점수 :", score)
print("학점 :", grade)
이런 식으로 하면 확실히 코드가 줄어들 겁니다 ㅎㅎ

