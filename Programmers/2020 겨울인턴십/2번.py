# 2번 15분 
def solution(encrypted_text, key, rotation):
    decrypted_text = '' # 암호가 풀린 결과물
    rotation %= len(encrypted_text) # len 이상의 순환은 제자리이다
    encrypted_text = encrypted_text[rotation:] + encrypted_text[:rotation] # 음수여도 같은 메커니즘으로 작동
    for i in range(len(encrypted_text)):
        key_move = ord(encrypted_text[i])-(ord(key[i])-96) # key로 변환된 만큼의 차이
        if key_move < 97 : key_move += 26 # key_move가 97보다 작으면 대문자 영역이므로 다시 z로 전환
        decrypted_text += chr(key_move)
    return decrypted_text

print(solution("defghbc","aaaaaaa", -9))

