
def josephus(num, target):
    # 나가는 순서 리스트
    queue = [0 for _ in range(num)]
    # 기본 리스트
    base = [i for i in range(1,num+1)]
    # base로 target만큼 이동시키며 queue 를 갱신
    idx = -1
    cnt = 0
    while True:
        queue[cnt] = base[(idx+target)%(len(base))]
        base.remove(base[(idx+target)%(len(base))])
        cnt += 1
        if len(base) == 0 :
            break
        base = base[(idx+target)%(len(base)):] + base[:(idx+target)%(len(base))]
   
    return queue

def main():
    print(josephus(7, 3)) #[3, 6, 2, 7, 5, 1, 4]이 반환되어야 합니다
    print(josephus(8, 2))
if __name__ == "__main__":
    main()