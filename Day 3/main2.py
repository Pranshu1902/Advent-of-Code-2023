input_file = open("input", 'r')
lines = input_file.readlines()

rows = len(lines)
columns = len(lines[0])-1

row_index = 0
column_index = 0

ans = 0

def extractNumber(row, col):
    left = col
    right = col

    # traverse in both directions
    while left>=0 and lines[row][left].isnumeric():
        left -= 1
    
    while right<rows and lines[row][right].isnumeric():
        right += 1
    
    # check if we went 1 step extra
    if not lines[row][left].isnumeric():
        left += 1
    if not lines[row][right].isnumeric():
        right -= 1
    
    number = int(lines[row][left:right+1])
    return number


for row_index in range(rows):
    for column_index in range(columns):
        if lines[row_index][column_index] == "*":
            numbers = []
            # top left
            if row_index-1>=0 and column_index-1>=0:
                if lines[row_index-1][column_index-1].isnumeric():
                    num = extractNumber(row_index-1, column_index-1)
                    if num not in numbers:
                        numbers.append(num)
            
            # top
            if row_index-1>=0:
                if lines[row_index-1][column_index].isnumeric():
                    num = extractNumber(row_index-1, column_index)
                    if num not in numbers:
                        numbers.append(num)
            
            # top right
            if row_index-1>=0 and column_index+1<columns:
                if lines[row_index-1][column_index+1].isnumeric():
                    num = extractNumber(row_index-1, column_index+1)
                    if num not in numbers:
                        numbers.append(num)
            
            # left
            if column_index-1>=0:
                if lines[row_index][column_index-1].isnumeric():
                    num = extractNumber(row_index, column_index-1)
                    if num not in numbers:
                        numbers.append(num)
            
            # left
            if column_index+1<columns:
                if lines[row_index][column_index+1].isnumeric():
                    num = extractNumber(row_index, column_index+1)
                    if num not in numbers:
                        numbers.append(num)
            
            # bottom left
            if row_index+1<rows and column_index-1>=0:
                if lines[row_index+1][column_index-1].isnumeric():
                    num = extractNumber(row_index+1, column_index-1)
                    if num not in numbers:
                        numbers.append(num)
            
            # bottom
            if row_index+1<rows:
                if lines[row_index+1][column_index].isnumeric():
                    num = extractNumber(row_index+1, column_index)
                    if num not in numbers:
                        numbers.append(num)

            # bottom right
            if row_index+1<rows and column_index+1<columns:
                if lines[row_index+1][column_index+1].isnumeric():
                    num = extractNumber(row_index+1, column_index+1)
                    if num not in numbers:
                        numbers.append(num)

            # compute gear ration
            if len(numbers)==2:
                print(numbers)
                gear = numbers[0] * numbers[1]
                print(gear)
                print()
                ans += gear


print(ans)

# 82914378- too low
