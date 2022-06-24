
# ***********순열 조합 itertools 없이 구현하기
# BOJ - 15649
n,m = list(map(int,input().split()))
s = []
def dfs():
    # 원하는 나열의 수 [1,2,3,4] 중 2개 할때 그 2에 해당하면
    if len(s)==m:
        # 이게 결과값
        print(' '.join(map(str,s)))
        return
    
    # 1부터 n까지 / 문제의 따라 array를 넣으면 됨
    for i in range(1,n+1):
        # s요소에 원소가 없으면 - [1,1] 들어가는 것 방지
        if i not in s:
            s.append(i)
            # 만들어둔 s에 포함하고
            dfs()
            # s가 꽉차면 뒷 요소 pop
            s.pop()
dfs()
 

# BOJ - 15650번
n,m = list(map(int,input().split()))
s = []
def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    # 시작점을 설정해주는 것이 가장 큰 차이
    for i in range(start,n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            # [1,2]/[2,1] 반복해서 세지 않기 위함
            s.pop()
dfs(1)


# BOJ - 15656번 (itertools,중복순열 dfs로 푼 것)
from itertools import product
n, m = map(int,input().split())
arr = [int(x)for x in input().split()]
arr.sort()
for i in product(arr,repeat=2):
  print(*i)

# 이 코드 잘 봐두기 - dfs()
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
temp = []

def dfs():
    if len(temp) == m:
        print(*temp)
        return

    # 다 똑같은데 위에 있던 if i not in s 조건만 없애주면 됨
    # 중복 조합도 비슷함 - start값만 잘 지정해주면 됨
    for i in range(n):
            temp.append(nums[i])
            dfs()
            temp.pop()

dfs()