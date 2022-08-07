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

import sys
from os.path import abspath, dirname, join

ex = "  봄밤 / 이면우\n\n늦은 밤 아이가 현관 자물통을 거듭 확인한다\n가져갈 게 없으니 우리 집엔 도둑이 오지 않는다고 말해주자\n아이 눈 동그래지며, 엄마가 계시잖아요 한다\n그래 그렇구나, 하는 데까지 삼 초쯤 뒤 아이 엄마를 보니\n얼굴에 붉은 꽃, 소리없이 지나가는 중이다. "

root = dirname(abspath(__file__))

def printCountWord(text, word, name):
    name = name+".txt"
    cnt = text.count(word)

    print("\n입력된 글 : \n", text)
    print("검색 단어 : ", word)
    print("글자 수 : ", cnt)
    
    
    f = open(join(dirname(abspath(__file__)), name), 'w', encoding="utf-8")
    f.write("\n입력된 글 : \n"+ text)
    f.write("\n검색 단어 : "+ word)
    f.write("\n글자 수 : "+ str(cnt))
    f.close()


print("\n******************************************")
print("입력한 문장의 특정 글자 수를 세어 저장하는 프로그램입니다.\n 빈 칸 입력시 예시 문구가 입력됩니다.")
print("*********************************************")


a = input("저장할 글을 입력해주세요: ")
if a.strip(" ") == "":
    print("빈 값을 입력하셨습니다. 예시 문구가 출력됩니다.")
    a = ex

b = input("찾을 글자를 입력해주세요: ")
name = input("저장 파일 이름을 입력해주세요 : ")
if name.strip(" ") == "":
    name = "JM_countString_data"

printCountWord(a, b, name)
print("\n출력된 값이 저장되었습니다. 파일 이름 : ", name)
print("출력된 값은 다음 경로에 저장됩니다: ", root)
