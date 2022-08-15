"""
📌Q2. 다음과 같이 학생들의 시험 답지가 있습니다. 그리고 답안지도 있습니다.
함수를 하나 만들어 채점을 하고 학생들의 점수를 출력하고 등수도 함께 출력해주세요.

# 학생 답
s = ["김갑,3242524215",
"이을,3242524223",
"박병,2242554131",
"최정,4245242315",
"정무,3242524315"]

# 정답지
a = [3,2,4,2,5,2,4,3,1,2]

🧐hint
# 문자열도 숫자 정렬 가능
a = ["5","2","3"]
a.sort()
["2", "3", "5"]
# 내림차순 정렬 가능
a.sort(reverse=True)
["5", "3", "2"]
✅출력 예시
grader(s, a)
학생: 정무 점수: 90점 1등
학생: 김갑 점수: 80점 2등
학생: 이을 점수: 70점 3등
학생: 박병 점수: 50점 4등
학생: 최정 점수: 40점 5등
"""

#함수 하나로 만들어 보기 위해 노력해봤습니다.. 그런데 반복문을 세번이나 쓰는 게 맘이 안 드네요 ㅠㅠ

s = [                                                                  #예시 학생 답 리스트
    "김갑,3242524215",
    "이을,3242524223",
    "박병,2242554131",
    "최정,4245242315",
    "정무,3242524315"
]

q = [3,2,4,2,5,2,4,3,1,2]                                               #예시 답안
resultList = []                                                         #결과리스트 전역변수

#파라미터 : 학생답안 리스트, 정답 리스트
#두 리스트를 받아 학생 이름과 점수 결과를 출력하는 함수
def printScore(list, answer):
    global resultList                                                   # 결과리스트 전역변수를 사용하겠다고 명시
    list_answer = [str(int) for int in answer]                          # int타입을 string타입으로 수정. list_answer: answer값을 문자열로 갖고있는 리스트
    string_answer = "".join(list_answer)                                # string_answer : answer를 하나의 문자열로 생성

    for val in list:                                                    # 학생답안 리스트에서 각 항목의 데이터 추출 반복문
        student = val.split(",")                                            # 항목을 ','를 기준으로 split / student: 학생 이름, 학생답안을 갖고있는 리스트
        stName = student[0]                                                 # stName = 학생의 이름
        stAnswer = student[1]                                               # stAnswer = 학생의 답변
        score = 0                                                           # 학생의 점수를 확인하기 위한 변수 생성 및 초기화
        for i, v in enumerate(string_answer):                               # enumerate()함수 : 인덱스, 값 확인가능 / string_answer: 정답문자열의 길이만큼 반복, 인덱스를 통해 학생의 답안과 정답을 비교
            if stAnswer[i] == v:                                                # stAnswer[i]: 학생의 답 중 i인덱스의 값 == 정답의 i인덱스의 값 비교
                score += 1                                                          # 정답과 학생답안이 일치할 경우 점수 +1
            res = str(score*10) + "," + str(stName)                             # res = '점수*10,학생이름'

            if i == len(string_answer)-1:                                       # 반복문의 마지막에 resultList에 res값을 리스트로 저장
                resultList.append(res)

    resultList.sort(reverse=True)                                       # resultList의 값을 점수가 높은 순으로 정렬
    for index, value in enumerate(resultList):                          # 정렬된 resultList 값을 정제하여 출력하기 위한 반복문
        res = value.split(",")                                              # 정렬된 resultList의 항목을 ','로 나눔: res[0] = 점수 / res[1] = 학생이름
        print(f"학생이름 : {res[1]} | 점수: {res[0]} | 등수 : {index+1}등")       # 정제된 형식으로 값 출력


#함수 실행 코드
printScore(s,q)


