def check_palindrome(st):
    st = st.lower().replace(" ","")
    if st == st[::-1]:
        print("Yes it is a palindrome string")
    else:
        print("No, it is not a palindromestring")
check_palindrome("A man a pan a panama")
check_palindrome("a man is in jungle")
