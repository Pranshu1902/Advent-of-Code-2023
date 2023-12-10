input_file = open("input", 'r')
lines = input_file.readlines()

rows = len(lines)
columns = len(lines[0])-1

symbols = ""
row_index = 0
column_index = 0

ans = 0

def checkSpecificSymbol(val):
    if not val.isalnum() and val != ".":
        return True
    return False

def searchSymbol(lines, start, end):
    # check left
    if start[1] > 0 and checkSpecificSymbol(lines[start[0]][start[1]-1]):
        return True

    # check right
    if end[1] < columns-1 and checkSpecificSymbol(lines[end[0]][end[1]]):
        return True

    # check top and bottom rows
    rowIndex = start[0]-1
    topRow = rowIndex >= 0

    bottomRowIndex = start[0]+1
    bottomRow = bottomRowIndex < rows

    if start[1]>0:
        left = start[1]-1
    else:
        left = start[1]

    if end[1] < columns-1:
        right = end[1]
    else:
        right = end[1]

    for i in range(left, right+1):
        if topRow and checkSpecificSymbol(lines[rowIndex][i]):
            return True

        if bottomRow and checkSpecificSymbol(lines[bottomRowIndex][i]):
            return True
    
    return False


while row_index<rows:
    while column_index<columns:
        if lines[row_index][column_index].isnumeric():
            start = (row_index, column_index)

            end = start
            while lines[end[0]][end[1]].isnumeric() and end[1]<columns:
                end = (end[0], end[1]+1)
            
            # # if last digit of column is numeric
            # if lines[end[0]][end[1]].isnumeric():
            #     end = (end[0], end[1]+1)
            
            # update for next step
            if lines[end[0]][end[1]].isnumeric():
                column_index = end[1]+1
            else:
                column_index = end[1]
            
            # find symbol
            if searchSymbol(lines, start, end):
                number = int(lines[start[0]][start[1]:end[1]])
                ans += number
        
        else:
            column_index += 1

    column_index = 0
    row_index += 1

print(ans)
# 509768 too low
# 554826 too hight
