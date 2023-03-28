
def strcmp(*args):
    for i in range(min(len(s), len(t))):
        if ord(args[0][i])>ord(args[1][i]):
            return 1
        elif ord(args[0][i])==ord(args[1][i]):
            continue
        else:
            return -1
    if len(s)==len(t):
        return 0
    else:
        return -1

s=input('첫번째 문자열 입력: ')
t=input('두번째 문자열 입력: ')

result=strcmp(s,t)
print(result)
