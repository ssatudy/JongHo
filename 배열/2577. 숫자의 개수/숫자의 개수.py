A = int(input())
B = int(input())
C = int(input())

D = list(str(A * B * C))
print(D.count('0'))
for i in range(1, 10):  
    print(D.count(str(i)))
