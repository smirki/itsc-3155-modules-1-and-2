num_list = []

for i in range(1, 11):
    print("Enter number: " + str(i))
    x = int(input())
    num_list.append(x)

print("Original List:", num_list)
new_list = []


for x in num_list:
    counter = 0
    for y in num_list:
        if x == y:
            counter+=1
    if counter == 1:
        new_list.append(x)

print(new_list)



