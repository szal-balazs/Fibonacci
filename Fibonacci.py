def fibonacci(num):
    num1 = 0
    num2 = 1
    for i in range(num):
        yield num1
        num3 = num1 + num2
        num1 = num2
        num2 = num3


for x in fibonacci(10):
    print(x)
