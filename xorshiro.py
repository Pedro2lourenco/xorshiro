import os

def seed_gen():

    seed0 = int.from_bytes(os.urandom(8),byteorder='big')
    seed1 = int.from_bytes(os.urandom(8),byteorder='big')

    if seed0 == 0 and seed1 == 1:
        return seed_gen

    return seed0,seed1

s1,s0 = seed_gen()


def rotl(x, k):
    return ((x << k) & 0xFFFFFFFFFFFFFFFF) | (x >> (64 - k))

def next_xorshiro():
    global s0, s1
    
    result = (s0 + s1) & 0xFFFFFFFFFFFFFFFF
    
    s1 ^= s0
    s0 = (rotl(s0, 55) ^ s1 ^ (s1 << 14)) & 0xFFFFFFFFFFFFFFFF
    s1 = rotl(s1, 36)
    
    return result

def rand_uniform():
    return (next_xorshiro() >> 11) / (1 << 53)

print(rand_uniform())