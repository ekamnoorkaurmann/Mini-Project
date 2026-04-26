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

    # Show result
    result_text.set(f"{name}'s Average Mark: {average:.2f}")

    # Write to file
    with open("summary_of_math_grades.txt", "a") as file:
        file.write(f"Name: {name}, Average: {average:.2f}, Grades: {grades}\n")

    show_frame(result_frame)


# ---------- FRAMES ----------
welcome_frame = tk.Frame(root)
input_frame = tk.Frame(root)
result_frame = tk.Frame(root)

for frame in (welcome_frame, input_frame, result_frame):
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

# ---------- RESULT ----------
result_text = tk.StringVar()

tk.Label(result_frame, textvariable=result_text, font=("Arial", 12)).pack(pady=20)

tk.Button(result_frame, text="Back to Home",
          command=lambda: show_frame(welcome_frame)).pack()

# Start
show_frame(welcome_frame)
root.mainloop()




    

