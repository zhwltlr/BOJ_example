# BOJ_1157 - 단어공부

<h2> 방법1) dict 자료형과 get()으로 문제 풀기 </h2>
get을 이용해서 data에 단어값 저장
i = word에 있는 알파벳들, 0 = get은 없을때 none으로 표시되므로 none 말고 0으로 표시되게 함
1 = 해당 알파벳이 중복될 때 +1씩



<h2> 방법2) list, Counters, sort(lambda=x:x[0])으로 문제 풀기 </h2>
for k,v in Counter(s).items():
 ---- lst.append([k,v])
 ---- lst.sort(reverse=True,key = lambda x:x[1])
