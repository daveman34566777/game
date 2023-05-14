print('word')
b=input()
print('word')
c=input()
print('word')
d=input()
a=[b,c,d]
f=0

for e in range(0,9,1):
    g=f+1
    print(a[f,g])
    g=g+1
    if g==2:
        f=1
        g=0
    if g==1 and f==1:
        g=2
    if g==2 and f==1:
        g=3
        f=2
        




