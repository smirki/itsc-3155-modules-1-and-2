print("Enter a row num 1 to 5: ")
row = int(input())

print("Enter a col num 1 to 5: ")
col = int(input())

row_list = []

def ZeroReturn():
    return "0 0 0 0 0 "

for x in range(1, 6):
    if x == row:
        special_string = ""
        for y in range(1, 6):
            if y == col:
                special_string += "1 "
            else:
                special_string += "0 "
        row_list.append(special_string)
    else:
        row_list.append(ZeroReturn())

print('\n'.join(row_list))
