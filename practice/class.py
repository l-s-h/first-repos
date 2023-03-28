hour = int(input("시 입력"))
min = int(input("분 입력"))
sec = int(input("초 입력"))


class Time:
    result=0
    
    def __init__(self,hour,min,sec,day=0):
        self.hour=hour
        self.min=min
        self.sec=sec
        self.day=day

    def __sub__(self,other):
        
        self_total=self.hour*3600+self.min*60+self.sec
        other_total=other.hour*3600+other.min*60+other.sec

        total=(self_total-other_total)

        max=86400
        
        if total<0:
            total=total+max
            self.day=-1
        
        hour=total//3600
        total=total%3600
        min=total//60
        total=total%60
        sec=total

        return Time(hour,min,sec,self.day)
    
    def __add__(self,other):
        
        self_total=self.hour*3600+self.min*60+self.sec
        other_total=other.hour*3600+other.min*60+other.sec

        total=(self_total+other_total)

        max=86400
        
        if total>=max:
            total=total-max
            self.day=1
        
        hour=total//3600
        total=total%3600
        min=total//60
        total=total%60
        sec=total

        return Time(hour,min,sec,self.day)

    def __repr__(self):
        
        return str(self.day)+"일 "+str(self.hour)+"시 "+str(self.min)+"분 "+str(self.sec)+"초 입니다"
    
    def __lt__(self,other):
        
        return self.sec-other.sec<0
    
    def __eq__(self,other):
        
        return self.sec-other.sec==0
    
    def __gt__(self,other):
        return self.sec-other.sec>0
    



first_time = Time(10, 10, 10)
second_time = Time(hour, min, sec)


add_time = first_time + second_time
sub_time = first_time - second_time

print("두 시간의 합은")
print(add_time)

print("두 시간의 차는")
print(sub_time)


if (first_time > second_time):
    print("첫번째 시간이 늦은 시간입니다")
    
if (first_time < second_time):
    print("첫번째 시간이 이른 시간입니다")
    
if (first_time == second_time):
    print("두 시간이 같은 시간입니다")
    
