# 1시간 5분
# '#'를 처리할 함수
def sharp(music):
    idx = 0
    while idx < len(music):
        # C#은 c로, D#은 d로..
        if music[idx] == "#":
            music = music[:idx-1] + chr(ord(music[idx-1])+32) + music[idx+1:]
        else:
            idx += 1
    return music

# music info를 넣을 때 정보를 분리할 함수
def processing_info(musicinfo):
    start, finish, name, melody = musicinfo.split(',')
    # '#' 문자열 처리
    melody = sharp(melody)
    hh1, mm1 = map(int, start.split(':'))
    hh2, mm2 = map(int, finish.split(':'))
    # play시간을 초로 계산
    playtime = (hh2-hh1)*60 + (mm2-mm1)
    # 주어진 시간을 멜로디 길이로 나눈 몫과 나머지
    q, r = divmod(playtime, len(melody))
    playmusic = melody*q + melody[:r]
    # 음악 이름, 해당 문자열을 반환
    return name, playmusic, playtime

def solution(m, musicinfos):
    max_time = 0
    result = ""
    for i in range(len(musicinfos)):
        name, playmusic, playtime = processing_info(musicinfos[i])
        # '#' 문자열 처리
        m = sharp(m)
        if m in playmusic and playtime > max_time:
            result = name
            max_time = playtime
    return '(None)' if result == "" else result



print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))