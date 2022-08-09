# 모두를 위한 파이썬 PY4E 
# 4주차 팀 과제
# 팀: 턴태코치_2팀 / 작성자: jm / 기여자: chabbo, jm, Noas / 작성일: 220726
# 👍👍4주차 미션 목적 - 문자열의 다양한 활용법 익히기

"""
📌Q1. 우리는 큰 수를 나타낼 때 3자리마다 , 를 찍어서 구분해 줍니다. 파이썬에서는 아래와 같이 쉽게 나타낼 수 있습니다.

# f"{숫자:,}"
print(f"{1000:,}")

하지만 이번 미션에서는 숫자를 입력 받고 3자리마다 ,를 찍어주는 함수를 만들어 봅시다.

🔽출력 예시

make_comma(1000000)
1,000,000
"""

#########################################################
#                        Noas                           #
#########################################################

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


"""
 - 코멘트 -

JM :
- isnumeric() 함수를 if절에 넣어 사용해보세요! 저는 그렇게 하면 try-exept문을 안 쓸 수 있어 편리했습니다.
- 저도 소숫점을 입력받았을땐 정수로 입력받도록 넘겼어요ㅠㅠ.. 
chabo : 저도 처음에 int로 가능한지 물어보고 걍 넘겨서 조건잡기가 어렵네요ㅜㅜ 궁금합니당!!!
"""

#########################################################
#                        chabbo                         #
#########################################################

def print_comma(number):
    zero = 0
    num = ''
    for i in reversed(number):
        num = i + num
        zero += 1
        if (zero == 3):
            num = ',' + num
            zero = 0
    print(num)
        

number = input('숫자를 입력해주세요 : ')
    
if (number.isnumeric()):
    print_comma(number)
else:
    print('숫자를 입력해주세요!')
    
    
"""
 - 코멘트 -
JM: 와 가장 수업내용을 활용해서 작성해주셨어요!! 멋진 코드 ㅠㅠ ~! reversed라는 걸 새로 배웠네요!
"""
#########################################################
#                          jm                           #
#########################################################

#최대한 깔끔하게 만들기위해 노력했습니다

def getNumber():
    num = input("숫자를 입력해주세요: ")
    if num.isnumeric():
        return num
    else:
        print("잘못된 값을 입력하셨습니다.")
        return getNumber()


print("\n******************************************")
print("입력한 숫자에 ','를 삽입하는 프로그램입니다.")
print("*********************************************")

num = int(getNumber())

print(f"make_comma({num})")
print(format(num, ","))

"""
📌Q2. 어느날 여러분이 어떤 글을 읽고 있는데, 갑자기 특정 글자가 전체 글에서 몇개 들어있는지 궁금해졌습니다. 그럼 한 번 파이썬 함수로 만들어 봅시다.
글은 어떤 글이 좋습니다. 인터넷에서 검색해서 복사 붙여넣기로 변수에 넣어 줍니다.
변수에 담긴 글을 함수에 넣어주면 txt 파일로 저장도 함께 되도록 해줍니다.


🔽출력 예시

a =\"""안녕하세요. 
반갑습니다. 파이썬 공부는 정말 재밌습니다.
\"""

count_word(a, "습니다")
2
"""


"""종목명	현재가	등락률	시가총액(억)	거래량 """

stock_top10 = '''삼성전자
005930
60,000
800800
-1.32%
3,581,870	15,732,380
LG에너지솔루션
373220
457,500
10,50010,500
+2.35%
1,070,550	583,882
SK하이닉스
000660
95,100
1,2001,200
-1.25%
692,330	3,024,190
삼성바이오로직스
207940
900,000
0
0.00%
640,566	36,195
LG화학
051910
671,000
19,00019,000
+2.91%
473,675	326,789
삼성전자우
005935
55,100
400400
-0.72%
453,411	737,066
NAVER
035420
265,500
7,0007,000
+2.71%
435,550	491,422
삼성SDI
006400
615,000
18,00018,000
+3.02%
422,902	314,942
현대차
005380
193,500
2,5002,500
-1.28%
413,448	930,935
카카오
035720
83,300
1,3001,300
+1.59%
370,642	1,501,390'''


#########################################################
#                        Noas                           #
#########################################################


