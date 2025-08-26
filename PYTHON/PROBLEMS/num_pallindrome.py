#Pallindrome Number --> reverse and number are both same
# example {121}, {131},etc..

n = int(input("Enter the number to check: "))
temp = n
rev = 0
while n > 0:
    dig = n%10
    rev = rev * 10 + dig
    n = n//10
if rev == temp:
    print("Number is Pallindrome")
else:
    print("Not a pallindrome number")


    