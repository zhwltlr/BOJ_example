
# # 백준 11724번
# # 1. 입력 조건 (많은 dfs 문제 입력 방식이 유사)
# n, m = map(int,input().split())
# graph = [[]for _ in range(n+1)]
# visited = [False] * (n+1)
# cnt = 0
# # 연결 요소 개수 세어줄 cnt 초기화 설정
# for i in range(m):
#   a, b = map(int,input().split())
#   graph[a].append(b)
#   graph[b].append(a)

# # 2. dfs() 기본함수 + cnt 세어주는 조건 설정
# def dfs(v):
#   global cnt
#   visited[v] = True

#   for i in graph[v]:
#     if not visited[i]:
#     #   print('graph[v]=',graph[v],'visited[i]=',visited[i],'i=',i)
#       dfs(i)

# # 3. 시작점이 주어지지 않았기 때문에 1부터 n까지 노드를 방문하면서 dfs를 다 돌았다면 cnt +1을 해준다
# for i in range(1,n+1):
#   if not visited[i]:
#     # print(i)
#     dfs(i)
#     cnt +=1
# print(cnt)






n , m = map(int,input().split())
graph = [[]for _ in range(n+1)]
for i in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)
cnt = 0
visited = [False] * (n+1)
def dfs(v):
  global cnt
  visited[v] = True

  for i in graph[v]:
    if not visited[i]:
      dfs(i)

for i in range(1,n+1):
  if not visited[i]:
    dfs(i)
    cnt += 1
print(cnt)