a = input('글을 입력해주세요 ')
b = a.count(input('찾을 단어를 입력해주세요 '))

def text_counter(a,b):
    if b == 0:
        print('해당 단어가 존재하지 않습니다')
    else:
        print('해당 단어가', b, '개 존재합니다.')
    file = open("test.txt", "w")
    file.write(a)
    file.close()

text_counter(a,b)


"""
JM 코멘트:
- 최고의 코드!!! 깔끔함 그 자체네요 최고에요! 크으
"""

#########################################################
#                        chabbo                         #
#########################################################

''' 크롤링해온다는 가정하에 제가 지정한 문자 찾는 걸로 생각했네요ㅜㅜ..흑'''

def count_word(word):
    lines = stock_top10.split('\n')
    f = open("new_text.txt", 'w')
    for i in lines:
        f.write(i)

    plus = 0
    minus = 0
    plus_company = []
    minus_company = []

    for idx, line in enumerate(lines) :
        if '+' in line:
            plus += 1 
            plus_company.append(lines[idx-4])
        elif '-' in line:
            minus += 1
            minus_company.append(lines[idx-4])
    print(f'금일 코스피 10기업중 \n상승한 기업은 {plus}개, \n기업명 : {plus_company}')
    print(f'하락한 기업은 {minus}개, \n기업명 : {minus_company}')

count_word(stock_top10)

"""
- 코멘트 -
JM: 와 크롤링! 저는 받아올 생각은 못했네요!
"""

#########################################################
#                          jm                           #
#########################################################

#파일 위치를 지정해서 저장하도록 구현했습니다.
#그리고 스페이스바, 엔터 등을 누르면 예시문구를 출력하게 만들었습니다.
import sys
from os.path import abspath, dirname, join

ex = "  봄밤 / 이면우\n\n늦은 밤 아이가 현관 자물통을 거듭 확인한다\n가져갈 게 없으니 우리 집엔 도둑이 오지 않는다고 말해주자\n아이 눈 동그래지며, 엄마가 계시잖아요 한다\n그래 그렇구나, 하는 데까지 삼 초쯤 뒤 아이 엄마를 보니\n얼굴에 붉은 꽃, 소리없이 지나가는 중이다. "

root = dirname(abspath(__file__))

def printCountWord(text, word, name):
    name = name+".txt"
    cnt = text.count(word)

    #JM: 프린트와 write를 동시에 구현하고 싶었는데 방법을 찾지 못했네요..ㅠ
    print("\n입력된 글 : \n", text)
    print("검색 단어 : ", word)
    print("글자 수 : ", cnt)
    
    f = open(join(dirname(abspath(__file__)), name), 'w', encoding="utf-8")
    f.write("\n입력된 글 : \n"+ text)
    f.write("\n검색 단어 : "+ word)
    f.write("\n글자 수 : "+ str(cnt))
    f.close()


print("\n******************************************")
print("입력한 문장의 특정 글자 수를 세어 저장하는 프로그램입니다. 빈 칸 입력시 예시 문구가 입력됩니다.")
print("*********************************************")


a = input("저장할 글을 입력해주세요: ")
if a.strip(" ") == "":
    print("빈 값을 입력하셨습니다. 예시 문구가 출력됩니다.")
    a = ex

b = input("찾을 글자를 입력해주세요: ")
name = input("저장 파일 이름을 입력해주세요 : ")
if name.strip(" ") == "":
    name = "JM_CountString_data"

printCountWord(a, b, name)
print("\n출력된 값이 저장되었습니다. 파일 이름 : ", name)
print("출력된 값은 다음 경로에 저장됩니다: ", root)


"""
📌Q3. 요즘 식당에 들어가면 방명록을 적게 되어있습니다.
어느 식당의 사장님이 여러분에게 방명록을 주면서 전화번호를 제대로 적었는지 검사해달라는 부탁을 했습니다.
아래와 같은 방명록이 있을 때 방명록을 잘 못쓴 사람의 이름과 잘 못된 번호를 출력하는 함수를 만들어 봅시다.
 
함수에 방명록을 넣으면 txt 파일로 저장되게 해줍니다.
제대로 적은 방명록의 조건은 다음과 같습니다
010 으로 시작함
번호가 - 로 구분이 되어 있음
-를 포함하여 길이가 13임

🔽출력 예시

guest_book = \"""김갑,123456789
이을,010-1234-5678
박병,010-5678-111
최정,111-1111-1111
정무,010-3333-3333\"""
wrong_guest_book(guest_book)

잘못 쓴 사람: 김갑
잘못 쓴 번호: 123456789

잘못 쓴 사람: 박병
잘못 쓴 번호: 010-5678-111

잘못 쓴 사람: 최정
잘못 쓴 번호: 111-1111-1111
"""

