a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
def greatest(a,b,c):
    if a == b == c:
        return ("All the numbers are equal")
    else:
        if (a > b) and (a > c):
            return (f'{a} is the greatest number')
        elif (b > a) and (b > c):
            return (f'{b} is the greatest number')
        else:
            return (f'{c} is the greatest number')

print(greatest(a,b,c))