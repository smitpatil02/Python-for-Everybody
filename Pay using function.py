def computepay(h,r):
    h = int(h)
    r = float(r)
    if h<=40:
        pay=h*r
        return pay
    else:
        a=40*r
        r=r*1.5
        h=h-40
        b=h*r
        pay=a+b
        return pay


hrs = input("Enter Hours:")
rate = input("Enter Rate:")
p = computepay(hrs,rate)
print(p)