#########################################################
#                        Noas                           #
#########################################################

a = """김갑,123456789
이을,010-1234-5678
박병,010-5678-111
최정,111-1111-1111
정무,010-3333-3333"""

def wrong_guest_book(a):
    a.split('\n')


#########################################################
#                        chabbo                         #
#########################################################

'''저는 split으로 나눠서 진행해봤습니당~:) '''

def wrong_guest_book(guest_book):
    lines = guest_book.split('\n')
    f = open("guest_book.txt", 'w')
    for line in lines:
        f.write(line)
        sep_line = line.split(',')
        num = sep_line[1].split('-')
        if not (sep_line[1].startswith('010') or len(sep_line[1]) == 13):
            print(f'\n잘못 쓴 사람 : {sep_line[0]}\n잘못 쓴 번호 : {sep_line[1]}')

        elif not (len(num[0]) == 3 and len(num[1]) == 4 and len(num[2]) == 4):
            print(f'\n잘못 쓴 사람 : {sep_line[0]}\n잘못 쓴 번호 : {sep_line[1]}')

wrong_guest_book(guest_book)

"""
- 코멘트 -
JM: chabbo님 for문 활용을 항상 멋지게 하세요!!
전 매번 range만 쓰는데 딱 제때 맞는 반복문을 사용하셔서 많이 배워요 +_+
그리고 if, elif가 한번씩만 쓰이다니.. 이 문제가 이렇게 간결하게 해결될 수 있는게 놀라워요!!
"""

#########################################################
#                          jm                           #
#########################################################

#딕셔너리를 활용해서 풀어보았는데 새로운 코드를 알게되어 재밌게 풀었습니다.
#collections.OrderedDict(sorted(wrongGB.items(), key=lambda v: v, reverse=True)) < 딕셔너리를 내림차순으로 정렬해서 다시 딕셔너리로 리턴하는 함수를 알게되었어요.

import collections
import sys
from os.path import abspath, dirname, join

ex = "김갑,123456789\n이을,010-1234-5678\n박병,010-5678-111\n최정,111-1111-1111\n정무,010-3333-3333"
fnameEx = "JM_GuestBook_data"
root = dirname(abspath(__file__))


#프린트
def printWrongData(person, number):
    print("잘못 쓴 사람: ", person)
    print("잘못 쓴 번호: ", number, "\n")


#파일 저장
def saveGuestBook(guestBook, fname, wrongGB):
    fname = fname + ".txt"
    f = open(join(dirname(abspath(__file__)), fname), 'w', encoding="utf-8")

    f.write(f"guest_book : {guestBook}\n\n")
    f.write("wrong_guest_book(guest_book)\n\n")
    for _ in range(0, len(wrongGB)):
        item = wrongGB.popitem()

        f.write(f"잘못 쓴 사람: {item[0]}\n")
        f.write(f"잘못 쓴 번호: {item[1]}\n\n")

    f.close()

    print("\n출력된 값이 저장되었습니다. 파일 이름 : ", fname)
    print("출력된 값은 다음 경로에 저장됩니다: ", root)

#잘못된 방명록 작성자, 번호 추출
def getWrongGuests(guestBook, fname):
    ss = guestBook.split("\n")
    res = dict()
    wrongGB = dict()

    for i, el in enumerate(ss):
        line = el.split(",")
        res[line[0]] = line[1]
        number = line[1]

        lineModi = number.replace('-', '')
        #길이가 다른 번호
        if len(lineModi) != 11:
            wrongGB[line[0]] = line[1]

        #앞자리가 010이 아닌 번호
        elif number[0:3] != '010':
            wrongGB[line[0]] = line[1]


        if i == len(ss)-1:
            #딕셔너리를 내림차순으로 변경 후 딕셔너리로 반환
            wrongGB = collections.OrderedDict(sorted(wrongGB.items(), key=lambda v: v, reverse=True))
            wrongGB2 = dict()
            wrongGB2 = wrongGB.copy()
            
            for _ in range(0, len(wrongGB)):
                item =  wrongGB.popitem()
                printWrongData(item[0], item[1])

            saveGuestBook(guestBook, fname, wrongGB2)

        
