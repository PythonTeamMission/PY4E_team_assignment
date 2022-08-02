n = input("첫 번째 수 입력 : ")
m = input("두 번째 수 입력 : ")
x = 0

if n.isdigit() and m.isdigit():
    for i in range(int(n), int(m) + 1):
        y = 0
        for z in range(1, i + 1):
            if i % z == 0:
                y += 1
        if y == 2:
            x += 1
else:
    print("잘못된 값을 입력하셨습니다.")
    quit()

print('소수는',x,'개 입니다.')