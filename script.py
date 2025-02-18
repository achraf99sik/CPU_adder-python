a = 0
b = 0
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
        return [int(sum[0]),int(Carry)]
    else:
        return [int(sum[0]),int(Carry)]

def DecToBin(num):
    binary_8bit = list(format(num, '08b'))  # '08b' means 8-bit binary
    binary_8bit.reverse()
    return binary_8bit

def BinToDec(bin):
    return int(bin, 2)

# print(fullAdder(a, b, c))
a = DecToBin(int(input("enter first number: ")))
b = DecToBin(int(input("enter second number: ")))

res = []
cache = [halfAdder(a[0],b[0])]
res.insert(0,cache[0][0])
res.insert(0,fullAdder(a[1],b[1],cache[0][1])[0])
cache.append(fullAdder(a[1],b[1],cache[0][1]))
res.insert(0,fullAdder(a[2],b[2],cache[1][1])[0])
cache.append(fullAdder(a[2],b[2],cache[1][1]))
res.insert(0,fullAdder(a[3],b[3],cache[2][1])[0])
cache.append(fullAdder(a[3],b[3],cache[2][1]))
res.insert(0,fullAdder(a[4],b[4],cache[3][1])[0])
cache.append(fullAdder(a[4],b[4],cache[3][1]))
res.insert(0,fullAdder(a[5],b[5],cache[4][1])[0])
cache.append(fullAdder(a[5],b[5],cache[4][1]))
res.insert(0,fullAdder(a[6],b[6],cache[5][1])[0])
cache.append(fullAdder(a[6],b[6],cache[5][1]))
res.insert(0,fullAdder(a[7],b[7],cache[6][1])[0])
cache.append(fullAdder(a[7],b[7],cache[6][1]))
# def bitadder(bit=7):
#     for i in range(bit):
#         # print("res.insert(0,fullAdder(a["+str(i+1)+"],b["+str(i+1)+"],cache["+str(i)+"][1])[0])\ncache.append(fullAdder(a["+str(i+1)+"],b["+str(i+1)+"],cache["+str(i)+"][1]))")
#         res.insert(0,fullAdder(a[i+1],b[i+1],cache[i][1])[0])
#         cache.append(fullAdder(a[i+1],b[i+1],cache[i][1]))

# bitadder()


res = "".join(map(str,res))

print("\nresult in decimal:",BinToDec(res))
print("result in binary:",res)