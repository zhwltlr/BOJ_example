n = int(input())
graph = []

# 각각의 단지에 속하는 집의 수 측정 후 보관할 data
data = []
# 집의 수 측정용
cnt = 0

for i in range(n):
  graph.append(list(map(int,input())))

def dfs(x,y):
    # 범위 벗어나는 조건 False 처리
  if x >= n or x < 0 or y >= n or y < 0:
    return False
    # 1인 경우 0처리 하고 상하좌우 살피기
    # 집의 수 +1씩 카운팅
  if graph[x][y] == 1:
    global cnt
    cnt += 1
    graph[x][y] = 0
    dfs(x,y-1)
    dfs(x,y+1)
    dfs(x+1,y)
    dfs(x-1,y)
    # dx,dy설정하고 for반복문 돌려서 호출해도 됨
    return True
    # 1인 집은 true 아닌 건 다 false 처리
  return False

result = 0
cnt = 0
for i in range(n):
  for j in range(n):
    if dfs(i,j) == True:
      result += 1 #총 단지 수 (DFS수)
      data.append(cnt)
      cnt = 0
print(result)
data.sort()
print(*data,sep='\n')