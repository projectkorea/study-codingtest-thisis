# 보드의 크기
n = int(input())

# 사과의 개수
k = int(input())

# 맵정보
# 1) n+1한 이유는 처음 좌표를 1,1로 설정하기 위함
data = [[0]*(n+1) for _ in range(n+1)]

# 사과정보 업데이트
for _ in range(k):
    # 2) 따로 split받고 행과 열로 나눠 저장
    x,y=map(int,input().split())
    data[x][y] = 1

# 방향 회전 개수
l = int(input())
info = []

# 방향 회전 정보 업데이트
for _ in range(l):
    x,c = input().split()
    # 3) 따로 split받고 append를 콤마로 나누어 튜플로 저장
    info.append((int(x),c))

# 방향 설정
# 4) 처음엔 동쪽을 바라본다 => 동쪽 좌표 시작
# 90도씩 돈다 => 0을 기준으로 -1, 1 인덱스는 북또는남이 되어야함
# 동남서북
# direction 값으로 정해놓고, 4로 나눈 나머지 값으로 인덱스를 찾음
dx = [0,1,0,-1]
dy = [1,0,-1,0]

# direction 결정 함수
def turn(direction,c):
    if c == "L":
        direction = (direction -1) % 4
    else:
        direction = (direction+1) % 4
    return direction

def simulate():
    x,y = 1,1
    data[x][y] = 2 # 뱀이 존재하는 위치는 2로 설정
    direction = 0 # 처음엔 동쪽을 바라보고 있음
    time = 0
    l_count = 0 # 다음에 회전할 정보 변수
    q = [(x,y)] # 뱀이 차지하고 있을 위치 정보
    
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 종료 조건인지 확인
        # 맵에 범위 안에 있고, 뱀의 몸통이 없는 위치라면
        if 1 <= nx and nx <= n and 1<= ny and ny<=n and data[nx][ny] !=2:
            # 다음 좌표로 움직이기
            data[nx][ny] = 2
            q.append((nx,ny))
            # 사과가 없다면 이동 후에 꼬리 제거
            if data[nx][ny] == 0 :
                # 꼬리 제거, 가장 깊은 곳에 쌓인 인덱스 pop시키는 것
                px,py = q.pop(0)
                data[px][py] = 0
        
        # 벽이나 뱀의 몸통과 마딱뜨렸다면
        else:
            time += 1
            break
        
        # 뱀의 머리를 이동
        x,y=nx,ny
        time +=1
        # 다음에 움직일 게 방향전환이 필요하면
        if l_count < l and time == info[l_count][0]:
            direction = turn(direction,info[l_count][1])
            l_count +=1 
    return time


















