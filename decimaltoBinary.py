a = int(input("Enter Number : "))

l = []

while(a > 0):
    rem = a % 2
    l.append(rem)
    a //=2

l.reverse()
for i in l:
    print(i,end =" ")
