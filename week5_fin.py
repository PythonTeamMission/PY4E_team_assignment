# 모두를 위한 파이썬 PY4E
# 5주차 팀 과제
# 팀: 턴태코치_2팀 / 작성자: jm / 기여자: chabbo, jm, Noas / 작성일: 220816
# 👍👍5주차 미션 목적 - 조건문, 반복문, 문자열, 리스트의 활용

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

#########################################################
#                        Noas                           #
#########################################################



#########################################################
#                        chabbo                         #
#########################################################



#########################################################
#                          jm                           #
#########################################################

import re
import random

# 정규표현식 사용에 도전해봤습니다!
# 게임 규칙을 변수에 넣고 필요한 경우 출력하도록 설계했습니다.

RULE_TYPE = "* 마지막 값과 연속된 숫자를 입력해주세요. ex) 1 2 3"
RULE_START = "* 처음 숫자는 1부터 시작합니다."
RULE_LEN = "* 숫자는 최소 하나를, 최대 세개로 입력해주세요."
RULE_WIN = "* 31을 외치면 패배입니다! 승리를 기원합니다!\n"

YOU = "당신"                                                         # string값을 변수화 = 당신
COMPUTER = "컴퓨터"                                                   # string값을 변수화 = 컴퓨터

lastNum = 0                                                         # 전역변수 lastNum: 해당 라운드의 마지막 숫자

print("\n----------------------------------------------")
print("          베스킨라빈스 써리원 게임")
print("----------------------------------------------\n")
print(RULE_TYPE)
print(RULE_START)
print(RULE_LEN)
print(RULE_WIN)


# 승자 출력 함수
def printWinner(winner):
    if winner == YOU:
        print(f"\n🎉{winner}의 승리입니다! 축하합니다 ! 🎉\n")
    else:
        print(f"\n{winner}의 승리입니다😭 다시 도전해보세요~! \n")


# 사용자의 값을 입력받는 함수
def verifyInput(lastNum):
    myNum = input("\n당신의 숫자를 입력하세요 : ")                             # myNum : 입력받은 변수
    myList = re.findall('[0-9]+', myNum)                                # 0~9까지 숫자중 일치하는 요소만 리스트로 반환 /장: 중간 어떤 문자(, - ' ')가 들어가도 숫자만 얻음/ 단:오류발생가능

    if len(myList) == 0 or 3 < len(myList):                             # 입력받은 값이 없을때, 값이 넷 이상일때
        print(RULE_LEN)                                                     # 규칙 출력
        return verifyInput(lastNum)                                         # 재귀함수 - 다시 사용자의 값을 입력받음

    if myList[0] == 0:                                                  # 입력받은 값이 0일때
        print(RULE_START)                                                   # 규칙 출력
        return verifyInput(lastNum)                                         # 재귀함수 - 다시 사용자의 값을 입력받음

    if lastNum + 1 != int(myList[0]):                                   # 입력받은 값이 마지막 값+1 이 #아닐때
        print(RULE_TYPE)                                                    # 규칙 출력
        return verifyInput(lastNum)                                         # 재귀함수 - 다시 사용자의 값을 입력받음

    for index, value in enumerate(myList):                              # 입력받은 리스트 반복
        val = int(myList[0])                                                # 리스트 값을 int로 변환
        if int(val + index) != int(myList[index]):                          # 첫 숫자 + index = 입력된 숫자 -> 성립되지 않으면 잘못된 값 입력
            print(RULE_TYPE)                                                    # 규칙 출력
            return verifyInput(lastNum)                                         # 재귀함수 - 다시 사용자의 값을 입력받음

        if int(value) == 31:                                                # 입력한 리스트에 31이 있는지 확인
            printWinner(COMPUTER)                                               # 컴퓨터의 승리, 승자 출력 함수 호출
            break                                                               # 반복문 해제

    return myList[-1]                                                   # 규칙을 어기지 않았을때, 마지막 값 리턴


# 컴퓨터의 값을 출력하는 함수
def getComNum(lastNum):
    endNum = 0                                                          # 리턴할 변수 생성
    for i in range(1, random.randint(2, 4)):                            # 1~3까지 랜덤한 값을 i로 받도록 반복문 생성
        print("컴퓨터의 숫자 : ", i + lastNum)                                    # 마지막 숫자 + 랜덤한 값을 출력
        endNum = i + lastNum                                                  # 컴퓨터의 랜덤숫자를 endNum 저장 (최신 값으로 계속 바꿔줌)
        if i + lastNum == 31:                                                 # 31이 나왔을경우 사용자 승리
            printWinner(YOU)
            break
    return endNum                                                       # endNum 리턴 (가장 마지막으로 컴퓨터가 출력한 값)


