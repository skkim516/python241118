# Demo.py
import sys
import timeit

# List와 Tuple 생성
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

# 변경 가능성 테스트
def test_mutability():
    try:
        my_list[0] = 10
        print("List는 변경 가능합니다:", my_list)
    except TypeError:
        print("List는 변경할 수 없습니다.")

    try:
        my_tuple[0] = 10
    except TypeError:
        print("Tuple은 변경할 수 없습니다.")

# 메모리 사용량 비교
def test_memory_usage():
    list_size = sys.getsizeof(my_list)
    tuple_size = sys.getsizeof(my_tuple)
    print(f"List 메모리 크기: {list_size} bytes")
    print(f"Tuple 메모리 크기: {tuple_size} bytes")

# 실행 속도 비교
def test_execution_speed():
    list_time = timeit.timeit("[1, 2, 3, 4, 5]", number=1000000)
    tuple_time = timeit.timeit("(1, 2, 3, 4, 5)", number=1000000)
    print(f"List 생성 속도: {list_time:.5f}초")
    print(f"Tuple 생성 속도: {tuple_time:.5f}초")

# 함수 실행
print("== 변경 가능성 테스트 ==")
test_mutability()
print("\n== 메모리 사용량 비교 ==")
test_memory_usage()
print("\n== 실행 속도 비교 ==")
test_execution_speed()

