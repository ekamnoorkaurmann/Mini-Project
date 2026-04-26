# This program asks for user input and uses lists with dictionaries inside

# Asks for user input
name = input("Enter student name: ")

# Declaring constants
grades = {}
subject = 0
marks = []

# Subjects that gardes can be entered for
subjects = ["Algebra", "Trigonometry", "Patterns and Graphs", "Statistics", "Number"]

# Asks for grade in each subject
while True:
    for subjects in subjects:
        mark = int(input(f"Enter mark for {subjects}: "))
        marks.append(mark)
        subject +=1
        # Giving a Mark
        while True:
            if mark <= 7: # 24 is the highest you can get
                grade = "NA"
                print(grade)
                grades.update({subjects: grade})# adds to a dictionary
                break
            elif mark <= 13: # You need atleast 13 to pass
                grade = "A"
                print(grade)
                grades.update({subjects: grade})# adds to a dictionary
                break
            elif mark <= 19:
                grade = "M"
                print(grade)
                grades.update({subjects: grade})# adds to a dictionary
                break
            else:
                grade = "E"
                print(grade)
                grades.update({subjects: grade})# adds to a dictionary
                break
    if subject == 5:
        break  

# Display all data
print(f"Name: {name}")
for subject, mark in grades.items(): # .tem() means for every item in the list
    print(f"{subject}: {mark}")