# 실행코드
while lastNum < 31:                                                 # 마지막 값이 30이하일 경우 계속 반복

    print("\n---- 현재 숫자 : ", lastNum, " ----")
    lastNum = int(verifyInput(lastNum))
    if lastNum == 31: break
    print("\n---- 현재 숫자 : ", lastNum, " ----\n")
    lastNum = getComNum(lastNum)
    if lastNum == 31: break

"""
📌Q2. 다음과 같이 학생들의 시험 답지가 있습니다. 그리고 답안지도 있습니다.
함수를 하나 만들어 채점을 하고 학생들의 점수를 출력하고 등수도 함께 출력해주세요.
 
# 학생 답
s = ["김갑,3242524215",
"이을,3242524223",
"박병,2242554131",
"최정,4245242315",
"정무,3242524315"]

# 정답지
a = [3,2,4,2,5,2,4,3,1,2]

🧐hint
# 문자열도 숫자 정렬 가능
a = ["5","2","3"]
a.sort()
["2", "3", "5"]
# 내림차순 정렬 가능
a.sort(reverse=True)
["5", "3", "2"]
✅출력 예시
grader(s, a)
학생: 정무 점수: 90점 1등
학생: 김갑 점수: 80점 2등
학생: 이을 점수: 70점 3등
학생: 박병 점수: 50점 4등
학생: 최정 점수: 40점 5등
"""


#########################################################
#                        Noas                           #
#########################################################



#########################################################
#                        chabbo                         #
#########################################################



#########################################################
#                          jm                           #
#########################################################


#함수 하나로 만들어 보기 위해 노력해봤습니다..
# 반복문을 세번이나 쓰는 게 맘이 안 드네요 ㅠㅠ

s = [                                                                  #예시 학생 답 리스트
    "김갑,3242524215",
    "이을,3242524223",
    "박병,2242554131",
    "최정,4245242315",
    "정무,3242524315"
]

q = [3,2,4,2,5,2,4,3,1,2]                                               #예시 답안
resultList = []                                                         #결과리스트 전역변수

#파라미터 : 학생답안 리스트, 정답 리스트
#두 리스트를 받아 학생 이름과 점수 결과를 출력하는 함수
def printScore(list, answer):
    global resultList                                                   # 결과리스트 전역변수를 사용하겠다고 명시
    list_answer = [str(int) for int in answer]                          # int타입을 string타입으로 수정. list_answer: answer값을 문자열로 갖고있는 리스트
    string_answer = "".join(list_answer)                                # string_answer : answer를 하나의 문자열로 생성

    for val in list:                                                    # 학생답안 리스트에서 각 항목의 데이터 추출 반복문
        student = val.split(",")                                            # 항목을 ','를 기준으로 split / student: 학생 이름, 학생답안을 갖고있는 리스트
        stName = student[0]                                                 # stName = 학생의 이름
        stAnswer = student[1]                                               # stAnswer = 학생의 답변
        score = 0                                                           # 학생의 점수를 확인하기 위한 변수 생성 및 초기화
        for i, v in enumerate(string_answer):                               # enumerate()함수 : 인덱스, 값 확인가능 / string_answer: 정답문자열의 길이만큼 반복, 인덱스를 통해 학생의 답안과 정답을 비교
            if stAnswer[i] == v:                                                # stAnswer[i]: 학생의 답 중 i인덱스의 값 == 정답의 i인덱스의 값 비교
                score += 1                                                          # 정답과 학생답안이 일치할 경우 점수 +1
            res = str(score*10) + "," + str(stName)                             # res = '점수*10,학생이름'

            if i == len(string_answer)-1:                                       # 반복문의 마지막에 resultList에 res값을 리스트로 저장
                resultList.append(res)

    resultList.sort(reverse=True)                                       # resultList의 값을 점수가 높은 순으로 정렬
    for index, value in enumerate(resultList):                          # 정렬된 resultList 값을 정제하여 출력하기 위한 반복문
        res = value.split(",")                                              # 정렬된 resultList의 항목을 ','로 나눔: res[0] = 점수 / res[1] = 학생이름
        print(f"학생이름 : {res[1]} | 점수: {res[0]} | 등수 : {index+1}등")       # 정제된 형식으로 값 출력


#함수 실행 코드
printScore(s,q)




