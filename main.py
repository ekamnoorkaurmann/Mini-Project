# This program imports premade

import GradeUtils

print(dir(GradeUtils))

mark = int(input('Enter students mark : '))
grade = GradeUtils.calculate_grade(mark)

print('Student Grade : ', grade)
