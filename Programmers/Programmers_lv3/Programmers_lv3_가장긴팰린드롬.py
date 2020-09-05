def is_palindrome(lst):
    if len(lst)%2 == 0 and lst[:len(lst)//2] == lst[len(lst)//2:][::-1]: return True
    elif len(lst)%2 == 1 and lst[:len(lst)//2] == lst[(len(lst)//2)+1:][::-1]: return True
    return False    


def solution(s):
    # 최소 한자리이므로
    max_len = 1
    for i in range(len(s)-1):
        for j in range(i, len(s)):
            if s[i] == s[j] and is_palindrome(s[i:j+1]):
                if j-i+1 > max_len:
                    max_len = j - i + 1
    return max_len

print(solution("abcdcba"))