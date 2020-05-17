def stackcontrol(e): # e : elements
    # push
    if e.isdigit(): # if e is num
        stk.append(int(e)) # push
    # error
    if not stk: # stack underflow in case of pop, dup, +, -
        return "e" 
    elif len(stk) == 1: # stack has 1 element
        if e == "+" or e == "-": # error for +, - (needs 2 elements)
            return "e" 
    # possible to operate
    if e == "DUP":
        stk.append(stk[-1]) # duplicate
    elif e == "POP":
        stk.pop() # pop
    elif e == "+":
        top = stk.pop()
        top2 = stk.pop()
        stk.append(top+top2) # add
    elif e == "-":
        top = stk.pop()
        top2 = stk.pop()
        stk.append(top-top2) # subtract
        if stk[-1] < 0:
            return "e"
        
def solution(S):
    operation = S.split() # operation list
    global stk # Stack
    stk = []
    for i in range(len(operation)):
        if stackcontrol(operation[i]) == "e" :
            return -1
    return stk[-1]
    

print(solution("3 DUP 5 - -"))

