# 소수일경우 32135.13 어떻게 해야할지
def make_comma(number):
    try:
        type(int(number)) == type(3)
        number = str(number)
        length = len(number)
        # 자릿수 3자리 이하면 그대로 출력
        if length <= 3:
            print(number)
        num_comma = length // 3
        if length % 3 ==0:
            num_comma = num_comma -1

        new_number = ""
        n = -1
        while num_comma != 0:
            new_number = number[n] + new_number
            if  n % 3 == 0:
                new_number = "," + new_number
                num_comma = num_comma - 1
            n = n - 1
        print(number[:n+1]+new_number)
    except:
        print('정수를 입력해주세요. 처음부터 다시 실행해주세요')


make_comma(input('숫자를 입력해주세요: '))




#포맷함수사용
try:
    number = int(input('숫자를 입력해주세요 '))
    number = format(number,',')
    print(number)
except:
    print('정수를 입력해주세요. 처음부터 다시 실행해주세요')
