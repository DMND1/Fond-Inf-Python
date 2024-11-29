quad = set()
cube = set()
i=1
while i**2 < 1000:
    num = i**2
    quad.add(num)
    i += 1

k = 1
while k**3 < 1000:
    numk = k**3
    cube.add(numk)
    k += 1

print(quad,"\n",cube)

