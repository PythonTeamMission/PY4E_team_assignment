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
