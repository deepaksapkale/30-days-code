N = int(input())

for i in range(0, N):

    S = input()

    for i in range(0, len(S)):
        if i % 2 == 0:
            print(S[i] + ' ')

    print(" ", end='')

    for i in range(0, len(S)):
        if i % 2 != 0:
            print(S[i]+ ' ')

    print("")