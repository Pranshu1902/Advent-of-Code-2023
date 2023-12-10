input_file = open("input1", 'r')
lines = input_file.readlines()

possible = 0
max_balls = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

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
    not_possible = False

    for f in fetches:
        all_balls = f.split(",")
        for ball in all_balls:
            ball = ball.split()
            count = int(ball[0])
            color = str(ball[1])

            if count > max_balls[color]:
                not_possible = True
                break
    
    if not not_possible:
        possible += game
    
print(possible)
