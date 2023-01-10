# dfs로 풀어보려고 했으나 실패한 것
m, n, h = list(map(int,input().split()))
graph = []
for i in range(n*h):
  graph.append(list(map(int,input().split()))) 

def dfs(x,y):
  if x >= m or x < 0 or y >= n*h or y < 0:
    return False
#   if graph[x][y] == -1:
#     return False
  if graph[x][y] == 1:
    graph[x][y] = 0
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    dfs(x-n,y)
    dfs(x+n,y)
    return True
  return False

result = 0
if 0 not in graph:
  print('0:',0)

for i in range(m):
    for j in range(n*h):
        if dfs(i,j) == True:
            result += 1
        else:
            print('else:',-1)
print('result:',result)


# bfs로 풀어보기 - 정답
from collections import deque
m, n, h = map(int,input().split())
graph = []
q = deque([])
for i in range(h):
  temp = []
  for j in range(n):
    temp.append(list(map(int,input().split())))
    for k in range(m):
      # 만약 익은 토마토라면 q에 추가
      if temp[j][k] == 1:
        q.append([i,j,k])
  graph.append(temp)

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

while q:
    x,y,z = q.popleft()

  # 방향이 6방향이므로
    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]
      nz = z + dz[i]
      # 안되는 조건 말고, 덜익어서 익을 수 있는 가능성이 있을 때만 확인하기
      if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and graph[nx][ny][nz] == 0:
        q.append([nx,ny,nz])
        graph[nx][ny][nz] = graph[x][y][z] + 1
        # 최단거리 구할 때 처럼 +1하면서 날짜 세는 거

result = 0
for i in graph:
  for j in i:
    for k in j:
      # 만약 아예 익을 수 없는 상황이라면 -1
      if k == 0 :
        print(-1)
        # 문제 없이 깨끗한 종료를 의미함
        exit(0)
    result = max(result,max(j))
print(result-1)


# 흐름은 비슷하나 최단거리를 구하려면 bfs를 사용할 것, 그리고 잘 생각해보기....