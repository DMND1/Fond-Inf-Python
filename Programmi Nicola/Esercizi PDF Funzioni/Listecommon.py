def commonlist(l,k):
    comune = False
    for i in (l):
        if i in k:
            comune = True

    return comune

l = [5,7,9,3,5]
k = [1,6,4,2,0]

print(commonlist(l,k))

        