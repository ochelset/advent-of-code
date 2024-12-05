target_area = [70, -179, 96, -124]
#target_area = [20, -10, 30, -5]

def calc(start, v):
    nx = start[0] + v[0]
    ny = start[1] + v[1]
    d = -1 if v[0] > 0 else 1 if v[0] < 0 else 0
    v = (v[0] + d, v[1]-1)
    return (nx, ny), v

def is_inside(pos):
    return pos[0] >= target_area[0] and pos[0] <= target_area[2] and pos[1] >= target_area[1] and pos[1] <= target_area[3]

top = 0
possibles = set()

for vx in range(1, 200):
    for vy in range(-200, 200):
        velocity = (vx, vy)
        probe = (0, 0)
        inside = False
        current_top = 0
        for n in range(400):
            probe, velocity = calc(probe, velocity)
            ahead, _ = calc(probe, velocity)

            if probe[1] > current_top or ahead[1] > current_top:
                current_top = max(probe[1], ahead[1])

            if is_inside(probe) or is_inside(ahead):
                inside = True
                break

        if inside:
            if current_top > top:
                top = current_top
            possibles.add((vx, vy))

print("Part 1:", top)
print("Part 2:", len(possibles))
