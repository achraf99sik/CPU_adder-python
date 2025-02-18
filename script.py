def halfAdder(a, b):
    a = int(a)
    b = int(b)
    SUM = ((a and not(b)) or (not(a) and b))
    Carry = a and b
    if SUM:
        return [int(SUM),int(Carry)]
    else:
        return [int(SUM),int(Carry)]

def fullAdder(a, b , c):
    a = halfAdder(a, b)
    sum = halfAdder(a[0], c)
    Carry = a[1] or sum[1]
    if not(sum) and Carry:
        return [int(sum[0]),int(Carry)]
    else:
        return [int(sum[0]),int(Carry)]

bits = int(input("how many bits it's in your number: "))
def DecToBin(num):
    binary = list(format(num, '0'+str(bits)+'b'))
    binary.reverse()
    return binary

def BinToDec(bin):
    return int(bin, 2)

a = DecToBin(int(input("enter first number: ")))
b = DecToBin(int(input("enter second number: ")))

res = []
cache = [halfAdder(a[0],b[0])]
print("cache 0:",cache)
res.insert(0,cache[0][0])

def bitadder(bit):
    for i in range(bit):
        # print("res.insert(0,fullAdder(a["+str(i+1)+"],b["+str(i+1)+"],cache["+str(i)+"][1])[0])\ncache.append(fullAdder(a["+str(i+1)+"],b["+str(i+1)+"],cache["+str(i)+"][1]))")
        res.insert(0,fullAdder(a[i+1],b[i+1],cache[i][1])[0])
        cache.append(fullAdder(a[i+1],b[i+1],cache[i][1]))

bitadder(bits-1)

res = "".join(map(str,res))

print("\nresult in decimal:",BinToDec(res))
print("result in binary:",res)