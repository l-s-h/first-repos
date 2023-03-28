num=int(input('number 입력:'))
n=int(input('n 입력:'))

check=0x8000000000000000

i=0
num1=num

while (i<64):
    if (num1 & check) == 0:
        print('0', end='')
    else:
        print('1', end='')
    num1=num1<<1
        
    i+=1

print()

i=0
check1=1
check2=0x7FFFFFFFFFFFFFFF
    
    
while (i<n):
    if (num & check1) == 0:
        if (num>=0):
            num=num>>1
        else:
            num=num>>1
            num=num&check2
    else:
        if (num>=0):
            num=num>>1
            num=num|check
        else:
            num=num>>1
        
    i+=1


i=0

while (i<64):
    if (num & check) == 0:
        print('0', end='')
    else:
        print('1', end='')
    num=num<<1
        
    i+=1

    
