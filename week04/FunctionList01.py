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

#capacity 라는 변수에 10을 저장하고
#array라는 변수에 [None]*capacity를 하면 리스트에 None이 10개가 들어가게 된다
#size = 0 은 size라는 변구에 0이 저장된다
#def 가 isfull 이 함수 임을 정의하고 ()안에 매게변수(입력값)가 없기 때문에 return을 통해서 size == capacity의 결과를 반환한다.
#
