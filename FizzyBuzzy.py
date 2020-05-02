"""
In the game Fizz Buzz, players take turns counting up from one. If a player’s turn lands on a number that’s
divisible by 3, she should say fizz instead of the number, and if it lands on a number that’s divisible by 5,
she should say buzz instead of the number. If the number is both a multiple of 3 and of 5, she should say
fizzbuzz instead of the number.
"""



def main():
    n = int(input("Number to count to: "))
    x = n - n + 1
    for i in range(n):
        x = Fizz_Buzz(x)
        print(x)
        x = x + 1
        x = Fizz_Buzz(x)

def Fizz_Buzz(x):
    if (x % 3 == 0 and x % 5 == 0):
        print("Fizzbuzz")
        x = (x - 1) + 2
    elif (x % 3 == 0):
        print("Fizz")
        x = (x - 1) + 2
    elif (x % 5 == 0):
        print("Buzz")
        x = (x - 1) + 2
    return x


if __name__ == '__main__':
    main()