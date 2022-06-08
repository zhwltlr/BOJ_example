#  ***********stack/queue*************
# 주식가격 - 나중에 다시 풀어보기(아래는 답)
from collections import deque
def solution(p):
    ans = []
    q = deque(p)
    # 큐로 만들어주고

    # 큐가 빌때까지 반복
    while q:
        x = q.popleft()
        sec = 0
        # 큐를 돌면서 하나씩 비교
        for i in q:
            sec += 1
            # 만약 해당값보다 작은 값이 있으면 끝내고 ans에 sec값 넣어주기
            if x > i:
                break
        ans.append(sec)
    return ans

print(solution([1,2,3,2,3,1]))

