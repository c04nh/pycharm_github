# 해당하는 숫자는 박수를 몇 번 쳐야 하는가?

a = 613

카운터 = 0
문자열 = str(a)
for x in 문자열:
    if x == '3' or x == '6' or x == '9':
        카운터 += 1

print(카운터)