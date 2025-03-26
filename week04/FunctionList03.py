capacity = 10                        # 전역 변수
array = [None]*capacity              # 전역 변수
size = 0                             # 전역 변수

# 리스트의 연산: 일반 함수
def isFull():
    return size == capacity  # 비교 연산 결과를 바로 반환

def insert():
    global size  # size는 전역변수
    if not isFull():
        print("3) 현재의 size와 capacity의 값은 같은가?", isFull())         
        size += 1  # 요소의 수가 하나 증가
        print("4) 현재의 size 변수의 값은? ", size)         
    else:
        print("리스트 overflow 또는 유효하지 않은 삽입 위치")
        exit()

# 프로그램의 시작
if __name__ == "__main__":
    print("1) 현재 size 변수의 값은 ? ", size)   
    print("2) 현재 capacity 변수의 값은 ? ", capacity)   
    insert()