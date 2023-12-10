input_file = open("input", 'r')
lines = input_file.readlines()

n = len(lines)

cards = [1 for _ in range(n)]

for i in range(n):
    card = lines[i]
    start = card.index(":")+2
    mid = card.index("|")

    winning = list(map(int, card[start:mid].split()))
    numbers = list(map(int, card[mid+1:].split()))

    matches = 0
    for num in numbers:
        if num in winning:
            matches += 1
    
    count = cards[i]
    for k in range(i+1, i+matches+1):
        cards[k] += count
    
print(sum(cards))
