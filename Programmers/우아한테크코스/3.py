def solution(money, expected, actual):
    betting = 100 # base betting
    for i in range(len(expected)):
        money -= betting # spend betting money from money
        if expected[i] == actual[i] : # case of winning
            money += 2*betting
            betting = 100 # initializing betting money
        else : # case of losing
            if money >= 2*betting : # can afford next betting money
                betting *= 2
            else : # can't afford
                betting = money
        if money == 0 : return 0
    return money