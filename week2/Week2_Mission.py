# 모두를 위한 파이썬 PY4E 
# 2주차 팀 과제
# 팀: 턴태코치_2팀 / 작성자: jm / 기여자: chabbo, jm, Noas / 작성일: 220726
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

#########################################################
#                        Noas                           #
#########################################################


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


#########################################################
#                        chabbo                         #
#########################################################

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


#########################################################
#                          jm                           #
#########################################################


# 최대한 함수를 활용해서 코드를 만들어봤는데 더 복잡해진 것 같아요. 가위바위보를 더 가독성 좋게 만들려면 어떻게 해야할지 모르겠네요 ㅠㅠ..

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

#가위바위보 문자열 입력시 int로 변경하는 함수
def strRPS_to_intRPS(myStrRPS):
    if myStrRPS == "가위":
        return 0
    elif myStrRPS == "바위":
        return 1
    elif myStrRPS == "보":
         return 2
    else: return "fail"

#가위바위보 int 입력시 문자열로 변경하는 함수
def intRPS_to_strRPS(myIntRPS):
    if myIntRPS == 0:
        return "가위"
    elif myIntRPS == 1:
        return "바위"
    elif myIntRPS == 2: 
        return "보"
    else: return "fail"

#가위바위보 진행 함수
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

#가위바위보가 아닌 값을 확인하는 함수
def isFail(value):
    return value == "fail"


myRPC = input("\n'가위', '바위', '보' 혹은 0(가위),1(바위),2(보)를 입력해주세요: ")

try:
    #입력된 값이 int일때
    myIntRPS = int(myRPC)

    if isFail(intRPS_to_strRPS(myIntRPS)):
        print("잘못된 값을 입력하셨습니다.\n프로그램을 종료합니다.")
    else:   
        print("\n당신은 ", intRPS_to_strRPS(myIntRPS) ," 를 냈습니다!")
        print("컴퓨터는 ", intRPS_to_strRPS(computer) , " 를 냈습니다!")
        rockPaperScissors(myIntRPS)

except:
    #입력된 값이 str일때
    myStrRPS = myRPC

    if isFail(myStrRPS):
        print("잘못된 값을 입력하셨습니다.\n프로그램을 종료합니다.")
    else:
        print("\n당신은 ", myStrRPS , "를 냈습니다!")
        print("컴퓨터는 " + intRPS_to_strRPS(computer) + "를 냈습니다!")
        rockPaperScissors(strRPS_to_intRPS(myStrRPS))




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

#########################################################
#                        Noas                           #
#########################################################

monthly = input('월급을 입력해주세요 ')

if int(monthly) * 12 <= 12000000:
    print('세율은 6%입니다.')
    print('세전 연봉 :', float(monthly) * 12,'원')
    print('세전 연봉 :', int(monthly) * 12 * 0.94,'원')

elif int(monthly) * 12 > 12000000 and int(monthly) * 12 <= 46000000:
    print('세율은 15%입니다.')
    print('세전 연봉 :', float(monthly) * 12, '원')
    print('세전 연봉 :', int(monthly) * 12 * 0.85, '원')

elif int(monthly) * 12 > 46000000 and int(monthly) * 12 <= 88000000:
    print('세율은 24%입니다.')
    print('세전 연봉 :', float(monthly) * 12, '원')
    print('세전 연봉 :', int(monthly) * 12 * 0.76, '원')

elif int(monthly) * 12 > 88000000 and int(monthly) * 12 <= 150000000:
    print('세율은 35%입니다.')
    print('세전 연봉 :', float(monthly) * 12, '원')
    print('세전 연봉 :', int(monthly) * 12 * 0.65, '원')

elif int(monthly) * 12 > 150000000 and int(monthly) * 12 <= 300000000:
    print('세율은 38%입니다.')
    print('세전 연봉 :', float(monthly) * 12, '원')
    print('세전 연봉 :', int(monthly) * 12 * 0.62, '원')

elif int(monthly) * 12 > 300000000 and int(monthly) * 12 <= 500000000:
    print('세율은 40%입니다.')
    print('세전 연봉 :', float(monthly) * 12, '원')
    print('세전 연봉 :', int(monthly) * 12 * 0.60, '원')

