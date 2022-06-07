# 백준 13023번
# 1. 기본 입력 받기
n,m = map(int,input().split())
graph = [[]for _ in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n+1)
# 정답일 경우 1,0을 출력해야하므로 true/false로 답을 체크해놓는다 - 숫자로 표현해도 답은 같게 나옴
ans = False

# dfs 실행의 깊이가 4이상 일때 문제의 조건이 성립
# 2. dfs() 기본 함수 + depth == 4 조건 잡아주기
def dfs(v,depth):
    global ans
    visited[v] = True

    if depth == 4:
        ans = True #False값을 True로 변경 - 이게 모여서 정답이 될 것
        return
    
    # 기본 dfs()
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(i,depth+1)
            visited[i] = False
            # False로 초기화를 해야 다음 dfs()의 true/false를 판단할 수 있다

# 3. 시작값이 없으므로 모든 노드에서 dfs()를 해줘야함
for i in range(n):
    if not visited[i]:
        dfs(i,0)
        visited[i] = False
if ans == True:
    print(1)
else:
    print(0)



