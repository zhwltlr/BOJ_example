
# 처음 내가 푼 답 : 예제는 다 잘 나오는데 왜 실패인지 모르겠음
n = int(input())
a, b = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for i in range(m):
  x,y = map(int,input().split())
  graph[x].append(y)
  graph[y].append(x)
data = []
visited = [False] * (n+1)
# 기본 설정 + 결과를 담을 data 

def dfs(graph,a, visited):
  visited[a] = True
  data.append(a)
  # dfs 방문 노드들 기록하여 data에 담기

  for i in graph[a]:
    if not visited[i]:
      # visited[i] = True
      dfs(graph,i,visited)
dfs(graph,a,visited)

if b in data:
  print(data.index(b))
  # data에 있을 경우 인덱스 출력
else:
  print(-1)




# 수정해서 통과된 답 : cnt 조건 설정만 다른데... 이게 문제인건가...
n = int(input())
a, b = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for i in range(m):
  x,y = map(int,input().split())
  graph[x].append(y)
  graph[y].append(x)
data = []
visited = [False] * (n+1)
# 기본설정 + 결과 담을 data


# cnt로 직접 세기
def dfs(graph,a, cnt):
  cnt += 1
  visited[a] = True

  # 해당 노드에 방문했을 경우 cnt 값 data에 담기
  if a == b:
    data.append(cnt)

  for i in graph[a]:
    if not visited[i]:
      dfs(graph,i,cnt)
dfs(graph,a,0)
# 초기값은 0

# data가 비어있는건 방문하지 못했다는 뜻
if len(data) == 0:
  print(-1)
else:
  print(data[0]-1)
  # 방문했을 경우 cnt 값 출력 -1
