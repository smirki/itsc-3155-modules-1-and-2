word_list = []

for i in range(1, 6):
    print("Enter a word: ")
    x = input()
    word_list.append(x)

print("Original List: ", word_list)

s = ' '.join(word_list)

print("One String:", s)
