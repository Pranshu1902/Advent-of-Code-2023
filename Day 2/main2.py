input_file = open("input1", 'r')
lines = input_file.readlines()

sumOfPowerSets = 0

for l in range(len(lines)):
    line = lines[l]
    game = l+1

    line = line[line.index(":")+1:]

    fetches = line.split(";")
    d = {
        "red": 0,
        "blue": 0,
        "green": 0
    }

    for f in fetches:
        all_balls = f.split(",")
        for ball in all_balls:
            ball = ball.split()
            count = int(ball[0])
            color = str(ball[1])

            if count > d[color]:
                d[color] = count

    sumOfPowerSets += d["blue"] * d["green"] * d["red"]    
    
print(sumOfPowerSets)
