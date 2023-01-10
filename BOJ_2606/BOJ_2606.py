# DFS - 한 방향으로 계속 가다가 더이상 갈 수 없을 때까지 탐색 & 시작노드가 1로 주어졌으니 DFS가 가장 좋을 듯
n = int(input())
m = int(input())
# 0번 인덱스 비우기 위해 n+1
graph = [[]for _ in range(n+1)]

# m값 입력받기
for i in range(m):
  a, b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)
# [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]

# 방문여부 확인
visited = [False] * (n+1)
result = []

# 기본 dfs 형식과 똑같음
def dfs(graph,v,visited):
  visited[v] = True
  # 값을 배열로 저장후 길이출력 위함
  result.append(v)
  for i in graph[v]:
    if not visited[i]:
      visited[i] = True
      dfs(graph, i , visited)
    # 1을 포함하고 있어서 -1
  return len(result) -1

print(dfs(graph,1,visited))