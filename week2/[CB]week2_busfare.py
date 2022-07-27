"""
📌Q4. 나이와 현금 또는 카드를 입력하면 버스 요금이 출력되는 버스 요금 계산기를 만들어봅시다.
   📑아래의 요금표를 토대로 만들어주세요
8세 미만                :  무료
8세 이상  ~ 14세 미만   : 450원
14세 이상 ~ 20세 미만   : (카드)720원   / (현금) 1000원
20세 이상               : (카드)1200원 /  (현금) 1300원
75세 이상               : 무료

   🔽출력 예시
# 출력
나이: 30세
지불유형: 현금
버스요금: 1300원
"""

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