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

