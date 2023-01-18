print("Enter a String: ")
x = input()
x = list(x)

full_list = []

new_list = []
counter = 0

for idx, x in enumerate(x):
    if counter == 3:
        full_list.append(new_list)
        counter = 0
        new_list = []
    counter += 1
    new_list.append(x)
full_list.append(new_list)


print(full_list)