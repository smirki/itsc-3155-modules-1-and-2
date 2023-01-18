print('Enter a string: ')
suffix = input()

print('Enter another string: ')
full_string = input()

for i in range(len(suffix)):
    if full_string.find(suffix,len(full_string)-i-1) != -1:
        print('True')
        exit()
print('False')

