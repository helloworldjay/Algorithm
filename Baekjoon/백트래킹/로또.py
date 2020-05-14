# main 함수 만들때 import는 안에다 써주어야 한다.

def main():
    from sys import stdin
    from itertools import combinations
    testcase = []
    while True:
        n = list(map(int, stdin.readline().split()))
        testcase.append(n)
        if n == [0]:
            break
    for t in range(len(testcase)):
        if testcase[t] == [0]: # 입력값이 0 이면 함수 종료
            return
        else :
            n = testcase[t][1:]
            result = list(combinations(n,6)) # combination 결과는 튜플, 오름차순으로 나온다.
            for i in range(len(result)):
                print(' '.join(list(map(str, result[i]))))
        print()
if __name__ == '__main__':
    main()