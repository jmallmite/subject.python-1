capacity = 10                    # 전역 변수
array = [None]*capacity          # 전역 변수
size = 0                         # 전역 변수

# 리스트의 연산: 일반 함수
def isFull():
    return size == capacity  # 비교 연산 결과를 바로 반환

# 프로그램의 시작
if __name__ == "__main__":
    print("현재 size 변수의 값은 ? ", size)   
    print("현재 capacity 변수의 값은 ? ", capacity)   
    print("현재의 size와 capacity의 값은 같은가?", isFull())