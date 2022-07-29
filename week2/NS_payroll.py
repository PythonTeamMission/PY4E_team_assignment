monthly = input('월급을 입력해주세요 ')

if int(monthly) * 12 <= 12000000:
    print('세율은 6%입니다.')
    print('세전 연봉 :', float(monthly) * 12,'원')
    print('세전 연봉 :', int(monthly) * 12 * 0.94,'원')

elif int(monthly) * 12 > 12000000 and int(monthly) * 12 <= 46000000:
    print('세율은 15%입니다.')
    print('세전 연봉 :', float(monthly) * 12, '원')
    print('세전 연봉 :', int(monthly) * 12 * 0.85, '원')

elif int(monthly) * 12 > 46000000 and int(monthly) * 12 <= 88000000:
    print('세율은 24%입니다.')
    print('세전 연봉 :', float(monthly) * 12, '원')
    print('세전 연봉 :', int(monthly) * 12 * 0.76, '원')

elif int(monthly) * 12 > 88000000 and int(monthly) * 12 <= 150000000:
    print('세율은 35%입니다.')
    print('세전 연봉 :', float(monthly) * 12, '원')
    print('세전 연봉 :', int(monthly) * 12 * 0.65, '원')

elif int(monthly) * 12 > 150000000 and int(monthly) * 12 <= 300000000:
    print('세율은 38%입니다.')
    print('세전 연봉 :', float(monthly) * 12, '원')
    print('세전 연봉 :', int(monthly) * 12 * 0.62, '원')

elif int(monthly) * 12 > 300000000 and int(monthly) * 12 <= 500000000:
    print('세율은 40%입니다.')
    print('세전 연봉 :', float(monthly) * 12, '원')
    print('세전 연봉 :', int(monthly) * 12 * 0.60, '원')

else:
    print('세율은 42%입니다.')
    print('세전 연봉 :', float(monthly) * 12, '원')
    print('세전 연봉 :', int(monthly) * 12 * 0.58, '원')