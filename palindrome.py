x = str(input())
t = x.lower()
print(['no', 'yes'][t == t[::-1]])