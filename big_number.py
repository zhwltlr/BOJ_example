# 1. 내장함수 itertools로 풀었을 때
# 시간초과가 나온다 - 조건이 number는 2자리 이상, 1,000,000자리 이하인 숫자이기 때문에
from itertools import combinations
def solution(number, k):
    data = list(map(int,number))
    data = set(list(combinations(data,len(number) - k)))
    # k개 제거한거라서 len(number) - k

    lst = list(data)
    lst.sort(reverse=True)
    result = ''.join([str(a) for a in lst[0]])
    # 역순 정렬 후 제일 앞에 원소 출력
    return result



# 2. stack 이용하여 풀때
def solution(number, k):
    answer = [] # Stack
    
    for num in number:
        if not answer: #비어있다면
            answer.append(num) #일단 채운다
            continue
        if k > 0:
            # 만약 answer[-1]보다 number 문자열에서 다음 숫자가 더 크다면
            while answer[-1] < num:
                answer.pop() #그 [-1]은 뻬주고
                k -= 1 #k도 -1 해주고
                if not answer or k <= 0:
                    break #k가 0이 되거나 answer가 없다면 멈춰!
        answer.append(num) 
    # k개 만큼 나열하는 것
    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)

# 다음 인덱스와 현재 인덱스를 구분할 때 좀 어려움을 겪는다.
# stack 떠올릴 수 있도록 노력하자