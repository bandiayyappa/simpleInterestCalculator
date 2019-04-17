#  interest calculator

while True:
    p = input('enter Principal amount ')
    if not p.isdigit():
        print('value Error:\n\t\t Amount should be numbers only ')
        continue
    break

while True:
    t = input('enter number of years ')
    if not t.isdigit():
        print('value Error:\n\t\t Years should be numbers only ')
        continue
    break

while True:
    r = input('enter rate of interest in Rs for every 100Rs ')
    if not r.isdigit():
        print('value Error:\n\t\t Rate should be numbers only')
        continue
    break
p = int(p)
t = int(t)
r = int(r)
print('Interest = ',((p*t*r)/100))
