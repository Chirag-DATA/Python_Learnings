print("****** Provide input for printing the fibonacci series ******")
n = int(input("Enter the number of terms: "))
print("The Series you want is: ")
if n == 1:
    print("1")
else:
    a = 0
    b = 1
    print(a, b,end = " ")
    for i in range(2,n):
        c = a+b
        a = b
        b = c
        print(c,end = " ")