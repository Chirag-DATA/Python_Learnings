a = input("Enter any letter from alphabets to check: ")
b = a.lower()
if b in "aeiou":
    print(f'{a} is an Vowel')
else:
    print(f'{a} is not an Vowel')