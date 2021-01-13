def solution(N: int, coffee_times: list) -> list:
    from collections import deque
    if N == 1:
        return [i for i in range(1, len(coffee_times) + 1)]
    result = []
    machine = []
    coffee_times_number = deque([])
    for number, time in enumerate(coffee_times):
        coffee_times_number.append((time, number + 1))
    while coffee_times_number and len(machine) < N:
        machine.append(coffee_times_number.popleft())
    while True:
        temp_index = []
        temp_value = []
        for i in range(len(coffee_times_number)):
            time_left, number = coffee_times_number[i]
            coffee_times_number[i] = (time_left - 1, number)
            if coffee_times_number[i][0] == 0:
                temp_index.append(number)
                temp_value.append(coffee_times_number[i])
        temp_index.sort()
        result += temp_index
        for i in range(len(temp_value)):
            print(temp_value)
            machine.remove(temp_value[i])
        while coffee_times_number and len(machine) < N:
            machine.append(coffee_times_number.popleft())
        if len(machine) == 0:
            break
    return result


print(solution(3, [4, 2, 2, 5, 3]))
