from Student import Student

class Roster:
    
    student_one = Student("Amy","Jones",14,"009876", 3.8)
    student_two = Student("Kevin","Jones",14,"008765", 3.9)
    student_three = Student("Lisa","James",15,"001245", 3.7)
    student_four = Student("Theo","Khan",14,"003674", 3.8)
    student_five = Student("Joseph","Shetz",16,"002386", 3.2)
    
    print(f"Student One:\n{student_one}")
    print(f"Student Two:\n{student_two}")
    print(f"Student Three:\n{student_three}")
    print(f"Student Four:\n{student_four}")
    print(f"Student Five:\n{student_five}")
    
    student_one.setGPA(3.4)
    print(f"Student One has one change in GPA: {student_one.getGPA()}\n")