print("Enter a number: ")
number = int(input())

output = []

for i in range(number):
    print(f"Enter number {i+1}: ")
    new_number = float(input())
    output.append(new_number)

print(output)
output = sum(output)
print("Mean is:", output/number)