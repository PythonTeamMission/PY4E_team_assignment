"""
📌Q3. 요즘 식당에 들어가면 방명록을 적게 되어있습니다.
어느 식당의 사장님이 여러분에게 방명록을 주면서 전화번호를 제대로 적었는지 검사해달라는 부탁을 했습니다.
아래와 같은 방명록이 있을 때 방명록을 잘 못쓴 사람의 이름과 잘 못된 번호를 출력하는 함수를 만들어 봅시다.


김갑,123456789
이을,010-1234-5678
박병,010-5678-111
최정,111-1111-1111
정무,010-3333-3333
 

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


