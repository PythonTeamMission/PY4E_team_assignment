
모두의 파이썬 팀과제 week4 파일을 제출하는 폴더입니다.



## 턴테코치님의 피드백 :

#### Q1에서 소수점이 있을 때는 어떻게 구현하나? 에 대한 질문에 저도 궁금해서 미션 답안 코드를 살짝 변경해봤습니다.

```
def make_comma(num):
    origin_num = str(num).split('.')

    num = origin_num[0]
    float_num = '.' + origin_num[1] if len(origin_num) > 1 else ""

    new_num = ""
    commas = len(num) // 3

    if len(num) % 3 == 0:
        commas -= 1

    if commas == 0:
        print(num + float_num)
        return

    n = -1

    while commas > 0:
        new_num = num[n] + new_num
        if n % 3 == 0:
            new_num = "," + new_num
            commas -= 1
        n -= 1

    print(num[:n + 1] + new_num + float_num)


num = input()

make_comma(num)
```

그리 깔끔하진 않으나, 소수점을 최대한 살려봤습니다. 그리고 기존 답안에서 세 자리 수를 입력하면 공백을 출력하기 때문에 이에 대한 예외도 처리했습니다.
그리고 이미 파이썬에 대한 이해도나 새로운 시도 등이 상당히 좋으셔서 제가 오히려 더 배웁니다.


#### Q3에서는 정규표현식을 사용해봤어요.

```
import re

phone = input()

if re.match('^010\-\d{4}\-\d{4}', phone):
    # if re.match('^010[-][0-9]{4}[-][0-9]{4}', phone): 도 가능
    print("correct")
else:
    print("NOPE")
    
```


이렇게 빠르게 형식에 맞는지 확인할 수 있습니다.
비슷하게 Q4에서도 정규표현식을 사용하면 코드 길이가 크게 줄어들 수 있을 것 같습니다.
물론 내용이 매우 복잡하므로 참고만 해주시길 바랍니다!

https://wikidocs.net/4308

매번 열심히 해주셔서 감사합니다 :))