#시작 코드
print("\n******************************************")
print("방명록을 잘못적은 사람과 번호를 찾아 파일로 저장하는 프로그램입니다.\n방명록에 빈 칸을 입력하면 예시 방명록이 사용됩니다.")
print("*********************************************")

#파일명 입력
fname = input("저장될 파일 이름을 적어주세요 : ")
if fname.strip(" ") == "":
    fname = fnameEx

#방명록 입력
guestBook = input("방명록을 적어주세요 : ")
if guestBook.strip(" ") == "":
    print("빈 값을 입력하셨습니다. 예시 문구를 사용합니다.")
    print("예시 문구 : \n", ex )
    guestBook = ex


getWrongGuests(guestBook, fname)

"""
📌Q4.  주민등록번호의 앞 6자리는 생년월일이고 뒷자리의 시작번호는 성별을 나타냅니다. 주민등록번호를 입력하면 몇년 몇월 생인지 그리고 남자인지 여자인지 출력하는 함수를 만들어 봅시다.

주민등록번호는 6자리 이후에 -로 구분되어야 하고 길이는 -포함 14임. 뒷자리는 1,3 은 남자 2,4는 여자
00 ~ 21로 시작할 경우 2000년 이후 출생자인지 물어 볼 것 (맞으면 o 틀리면 x)
뒷자리 3, 4를 가질 수 있는 사람은 00년생 이후 출생자 밖에 없음

주민등록번호 조건을 만족하지 않는 수가 입력되면 "잘못된 번호입니다"를 출력해주세요.


🔽출력 예시

a = "500629-2222222"
check_id(a)
50년06월 여자

a = "000629-2222222"
check_id(a)
2000년 이후 출생자 입니까? 맞으면 o 아니면 x : o
잘못된 번호입니다.
올바른 번호를 넣어주세요

a = "000629-2222222"
check_id(a)
2000년 이후 출생자 입니까? 맞으면 o 아니면 x : x
00년06월 여자

"""

#########################################################
#                        Noas                           #
#########################################################

a = input('주민번호를 입력해주세요 (-)포함 ')
m = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
om = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21']
d = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
by = a[0:2]
bm = a[2:4]
bd = a[4:6]


def resi_number(a):
    if a[6] == '-' and len(a) == 14 and type(int(a[0:6])) == type(3) and type(int(a[8:14])) == type(3) and bm in m and bd in d:
        if a[7] == '1' or a[7] == '3':
            gender = '남자'
        elif a[7] == '2' or a[7] == '4':
            gender = '여자'
        else:
            print('잘못된 번호를 입력하셨습니다. 처음부터 다시 실행해주세요.')
        if by in om:
            ox = input ('2000년 이후 출생자 입니까? 맞으면 o 아니면 x (소문자 영문)을 입력해주세요 ')

            if ox == 'o':
                if a[7] == '3' or a[7] == '4':
                    print("생년월일 : 20{0}년 {1}월 {2}일".format(by, bm, bd))
                    print("성별 : {0}".format(gender))
                else:
                    print('잘못된 번호를 입력하셨습니다. 처음부터 다시 실행해주세요.')

            elif ox == 'x':
                if a[7] == '3' or a[7] == '4':
                    print('잘못된 번호를 입력하셨습니다. 처음부터 다시 실행해주세요.')
                else:
                    print("생년월일 : 19{0}년 {1}월 {2}일".format(by, bm, bd))
                    print("성별 : {0}".format(gender))

            else:
                print("소문자 영문 'o'나 'x'를 입력해주세요. 처음부터 다시 실행해주세요")
        else:
            if a[7] == '3' or a[7] == '4':
                print('잘못된 번호를 입력하셨습니다. 처음부터 다시 실행해주세요.')

            else:
                print("생년월일 : 19{0}년 {1}월 {2}일".format(by, bm, bd))
                print("성별 : {0}".format(gender))
    else:
        print('잘못된 번호를 입력하셨습니다. 처음부터 다시 실행해주세요.')

