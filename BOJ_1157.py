# ***** 방법 1 ( dict, get() 이용 )
word = list(map(ord,input().upper()))
data = {} #dict 형태
for i in word:
  data[i] = data.get(i,0) + 1
# get을 이용해서 data에 단어값 저장
# i = word에 있는 알파벳들, 0 = get은 없을때 none으로 표시되므로 none 말고 0으로 표시되게 함
# 1 = 해당 알파벳이 중복될 때 +1씩 

print(data)
# ex) mississipi => {65: 1, 66: 1, 67: 1, 68: 1, 69: 1, 70: 1, 83: 1}

maxV = [k for k,v in data.items() if max(data.values()) == v]
# dict에서 value값 비교를 통해 최대 value의 key값 도출

# 최종 출력
if len(maxV) == 1:
  print(chr(maxV[0]))
else:
  print('?')




# ***** 방법 2 ( list, counter, sort(lambda)이용 )
s = list(map(str,(input().upper())))

from collections import Counter
lst = []
# counters통해서 k,v 뽑아내기
for k,v in Counter(s).items():
  lst.append([k,v])
  lst.sort(reverse=True,key = lambda x:x[1])
# append와 동시에 v값이 더 큰 [k,v]가 맨 앞으로 오게 조정

print(lst)
# ex) [['I', 4], ['S', 4], ['M', 1], ['P', 1]]

# 최종 출력
if len(lst) == 1 or lst[0][1] != lst[1][1]:
  print(lst[0][0])
else:
  print('?')