#1629

# A를 B번 곱하고 이를 C로 나눈 나머지
A,B,C=map(int,input().split())


def dc(a,b,c):
    if b==1:
        return a%c
    elif b % 2 == 0:
        return (dc(a,b//2,c)**2 )%c
    else:
        return ((dc(a,b//2,c)**2)*a)%c
print(dc(A,B,C))