"""
📌Q3. 숫자 맞추기 게임을 만들어 볼게요. 컴퓨터가 임의의 숫자를 3개 만들고 우리가 그것을 맞춰보겠습니다.
😲조건1 - 숫자는 0 ~ 100까지 숫자를 3개 만듭니다(중복 불가).
😲조건2 - 5회, 10회까지 정답을 못맞추면 최솟값, 최대값에 대한 힌트를 줍니다.
😲조건3 - 정답을 맞추면, 맞춘 정답이 최솟값인지, 중간값인지, 최댓값인지 알려줍니다.
import random
number = random.randint(0, 100)
✅출력 예시
guess_numbers()

1차 시도
숫자를 예측해보세요 : 39
숫자를 맞추셨습니다! 39는 최솟값입니다.
2차 시도
숫자를 예측해보세요 : 48
숫자를 맞추셨습니다! 48는 최댓값입니다.
3차 시도
숫자를 예측해보세요 : 100
숫자를 맞추셨습니다! 100는 최댓값입니다.
게임종료
3번 시도만에 예측 성공

...
5차 시도
숫자를 예측해보세요 : 9
9는 없습니다
최솟값은 9보다 작습니다
6차 시도
숫자를 예측해보세요 : 9
이미 예측에 사용한 숫자입니다
6차 시도 
"""

#########################################################
#                        Noas                           #
#########################################################



#########################################################
#                        chabbo                         #
#########################################################



#########################################################
#                          jm                           #
#########################################################

import random

GUESS_NUM_RULE = "* 0~100 사이의 숫자 하나를 입력해주세요."

roundCount = 0
score = 0
answerList = []

#컴퓨터의 랜덤숫자 생성함수
def createComNums():
    comNums = []
    for i in range(0, 3):
        randomNum = random.randint(0, 100)
        if not comNums.__contains__(randomNum):
            comNums.append(randomNum)
    return (comNums)

#힌트함수
def giveHint(min, max, user):
    closeMin = abs(user-min)
    closeMax = abs(user-max)
    if closeMin < closeMax:
        if min < user:
            print(f"최솟값은 {user}보다 작습니다.")
        elif min > user:
            print(f"최솟값은 {user}보다 큽니다.")
    else:
        if max < user:
            print(f"최댓값은 {user}보다 작습니다.")
        elif max > user:
            print(f"최댓값은 {user}보다 큽니다.")

#진행함수
def guessNumbers(comNums):
    global roundCount
    global score
    minNum = min(comNums)
    maxNum = max(comNums)

    roundCount += 1
    print(f"\n----- {roundCount}차 시도 -----\n")
    uInput = input("숫자를 예측해보세요 : ")
    userNum = 0

    try:
        if -1 < int(uInput) and int(uInput) <= 100:
            userNum = int(uInput)

            if answerList.__contains__(userNum):
                print("이미 예측에 사용한 문자입니다.")
                return guessNumbers(comNums)
        else:
            print(GUESS_NUM_RULE)
            return guessNumbers(comNums)

    except:
        print(GUESS_NUM_RULE)
        return guessNumbers(comNums)

    answerList.append(userNum)

    if roundCount > 4 and score < 2:
        giveHint(minNum, maxNum, userNum)

    if comNums.__contains__(userNum):
        if userNum == minNum : print(f"축하합니다!! 숫자를 맞추셨습니다! {userNum}은 최솟값입니다.")
        elif userNum == maxNum : print(f"축하합니다!! 숫자를 맞추셨습니다! {userNum}은 최댓값입니다.")
        else: print(f"축하합니다!! 숫자를 맞추셨습니다! {userNum}은 중간값입니다.")
        score += 1


#실행코드
print("\n----------------------------------------------")
print("       0~100 사이의 세개의 숫자를 맞추는 게임입니다.")
print("----------------------------------------------\n")
#print(GUESS_NUM_RULE)                      #답안코드
comNums = createComNums()
print(comNums)

while score < 3:
    guessNumbers(comNums)

print("\n------------------- 게임종료 ---------------------\n")
print(f"               {roundCount}번의 시도에 예측 성공!              ")


"""
📌Q4. 오늘 애인이 생겼다고 해봅시다. 100일을 기념하고 싶은데요.
날짜를 넣으면 100일 뒤가 몇월 며칠인지 계산해주는 함수를 만들어 보겠습니다.
😲조건1 - "오늘부터 1일"이기 때문에 날짜를 계산할 때 오늘을 포함합니다
😲조건2 - 몇년도인지 구분하지 않고 윤년도 고려하지 않고 2월은 무조건 28일로 합니다.
🧐hint
# 특정 원소의 위치를 찾는 방법
a = [1,2,3,4]
a.index(1)
0
✅출력 예시
after_100(6,21,"월")
6월 21일 월요일부터 100일 뒤는 9월 28일 화요일

"""

#########################################################
#                        Noas                           #
#########################################################



#########################################################
#                        chabbo                         #
#########################################################



#########################################################
#                          jm                           #
#########################################################
