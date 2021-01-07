from collections import deque


def solution(skill: str, skill_trees: list) -> int:
    possible_skill = 0
    for test_case in skill_trees:
        # test_case를 순회하며 skill에 있지만 첫번째 요소와 다르면 false, 같으면 뺀다.
        skill_deque = deque(list(skill))
        for one_skill in test_case:
            if one_skill in skill_deque:
                if skill_deque[0] != one_skill: break
                skill_deque.popleft()
        else:
            possible_skill += 1
    return possible_skill
