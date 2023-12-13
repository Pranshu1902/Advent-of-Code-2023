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


steps = 0

current = "AAA"

while current != "ZZZ":
    for i in instruction:
        current = data[current][i]
    
    steps += 1

print(steps * len(instruction))
