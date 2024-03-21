#1924
x,y=map(int,input().split())

arr=[31,28,31,30,31,30,31,31,30,31,30,31,30]
week=['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
day=0
for i in range(x-1):
    day=day+arr[i]
day=(day+y)%7

print(week[day])

