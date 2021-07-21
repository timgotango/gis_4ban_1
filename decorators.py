# 데코레이터 Decorator

def decorator(func):
    def decorated(input_text):
        print('함수 시작!')
        func(input_text)
        print('함수 끝!')
    return decorated    # ()로 호출하면 안됨

@decorator
def hello_world(input_text):
    print(input_text)

hello_world('Hello World')

# 삼각형 / 사각형 넓이 계산 함수
# 입력값이 모두 양수인지 확인하고, 아닐 경우 Error 발생시키는 Decorator 작성 및 적용
@decorator
def triangle(height, width):
    return height * width / 2

@decorator
def rectangle(height, width):
    return height * width

def decorator(func):
    def decorated(height, width):
        if height > 0 and height > 0:
            return func(height, width)
        else:
            raise ValueError('양수를 입력하시오')
    return decorated

print(triangle(2,3))


# User 클래스 작성
# User 클래스 내 is_authenticated 변수 작성
# User 객체를 넓이 함수 인자로 전달
# is_authenticated 변수 확인하고 True 아닐 경우 Error 발생

