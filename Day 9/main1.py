input_file = open("input", 'r')
lines = input_file.readlines()

ans = 0

def predictNext(arr):
    temp = []
    temp.append(arr)
    
    while len(set(temp[-1])) != 1 or temp[-1][0] != 0:
        diff = []
        for i in range(1, len(temp[-1])):
            diff.append(temp[-1][i] - temp[-1][i-1])
        
        temp.append(diff)
    
    while len(temp) != 1:
        difference = temp[-1][-1]
        temp[-2].append(temp[-2][-1] + difference)

        temp.pop(-1)

    return temp[0][-1]

for line in lines:
    arr = list(map(int, line.split()))
    ans += predictNext(arr)

print(ans)
