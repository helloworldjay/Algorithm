# 전체 검색 O(N^2)
# 조건이 len(points) <= 100,000 이므로 속도 에러발생
# def maxSlope(points) :
#     '''
#     n개의 점들 중에서 2개의 점을 선택했을 때, 얻을 수 있는 기울기의 절댓값 중에서 가장 큰 값을 반환하는 함수를 작성하세요.

#     **주의** : 소숫점 넷째자리에서 반올림하는 것은 고려할 필요가 없습니다. 이는 main()에서 출력을 할 때에 처리가 되므로, 기울기의 최댓값을 구하는 것에 집중해 주시길 바랍니다.
#     '''
#     maxGradient = 0
#     for i in range(len(points)-1):
#         for j in range(i,len(points)):
#             if points[i][0] == points[j][0]:
#                 continue
#             gradient = abs((points[i][1] - points[j][1])/(points[i][0]-points[j][0]))
#             if gradient > maxGradient:
#                 maxGradient = gradient
#     return round(maxGradient, 4)

def getSlope(a,b):
    return abs((a[1]-b[1])/(a[0]-b[0]))


def maxSlope(points) :
    '''
    n개의 점들 중에서 2개의 점을 선택했을 때, 얻을 수 있는 기울기의 절댓값 중에서 가장 큰 값을 반환하는 함수를 작성하세요.

    **주의** : 소숫점 넷째자리에서 반올림하는 것은 고려할 필요가 없습니다. 이는 main()에서 출력을 할 때에 처리가 되므로, 기울기의 최댓값을 구하는 것에 집중해 주시길 바랍니다.
    '''
    points.sort()
    result = 0
    for i in range(len(points)-1):
        result = max(result, getSlope(points[i],points[i+1]))
    return result

    return 0

