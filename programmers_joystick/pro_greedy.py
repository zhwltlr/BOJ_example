
def solution(name):
    answer = 0
    
    # 무조건 좌우로 이동하면서 숫자를 증감시켜야하므로
    # 기본 최소 좌우이동 횟수는 길이 - 1
    min_move = len(name) - 1
    
    for i, char in enumerate(name):
        # enumerate -> i,v값 모두 나타낼 수 있는 함수
    	# 해당 알파벳 변경 최솟값 추가
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        # A에 가까운 알파벳, Z에 가까운 알파벳 비교
        
        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
            
        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
        min_move = min([min_move, 2 *i + len(name) - next, i + 2 * (len(name) -next)])
        
    # 알파벳 변경(상하이동) ord()통해 나타난 숫자 + 횟수에 좌우이동 횟수 추가
    answer += min_move
    return answer