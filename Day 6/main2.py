input_file = open("input", 'r')
lines = input_file.readlines()

time = int(lines[0][6:].replace(" ", ""))
distance = int(lines[1][9:].replace(" ", ""))

ans = 1

count = 0
for t in range(1, time):
    charge = t
    dist = charge*(time-t)
    if dist > distance:
        count += 1
    
ans *= count

print(ans)
