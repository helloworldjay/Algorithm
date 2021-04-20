immutable = 0
mutable = [1, 2, 3, 4, 5]


def func_without_parameter():
    if immutable == 0:  # 에러 발생
        print(immutable)
    mutable[0] = 2
    mutable[1] = 4
    # ...


def func_with_parameter(mutable, immutable):
    if immutable == 0:  # 함수 바깥에서 선언된 immutable과 관련없는 parameter 값
        print(1)
    mutable[0] = 2  #
    print(mutable)
    # ...
# func_with_parameter(mutable, immutable)
# print(mutable)

def func_for_assignment():
    mutable = [2, 4, 6, 8, 10]
func_for_assignment()
print(mutable)