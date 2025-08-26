print("**** Provide number to check if it is prime")
n = int(input("Enter any number: "))

if n <= 1:
    print("Not Prime")
else:
    count = 0
    for i in range(2,n):
        if n%i == 0:
            count += 1
            break
        else:
            pass
    if count == 0:
        print("Prime Number")
    else:
        print("Not a prime number")


    
