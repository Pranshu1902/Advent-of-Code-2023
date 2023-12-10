input_file = open("sample", 'r')
lines = input_file.readlines()
n = len(lines)

# getting the seeds
mapped_data = list(map(int, lines[0][6:].split()))

# format
# dest src length

def mapping(s):
    # find start row
    ind = -1
    for l in range(n):
        if s in lines[l]:
            ind = l+1
            break
    
    d = {}
    ranges = []
    while ind<len(lines) and lines[ind] != "\n":
        # extract
        data = list(map(int, lines[ind].split()))
        ranges.append(data)
        # for i in range(length):
        #     d[src+i] = dest+i

        ind+=1
    
    for i in range(len(mapped_data)):
        for dest, src, length in ranges:
            if mapped_data[i] >= src and mapped_data[i] < src+length:
                mapped_data[i] = dest + (mapped_data[i] - src)
                break

        # if mapped_data[i] in d.keys():
        #     mapped_data[i] = d[mapped_data[i]]

transitions = [
    "seed-to-soil",
    "soil-to-fertilizer",
    "fertilizer-to-water",
    "water-to-light",
    "light-to-temperature",
    "temperature-to-humidity",
    "humidity-to-location"
]

for t in transitions:
    mapping(t)

print(min(mapped_data))
