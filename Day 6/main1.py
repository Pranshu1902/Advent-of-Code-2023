input_file = open("input", 'r')
lines = input_file.readlines()

times = list(map(int, lines[0][6:].split()))
distances = list(map(int, lines[1][9:].split()))

n = len(times)

ans = 1

for i in range(n):
    time = times[i]
    count = 0
    for t in range(1, time):
        charge = t
        dist = charge*(time-t)
        if dist > distances[i]:
            count += 1
    
    ans *= count

print(ans)
