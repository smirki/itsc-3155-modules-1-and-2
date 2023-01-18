print('Enter a grade from 0 to 100: ')
grade = input()
grade = int(grade)

if grade >= 90:
    grade = 'A'
elif grade >= 80:
    grade = 'B'
elif grade >= 70:
    grade = 'C'
elif grade >= 60:
    grade = 'D'
else:
    grade = 'F'

print('Your grade is ' + grade)