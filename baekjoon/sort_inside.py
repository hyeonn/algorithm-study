num = list(map(int, list(input())))
s = list(map(str, sorted(num, reverse=True)))
print(''.join(s))