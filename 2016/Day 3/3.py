triangles = open("input.data").read().strip().splitlines()

def is_valid(triangle):
    a, b, c = triangle
    if a + b > c and a + c > b and b + c > a:
        return True
    return False

valid_triangles = []
for triangle in triangles:
    t = (int(x) for x in triangle.strip().replace("   ", " ").replace("  ", " ").split(" "))
    if is_valid(t):
        valid_triangles.append(t)

print("Part 1:", len(valid_triangles))

valid_triangles = []
for col in range(3):
    row = []
    for i in range(len(triangles)):
        r1 = triangles[i].strip().replace("   ", " ").replace("  ", " ").split(" ")
        row.append(int(r1[col]))

    for i in range(2, len(triangles), 3):
        t = (row[i-2], row[i-1], row[i])
        if is_valid(t):
            valid_triangles.append(t)

print("Part 2:", len(valid_triangles))
