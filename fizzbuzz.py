def fizz_buzz():
    upper = int(input())

    for num in range(1, upper + 1):
        if num % 15 == 0:
            print("Fizz Buzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

result = fizz_buzz()
print(result)