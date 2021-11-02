from hashlib import sha256

s = input('Enter something:\n')
print(sha256(s.encode('utf-8')).hexdigest())
