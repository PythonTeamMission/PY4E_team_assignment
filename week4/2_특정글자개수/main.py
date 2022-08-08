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
