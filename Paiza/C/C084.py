S = str(input())

def headerAndFooter(S):
    for i in range(len(S) + 2):
        print('+', end='')
    print()
    print(f'+{S}+')
    for i in range(len(S) + 2):
        print('+', end='')

headerAndFooter(S)