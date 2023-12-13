import math

input_file = open("input", 'r')
lines = input_file.readlines()

# instruction
instruction = str(lines[0].strip())

# convert data to hash-map
data = {}

for line in lines[2:]:
    start = str(line[:4].strip())

    left = str(line[7:10])
    right = str(line[12:15])

    data[start] = {"L": left, "R": right}

current = []

for nodes in data.keys():
    if nodes[-1] == "A":
        current.append(nodes)

steps = []
for c in current:
    step_s = 0
    while c[-1]!="Z":
        for j in instruction:
            c = data[c][j]
        step_s += 1
    steps.append(step_s * len(instruction))

ans = 1
for i in steps:
    ans = math.lcm(ans, i)

print(ans)
