korea = "태조,혜종,정종,광종,경종,성종,목종,현종,덕종,정종,문종,순종,선종,헌종,숙종,예종,인종,의종,명종,신종,희종,강종,고종,원조,충렬왕,충선왕,충숙왕,충혜왕,충목왕,충정왕,공민왕,우왕,창왕,공양왕"
chosun = "태조,정종,태종,세종,문종,단종,세조,예종,성종,연산군,중종,인종,명종,선조,광해군,인조,효종,현종,숙종,경종,영조,정조,순조,헌종,철종,고종,순종"

def king(korea, chosun):
    king_dict = dict()

    korea = korea.split(",")
    chosun = chosun.split(",")

    for kor in korea:
        king_dict[kor] = 1

    for cho in chosun:
        if king_dict.get(cho, 0) >= 1:
            king_dict[cho] = king_dict[cho] + 1
        else:
            continue

    repeated_king = []
    for (k, v) in king_dict.items():
        if v >= 2:
            repeated_king.append(k)

    count = 0
    for king in repeated_king:
        print(f"조선과 고려에 모두 있는 왕 이름 : {king}")
        count = count + 1
    print(f"조선과 고려에 모두 있는 왕 이름은 총 {count}개 입니다")

print(king(korea, chosun))