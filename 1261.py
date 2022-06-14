# 1261번
from collections import deque
m , n = map(int,input().split())
# 가로가 m 세로가 n
graph = [[int(x) for x in input()]for _ in range(n)]
# visited를 -1로 설정하는 이유를 모르겠음...
# 아마도 1로 하면 결과값에서 1을 빼야해서 미리 빼주는 거 같다
visited = [[-1]*(m)for _ in range(n)]
visited[0][0] = 0
dx = [0,0,-1,1]
dy = [-1,1,0,0]
q = deque()
q.append([0,0])

def bfs():
  while q:
    x,y = q.popleft() # 0,0

    # 상하좌우
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<n and 0<=ny<m:
        if visited[nx][ny] == -1:
          if graph[nx][ny] == 0:
            visited[nx][ny] = visited[x][y]
            q.appendleft([nx,ny])
            # 0이 우선권을 가지기 위해서 appendleft를 사용한다
          else:
            visited[nx][ny] = visited[x][y] +1
            q.append([nx,ny])

bfs()
print(visited[n-1][m-1])    