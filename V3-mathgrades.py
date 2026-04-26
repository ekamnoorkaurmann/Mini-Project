# Start program with welcome screen 

import tkinter as tk
from tkinter import messagebox

def show_frame(frame):
    frame.tkraise()

root = tk.Tk()
root.title("Simple Quiz")
root.geometry("500x400")

subjects = ["Algebra", "Trigonometry", "Patterns and Graphs", "Statistics", "Probability"]
entries = {}

students_data = []   # this list will store every student's data 

# ---------- FUNCTIONS ----------

def calculate_results():
    name = name_entry.get()

    total = 0 # this counter is for calculating average at the end

    if name == "":
        messagebox.showerror("Error", "Enter your name")
        return

    grades = {}

    # Get marks and calculate grades
    for subject in subjects:
        try:
            mark = int(entries[subject].get())
            total += mark

        except ValueError:
            messagebox.showerror("Error", f"Invalid input for {subject}")
            return
        if mark < 0 or mark > 24:
                messagebox.showerror("Error", f"Mark for {subject} must be between 0 and 24")
                return

        if mark <= 7:
            grade = "NA"
            grades.update({subject:grade}) # .update() adds to a dictionary
        elif mark <= 13:
            grade = "A"
            grades.update({subject:grade}) # .update() adds to a dictionary
        elif mark <= 19:
            grade = "M"
            grades.update({subject:grade}) # .update() adds to a dictionary
        else:
            grade = "E"
            grades.update({subject:grade}) # .update() adds to a dictionary

    average = total / len(subjects)

    # Adding a summary of each student
    marks = {}  # create empty dictionary

    for subject in subjects:
        mark = int(entries[subject].get())
        marks[subject] = mark   # store like {"Algebra": 12}

    # create student dictionary
    student = {
        "name": name,
        "marks": marks,
        "average": average
        }

    # adding student to the list
    students_data.append(student)

    # Write to file
    with open("summary_of_math_grades.txt", "a") as file:
        file.write(f"Name: {name}, Average: {average:.2f}, Grades: {grades}\n")

    show_frame(result_frame)

    # ---------- RESULT ----------
    tk.Label(result_frame, text=f"{name}'s Average Mark: {average:.2f}", font=("Arial", 12)).pack(pady=20)
    tk.Button(result_frame, text="Next", command=lambda: show_frame(add_or_end_frame)).pack(pady=20)


def reset_form(): # To add another student
    name_entry.delete(0, tk.END)

    for subject in subjects:
        entries[subject].delete(0, tk.END)
        
    show_frame(welcome_frame) # Goes back to welcome frame

def show_graphs():
    import matplotlib.pyplot as plt

    # Check if there is any student data
    
    # If no students have been added, stop the function
    if len(students_data) == 0:
        messagebox.showerror("Error", "No student data to display")
        return

    # Graph for Average mark per subject

    # Creating a list of totals for each subject
    # [0, 0, 0, 0, 0] → one 0 for each subject
    totals = [0] * len(subjects)

    # Going through each student
    for student in students_data:

        # enumerate() does 2 things:
        # i = position (0,1,2,3...)
        # subject = actual subject name ("Algebra", etc)
        for i, subject in enumerate(subjects):

            # This adds each student's mark into totals
            # Example: totals[0] = totals[0] + Algebra mark
            totals[i] += student["marks"][subject]

    # Now calculate averages
    averages = []
    
    for total in totals:

        # divide by number of students to get average
        avg = total / len(students_data)

        # add to averages list
        averages.append(avg)


    # ---------- Showing Graph 1 ----------
    plt.figure()  # create new graph

    # x-axis = subjects
    # y-axis = averages
    plt.bar(subjects, averages)

    plt.title("Average Marks Per Subject")   # title of graph
    plt.xlabel("Subjects")                  # x-axis label
    plt.ylabel("Average Mark")              # y-axis label
    plt.ylim(0, 24)  # marks go from 0 to 24, setting minimum and maximum
    plt.show()       # display graph


    # Graph for each students marks
    plt.figure()

    for student in students_data:

        marks = []  # empty list to store a student's marks
        # Going through each subject 
        for subject in subjects:
            # getting the mark for each subject and adding to list
            marks.append(student["marks"][subject])

    plt.bar(subjects, marks)
    plt.title("Student Performance")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.ylim(0, 24)

    plt.show()


# ---------- FRAMES ----------
welcome_frame = tk.Frame(root)
input_frame = tk.Frame(root)
result_frame = tk.Frame(root)
add_or_end_frame = tk.Frame(root)

for frame in (welcome_frame, input_frame, result_frame, add_or_end_frame):
    frame.grid(row=0, column=0, sticky="nsew")

# ---------- WELCOME ----------
tk.Label(welcome_frame, text="Welcome", font=("Arial", 16)).pack(pady=20)

tk.Label(welcome_frame, text="What is your name:").pack()
name_entry = tk.Entry(welcome_frame)
name_entry.pack()

tk.Button(welcome_frame, text="Next", command=lambda: show_frame(input_frame)).pack(pady=20)

# ---------- INPUT ----------
for i, subject in enumerate(subjects): # enumerate adds a counter to an iterable (such as a list, tuple, or string)
    tk.Label(input_frame, text= f"Enter mark for {subject}:").grid(row=i, column=0, padx=10, pady=10)

    entry = tk.Entry(input_frame)
    entry.grid(row=i, column=1)

    entries[subject] = entry

tk.Button(input_frame, text="Submit", command=calculate_results).grid(row=6, column=0, columnspan=2, pady=20)

# ---------- Finishing the program ----------

tk.Label(add_or_end_frame, font=("Arial", 16)).pack(pady=20)

tk.Label(add_or_end_frame, text="Do you want to add another student or finish the program or return the beginning or see the graphs").pack()

tk.Button(add_or_end_frame, text="Home", command=lambda:show_frame(welcome_frame)).pack(pady=20)
tk.Button(add_or_end_frame, text="Add", command=reset_form).pack(pady=20)
tk.Button(add_or_end_frame, text="Exit", command=root.destroy).pack(pady=20)# .destroy deletes the whole program
tk.Button(add_or_end_frame, text="Graphs", command=show_graphs).pack(pady=20)

# Start
show_frame(welcome_frame)
root.mainloop()




    
