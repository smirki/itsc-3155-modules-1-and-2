first_list = []
second_list = []
third_list = []

def ListForm(listm, listName):
    for x in range(0,5):
        print("Enter a number for the " + listName + " list: ")
        number = int(input())
        listm.append(number)

ListForm(first_list, "first")
ListForm(second_list, "second")

for x in second_list:
    if x in first_list:
        if x in third_list:
            print()
        else:
            third_list.append(x)

print("First list: ", first_list)
print("Second list: ", second_list)
print("Common List: ", third_list)