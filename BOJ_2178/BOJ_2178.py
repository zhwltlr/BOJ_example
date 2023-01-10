from collections import deque
# 최단경로를 묻는 문제로 bfs 사용 , deque 불러오기

n , m = map(int,input().split())
graph = []
# 0과 1로만 이루어진 그래프여서 visited 만들 필요x
for i in range(n):
  graph.append(list(map(int,input())))

# 상하좌우 나타내는 방향 그래프
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
  q = deque()
  q.append((x,y))

  while q:
    x,y = q.popleft()
    for i in range(4):
    #  상하좌우 돌면서 0인지 1인지 길이 없는지 확인
      nx = x + dx[i]
      ny = y + dy[i]

    #   1. 범위 벗어나는 조건
      if nx >= n or nx < 0 or ny >= m or ny < 0:
        continue

    # 2. 갈 수 없는 칸인 조건
      if graph[nx][ny] == 0:
        continue

    # 3. *** 갈 수 있는 칸인 조건
      if graph[nx][ny] == 1:
        # 경로를 지날때마다 +1을 해가면서 
        graph[nx][ny] = graph[x][y] + 1
        q.append((nx,ny))
#   최종 목적지 도착했을 때의 값 구하기
  return graph[n-1][m-1]
print(bfs(0,0))
# 시작점이 1,1로 정해져 있으므로 인덱스 번호 (0,0)