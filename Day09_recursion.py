def factorial(number):
    if number <=1:
        return 1
    else:
        return factorial(number - 1) * number
answer = factorial(int(input()))
print(answer)
