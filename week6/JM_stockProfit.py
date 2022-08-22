"""
📌Q3. 예금 금리가 너무 낮아서 주식을 시작했습니다. 아래와 같이 매수한 종목 이름, 수량, 매수 평균 금액이 있습니다. 판매가는 따로 주어집니다. 종목과 수익률만 출력하시고 종목별 수익률이 높은 순서대로 출력해주세요. (소수 둘째자리까지 출력)

stocks = "삼성전자/10/85000,카카오/15/130000,LG화학/3/820000,NAVER/5/420000"
sells = [82000, 160000, 835000, 410000]
# 소수 둘째자리까지 출력하는 방법
a = 3.141592
print(f"{a:.3}")
3.14
✅출력 예시
stock_profit(stocks, sells)
카카오의 수익률 23.1
LG화학의 수익률 1.83
NAVER의 수익률 -2.38
삼성전자의 수익률 -3.53
"""

#지난번에 알려주신 sort 람다식을 활용해봤습니다.

stocks = "삼성전자/10/85000,카카오/15/130000,LG화학/3/820000,NAVER/5/420000"
sells = [82000, 160000, 835000, 410000]

def stock_profit(stocks, sells):                                                                                    # stocks, sells를 받아 주식 종목별 수익률이 높은 순서로 출력 함수
    myStock = stocks.split(',')                                                                                         # myStock: stocks을 종목별로 나눈 리스트
    stockDict = dict()                                                                                                  # stockDict: key - 종목명 / value - 수익률 을 담을 딕셔너리 준비

    for idx, val in enumerate(myStock):                                                                                 # 갖고있는 종목만큼 반복문
        items = val.split('/')                                                                                              # items: 종목명/ 보유량/ 매수 평균 금액 리스트
        buyPrice = int(items[2])                                                                                            # buyPrice: 매수 평균 금액 int화
        buyCount = int(items[1])                                                                                            # buyCount: 보유량 int화

        result = ((sells[idx] - buyPrice) / buyPrice)*100                                                                   # result: 수익률
        stockDict[items[0]] = round(result, 2)                                                                              # stockDict: key - 종목명 / value - 수익률  대입

    #람다식을 활용한 value 기반 오름차순 정렬
    #dict(sorted(stockDict.items(), key=lambda stockDict: stockDict[1]))
    stockDict = dict((sorted(stockDict.items(), key=lambda stockDict: stockDict[1], reverse=True)))                         # 람다식을 활용한 value 기반 내림차순 정렬, 딕셔너리형태로 변경

    for key, val in stockDict.items():                                                                                  # stockDict 아이템 길이만큼 반복문
        print(f'{key} 의 수익률 : {val}')                                                                                    # 출력


#실행코드
print('\n-------------------------------------------')
print('주식을 종목별 수익률이 높은 순서로 출력하는 프로그램입니다.')
print('-------------------------------------------')
stock_profit(stocks, sells)