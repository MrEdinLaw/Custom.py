import hashlib
from itertools import chain, product

# get the hash to compare to
password = input('paste your hash: ')
attempts = 0
def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, maxlength + 1)))
	
for attempt in bruteforce("abcdefghijklmnopqrstuvwxyz1234567890", 5):
    a = bytes(attempt, encoding="utf-8")
    b = hashlib.md5(a).hexdigest()
    if b == password:
        print(attempt)
        print("Attempts made: ",attempts)
        break
    else:
        attempts +=1
        if(attempts % 100 == 0):
            print("Checkpoint attempts: ",attempts)
