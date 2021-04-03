def solution(enroll, referral, seller, amount):
    account = {name: 0 for name in enroll}
    parents = {enroll[i] : referral[i] for i in range(len(enroll))}
    for i in range(len(seller)):
        base_money = (amount[i]*100)
        person_to_get_money = seller[i]
        while True:
            money_to_give = int(base_money/10)
            account[person_to_get_money] += base_money - money_to_give
            base_money = money_to_give
            if parents[person_to_get_money] == "-": break
            person_to_get_money = parents[person_to_get_money]
    return list(account.values())


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))
