n = int(input ("Enter the number: "))
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

print(f'The factorial of {n} is {fact(n)}')
      