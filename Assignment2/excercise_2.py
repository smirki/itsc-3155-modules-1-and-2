x = input("Input your String Here: ")
x = x.replace(" ","")

upper = lower = ""

for element in x:
    if element.isupper():
        upper += element
    else: lower += element

final = lower + upper

print(final)