import re

if True:
    with open("input.txt") as f:
        text = f.read().strip()
    w = 101
    h = 103
    t = 7623
else:
    text = """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
""".strip()
    w = 11
    h = 7
    t = 100

def render(robots):
    grid = [[' '] * w for _ in range(h)]
    for x, y in robots:
        grid[y][x] = '#'
    return '\n'.join(''.join(line) for line in grid)

def pprint(robots):
    print(render(robots))

quadrent_counts = [[0, 0], [0, 0]]
half_w = w // 2
half_h = h // 2
end_coords = []
robot_positions = []
robot_velocities = []
for line in text.split('\n'):
    px, py, vx, vy = map(int, re.findall(r'-?\d+', line))
    robot_positions.append([px, py])
    robot_velocities.append([vx, vy])

for i in range(1, t+1):
    for pos, vel in zip(robot_positions, robot_velocities):
        pos[0] += vel[0]
        pos[1] += vel[1]
        pos[0] %= w
        pos[1] %= h
    print(f"======== {i} ========")
    pprint(robot_positions)