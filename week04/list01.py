# 배열과 크기 정의
array = []  # 빈 리스트로 시작
size = 0     # 초기 크기 0

def insert(position, value):
    global size
    array.insert(position, value)
    size += 1

def delete(position):
    global size
    if 0 <= position < size:
        array.pop(position)
        size -= 1

if __name__ == "__main__":
    print("최초       ", array[0:size])
    insert(0, 10)
    insert(0, 20)
    insert(1, 30)
    insert(size, 40)
    insert(2, 50)
    print("삽입x5     ", array[0:size])
    delete(2)
    print("삭제(2)    ", array[0:size])
    delete(3)
    print("삭제(3)    ", array[0:size])
    delete(0)
    print("삭제(0)    ", array[0:size])