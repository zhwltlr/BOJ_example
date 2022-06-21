
#p. 315 볼링공 고르기 - 답은 나옴
# itertools 사용에 관한 고민이 좀 있음 갠적으로...
from itertools import combinations
n, m = map(int,input().split())
ball = list(map(int,input().split()))
result =[]
# 순열로 2개씩 뽑기
for i in combinations(ball,2):
    # set으로 같은 숫자 나오는 경우 제외해주기
    if len(set(i)) == 1:
        continue
    else:
        result.append(i) #나머지는 result에 추가해주기
print(len(result))


# itertool 없이 푼 답
n, m = map(int,input().split())
ball = list(map(int,input().split()))
# 무게 x에 해당하는 인덱스 x번에 +1해주기
weight = [0] * 11
for x in ball:
    weight[x] += 1

result = 0
# A는 만약 1이라면 나머지 4개를 모두 선택할 수 있고
# 만약 2라면 2를 제외한 3개 선택 가능한데 1의경우에서 세어준 경우를 제외하면 2개 선택 가능
for i in range(1,m+1):
    n -= weight[i] # A가 선택하는 경우의 수 제외
    result += weight[i]*n #B가 선택하는 수와 곱하기
# 이걸 함수로 나타낸 게 위의 식
print(result)