a = 23891471923807487.142352314353455
b = 23891471923807487.142352314356734
c = 23891471923843245.142352314334563
d = 23891471923843245.142352314334553

aa = 2
bb = 3
cc = 2
dd = 3

aaa = 3
bbb = 2
ccc = 3
ddd = 2
def f(a,b,c,d):
    if (a + c) > (b + d):
        print("true", (a + c), ">", (b + d))
    else:
        print("False", (a + c), "<", (b + d))
    return 0

print(f(a,b,c,d))
print(f(aa,bb,cc,dd))
print(f(aaa,bbb,ccc,ddd))