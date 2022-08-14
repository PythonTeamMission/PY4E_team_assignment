
"""
📌Q1. 여러분 혹시 베스킨라빈스31 게임을 아시나요? 1부터 31까지 숫자를 플레이어들끼리 번갈아 외치다가 31을 외치는 사람이 패배하는 게임인데요.

이번엔 이 게임을 파이썬 함수로 만들어 봅시다. 지성이 없이 숫자를 랜덤하게 외치는 컴퓨터와 대결을 해보겠습니다.

😲조건1 - 나의 턴에서는 숫자를 직접 입력하며 한 번 입력 후에 space 한 번으로 구분

Ex)
my = input("My turn - 숫자를 입력하세요: ")
1 2 3
😲조건2 - 나와 컴퓨터 모두 한 턴에 1회 ~ 3회까지만 숫자를 외칠 수 있음

😲조건3 - 외쳐진 숫자보다 1큰 수만 외칠수 있음 (ex: 5 다음엔 무조건 6)

위 조건이 안맞을 경우 다시 입력
🧐hint

# 컴퓨터가 1~3회 중에서 몇 번을 시도할 것인지 랜덤하게 고르는 방법
import random
computer_turn_num = random.randint(1,3)

# 첫번째를 나타내는 인덱스 0, 마지막을 나타내는 인덱스 -1
example = [1,2,3]
print(example[0]) # 1
print(example[-1] # 3
✅출력 예시
bs31()

베스킨라빈스 써리원 게임
------------------
My turn - 숫자를 입력하세요: 1 2 3
현재 숫자 : 3
컴퓨터 : 4
현재 숫자 : 4

My turn - 숫자를 입력하세요: 5
현재 숫자 : 5
컴퓨터 : 6
컴퓨터 : 7
현재 숫자 : 7


"""
import re
import random

#정규표현식 사용에 도전해봤습니다!
#게임 규칙을 변수에 넣고 필요한 경우 출력하도록 설계했습니다.

RULE_TYPE = "* 마지막 값과 연속된 숫자를 입력해주세요. ex) 1 2 3"
RULE_START = "* 처음 숫자는 1부터 시작합니다."
RULE_LEN = "* 숫자는 최소 하나를, 최대 세개로 입력해주세요."
RULE_WIN = "* 31을 외치면 패배입니다! 승리를 기원합니다!\n"

YOU = "당신"                                                                    #string값을 변수화 = 당신
COMPUTER = "컴퓨터"                                                             #string값을 변수화 = 컴퓨터

lastNum = 0                                                                     #전역변수 lastNum: 해당 라운드의 마지막 숫자

print("\n----------------------------------------------")
print("          베스킨라빈스 써리원 게임")
print("----------------------------------------------\n")
print(RULE_TYPE)
print(RULE_START)
print(RULE_LEN)
print(RULE_WIN)


#승자 출력 함수
def printWinner(winner):
    if winner == YOU:
        print(f"\n🎉{winner}의 승리입니다! 축하합니다 ! 🎉\n")
    else :
        print(f"\n{winner}의 승리입니다😭 다시 도전해보세요~! \n")


#사용자의 값을 입력받는 함수
def verifyInput(lastNum):
    myNum = input("\n당신의 숫자를 입력하세요 : ")                                  #myNum : 입력받은 변수            
    myList = re.findall('[0-9]+', myNum)                                          #0~9까지 숫자중 일치하는 요소만 리스트로 반환 /장: 중간 어떤 문자(, - ' ')가 들어가도 숫자만 얻음/ 단:오류발생가능

    if len(myList) == 0 or 3 < len(myList) :                                      #입력받은 값이 없을때, 값이 넷 이상일때          
        print(RULE_LEN)                                                                 #규칙 출력
        return verifyInput(lastNum)                                                     #재귀함수 - 다시 사용자의 값을 입력받음

    if myList[0] == 0:                                                            #입력받은 값이 0일때
        print(RULE_START)                                                               #규칙 출력
        return verifyInput(lastNum)                                                     #재귀함수 - 다시 사용자의 값을 입력받음

    if lastNum + 1 != int(myList[0]):                                             #입력받은 값이 마지막 값+1 이 #아닐때
        print(RULE_TYPE)                                                                #규칙 출력
        return verifyInput(lastNum)                                                     #재귀함수 - 다시 사용자의 값을 입력받음
    
    for index, value in enumerate(myList):                                        #입력받은 리스트 반복
        val = int(myList[0])                                                            #리스트 값을 int로 변환
        if int(val+index) != int(myList[index]) :                                       # 첫 숫자 + index = 입력된 숫자 -> 성립되지 않으면 잘못된 값 입력
            print(RULE_TYPE)                                                            #규칙 출력 
            return verifyInput(lastNum)                                           #재귀함수 - 다시 사용자의 값을 입력받음

        if int(value) == 31:                                                      #입력한 리스트에 31이 있는지 확인
            printWinner(COMPUTER)                                                      #컴퓨터의 승리, 승자 출력 함수 호출
            break                                                                      #반복문 해제
    
    return myList[-1]                                                              #규칙을 어기지 않았을때, 마지막 값 리턴



#컴퓨터의 값을 출력하는 함수
def getComNum(lastNum):
    endNum = 0                                                                     #리턴할 변수 생성
    for i in range(1, random.randint(2,4)):                                        # 1~3까지 랜덤한 값을 i로 받도록 반복문 생성
        print("컴퓨터의 숫자 : ", i+lastNum)                                        # 마지막 숫자 + 랜덤한 값을 출력
        endNum = i+lastNum                                                         # 컴퓨터의 랜덤숫자를 endNum 저장 (최신 값으로 계속 바꿔줌)
        if i+lastNum == 31:                                                             #31이 나왔을경우 사용자 승리
            printWinner(YOU)
            break
    return endNum                                                                  #endNum 리턴 (가장 마지막으로 컴퓨터가 출력한 값)



#실행코드
while lastNum < 31:                                                                #마지막 값이 30이하일 경우 계속 반복
    
    print("\n---- 현재 숫자 : " , lastNum, " ----")
    lastNum = int(verifyInput(lastNum))
    if lastNum == 31: break
    print("\n---- 현재 숫자 : " , lastNum, " ----\n")
    lastNum = getComNum(lastNum)
    if lastNum == 31: break



