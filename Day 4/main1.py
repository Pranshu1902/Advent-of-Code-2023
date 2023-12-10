input_file = open("input", 'r')
lines = input_file.readlines()

n = len(lines)

points = 0

for i in range(n):
    card = lines[i]
    start = card.index(":")+2
    mid = card.index("|")

    winning = list(map(int, card[start:mid].split()))
    numbers = list(map(int, card[mid+1:].split()))

    point = 0
    for num in numbers:
        if num in winning:
            if point>0:
                point *= 2
            else:
                point += 1
    
    points += point

print(points)
