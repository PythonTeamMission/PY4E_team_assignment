"""
📌Q4. 오늘 애인이 생겼다고 해봅시다. 100일을 기념하고 싶은데요.
날짜를 넣으면 100일 뒤가 몇월 며칠인지 계산해주는 함수를 만들어 보겠습니다.
😲조건1 - "오늘부터 1일"이기 때문에 날짜를 계산할 때 오늘을 포함합니다
😲조건2 - 몇년도인지 구분하지 않고 윤년도 고려하지 않고 2월은 무조건 28일로 합니다.
🧐hint
# 특정 원소의 위치를 찾는 방법
a = [1,2,3,4]
a.index(1)
0
✅출력 예시
after_100(6,21,"월")
6월 21일 월요일부터 100일 뒤는 9월 28일 화요일
"""

import datetime
from datetime import date, timedelta

days = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']

today = date.today()
Ddate = timedelta(days=100, hours=0, minutes=0)

tdayMonth = today.month
tdayDate = today.day
td = datetime.datetime.today().weekday()
tdayDay = days[td]

dDay = today+Ddate
dDayYear = dDay.year
dDayMonth = dDay.month
dDayDate = dDay.day
dd = datetime.date(dDayYear, dDayMonth, dDayDate).weekday()
dDayDay = days[dd]

print(f'{tdayMonth}월 {tdayDate}일 {tdayDay}부터 100일 뒤는 {dDayMonth}월 {dDayDate}일 {dDayDay}')
