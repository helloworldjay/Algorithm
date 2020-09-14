def solution(boxes):
    boxes.sort()
    idx= 0
    # 요소가 같으면 제거해준다.
    while idx < len(boxes):
        if boxes[idx][0] == boxes[idx][1]: del boxes[idx]
        else: idx += 1
    # 새로 사야하는 물건의 개수
    cnt = 0
    idx = 0
    # 박스가 있는 동안 순회
    while True:
        before = len(boxes)
        # idx의 1번째 인덱스 요소가 뒤에 존재하는지 확인하는데 우선 0번째 인덱스들을 확인한다.
        for i in range(idx+1, len(boxes)):
            # boxes의 idx의 인덱스 1번째 요소가 뒤의 요소 중 0번째에 존재하면
            if boxes[idx][1] == boxes[i][0]:
                boxes[idx][0], boxes[i][0] = boxes[i][0], boxes[idx][0]
                if boxes[i][0] == boxes[i][1]: del boxes[i]
                del boxes[idx]
                break
            elif boxes[idx][1] == boxes[i][1]:
                boxes[idx][0], boxes[i][1] = boxes[i][1], boxes[idx][0]
                if boxes[i][0] == boxes[i][1]: del boxes[i]
                del boxes[idx]
                break
            elif boxes[idx][0] == boxes[i][0]:
                boxes[idx][1], boxes[i][0] = boxes[i][0], boxes[idx][1]
                if boxes[i][0] == boxes[i][1]: del boxes[i]
                del boxes[idx]
                break
            elif boxes[idx][0] == boxes[i][1]:
                boxes[idx][1], boxes[i][1] = boxes[i][1], boxes[idx][0]
                if boxes[i][0] == boxes[i][1]: del boxes[i]
                del boxes[idx]
                break
        after = len(boxes)
        if after == 0 or before == after: break
    return len(boxes)

print(solution([[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]]))

