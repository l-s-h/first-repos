import sys # 강제종료 할라고

s=input('16진수를 입력하시오\n')

value=0 #이전값
v=0 #c가 숫자됨

for c in s: # 일일이 메모리에 접근해서 숫자 만들고 이전값에 16곱한 거에 더해가는 함수
    if (c>='0' and c<='9'):
        v=int(c)
    elif (c>='A' and c<='F'):
        v=ord(c)-ord('A')+10
    else:
        print('16진수가 아닙니다.')
        sys.exit(0)
    value=value*16+v

print('16진수 {0} 은 10진수 {1} 입니다.'.format(s, value))
