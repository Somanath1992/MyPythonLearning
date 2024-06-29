# Program to find out given number is prime number or not
# Prime numbers are natural numbers that are divisible by only 1 and the number itself
def prime_number(num):
    count = 0
    if num > 1:
        for i in range(1, num + 1):
            if num % i == 0:
                count = count + 1
    if count == 2:
        print(num, "is prime number")
    else:
        print(num, "is not prime number")


number = int(input("Enter value of number:"))
prime_number(number)
