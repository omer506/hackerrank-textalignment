a=int(input("Enter : "))
c=-1
d=-1
for i in range(0,a):
    d = d + 2
for i in range(0,a):
    c = c + 2
    print(("H"*c).center(d," "))


for i in range(0,a):
    b=('H'*a)
    b1=(a*5)-(2*a)-(int((c-a)/2))+a-1
    print(b.center(c,' '),b.rjust(b1,' '))

for i in range(0,a):
   print(('H'*(a*5)).center((a*5)+(c-a),' '))

for i in range(0,a):
    b=('H'*a)
    b1=(a*5)-(2*a)-(int((c-a)/2))+a-1
    print(b.center(c,' '),b.rjust(b1,' '))

d=d+2
d1=(a*5)+(2*a)+(c-a)+(2*a)
for i in range(0,a):
    d = d - 2
    print(("H"*d).center(d1," "))