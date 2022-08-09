"""
📌Q4.  주민등록번호의 앞 6자리는 생년월일이고 뒷자리의 시작번호는 성별을 나타냅니다. 주민등록번호를 입력하면 몇년 몇월 생인지 그리고 남자인지 여자인지 출력하는 함수를 만들어 봅시다.


주민등록번호는 6자리 이후에 -로 구분되어야 하고 길이는 -포함 14임
뒷자리는 1,3 은 남자 2,4는 여자
00 ~ 21로 시작할 경우 2000년 이후 출생자인지 물어 볼 것 (맞으면 o 틀리면 x)
뒷자리 3, 4를 가질 수 있는 사람은 00년생 이후 출생자 밖에 없음

주민등록번호 조건을 만족하지 않는 수가 입력되면 "잘 못된 번호입니다"를 출력해주세요.


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



def checkGender(gen):
    if gen == 1 or gen == 3:
        return "남성"
    elif gen == 2 or gen == 4:
        return "여성"
    else:
        return "잘못된 값을 입력하셨습니다."


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

    

def parseIdNum(idNum):
    
    ids = idNum.split("-")
    year = idNum[0:2]
    month = idNum[2:4]
    day = idNum[4:6]

    sec = ids[1]
    gender = checkId(int(year), int(sec[0]))
    
    if gender != None:
        print(f"{year}년 {month}월 {gender}")


parseIdNum(getIdNum())