def solution(money):
    did_rob_first_dp = [money[0]] + [money[0]] * (len(money) - 1)
    didnot_rob_first_dp = [0, money[1]] + [0] * (len(money) - 2)
    for i in range(2, len(money) - 1):
        did_rob_first_dp[i] = max(did_rob_first_dp[i-2] + money[i], did_rob_first_dp[i-1])
        didnot_rob_first_dp[i] = max(didnot_rob_first_dp[i-2] + money[i], didnot_rob_first_dp[i-1])
    didnot_rob_first_dp[len(money)-1] = max(didnot_rob_first_dp[len(money)-3] + money[len(money)-1], didnot_rob_first_dp[len(money)-2])
    return max(max(did_rob_first_dp), max(didnot_rob_first_dp))


def solution2(money):
    # 첫 번째 집 털었을 때 = [첫 집 털 때, 첫 집 털고 둘째 집 못 털 때]
    f_dp = [money[0], money[0] + 0]
    # 첫 번째 집 못 털었을 때 = [0, 첫 집 못 털고 둘째 집 털 때]
    l_dp = [0, money[1]]

    # 마지막집은 못터니까 len(money)-1까지
    for i in range(2, len(money) - 1):
        # 전 집 못 털었을때 + 지금집 털때 ,지금집 못털 때(바로 전까지 메모제이션해둔 값과 동일) 값 중 최대
        f_dp.append(max(f_dp[i - 2] + money[i], f_dp[i - 1]))

    for i in range(2, len(money)):
        l_dp.append(max(l_dp[i - 2] + money[i], l_dp[i - 1]))
    return max(f_dp[-1], l_dp[-1])  # 둘 중 최대

print(solution2([1,2,3,1]))