else:
    print('세율은 42%입니다.')
    print('세전 연봉 :', float(monthly) * 12, '원')
    print('세전 연봉 :', int(monthly) * 12 * 0.58, '원')



#########################################################
#                        chabbo                         #
#########################################################


def tariff_cal(year_pay):
    if (year_pay >= 1200):
        tariff = 0.06
    elif (year_pay >= 4600):
        tariff = 0.15
    elif (year_pay >= 8800):
        tariff = 0.24
    elif (year_pay >= 15000):
        tariff = 0.15
    elif (year_pay >= 30000):
        tariff = 0.38
    elif (year_pay >= 50000):
        tariff = 0.40
    else:
        tariff = 0.42
    return tariff
    

def main_print():
    print('''
    ============== 세전/세후 연봉 계산기 =============
    월급을 입력해주시면 세전/세후 연봉을 계산해드립니다:)
    ''')


def main():
    main_print()
    while(1):
        try:
            month_pay = int(input('월급을 숫자로 입력해주세요(단위:만원) : '))
            if (month_pay == 0):
                print('월급이 만원 미만입니다. 다시 입력해주세요.\n')
                continue
        except:
            print('월급을 숫자로 입력해주세요 :)\n')
            continue
        year_pay = month_pay * 12
        tariff = tariff_cal(year_pay)
        real_year_pay = int(year_pay * (1 - tariff))
        print('='*40)
        print('계산 금액은 만원단위로 나타냅니다.')
        print(f'- 세전 연봉 : {year_pay}만원\n- 세후 연봉 : {real_year_pay}만원')
        print('='*40)

        print('계산을 계속하시겠습니까?')
        choice = input('계속 하시려면 enter를 눌러주세요. (다른 키를 입력하면 프로그램이 종료됩니다)')
        if (choice == ''):
            continue
        else:
            print('연봉계산기를 종료합니다:)')
            break

if __name__ == "__main__":
	main()


#########################################################
#                          jm                           #
#########################################################


#최대한 깔끔하게 적기 위해 노력했습니다. + 사용자가 반복해서 int가 아닌 타입으로 입력했을 경우를 방지하려면 for문 말고 다른 방법이 있는지 고민하고있습니다.

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
#########################################################
#                        Noas                           #
#########################################################

#학점계산기
def grader(name, score):
    if type(score) != type(3):
        print('점수를 제대로 입력해주세요 (정수형태)')
        #type(score) != type(int)

    elif int(score) < 60:
        print("학생 이름 :", name)
        print("점수 :", score)
        print("학점 : F")

    elif int(score) >= 60 and int(score) <= 64:
        print("학생 이름 :", name)
        print("점수 :", score)
        print("학점 : D")

    elif int(score) >= 65 and int(score) <= 69:
        print("학생 이름 :", name)
        print("점수 :", score)
        print("학점 : D+")

    elif int(score) >= 70 and int(score) <= 74:
        print("학생 이름 :", name)
        print("점수 :", score)
        print("학점 : C")

    elif int(score) >= 75 and int(score) <= 79:
        print("학생 이름 :", name)
        print("점수 :", score)
        print("학점 : C+")

    elif int(score) >= 80 and int(score) <= 84:
        print("학생 이름 :", name)
        print("점수 :", score)
        print("학점 : B")

    elif int(score) >= 85 and int(score) <= 89:
        print("학생 이름 :", name)
        print("점수 :", score)
        print("학점 : B+")

    elif int(score) >= 90 and int(score) <= 94:
        print("학생 이름 :", name)
        print("점수 :", score)
        print("학점 : A")

    elif int(score) >= 95 and int(score) <= 100:
        print("학생 이름 :", name)
        print("점수 :", score)
        print("학점 : A+")


grader(input("이름을 입력해주세요 "), int(input("점수를 입력해주세요 ")))

quit()


#########################################################
#                        chabbo                         #
#########################################################

