import re
def mail_validate(mail):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern,mail) is not None

print(mail_validate('test@gmail.com'))
print(mail_validate('testmail.com'))