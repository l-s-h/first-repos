class Compare:
    
    def __init__(self,a,b):
        self.s=a
        self.t=b
    def cmp(self):
        pass

class Strcmp(Compare):
    
    def __init__(self,x,y):
        super().__init__(x,y)
        
    def cmp(self):
        
        for i in range(min(len(self.s), len(self.t))):
            if ord(self.s[i])>ord(self.t[i]):
                return 1
            elif ord(self.s[i])==ord(self.t[i]):
                continue
            else:
                return -1
            
        if len(self.s)==len(self.t):
            return 0
        elif len(self.s)>len(self.t):
            return 1
        else:
            return -1
        
class Numcmp(Compare):
    
    def __init__(self,w,z):
        super().__init__(w,z)
        
    def cmp(self):
        if float(self.s)>float(self.t):
            return 1
        elif float(self.s)==float(self.t):
            return 0
        else:
            return -1
            

        

s=input("첫번째 문자열 입력: ")
t=input("두번째 문자열 입력: ")

NUM, CHARCT=1,2
cond=NUM
        
for i in range(len(s)):
    c=s[i]
    if i==0 and c=='-':
        continue
    if c.isdigit() or c=='.':
        continue
    else:
        cond=CHARCT
        break

if cond==NUM:
    for i in range(len(t)):
        c=t[i]
        if i==0 and c=='-':
            continue
        if c.isdigit() or c=='.':
            continue
        else:
            cond=CHARCT
            break

if cond==NUM:
    p=Numcmp(s,t)
else:
    p=Strcmp(s,t)


print(p.cmp())

