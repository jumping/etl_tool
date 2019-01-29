import os


def randomString(n):
    return (''.join(map(lambda xx: (hex(ord(xx))[2:]), os.urandom(n))))[0:16]


def random_string(length=8):
    return ''.join(map(lambda x: hex(x)[2:], os.urandom(length // 2)))


print(random_string())