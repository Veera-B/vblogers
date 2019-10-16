import random
import string

def rand_str_generator(size=10,chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

#print(rand_str_generator())
#print(rand_str_generator(40))
