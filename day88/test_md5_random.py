import hashlib
import random
import string


def gen_random_string(str_len):
    return ''.join(
        random.choice(string.ascii_letters + string.digits) for _ in range(str_len))


def gen_md5(*args):
    return hashlib.md5("".join(args).encode('utf-8')).hexdigest()


print(gen_random_string(8))
print(gen_md5("admin"))

