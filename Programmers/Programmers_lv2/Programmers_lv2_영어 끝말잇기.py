def solution(n: int, words: list) -> list:
    game_dict = {words[0]:1}
    for i in range(1, len(words)):
        if words[i - 1][-1] != words[i][0] or words[i] in game_dict:
            return [(i % n) + 1, i // n + 1]
        game_dict[words[i]] = 1
    return [0, 0]

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))