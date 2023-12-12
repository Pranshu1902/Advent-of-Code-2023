from functools import cmp_to_key

input_file = open("input", 'r')
lines = input_file.readlines()

strength = {"A": 12, "K": 11, "Q": 10, "J": 9, "T": 8, "9": 7, "8": 6, "7": 5, "6": 4, "5": 3, "4": 2, "3": 1, "2": 0}

def categorizeType(d):
    # five of a kind
    if len(d.keys()) == 1:
        return 7 # highest
    
    # four of a kind
    if len(d.keys()) == 2 and max(d.values()) == 4:
        return 6
    
    # full house
    if len(d.keys()) == 2 and max(d.values()) == 3:
        return 5
    
    # three of a kind
    if len(d.keys()) == 3 and max(d.values()) == 3:
        return 4

    # two pair
    if len(d.keys()) == 3 and list(d.values()).count(2) == 2:
        return 3

    # one pair
    if len(d.keys()) == 4 and max(d.values()) == 2:
        return 2
    
    # high card
    if len(d.keys()) == 5:
        return 1

def cardCompare(a, b):
    for i in range(5):
        if strength[a[i]] > strength[b[i]]:
            return 1
        elif strength[a[i]] < strength[b[i]]:
            return -1
    
    return 0

def compare(a, b):
    d_a = {}
    d_b = {}

    for i in a:
        if i in d_a.keys():
            d_a[i] += 1
        else:
            d_a[i] = 1
    
    for i in b:
        if i in d_b.keys():
            d_b[i] += 1
        else:
            d_b[i] = 1
    
    type_a = categorizeType(d_a)
    type_b = categorizeType(d_b)

    if type_a > type_b:
        return 1
    elif type_a < type_b:
        return -1
    else:
        return cardCompare(a, b)

def sortCards(cards):
    # sort the cards but use the custom compare method declared above
    sorted_cards = sorted(cards, key=cmp_to_key(compare))
    return sorted_cards

def calculateBid(cards, bid):
    cards = sortCards(cards)
    totalBid = 0
    for i in range(len(cards)):
        totalBid += (i+1) * bid[cards[i]]
    
    return totalBid

bids = {}
cards = []

for line in lines:
    data = line.split()
    cards.append(data[0])
    bids[data[0]] = int(data[1])

output = calculateBid(cards, bids)
print(output)
