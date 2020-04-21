def solution(s):
    lst = list(map(int, s.split()))
    return "{} {}".format(min(lst), max(lst))    
    