ans = 0
d = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
dr = {'eno': '1', 'owt': '2', 'eerht': '3', 'ruof': '4', 'evif': '5', 'xis': '6', 'neves': '7', 'thgie': '8', 'enin': '9'}

input_file = open("input", 'r')
lines = input_file.readlines()
for line in lines:
# for i in range(1):
    # line = "4nine9twooneeightwoz"
    start = 0
    end = 0

    index = 1000000
    val = ""
    for n in d.keys():
        if n in line and line.index(n)<index:
            index = line.index(n)
            val = d[n]
    start = val
    for i in range(index):
        if line[i].isnumeric():
            start = str(line[i])
            break

    index = -1
    val = ""
    liner = line[::-1]
    for n in dr.keys():
        if n in liner and liner.index(n)>index:
            # print(n)
            ind = liner.index(n)
            # ind = index

            # while n in liner[ind+1:] and ind<=len(liner)-1:
            #     # print(n)
            #     # print(ind)
            #     # print(line[ind+1:])
            #     ind += liner[ind+1:].index(n) + len(n)
            # if ind>index:
            index = ind
            val = dr[n]
    end = val
    index = len(line)-index-1
    for i in range(len(line)-1, index, -1):
        if line[i].isnumeric():
            end = str(line[i])
            break
    print(line)
    print(start, end)
    num = int(start+end)
    print(num)
    print()
    ans += num

print(ans)