#학점계산기
def grader(name, score):
    if type(score) != type(3):
        print('점수를 제대로 입력해주세요 (정수형태)')
        #type(score) != type(int)

    elif int(score) < 60:
        print("학생 이름 :", name)
        print("점수 :", score)
        print("학점 : F")

    elif int(score) >= 60 and int(score) <= 64:
        print("학생 이름 :", name)
        print("점수 :", score)
        print("학점 : D")

    elif int(score) >= 65 and int(score) <= 69:
        print("학생 이름 :", name)
        print("점수 :", score)
        print("학점 : D+")

    elif int(score) >= 70 and int(score) <= 74:
        print("학생 이름 :", name)
        print("점수 :", score)
        print("학점 : C")

    elif int(score) >= 75 and int(score) <= 79:
        print("학생 이름 :", name)
        print("점수 :", score)
        print("학점 : C+")

    elif int(score) >= 80 and int(score) <= 84:
        print("학생 이름 :", name)
        print("점수 :", score)
        print("학점 : B")

    elif int(score) >= 85 and int(score) <= 89:
        print("학생 이름 :", name)
        print("점수 :", score)
        print("학점 : B+")

    elif int(score) >= 90 and int(score) <= 94:
        print("학생 이름 :", name)
        print("점수 :", score)
        print("학점 : A")

    elif int(score) >= 95 and int(score) <= 100:
        print("학생 이름 :", name)
        print("점수 :", score)
        print("학점 : A+")


grader(input("이름을 입력해주세요 "), int(input("점수를 입력해주세요 ")))

quit()

#########################################################
#                          jm                           #
#########################################################

#동작되는 모든 기능을 함수로 작성해보았습니다. main함수 하나만 호출하면 프로그램이 작동되도록 도전했습니다.
#점수를 잘못 입력시 프로그램을 다시 시작합니다!

#학점 변환 함수
def getGrade(score):
    if score < 0 or 100 < score:
        return "fail"
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
    else :
        return "A+"

#학점 결과 함수
def printGradeResult(name, score):
    result = getGrade(score)
    if result == "fail":
        print("\n점수를 0~100점 사이값으로 입력해주세요.")
        print("프로그램을 다시 시작합니다.")
        main()
    else:
        print(f"\n학생이름 : {name}")
        print(f"점수 : {score}")
        print(f"학점 : {result}\n")
        

#학점 변환 입력 함수
def main():
    print("\n ********************************** \n")
    print("이름과 점수를 입력하면 학점을 출력하는 학점 변환기 입니다.")
    print("\n **********************************")

    name = input("\n이름을 입력해주세요 : ")
    score = input("점수를 입력해주세요 : ")

    try:
        score = int(score)
    except:
        int(input("점수를 정수로 입력해주세요 : "))

    printGradeResult(name, score)


#함수 호출
main()


"""
📌Q4. 나이와 현금 또는 카드를 입력하면 버스 요금이 출력되는 버스 요금 계산기를 만들어봅시다.

   📑아래의 요금표를 토대로 만들어주세요

8세 미만                :  무료
8세 이상  ~ 14세 미만   : 450원
14세 이상 ~ 20세 미만   : (카드)720원   / (현금) 1000원
20세 이상               : (카드)1200원 /  (현금) 1300원
75세 이상               : 무료

   🔽출력 예시

# 버스 요금 입력
bus_fare(30, "현금")

# 출력
나이: 30세
지불유형: 현금
버스요금: 1300원
"""

#########################################################
#                        Noas                           #
#########################################################


payment = ['카드', '현금']

def bus_fare(age, pmtype):
    if type(age) != type(3) or pmtype not in payment:
        print('나이나 지불유형을 제대로 입력해주세요. 나이는 정수 입력, 지불유형은 카드 또는 현금을 입력해주세요.')

    else:
        if int(age) < 4:
            print('나이 :', age)
            print('지불유형 :', pmtype)
            print('버스요금 : 무료')

        elif int(age) >= 4 and int(age) < 14:
            print('나이 :', age)
            print('지불유형 :', pmtype)
            print('버스요금 : 450원')

        elif int(age) >= 14 and int(age) < 20:
            if pmtype == '카드':
                print('나이 :', age)
                print('지불유형 :', pmtype)
                print('버스요금 : 720원')
            else:
                print('나이 :', age)
                print('지불유형 :', pmtype)
                print('버스요금 : 1000원')

        elif int(age) >= 20 and int(age) < 75:
            if pmtype == '카드':
                print('나이 :', age)
                print('지불유형 :', pmtype)
                print('버스요금 : 1200원')
            else:
                print('나이 :', age)
                print('지불유형 :', pmtype)
                print('버스요금 : 1300원')
        else:
            print('나이 :', age)
            print('지불유형 :', pmtype)
            print('버스요금 : 무료')



