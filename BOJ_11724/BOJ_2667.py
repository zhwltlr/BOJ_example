# 백준 2667번 - 다시 풀어보기 (접근은 일단 전보다 훨씬 나아졌음)
n = int(input())
graph = [list(map(int,input()))for i in range(n)]
visited = [[False]*n for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
cnt = 0
ans = []

def dfs(x,y):
  global cnt
  visited[x][y] = True

  if graph[x][y] == 1:
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny <n:
        # 범위 넘지 않는 조건중 방문하지 않은 인근집 방문하여 dfs()
            if visited[nx][ny] == False and graph[nx][ny] == 1:
                dfs(nx,ny)

for i in range(n):
  for j in range(n):
    if graph[i][j] == 1 and visited[i][j] == False:
      dfs(i,j)
      ans.append(cnt)
      cnt = 0
print(ans)




n = int(input())
graph = [list(map(int,input()))for _ in range(n)]
visited = [[False]*n for _ in range(n)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
ans = []
cnt = 0

def dfs(x,y):
    global cnt
    visited[x][y] = True

    if graph[x][y] == 1:
        cnt += 1
        for i in range(4):
                nx = x + dx[i] 
                ny = y + dy[i] 
                if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1 and visited[nx][ny] == False:
                    dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            dfs(i,j)
            ans.append(cnt)
            cnt = 0
