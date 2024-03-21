# 2869
a, b, v = input().split()
a, b, v = int(a), int(b), int(v)
d=int((v-a)/(a-b))
if (v-a)%(a-b)==0:
    print(d+1)
else:
    print(d+2)




# s = 0
# d = 0
# while 1:
#     d += 1
#     s += int(a) #낮에 올라가는즁
#     if s >= int(v): #만약 낮에 올라가는중에 목표에 도달하면 그만 멈추기
#         break
#     s -= int(b) #밤에 내려가는즁
#
# print(d)
