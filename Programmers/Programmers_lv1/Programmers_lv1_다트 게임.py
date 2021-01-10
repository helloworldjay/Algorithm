def get_score(dart:str) -> int:
    if dart[-1] == "D":
        return int(dart[:-1])**2
    elif dart[-1] == "T":
        return int(dart[:-1])**3
    return int(dart[:-1])
def solution(dartResult:str) -> int:
    game = ""
    total_score = 0
    this_game_score = 0
    formal_game_score = 0
    for dart in dartResult:
        if dart.isdigit():
            game += dart
        elif dart.isalpha():
            game += dart
            total_score += get_score(game)
            formal_game_score = this_game_score
            this_game_score = get_score(game)
            game = ""
        elif dart == "#":
            this_game_score *= -1
            total_score += 2*this_game_score
        elif dart == "*":
            total_score += (this_game_score + formal_game_score)
            this_game_score *= 2
            formal_game_score *= 2
    return total_score


print(solution("1S*2T*3S"))

