#1914
def hanoi (n, start ,destination,sub,count):

    if n ==1:
        if n <= 20:
            print(start,destination)
        return
    hanoi(n-1,start,sub,destination)
    count+1
    if n <= 20:
        print(start,destination)
    hanoi(n-1,sub,destination,start)
    count+1

print(hanoi(int(input()),1,3,2))