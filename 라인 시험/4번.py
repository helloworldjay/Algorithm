def solution(snapshots, transactions):
    done = [] # 이미 완료된 transaction인지 확인
    app = done.append
    for i in range(len(transactions)):
        if transactions[i][0] in done :
            pass
        else :
            if transactions[i][1] == "SAVE":
                for j in range(len(snapshots)):
                    if snapshots[j][0] == transactions[i][2]:
                        snapshots[j][1] = str(int(snapshots[j][1]) + int(transactions[i][3]))
                        break
                    elif j == len(snapshots) - 1:
                        snapshots.append([transactions[i][2],transactions[i][3]])
                
            else :
                for j in range(len(snapshots)):
                    if snapshots[j][0] == transactions[i][2]:
                        snapshots[j][1] = str(int(snapshots[j][1]) - int(transactions[i][3]))
                        break
            app(transactions[i][0])
            
    return snapshots