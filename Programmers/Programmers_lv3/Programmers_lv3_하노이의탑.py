# 출발노드, 경유노드, 도착노드, 판의 수
def hanoi(start_node, pass_node, desti_node, n):
    global result
    if n == 1 : 
        return [start_node, desti_node]
    else :    
        result.append(hanoi(start_node, desti_node, pass_node,n-1))
        result.append([start_node, desti_node])
        result.append(hanoi(pass_node,start_node,desti_node,n-1))

def solution(n):
    global result
    result = []
    hanoi(1,2,3,n)
    result = list(filter(None, result))
    return result

print(solution(3))