# 이진탐색
# 데이터가 정렬되어 있어야만 사용가능, 절반씩 좁혀가며 데이터를 탐색한다.

# ****재귀함수로 나타낸 이진탐색
# 시작점, 끝점, 중간점, target데이터
def 이진탐색(이진리스트, target, start, end):
    if start > end:
        # 시작점이 끝점보다 크면 없어!반환
        return None
    # 중간값 만들어주기
    mid = (start + end) // 2
    if 이진리스트[mid] == target:
        return mid #중간값이 타겟일 경우 그대로 반환
    # 중간점이 타겟보다 크면 중간점-1을 끝점으로 설정
    elif 이진리스트[mid] > target:
        return 이진탐색(이진리스트, target, start,mid-1)
    # 중간점이 타겟보다 작으면 중간점+1을 시작점으로 설정
    else:
        return 이진탐색(이진리스트, target, mid+1, end)

# 원소 개수와 찾고자하는 문자열 입력
n, target = list(map(int,input().split()))
# 전체 원소 입력
이진리스트 = list(map(int,input().split()))

result = 이진탐색(이진리스트, target, 0, n-1)
if result == None:
    print('원소존재안함')
else:
    print(result+1)

# ****반복문으로 나타낸 이진탐색     
def 이진반복(이진리스트, target, start, end):
    while start <= end:
    # 시작점이 끝점과 같아지기 전까지 반복
        mid = (start + end) //2
        if 이진리스트[mid] == target:
            return mid
        # 중간값이 target이면 반환
        elif 이진리스트[mid] > target:
            end = mid - 1
        # 중간값이 target보다 크면 끝점은 mid-1로 변경
        else:
            start = mid + 1
        # 중간값이 target보다 작으면 끝점은 mid+1로 변경
    return None
# 원소 개수와 찾고자하는 문자열 입력
n, target = list(map(int,input().split()))
# 전체 원소 입력
이진리스트 = list(map(int,input().split()))

result = 이진탐색(이진리스트, target, 0, n-1)
if result == None:
    print('원소존재안함')
else:
    print(result+1)

# **********tip************
# 데이터 범위가 1000만 단위 이상일 경우 이진탐색을 최우선적으로 고려해보자
