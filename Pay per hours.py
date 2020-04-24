hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate per hour:")
r = float(rate)
if h<=40:
    pay = h * r
    print(pay)
else :
    pay1 = 40 * r
    x = h - 40
    r = r * 1.5
    pay2 = x * r
    pay = pay1 + pay2
    print(pay)
