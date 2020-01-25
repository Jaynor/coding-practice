def fizzbuzz(input):
    for i in range(input):
        if (i % 3 or i % 5) == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


def main():
    fizzbuzz(100)

main()
