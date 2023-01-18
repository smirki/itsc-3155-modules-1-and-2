num_list = []

contiue = True

while (contiue==True):
    print("Enter a number or QUIT to quit: ")
    x = input()
    if x == 'QUIT':
        break
    else:
        x = int(x)
    num_list.append(x)

print("All Nums:", num_list)

for x in num_list:
    if x % 2 == 0:
        print()
    else:
        num_list.remove(x)

print("Even Nums: ", num_list)
