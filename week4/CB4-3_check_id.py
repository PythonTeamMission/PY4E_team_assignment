'''
📌Q4.  주민등록번호의 앞 6자리는 생년월일이고 뒷자리의 시작번호는 성별을 나타냅니다. 
주민등록번호를 입력하면 몇년 몇월 생인지 그리고 남자인지 여자인지 출력하는 함수를 만들어 봅시다.

- 주민등록번호는 6자리 이후에 -로 구분되어야 하고 길이는 -포함 14임
- 뒷자리는 1,3 은 남자 2,4는 여자
- 00 ~ 21로 시작할 경우 2000년 이후 출생자인지 물어 볼 것 (맞으면 o 틀리면 x)
- 뒷자리 3, 4를 가질 수 있는 사람은 00년생 이후 출생자 밖에 없음

주민등록번호 조건을 만족하지 않는 수가 입력되면 "잘 못된 번호입니다"를 출력해주세요.
'''

def check_id(num):
    sep_num = num.split('-')
    if not(sep_num[0].isnumeric() or sep_num[1].isnumeric()):
        print('입력하신 주민등록번호가 형식에 맞지 않습니다. 숫자')
        return

    if not ((len(sep_num[0]) == 6) and (len(num) == 14)):
        print('입력하신 주민등록번호가 형식에 맞지 않습니다. 갯수')
        return

    else:
        year = int(sep_num[0][:2])
        month = int(sep_num[0][2:4])
        sex = int(sep_num[1][0])
        female = [2,4]
        male = [1,3]

        if (month == 0 or month > 12) or (sex not in female or sex not in male):
            print('입력하신 주민등록번호가 형식에 맞지 않습니다.')
            return
        

        if (00 <= year and year <= 21):
            choose = input('2000년 이후 출생자가 맞습니까? (맞으면 o 틀리면 x)').upper()
            if not (choose == 'O' or choose == 'X'):
                print('O 또는 X로 입력해주세요.')
                return 
            if not (choose =='O' and year in [female[1], male[1]]):
                print('입력하신 주민등록번호가 형식에 맞지 않습니다.')
                return
        elif (sex in [female[1], male[1]]):
            print('입력하신 주민등록번호가 형식에 맞지 않습니다.')
            return

        if (sex in male):
            return print(f'{year}년도 {month}월 남자')
        elif (sex in female):
            return print(f'{year}년도 {month}월 여자')
        else:
            print('입력하신 주민등록번호가 형식에 맞지 않습니다. ')


def main():
    while(1):
        num = input("주민등록번호를 입력해주세요('-' 포함) : ")
        check_id(num)


main()
    