bus_fare(int(input("나이를 입력해주세요 ")), input("지불유형을 입력해주세요. '카드'/'현금' "))


#########################################################
#                        chabbo                         #
#########################################################


def bus_fare(age, cash_type):
    if (age < 8 or age >= 75):
        payment = 0
    elif (age < 14):
        payment = 450
    elif (age < 20):
        if (cash_type == 0):
            payment = 720
        else :
            payment = 1000
    elif (age >= 20):
        if (cash_type == 0):
            payment = 1200
        else :
            payment = 1300
    return payment


def continue_choice():
    print('\n요금확인을 계속하시겠습니까?')
    choice = input('계속 하시려면 enter를 눌러주세요. (다른 키를 입력하면 프로그램이 종료됩니다)')
    if (choice == ''):
        return main()
    else:
        print('버스요금 계산을 종료합니다:)')
        exit()



def main_print():
    print('''
    ================== 대전광역시 버스요금 =================
    8세 미만                : 무료
    8세 이상  ~ 14세 미만   : 450원
    14세 이상 ~ 20세 미만   : (카드)720원   / (현금) 1000원
    20세 이상               : (카드)1200원 /  (현금) 1300원
    75세 이상               : 무료
    고객님의 나이와 지불 유형을 선택해주시면 요금을 알려드립니다:) ''')

def main():
    main_print()
    while(1):
        try: 
            age = int(input('\n나이를 숫자로 입력해주세요 : '))
        except:
            print('나이를 숫자 형태로 입력해주세요\n')
            continue
        if (age < 8):
            print('나이가 어려 버스요금은 무료입니다:)')
            continue_choice()
            
        elif (age >= 75):
            print('나이가 많으셔서 버스요금은 무료입니다:)')
            continue_choice()
        
        print('지불 유형을 선택합니다.')
        try:
            cash_type = int(input('카드면 0, 현금이면 1을 입력해주세요 : '))
            if not (cash_type == (0 or 1)):
                print('지불 방식(카드/현금)에 따라 0 또는 1을 입력해주세요.')
                continue
        except:
            print('숫자로 입력해주세요!')
            continue
        
        payment = bus_fare(age, cash_type)
        cash_type_list = ['카드', '현금']

        print('=' * 40)
        print('- 나이 : ', age)
        print('- 지불 유형 : ', cash_type_list[cash_type])
        if (payment != 0):
            print(f'- 버스요금 : {payment}원')
        else:
            print('- 버스요금 : 무료입니다.')
        print('=' * 40)
        continue_choice()

if __name__ == "__main__":
	main()


#########################################################
#                          jm                           #
#########################################################

print("\n ********************************** \n")
print(" 버스 요금 계산기 입니다.")
print("\n **********************************")

#입력 코드
age = input("나이를 정수로 입력해주세요 : ")
payType = input("지불 유형을 '현금' 또는 '카드'로 입력해주세요: ")

#예외처리 코드
try:
    age = int(age)
except:
    age = input("나이를 숫자 정수로 입력해주세요 : ")
    age = int(age)


#출력 함수
def busFarePrint(age, payType, busFare):
    print("나이: ", age, " 세")
    print("지불유형: ", payType)
    print("버스요금: ", busFare)

#버스 요금 계산 함수
def getBusFare(age, payType):
    if -1 < age & age <8:
        busFarePrint(age, payType, "무료")
    elif age < 14:
        busFarePrint(age, payType, "450원")
    elif age < 20:
        if payType == "카드":
            busFarePrint(age, payType, "720원")
        elif payType == "현금":
            busFarePrint(age, payType, "1000원")
    elif age < 75:
        if payType == "카드":
            busFarePrint(age, payType, "1200원")
        elif payType == "현금":
            busFarePrint(age, payType, "1300원")
    elif age >= 75:
        busFarePrint(age, payType, "무료")
    else:
        busFarePrint(age, payType, "입력 오류입니다. 다시 시도해주세요.")


#함수 호출
if not ((payType == "현금") or (payType == "카드")):
    print("지불 유형을 잘못 작성하셨습니다.\n프로그램을 종료합니다.")
else: 
    getBusFare(age, payType)



