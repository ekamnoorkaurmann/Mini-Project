# this module is a grade utilities module
# it has pre set marks and its grade

def calculate_grade(mark):
    if mark  >=80:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 40:
        return "C"
    else:
        return "Fail"
    
