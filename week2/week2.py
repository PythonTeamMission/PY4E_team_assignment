# 모두를 위한 파이썬 PY4E 
# 2주차 팀 과제
# 팀: 턴태코치_2팀 / 작성자: jm / 작성일: 220725
# 👍👍2주차 미션 목적 - 조건부 실행과 함수 익히기

import random

"""
📌Q1. 컴퓨터와 함께하는 가위바위보 게임을 만들어봅시다!

조건1 : 함수의 인자로는 나의 가위바위보 선택이 들어감
          (0, 1 ,2 혹은 "가위", "바위", "보" 로 입력할 수 있습니다. - 총 6가지 방법으로 넣을 수 있음)

조건2 : 누가 무엇을 냈고, 누가 승리 했는지 출력이 되어야 함
 

hint: 컴퓨터가 가위바위보 하게 만드는 법
# 아래의 코드를 추가하면 됩니다
import random
# 0 ~ 2 숫자를 랜덤으로 뽑아내는 코드
computer = random.randint(0, 2)

"""

####################################

computer = random.randint(0, 2)
myIntRPS = int(-1)
myStrRPS = str()

print("\n ********************************** \n")
print("컴퓨터와 함께하는 가위바위보 게임입니다.")
print("\n **********************************")

def printWinner(winner):
    #winner == 0 : 컴퓨터의 승리 / winner == 1: 사람의 승리
    if winner == 0: print("\n컴퓨터의 승리입니다!\n")
    else: print("\n 축하합니다! 당신의 승리입니다!\n")

def strRPS_to_intRPS(myStrRPS):
    if myStrRPS == "가위":
        return 0
    elif myStrRPS == "바위":
        return 1
    else: return 2

def intRPS_to_strRPS(myIntRPS):
    if myIntRPS == 0:
        return "가위"
    elif myIntRPS == 1:
        return "바위"
    elif myIntRPS == 2: 
        return "보"

def rockPaperScissors(myIntRPS):
    if computer == myIntRPS:
        print("무승부 입니다!")
    elif myIntRPS == 0: #사람 - 가위
        if computer == 1: 
            #컴퓨터 - 바위
            printWinner(0)
        else: #컴퓨터 - 보
            printWinner(1)
    elif myIntRPS == 1: # 사람 - 바위
        if computer == 0: 
            #컴퓨터 - 가위
            printWinner(1)
        else: #컴퓨터 - 보
            printWinner(0)
    elif myIntRPS == 2: # 사람 - 보
        if computer == 0:
            #컴퓨터 - 가위
            printWinner(0)
        else: #컴퓨터 - 바위
            printWinner(1)

myRPC = input("\n'가위', '바위', '보' 혹은 0(가위),1(바위),2(보)를 입력해주세요: ")

try:
    myIntRPS = int(myRPC)
    print("\n당신은 ", intRPS_to_strRPS(myIntRPS) ," 를 냈습니다!")
    print("컴퓨터는 ", intRPS_to_strRPS(computer) , " 를 냈습니다!")
    rockPaperScissors(myIntRPS)

except:
    print("exception")
    myStrRPS = myRPC
    print("\n당신은 ", myStrRPS , "를 냈습니다!")
    print("컴퓨터는 " + intRPS_to_strRPS(computer) + "를 냈습니다!")
    rockPaperScissors(strRPS_to_intRPS(myStrRPS))


# 최대한 함수를 활용해서 코드를 만들어봤는데 더 복잡해진 것 같아요. 가위바위보를 더 가독성 좋게 만들려면 어떻게 해야할지 모르겠네요 ㅠㅠ..


"""
📌Q2. 월급을 입력하면 연봉을 계산해주는 계산기를 만들어 봅시다. 세전 연봉과 세후 연봉을 함께 출력하도록 해봅니다.
   📑아래의 세율 표를 토대로 만들어주세요(단, 실제 세율과 다를 수 있습니다!)
 
 1200만원 이하 : 6%
 4600만원 이하 : 15%
 8800만원 이하 : 24%
 1억 5천만원 이하 : 35%
 3억원 이하 : 38%
 5억원 이하 : 40%
 5억원 초과 : 42%

   🔽출력 예시

# 월급 입력
monthly_payment = 300
yearly_payment(monthly_payment)

# 출력
세전 연봉: 3600만원
세후 연봉: 3060만원
"""

print("\n ********************************** \n")
print("월급을 입력하면 연봉을 계산해주는 프로그램 입니다.")
print("\n **********************************")

def taxCalculator(ySal):
    if ySal <= 1200:
        return ySal - (ySal*0.06)
    elif ySal <= 4600:
        return ySal - (ySal*0.15)
    elif ySal <= 8800:
        return ySal - (ySal*0.24)
    elif ySal <= 15000:    
        return ySal - (ySal*0.35)
    elif ySal <= 30000:    
        return ySal - (ySal*0.38)
    elif ySal <= 50000:
        return ySal - (ySal*0.40)
    else:
        return ySal - (ySal*0.42)

mSal = input("\n월급을 입력해주세요: ")

try:
     ySal = int(mSal) * 12
except: 
    mSal = input("\n월급을 숫자로 입력해주세요: ")
    ySal = int(mSal) * 12

print("세전 연봉: ", ySal, "만원")
print("세후 연봉: ", int(taxCalculator(ySal)), "만원\n")

#최대한 깔끔하게 적기 위해 노력했습니다. + 사용자가 반복해서 int가 아닌 타입으로 입력했을 경우를 방지하려면 for문 말고 다른 방법이 있는지 고민하고있습니다.


"""
📌Q3. 학생 이름과 점수를 입력하면 학점을 출력하는 학점 변환기를 만들어 봅시다.

이름과 점수, 학점 모두 출력하도록 해봅니다.
 
   📑아래의 학점표를 토대로 만들어주세요
A+ : 95~100점
A  : 90~94점
B+ : 85~89점
B  : 80~84점
C+ : 75~79점
C  : 70~74점
D+ : 65~69점
D  : 60~64점
F  : 60점 미만

   🔽출력 예시

# 이름과 점수 입력
grader("이호창", 99)

# 출력
학생이름 : 이호창
점수 : 99점
학점 : A+
"""

print("\n ********************************** \n")
print("이름과 점수를 입력하면 학점을 출력하는 학점 변환기 입니다.")
print("\n **********************************")

name = input("\n이름을 입력해주세요 : ")
score = input("점수를 입력해주세요 : ")

try:
    score = int(score)
except:
    int(input("점수를 정수로 입력해주세요 : "))

def getGrade(score):
    if score < 0:
        return "존재하지 않는 점수 입니다. 다시 입력해주세요!"
    elif score <60:
        return "F"
    elif score < 65:
        return "D"
    elif score < 70:
        return "D+"
    elif score < 75:
        return "C"
    elif score < 80:
        return "C+"
    elif score < 85:
        return "B"
    elif score < 90:
        return "B+"
    elif score < 95:
        return "A"
    elif score <101:
        return "A+"
    else: return "존재하지 않는 점수 입니다. 다시 입력해주세요!"


print("\n학생이름 : ", name)
print("점수 : ", score)
print("학점 : ", getGrade(score), "\n")
        


"""
📌Q4. 나이와 현금 또는 카드를 입력하면 버스 요금이 출력되는 버스 요금 계산기를 만들어봅시다. 

 

   📑아래의 요금표를 토대로 만들어주세요

 

   🔽출력 예시

# 버스 요금 입력
bus_fare(30, "현금")

# 출력
나이: 30세
지불유형: 현금
버스요금: 1300원
"""