resi_number(a)


"""
- 코멘트 -
JM:
- 이슈 함께수정
- 클린코드작성 팁: 하나의 함수는 하나의 기능만 수행하도록 코드를 짜보세요! 저도.. 그렇게 하려고 노력중입니다 ㅜㅎㅎ
"""

#########################################################
#                        chabbo                         #
#########################################################

'''이번에 조건문으로 if문남발해서 좀 줄이고 싶은데 어떻게하면 좋을까요?'''

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

            
num = input("주민등록번호를 입력해주세요('-' 포함) : ")
check_id(num)


"""
- 코멘트 -
JM: ㅠㅠ 저도 if문을 주렁주렁 달아서 해결했어요.
input().upper() < 인풋에 이렇게 해결하셔서 새롭게 배웠어요!
그리고 연도랑 월까지 확실하게 체크해주신 점이.. 역시 chabbo님!!
"""

#########################################################
#                          jm                           #
#########################################################

# 함수 순서 
# 1. getIdNum() : 입력된 값의 자릿수, '-'문자 포함, int타입인지 확인 후 옳은 값(idNum) 리턴
# 2. parseIdNum(idNum) : 주민등록번호 앞자리의 연,월,일 변수화 + 뒷자리의 시작숫자 split, 변수화 (gen)
# 3. checkId(year, gen) : 연도와 gen 변수를 받아와서 2000년대 이후/이전인지 확인 + 잘못된 값을 입력했음을 프린트
# 4. checkGender(gen) : 유저가 옳은 값을 입력했다면 성별 리턴, 아닐경우 None

# 5. parseIdNum(idNum)에서 결과 출력 print(f"{year}년 {month}월 {gender}")


#잘못된 값 입력시 함수를 다시 실행
def getIdNum():
    idNum = input("주민등록번호를 입력해주세요 ex)500629-2222222 | 입력 : ")

    if not idNum.__contains__("-"):
        print("잘못된 값을 입력하셨습니다. 예시와 같이 입력해주세요.\nex)500629-2222222")
        return getIdNum()
    elif len(idNum) != 14:
        print("잘못된 값을 입력하셨습니다. 예시와 같이 입력해주세요.\nex)500629-2222222")
        return getIdNum()
    else:
        ids = idNum.split("-")
        if ids[0].isnumeric() and ids[1].isnumeric():
            print("입력한 주민등록번호 : ", idNum)
            return idNum
        else:
            print("잘못된 값을 입력하셨습니다. 예시와 같이 입력해주세요.\nex)500629-2222222")
            return getIdNum()


#성별 판별 함수
def checkGender(gen):
    if gen == 1 or gen == 3:
        return "남성"
    elif gen == 2 or gen == 4:
        return "여성"
    else:
        return "잘못된 값을 입력하셨습니다."

#2000년 이후 출생자 and 주민등록뒷번호 첫숫자가 3,4 -> o : 성별판별 
#2000년 이전 출생자 and 주민등록뒷번호 첫숫자가 1,2 -> x : 성별판별 (1900년 출생인 사람일 수 있으므로)
def checkId(year, gen):
    if 00<= int(year) <= 21:
        birth = input("2000년 이후 출생자 입니까? (o/x)")
        if gen == 3 or gen ==4:
            if birth.lower() == "o":
                return(checkGender(gen))
            else:
                print("잘못된 값을 입력하셨습니다.")
        else:
            if birth.lower() == "x":
                return(checkGender(gen))
            else :
                print("잘못된 값을 입력하셨습니다.")
            
    else:
        return(checkGender(gen))

    
#주민등록번호 해석 함수
def parseIdNum(idNum):
    
    ids = idNum.split("-")
    year = idNum[0:2]
    month = idNum[2:4]
    day = idNum[4:6]

    sec = ids[1]
    gender = checkId(int(year), int(sec[0]))
    
    if gender != None:
        print(f"{year}년 {month}월 {gender}")


#시작 코드
parseIdNum(getIdNum())

'''chabbo : 오 함수 나누니까 굉장히 깔끔해지네요!'''
