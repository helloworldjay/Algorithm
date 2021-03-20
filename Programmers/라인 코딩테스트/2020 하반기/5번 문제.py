def solution(cards):
    cards = cards[::-1]
    result = 0
    score = [i for i in range(11)] + [10,10,10]
    # 한 번의 게임
    while cards:
        dealer_open = 0
        dealer_hide = 0
        player = 0
        if len(cards) < 4: break 
        card = cards.pop()
        player += score[card]
        card = cards.pop()
        dealer_hide += score[card]
        card = cards.pop()
        player += score[card]
        card = cards.pop()
        dealer_open += score[card]
        # 블랙잭이면 플레이어가 3원을 받고 끝냄
        if player == 21:
            result += 3
            continue
        # 딜러가 블랙잭이면 플레이어가 2원을 잃고 끝냄
        if dealer_hide + dealer_open == 21:
            result -= 2
            continue
        
    return 