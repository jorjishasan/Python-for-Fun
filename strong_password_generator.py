
import random
import string

def get_password(length):
    pass_char=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(pass_char) for i in range(length))
    print(f'Your password is: {password}')
get_password(10)