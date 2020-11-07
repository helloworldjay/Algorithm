def solution(logs):
    from itertools import combinations
    suspects = []
    score_dict = {}
    for i in range(len(logs)):
        student_no, prob, score = logs[i].split() # student number, problem number, score
        if score_dict.get(student_no, -1) == -1 : # student_no doesn't exist
            score_dict[student_no] = {prob:score}
        else : # student_no exists
            score_dict[student_no][prob] = score # update or initialize score
    dict_keys = list(combinations(score_dict.keys(), 2))
    for cand1, cand2 in dict_keys:
        is_check = False
        cand1_keys, cand2_keys = sorted(list(score_dict[cand1].keys())), sorted(list(score_dict[cand2].keys()))
        if len(cand1_keys) < 5 or len(cand2_keys) < 5 or len(cand1_keys) != len(cand2_keys): # different number of problems solved
            continue
        if cand1_keys != cand2_keys : # different problems
            continue
        for i in range(len(cand1_keys)):
            if score_dict[cand1][cand1_keys[i]] != score_dict[cand2][cand1_keys[i]] : # different answer
                is_check = True
                break
        if is_check : continue
        suspects.append(cand1) # if it didn't escape above, it's suspect
        suspects.append(cand2)
    if not suspects : return ["None"]
    return sorted(list(set(suspects)))

print(solution(["1901 10 50", "1909 10 50"]))