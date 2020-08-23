# O(N^2)
# 완전 탐색
# LIS의 길이를 반환
# A의 모든 증가 부분 수열을 만든 뒤 그 중 가장 긴 것의 길이를 반환
def lis(A):
    if not A :
        return 0
    ret = 0 
    for i in range(len(A)):
        B = []
        # lis(A)가 첫 숫자로 A[j]를 골랐을 때,
        # 이를 찾기 위해 A[j+1: ]의 부분 증가 수열 중 가장 긴 증가 수열 B 찾기
        for j in range(i+1, len(A)):
            
            if A[i] < A[j]:
                B.append(A[j])
        ret = max(ret, 1 + lis(B))
    return ret

print(lis([3,2,1,7,5,4,2,6]))