a = 0
b = 1
c = 0
def halfAdder(a, b):
    SUM = ((a and not(b)) or (not(a) and b))
    Carry = a and b
    if not(SUM) and Carry:
        return [int(SUM),int(Carry)]
    else:
        return [int(SUM),int(Carry)]

def fullAdder(a, b , c):
    a = halfAdder(a, b)
    sum = halfAdder(a[0], c)
    Carry = a[1] or sum[1]
    if not(sum) and Carry:
        return str(int(Carry))+str(int(sum))
    else:
        return str(int(Carry))+str(int(sum[0]))

print(fullAdder(a, b, c))