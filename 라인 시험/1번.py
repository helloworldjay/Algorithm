def solution(inputString):
    n = list(inputString) # string을 개별로 나눠 리스트로 만든다.
    if n.count("(") != n.count(")") or n.count("{") != n.count("}") or n.count("[") != n.count("]") or n.count("<") != n.count(">"):
        return -1 
    else :
        for i in range(len(n)):
            if n[i] == ")":
                if n[:i].count("(") < n[:i+1].count(")"):
                    return -1
            elif n[i] == "}":
                if n[:i].count("{") < n[:i+1].count("}"):
                    return -1
            elif n[i] == "]":
                if n[:i].count("[") < n[:i+1].count("]"):
                    return -1
            elif n[i] == ">":
                if n[:i].count("<") < n[:i+1].count(">"):
                    return -1
    return n.count(")") + n.count("}") + n.count("]") + n.count(">") 

print