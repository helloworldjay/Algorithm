def solution(dataSource, tags):
    doclist = [0 for i in range(len(dataSource))]
    result = []
    app = result.append
    ziplist = []
    zapp = ziplist.append
    for i in tags:
        for j in range(len(dataSource)):
            if i in dataSource[j] :
                doclist[j] += 1
    for i in range(len(doclist)):
        if doclist[i] != 0 :
            zapp([doclist[i],dataSource[i][0]])
    z = sorted(ziplist, key = lambda x : (-x[0], x[1]))
    for i in range(len(z)):
        app(z[i][1])
    return result

print(solution([
    ["doc1", "t1", "t2", "t3"],
    ["doc2", "t0", "t2", "t3"],
    ["doc3", "t1", "t6", "t7"],
    ["doc4", "t1", "t2", "t4"],
    ["doc5", "t6", "t100", "t8"]
], ["t1", "t2", "t3"]))