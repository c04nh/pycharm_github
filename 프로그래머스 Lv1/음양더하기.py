def solution(absolutes, signs):
    sum_num = 0
    for i in range(len(absolutes)):
        if signs[i] is True:
            sum_num += absolutes[i]
        else:
            sum_num -= absolutes[i]
    return sum_num

if __name__ == '__main__':
    abs = [4, 7, 12]
    signs = [True, False, True]
    solution = solution(abs, signs)
    print(solution)