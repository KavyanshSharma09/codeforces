total = int(input())
res = []
for i in range(total):
    st = str(input())
    res.append(st)
temp = 0
for i in res:
    if i == "Tetrahedron":
        temp += 4
    if i == "Cube":
            temp += 6
    if i == "Octahedron":
            temp += 8
    if i == "Dodecahedron":
            temp += 12
    if i == "Icosahedron":
            temp += 20
print(temp)

