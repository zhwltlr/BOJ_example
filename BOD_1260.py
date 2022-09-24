n, m, start = map(int,input().split())
graph = [[]for _ in range(n+1)]
# [[],[],[],[]...]

# dfs / bfs 따로 해야 에러가 안난다
visited = [False] * (n+1)
visited2 = [False] * (n+1)

# 오랜만에 풀때 graph 만드는 법이 잘 안떠오름
# [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]
# 해당 노드에 인접한 노드가 다 표기 될 수 있도록 [a]에 append하면 [b]에도 append 해줘야함
for i in range(m):
  a, b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

# 작은 수부터 방문 해야하므로 graph를 sort() 해줘야 한다
for i in range(len(graph)):
  graph[i].sort()


# dfs 1
def dfs(v):
  visited[v] = True
  print(v, end=' ')

  for i in graph[v]:
    if not visited[i]:
      dfs(i)
dfs(start)
print()

# dfs 2 - 다른 문제에도 적용하려면 다 쓰는게 좋을 듯
def dfs(graph,v,visited):
  visited[v] = True
  print(v, end=' ')

  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i,visited)
dfs(graph,start,visited)


# bfs 1
from collections import deque
def bfs(v):
  q = deque([v])
  visited2[v] = True

  while q:
    v = q.popleft()
    print(v, end = ' ')

    for i in graph[v]:
      if not visited2[i]:
        q.append(i)
        visited2[i] = True
bfs(start)

# bfs 2 - 다른 문제에도 적용하려면 다 쓰는게 좋을 듯
def bfs(graph,v,visited2):
  q = deque([v])
  visited2[v] = True

  while q:
    v = q.popleft()
    print(v, end = ' ')

    for i in graph[v]:
      if not visited2[i]:
        q.append(i)
        visited2[i] = True
bfs(graph, start, visited2)