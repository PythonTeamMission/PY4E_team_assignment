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


