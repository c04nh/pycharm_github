def 보조함수(month, day):
    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0
    for i in range(month-1):
        total += month_list[i]
    total += day
    return total -1



def solution(start_month, start_day, end_month, end_day):
    start_total = 보조함수(start_month, start_day)
    end_total = 보조함수(end_month, end_day)
    return end_total - start_total

start_month = 1
start_day = 2
end_month = 2
end_day = 2
ret = solution(start_month, start_day, end_month, end_day)

print(ret)