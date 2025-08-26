def pass_check(pas):
    if len(pas) < 8:
        return ("WEAK PASSWORD...")
    if not any(ch.islower() for ch in pas):
        return ("WEAK PASSWORD...")
    if not any(ch.isupper() for ch in pas):
        return ("WEAK PASSWORD...")
    if not any(ch.isdigit() for ch in pas):
        return ("WEAK PASSWORD...")
    if not any(i in "!@#$%^&*" for i in pas):
        return ("WEAK PASSWORD...")
    
    return ("PASSWORD IS STRONG...")

print(pass_check("Password"))
print(pass_check("@Password"))
print(pass_check("Password@123"))