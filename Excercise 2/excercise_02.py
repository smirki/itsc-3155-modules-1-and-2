print("Enter a string : ")
txt = input()

string_front = ""
string_back= ""

for x in txt:
    if x == " ":
        string_front += ""
    elif x.islower():
        string_front += x
    else:
        string_back += x

print(string_front+string_back)