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