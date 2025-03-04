s = list(map(int, input()))

duplication_num = len(set(s))

if duplication_num == len(s):
    print('OK')
else:
    print('NG')