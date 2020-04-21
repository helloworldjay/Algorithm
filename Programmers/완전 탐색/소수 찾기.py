from itertools import permutations
#에라토스 테네스의 체가 더 빠르다고해서 했는데 조건이 9999999 이다보니 전체 배열 만드는게 더 오래 걸려서 시간 초과 뜬다. 해보고 안되면 이게 더 빠르다.
def isPrime(num):
    sqrt = int(int(num)**(0.5))
    if num == 1 or num == 0: # 이 조건을 안넣어 문제가 있었다. 특히 1만 생각하고 0을 생각 안해서 두번이나 틀림
        return False
    for i in range(2, sqrt+1):
        if num % i == 0 :
            return False
    return True
    
    # 모든 경우의 수 만들기
def solution(numbers):
    all_case = []
    app = all_case.append
    numlist = list(numbers)
    for i in range(1,len(numbers)+1):
        pmlist = list(permutations(numlist,i))
        for j in range(len(pmlist)):
            app(''.join(pmlist[j]))
    all_case = list(map(int,all_case))
    all_case_set = list(set(all_case))
    cnt = 0
    for i in range(len(all_case_set)):
        if isPrime(all_case_set[i]) == True:
            cnt += 1
    return cnt

