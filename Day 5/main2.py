input_file = open("input", 'r')
lines = input_file.readlines()
n = len(lines)

# getting the seeds
seeds = list(map(int, lines[0][6:].split()))

min_location = 10000000000000

# format
# dest src length

def mapping(seed):
    transitions = [
        "seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
        "humidity-to-location"
    ]

    for s in transitions:
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
            dest, src, length = map(int, lines[ind].split())
            if seed >= src and seed < src+length:
                seed = dest + (seed - src)
                break
            ind+=1

    return seed

for i in range(0, len(seeds)-1, 2):
    start = seeds[i]
    end = seeds[i] + seeds[i+1]
    for seed in range(start, end+1):
        s = mapping(seed)
        if s < min_location:
            min_location = s


print(min_location)
