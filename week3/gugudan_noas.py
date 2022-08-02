number = input("몇 단? : ")
if number.isnumeric():
    print(number, '단')
    for i in range(1, 50):
        if i % 2 == 1 and int(number) * i < 50:
            print(number, "x", i, " = ", int(number) * i)

else:
    print("잘못된 값을 입력하셨습니다.")
    quit()





