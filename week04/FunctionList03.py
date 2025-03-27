capacity = 5 # 전역 변수
array = [None] * capacity # 전역 변수
size = 0 # 전역 변수 

def isFull():
    return size == capacity  # 비교 연산 결과를 바로 반환 

def insert(pos, e):
    global size  # size는 전역변수
    if not isFull() and 0 <= pos <= size:
        array[pos] = e
        size += 1  # 요소의 수가 하나 증가
    else:
        print("리스트 overflow 또는 유효하지 않은 삽입 위치")
        exit()

if __name__ == "__main__":
    print("초기 size 변수의 값은", size)
    print("초기 capacity 변수의 값은", capacity) 

    # insert함수 호출 1
    insert(0, 10)
    print("현재 size변수의 값은?", size)
    print("현재 size와 capacity의 값은 같은가?", isFull())
    print("현재 array", array[0:capacity])


    # insert함수 호출 2
    insert(0, 20)
    print("현재 size변수의 값은?", size)
    print("현재 size와 capacity의 값은 같은가?", isFull())
    print("현재 array", array[0:capacity])

    # insert함수 호출 3
    insert(1, 30)
    print("현재 size변수의 값은?", size)
    print("현재 size와 capacity의 값은 같은가?", isFull())
    print("현재 array", array[0:capacity]) 

    # insert함수 호출 4
    insert(2, 40)
    print("현재 size변수의 값은?", size)
    print("현재 size와 capacity의 값은 같은가?", isFull())
    print("현재 array", array[0:capacity]) 

    # insert함수 호출 5
    insert(3, 50)
    print("현재 size변수의 값은?", size)
    print("현재 size와 capacity의 값은 같은가?", isFull())
    print("현재 array", array[0:capacity])
